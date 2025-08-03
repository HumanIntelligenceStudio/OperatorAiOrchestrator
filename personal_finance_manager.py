"""
Personal Finance Management System for OperatorOS
Extends existing financial capabilities with personal finance features
"""

import json
import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
try:
    from ai_providers_enhanced import AIProviderManager
except ImportError:
    from ai_providers import AIProviderManager

try:
    from exchange_rate_provider import ExchangeRateProvider
except ImportError:
    class ExchangeRateProvider:
        def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
            return 1.0
import sqlite3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class BudgetCategory:
    """Budget category configuration"""
    name: str
    monthly_limit: float
    currency: str = 'USD'
    parent_category: Optional[str] = None
    auto_categorize_keywords: Optional[List[str]] = None

@dataclass
class Expense:
    """Individual expense record"""
    id: str
    amount: float
    currency: str
    category: str
    description: str
    date: datetime.date
    merchant: Optional[str] = None
    payment_method: Optional[str] = None
    tags: Optional[List[str]] = None

@dataclass
class FinancialGoal:
    """Personal financial goal"""
    id: str
    name: str
    target_amount: float
    current_amount: float
    currency: str
    target_date: datetime.date
    priority: int  # 1-5 scale
    goal_type: str  # 'savings', 'debt_payoff', 'investment', 'emergency_fund'
    description: Optional[str] = None

@dataclass
class Investment:
    """Personal investment holding"""
    symbol: str
    shares: float
    purchase_price: float
    current_price: float
    currency: str
    purchase_date: datetime.date
    investment_type: str  # 'stock', 'bond', 'etf', 'crypto', 'mutual_fund'

@dataclass
class Debt:
    """Personal debt record"""
    id: str
    name: str
    balance: float
    interest_rate: float
    minimum_payment: float
    currency: str
    debt_type: str  # 'credit_card', 'auto_loan', 'mortgage', 'student_loan', 'personal_loan'
    payment_date: int  # Day of month
    term_months: Optional[int] = None

class PersonalFinanceManager:
    """
    Personal Finance Management System
    Integrates with existing OperatorOS financial infrastructure
    """
    
    def __init__(self, user_id: str = "default_user"):
        self.user_id = user_id
        self.ai_provider = AIProviderManager()
        self.exchange_provider = ExchangeRateProvider()
        self.db_path = f"personal_finance_{user_id}.db"
        self._init_database()
        
    def _init_database(self):
        """Initialize personal finance database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Budget categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS budget_categories (
                    name TEXT PRIMARY KEY,
                    monthly_limit REAL,
                    currency TEXT DEFAULT 'USD',
                    parent_category TEXT,
                    auto_keywords TEXT
                )
            ''')
            
            # Expenses table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id TEXT PRIMARY KEY,
                    amount REAL,
                    currency TEXT,
                    category TEXT,
                    description TEXT,
                    date TEXT,
                    merchant TEXT,
                    payment_method TEXT,
                    tags TEXT
                )
            ''')
            
            # Financial goals table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS financial_goals (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    target_amount REAL,
                    current_amount REAL,
                    currency TEXT,
                    target_date TEXT,
                    priority INTEGER,
                    goal_type TEXT,
                    description TEXT
                )
            ''')
            
            # Investments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS investments (
                    symbol TEXT PRIMARY KEY,
                    shares REAL,
                    purchase_price REAL,
                    current_price REAL,
                    currency TEXT,
                    purchase_date TEXT,
                    investment_type TEXT
                )
            ''')
            
            # Debts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS debts (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    balance REAL,
                    interest_rate REAL,
                    minimum_payment REAL,
                    currency TEXT,
                    debt_type TEXT,
                    payment_date INTEGER,
                    term_months INTEGER
                )
            ''')
            
            conn.commit()
            conn.close()
            logger.info(f"✅ Personal finance database initialized for user {self.user_id}")
            
        except Exception as e:
            logger.error(f"❌ Database initialization error: {e}")
            raise

    def set_budget_category(self, name: str, monthly_limit: float, currency: str = 'USD', 
                           keywords: Optional[List[str]] = None) -> Dict[str, Any]:
        """Set or update budget category"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            keywords_json = json.dumps(keywords) if keywords else None
            
            cursor.execute('''
                INSERT OR REPLACE INTO budget_categories 
                (name, monthly_limit, currency, auto_keywords)
                VALUES (?, ?, ?, ?)
            ''', (name, monthly_limit, currency, keywords_json))
            
            conn.commit()
            conn.close()
            
            # Convert to USD for consistent tracking
            usd_limit = monthly_limit
            if currency != 'USD':
                try:
                    rate = self.exchange_provider.get_exchange_rate(currency, 'USD')
                    if rate:
                        usd_limit = monthly_limit * rate
                except:
                    usd_limit = monthly_limit  # Fallback to original amount
            
            logger.info(f"✅ Budget set: {name} = {monthly_limit} {currency} (${usd_limit:.2f} USD)")
            
            return {
                'success': True,
                'category': name,
                'monthly_limit': monthly_limit,
                'currency': currency,
                'usd_equivalent': usd_limit
            }
            
        except Exception as e:
            logger.error(f"❌ Budget setting error: {e}")
            return {'success': False, 'error': str(e)}

    def add_expense(self, amount: float, description: str, category: Optional[str] = None,
                   currency: str = 'USD', merchant: Optional[str] = None) -> Dict[str, Any]:
        """Add expense with automatic categorization if needed"""
        try:
            # Auto-categorize if no category provided
            if not category:
                category = self._auto_categorize_expense(description, merchant)
            
            expense_id = f"exp_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            expense_date = datetime.date.today().isoformat()
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO expenses 
                (id, amount, currency, category, description, date, merchant)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (expense_id, amount, currency, category or "Other", description, expense_date, merchant))
            
            conn.commit()
            conn.close()
            
            # Check budget status
            budget_status = self._check_budget_status(category, currency)
            
            logger.info(f"✅ Expense added: ${amount} {currency} - {description} ({category})")
            
            return {
                'success': True,
                'expense_id': expense_id,
                'amount': amount,
                'currency': currency,
                'category': category,
                'description': description,
                'budget_status': budget_status
            }
            
        except Exception as e:
            logger.error(f"❌ Expense addition error: {e}")
            return {'success': False, 'error': str(e)}

    def _auto_categorize_expense(self, description: str, merchant: Optional[str] = None) -> str:
        """Automatically categorize expense using AI and keyword matching"""
        try:
            # First try keyword matching
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT name, auto_keywords FROM budget_categories WHERE auto_keywords IS NOT NULL')
            categories = cursor.fetchall()
            conn.close()
            
            text_to_match = f"{description} {merchant or ''}".lower()
            
            for category_name, keywords_json in categories:
                if keywords_json:
                    keywords = json.loads(keywords_json)
                    if any(keyword.lower() in text_to_match for keyword in keywords):
                        return category_name
            
            # If no keyword match, use AI categorization
            ai_prompt = f"""
            Categorize this expense into one of these common categories:
            - Food & Dining
            - Transportation
            - Shopping
            - Entertainment
            - Healthcare
            - Utilities
            - Housing
            - Education
            - Travel
            - Other
            
            Expense: {description}
            Merchant: {merchant or 'Unknown'}
            
            Return only the category name.
            """
            
            try:
                ai_response = self.ai_provider.get_response(ai_prompt, 'financial')
                category = ai_response.get('content', 'Other').strip() if not ai_response.get('error') else 'Other'
            except:
                category = 'Other'
            return category if category else "Other"
            
        except Exception as e:
            logger.error(f"❌ Auto-categorization error: {e}")
            return "Other"

    def _check_budget_status(self, category: str, currency: str = 'USD') -> Dict[str, Any]:
        """Check budget status for category"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get budget limit
            cursor.execute('SELECT monthly_limit, currency FROM budget_categories WHERE name = ?', (category,))
            budget_result = cursor.fetchone()
            
            if not budget_result:
                return {'status': 'no_budget', 'message': f'No budget set for {category}'}
            
            budget_limit, budget_currency = budget_result
            
            # Get current month spending
            current_month = datetime.date.today().strftime('%Y-%m')
            cursor.execute('''
                SELECT SUM(amount) FROM expenses 
                WHERE category = ? AND date LIKE ?
            ''', (category, f'{current_month}%'))
            
            spent_result = cursor.fetchone()
            spent = spent_result[0] if spent_result[0] else 0
            
            conn.close()
            
            # Convert to same currency for comparison
            if currency != budget_currency:
                try:
                    rate = self.exchange_provider.get_exchange_rate(currency, budget_currency)
                    if rate:
                        spent = spent * rate
                except:
                    pass  # Use original amount if conversion fails
            
            remaining = budget_limit - spent
            percent_used = (spent / budget_limit) * 100
            
            if percent_used >= 100:
                status = 'over_budget'
                message = f'⚠️ Over budget! Spent ${spent:.2f} of ${budget_limit:.2f} ({percent_used:.1f}%)'
            elif percent_used >= 80:
                status = 'near_limit'
                message = f'⚠️ Near budget limit: ${spent:.2f} of ${budget_limit:.2f} ({percent_used:.1f}%)'
            else:
                status = 'within_budget'
                message = f'✅ Within budget: ${spent:.2f} of ${budget_limit:.2f} ({percent_used:.1f}%)'
            
            return {
                'status': status,
                'message': message,
                'spent': spent,
                'budget_limit': budget_limit,
                'remaining': remaining,
                'percent_used': percent_used
            }
            
        except Exception as e:
            logger.error(f"❌ Budget check error: {e}")
            return {'status': 'error', 'message': str(e)}

    def set_financial_goal(self, name: str, target_amount: float, target_date: str,
                          goal_type: str = 'savings', currency: str = 'USD',
                          priority: int = 3) -> Dict[str, Any]:
        """Set financial goal"""
        try:
            goal_id = f"goal_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO financial_goals 
                (id, name, target_amount, current_amount, currency, target_date, priority, goal_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (goal_id, name, target_amount, 0, currency, target_date, priority, goal_type))
            
            conn.commit()
            conn.close()
            
            # Calculate timeline and recommendations
            timeline_analysis = self._analyze_goal_timeline(target_amount, target_date, currency)
            
            logger.info(f"✅ Financial goal set: {name} - ${target_amount} {currency} by {target_date}")
            
            return {
                'success': True,
                'goal_id': goal_id,
                'name': name,
                'target_amount': target_amount,
                'currency': currency,
                'target_date': target_date,
                'timeline_analysis': timeline_analysis
            }
            
        except Exception as e:
            logger.error(f"❌ Goal setting error: {e}")
            return {'success': False, 'error': str(e)}

    def _analyze_goal_timeline(self, target_amount: float, target_date: str, currency: str) -> Dict[str, Any]:
        """Analyze goal timeline and provide recommendations"""
        try:
            target_dt = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
            today = datetime.date.today()
            days_remaining = (target_dt - today).days
            months_remaining = days_remaining / 30.44  # Average days per month
            
            if months_remaining <= 0:
                return {'error': 'Target date is in the past'}
            
            monthly_savings_needed = target_amount / months_remaining
            weekly_savings_needed = target_amount / (days_remaining / 7)
            daily_savings_needed = target_amount / days_remaining
            
            # Get AI recommendations
            ai_prompt = f"""
            Provide savings strategy recommendations for this goal:
            - Target: ${target_amount} {currency}
            - Timeline: {months_remaining:.1f} months
            - Monthly savings needed: ${monthly_savings_needed:.2f}
            - Weekly savings needed: ${weekly_savings_needed:.2f}
            - Daily savings needed: ${daily_savings_needed:.2f}
            
            Provide 3 practical strategies to achieve this goal.
            """
            
            try:
                ai_response = self.ai_provider.get_response(ai_prompt, 'financial')
                strategies = ai_response.get('content', 'Unable to generate strategies') if not ai_response.get('error') else 'Unable to generate strategies'
            except:
                strategies = 'Unable to generate strategies'
            
            return {
                'days_remaining': days_remaining,
                'months_remaining': round(months_remaining, 1),
                'monthly_savings_needed': round(monthly_savings_needed, 2),
                'weekly_savings_needed': round(weekly_savings_needed, 2),
                'daily_savings_needed': round(daily_savings_needed, 2),
                'ai_strategies': strategies
            }
            
        except Exception as e:
            logger.error(f"❌ Goal timeline analysis error: {e}")
            return {'error': str(e)}

    def get_financial_health_score(self) -> Dict[str, Any]:
        """Calculate comprehensive financial health score"""
        try:
            # Get all financial data
            expenses_data = self._get_monthly_expenses()
            savings_data = self._get_savings_data()
            debt_data = self._get_debt_data()
            budget_adherence = self._get_budget_adherence()
            
            # Calculate component scores (0-100)
            budget_score = self._calculate_budget_score(budget_adherence)
            savings_score = self._calculate_savings_score(savings_data)
            debt_score = self._calculate_debt_score(debt_data)
            spending_score = self._calculate_spending_score(expenses_data)
            
            # Weighted overall score
            overall_score = (
                budget_score * 0.25 +
                savings_score * 0.25 +
                debt_score * 0.30 +
                spending_score * 0.20
            )
            
            # Get AI analysis
            ai_analysis = self._get_ai_financial_health_analysis({
                'overall_score': overall_score,
                'budget_score': budget_score,
                'savings_score': savings_score,
                'debt_score': debt_score,
                'spending_score': spending_score,
                'expenses_data': expenses_data,
                'debt_data': debt_data
            })
            
            return {
                'overall_score': round(overall_score, 1),
                'component_scores': {
                    'budget_adherence': round(budget_score, 1),
                    'savings_rate': round(savings_score, 1),
                    'debt_management': round(debt_score, 1),
                    'spending_control': round(spending_score, 1)
                },
                'grade': self._score_to_grade(overall_score),
                'ai_analysis': ai_analysis,
                'recommendations': self._get_improvement_recommendations(overall_score, {
                    'budget': budget_score,
                    'savings': savings_score,
                    'debt': debt_score,
                    'spending': spending_score
                })
            }
            
        except Exception as e:
            logger.error(f"❌ Financial health calculation error: {e}")
            return {'error': str(e)}

    def _get_ai_financial_health_analysis(self, data: Dict[str, Any]) -> str:
        """Get comprehensive AI analysis of financial health"""
        try:
            prompt = f"""
            Provide a comprehensive financial health analysis based on this data:
            
            Overall Score: {data['overall_score']:.1f}/100
            Component Scores:
            - Budget Adherence: {data['budget_score']:.1f}/100
            - Savings Rate: {data['savings_score']:.1f}/100  
            - Debt Management: {data['debt_score']:.1f}/100
            - Spending Control: {data['spending_score']:.1f}/100
            
            Provide insights on strengths, areas for improvement, and specific actionable recommendations.
            """
            
            try:
                ai_response = self.ai_provider.get_response(prompt, 'financial')
                return ai_response.get('content', 'Unable to generate analysis') if not ai_response.get('error') else 'Unable to generate analysis'
            except:
                return 'Unable to generate analysis'
            
        except Exception as e:
            logger.error(f"❌ AI financial health analysis error: {e}")
            return "Unable to generate AI analysis at this time."

    def _score_to_grade(self, score: float) -> str:
        """Convert numerical score to letter grade"""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"

    def _calculate_budget_score(self, adherence_data: Dict) -> float:
        """Calculate budget adherence score"""
        # Implementation for budget score calculation
        return 85.0  # Placeholder

    def _calculate_savings_score(self, savings_data: Dict) -> float:
        """Calculate savings rate score"""
        # Implementation for savings score calculation
        return 75.0  # Placeholder

    def _calculate_debt_score(self, debt_data: Dict) -> float:
        """Calculate debt management score"""
        # Implementation for debt score calculation
        return 80.0  # Placeholder

    def _calculate_spending_score(self, expenses_data: Dict) -> float:
        """Calculate spending control score"""
        # Implementation for spending score calculation
        return 70.0  # Placeholder

    def _get_monthly_expenses(self) -> Dict:
        """Get monthly expenses data"""
        # Implementation for expenses data retrieval
        return {}

    def _get_savings_data(self) -> Dict:
        """Get savings data"""
        # Implementation for savings data retrieval
        return {}

    def _get_debt_data(self) -> Dict:
        """Get debt data"""
        # Implementation for debt data retrieval
        return {}

    def _get_budget_adherence(self) -> Dict:
        """Get budget adherence data"""
        # Implementation for budget adherence calculation
        return {}

    def _get_improvement_recommendations(self, overall_score: float, component_scores: Dict) -> List[str]:
        """Get personalized improvement recommendations"""
        recommendations = []
        
        if component_scores['budget'] < 70:
            recommendations.append("Focus on staying within monthly budget limits")
        if component_scores['savings'] < 70:
            recommendations.append("Increase monthly savings rate to at least 20% of income")
        if component_scores['debt'] < 70:
            recommendations.append("Prioritize high-interest debt payoff")
        if component_scores['spending'] < 70:
            recommendations.append("Review and reduce discretionary spending")
            
        return recommendations

    def get_spending_insights(self, period: str = 'month') -> Dict[str, Any]:
        """Get spending insights and trends"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Define date filter based on period
            if period == 'week':
                date_filter = datetime.date.today() - datetime.timedelta(days=7)
            elif period == 'month':
                date_filter = datetime.date.today().replace(day=1)
            elif period == 'year':
                date_filter = datetime.date.today().replace(month=1, day=1)
            else:
                date_filter = datetime.date.today() - datetime.timedelta(days=30)
            
            # Get spending by category
            cursor.execute('''
                SELECT category, SUM(amount), currency, COUNT(*)
                FROM expenses 
                WHERE date >= ?
                GROUP BY category, currency
                ORDER BY SUM(amount) DESC
            ''', (date_filter.isoformat(),))
            
            spending_data = cursor.fetchall()
            conn.close()
            
            # Process and analyze data
            total_spending = sum(amount for _, amount, _, _ in spending_data)
            
            insights = {
                'period': period,
                'total_spending': total_spending,
                'top_categories': [],
                'spending_breakdown': [],
                'ai_insights': None
            }
            
            for category, amount, currency, count in spending_data:
                percentage = (amount / total_spending * 100) if total_spending > 0 else 0
                insights['spending_breakdown'].append({
                    'category': category,
                    'amount': amount,
                    'currency': currency,
                    'transaction_count': count,
                    'percentage': round(percentage, 1)
                })
            
            insights['top_categories'] = insights['spending_breakdown'][:5]
            
            # Get AI insights
            ai_prompt = f"""
            Analyze this spending pattern for the last {period}:
            Total spending: ${total_spending:.2f}
            Top categories: {', '.join([f"{cat['category']}: ${cat['amount']:.2f} ({cat['percentage']:.1f}%)" for cat in insights['top_categories']])}
            
            Provide insights on spending patterns and suggest optimizations.
            """
            
            try:
                ai_response = self.ai_provider.get_response(ai_prompt, 'financial')
                insights['ai_insights'] = ai_response.get('content', 'Unable to generate insights') if not ai_response.get('error') else 'Unable to generate insights'
            except:
                insights['ai_insights'] = 'Unable to generate insights'
            
            return insights
            
        except Exception as e:
            logger.error(f"❌ Spending insights error: {e}")
            return {'error': str(e)}

# Initialize the personal finance manager
def create_personal_finance_manager(user_id: str = "default_user") -> PersonalFinanceManager:
    """Factory function to create PersonalFinanceManager instance"""
    return PersonalFinanceManager(user_id)

if __name__ == "__main__":
    # Demo usage
    pf_manager = PersonalFinanceManager("demo_user")
    
    # Set up budget
    pf_manager.set_budget_category("Food & Dining", 600.0, "USD", ["grocery", "restaurant", "food"])
    
    # Add expense
    result = pf_manager.add_expense(45.0, "Grocery shopping at Whole Foods", merchant="Whole Foods")
    print(json.dumps(result, indent=2))
    
    # Set financial goal
    goal_result = pf_manager.set_financial_goal("Emergency Fund", 10000.0, "2025-12-31", "emergency_fund")
    print(json.dumps(goal_result, indent=2))
    
    # Get financial health score
    health_score = pf_manager.get_financial_health_score()
    print(json.dumps(health_score, indent=2))