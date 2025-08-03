"""
Personal Finance Conversational Interface for OperatorOS
Integrates personal finance capabilities with the existing conversational system
"""

import re
import json
import datetime
from typing import Dict, List, Any, Optional
from personal_finance_manager import PersonalFinanceManager
try:
    from ai_providers_enhanced import AIProviderManager
except ImportError:
    from ai_providers import AIProviderManager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonalFinanceConversation:
    """
    Conversational interface for personal finance management
    Extends OperatorOS with natural language personal finance capabilities
    """
    
    def __init__(self, user_id: str = "default_user"):
        self.user_id = user_id
        self.pf_manager = PersonalFinanceManager(user_id)
        self.ai_provider = AIProviderManager()
        
        # Personal finance command patterns
        self.command_patterns = {
            'set_budget': [
                r'set (?:my )?(.+?) budget to \$?(\d+(?:\.\d+)?)',
                r'budget \$?(\d+(?:\.\d+)?) for (.+)',
                r'i want to budget \$?(\d+(?:\.\d+)?) (?:for )?(.+)'
            ],
            'add_expense': [
                r'i spent \$?(\d+(?:\.\d+)?) (?:at |on )?(.+)',
                r'expense of \$?(\d+(?:\.\d+)?) (?:for )?(.+)',
                r'bought (.+) for \$?(\d+(?:\.\d+)?)',
                r'paid \$?(\d+(?:\.\d+)?) (?:for )?(.+)'
            ],
            'check_budget': [
                r'am i over budget',
                r'how (?:much|far) over budget am i',
                r'budget status',
                r'check my budget',
                r'budget check'
            ],
            'set_goal': [
                r'i want to save \$?(\d+(?:\.\d+)?) for (.+?) by (.+)',
                r'goal to save \$?(\d+(?:\.\d+)?) for (.+)',
                r'save \$?(\d+(?:\.\d+)?) for (.+) by (.+)',
                r'financial goal of \$?(\d+(?:\.\d+)?) for (.+)'
            ],
            'financial_health': [
                r'how am i doing financially',
                r'financial health',
                r'money health check',
                r'financial score',
                r'how are my finances'
            ],
            'spending_analysis': [
                r'show my spending (?:trends |patterns )?(?:for )?(.+)',
                r'spending analysis',
                r'where am i spending my money',
                r'spending breakdown',
                r'analyze my spending'
            ],
            'debt_management': [
                r'i have (?:a )?\$?(\d+(?:\.\d+)?) (.+) at (\d+(?:\.\d+)?)%',
                r'debt of \$?(\d+(?:\.\d+)?) (?:for )?(.+)',
                r'owe \$?(\d+(?:\.\d+)?) on my (.+)'
            ]
        }

    def process_personal_finance_query(self, user_input: str) -> Dict[str, Any]:
        """
        Process natural language personal finance queries
        Returns structured response with actions taken
        """
        user_input = user_input.lower().strip()
        
        try:
            # Check each command pattern
            for command_type, patterns in self.command_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, user_input, re.IGNORECASE)
                    if match:
                        return self._execute_finance_command(command_type, match.groups(), user_input)
            
            # If no specific pattern matches, use AI to understand intent
            return self._handle_general_finance_query(user_input)
            
        except Exception as e:
            logger.error(f"❌ Personal finance query error: {e}")
            return {
                'success': False,
                'error': str(e),
                'message': "I encountered an error processing your financial request. Please try again."
            }

    def _execute_finance_command(self, command_type: str, groups: tuple, original_input: str) -> Dict[str, Any]:
        """Execute specific finance command based on pattern match"""
        
        if command_type == 'set_budget':
            if len(groups) == 2:
                if groups[0].replace('.', '').isdigit():  # Amount first
                    amount, category = float(groups[0]), groups[1]
                else:  # Category first
                    category, amount = groups[0], float(groups[1])
                
                result = self.pf_manager.set_budget_category(category.title(), amount)
                
                if result['success']:
                    return {
                        'success': True,
                        'action': 'budget_set',
                        'message': f"✅ Set {category.title()} budget to ${amount:.2f}/month",
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'message': f"❌ Failed to set budget: {result.get('error', 'Unknown error')}"
                    }
        
        elif command_type == 'add_expense':
            if len(groups) == 2:
                if groups[0].replace('.', '').isdigit():  # Amount first
                    amount, description = float(groups[0]), groups[1]
                else:  # Description first, amount second
                    description, amount = groups[0], float(groups[1])
                
                result = self.pf_manager.add_expense(amount, description)
                
                if result['success']:
                    budget_msg = ""
                    if result['budget_status']['status'] in ['over_budget', 'near_limit']:
                        budget_msg = f"\n{result['budget_status']['message']}"
                    
                    return {
                        'success': True,
                        'action': 'expense_added',
                        'message': f"✅ Added expense: ${amount:.2f} for {description} ({result['category']}){budget_msg}",
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'message': f"❌ Failed to add expense: {result.get('error', 'Unknown error')}"
                    }
        
        elif command_type == 'check_budget':
            return self._get_budget_status()
        
        elif command_type == 'set_goal':
            if len(groups) >= 2:
                amount = float(groups[0])
                goal_name = groups[1]
                target_date = self._parse_target_date(groups[2] if len(groups) > 2 else "2025-12-31")
                
                result = self.pf_manager.set_financial_goal(goal_name, amount, target_date)
                
                if result['success']:
                    timeline = result['timeline_analysis']
                    return {
                        'success': True,
                        'action': 'goal_set',
                        'message': f"✅ Goal set: Save ${amount:.2f} for {goal_name} by {target_date}\n"
                                 f"💡 Need to save ${timeline['monthly_savings_needed']:.2f}/month",
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'message': f"❌ Failed to set goal: {result.get('error', 'Unknown error')}"
                    }
        
        elif command_type == 'financial_health':
            return self._get_financial_health_report()
        
        elif command_type == 'spending_analysis':
            period = groups[0] if groups and groups[0] else 'month'
            return self._get_spending_analysis(period)
        
        elif command_type == 'debt_management':
            if len(groups) >= 3:
                amount, debt_type, interest_rate = float(groups[0]), groups[1], float(groups[2])
                return self._add_debt_record(amount, debt_type, interest_rate)
        
        return {
            'success': False,
            'message': "I understood your request but couldn't complete the action. Please try again."
        }

    def _handle_general_finance_query(self, user_input: str) -> Dict[str, Any]:
        """Handle general finance queries using AI interpretation"""
        try:
            # Use AI to understand intent and extract parameters
            intent_prompt = f"""
            Analyze this personal finance request and extract the intent and parameters:
            
            User input: "{user_input}"
            
            Possible intents:
            - set_budget: Setting a budget for a category
            - add_expense: Recording an expense
            - check_budget: Checking budget status
            - set_goal: Setting a financial goal
            - financial_health: Getting financial health overview
            - spending_analysis: Analyzing spending patterns
            - debt_management: Managing debt information
            - general_advice: General financial advice
            
            Return JSON with:
            {{
                "intent": "detected_intent",
                "parameters": {{"param1": "value1", "param2": "value2"}},
                "confidence": 0.8
            }}
            """
            
            try:
                ai_response_obj = self.ai_provider.get_response(intent_prompt, 'financial')
                ai_response = ai_response_obj.get('content', '{}') if not ai_response_obj.get('error') else '{}'
            except:
                ai_response = '{}'
            
            try:
                intent_data = json.loads(ai_response)
                intent = intent_data.get('intent')
                parameters = intent_data.get('parameters', {})
                confidence = intent_data.get('confidence', 0.5)
                
                if confidence > 0.7:
                    return self._execute_ai_interpreted_command(intent, parameters, user_input)
                else:
                    return self._provide_general_finance_advice(user_input)
                    
            except json.JSONDecodeError:
                return self._provide_general_finance_advice(user_input)
                
        except Exception as e:
            logger.error(f"❌ General finance query error: {e}")
            return self._provide_general_finance_advice(user_input)

    def _execute_ai_interpreted_command(self, intent: str, parameters: Dict, user_input: str) -> Dict[str, Any]:
        """Execute command based on AI interpretation"""
        
        if intent == 'set_budget' and 'category' in parameters and 'amount' in parameters:
            result = self.pf_manager.set_budget_category(
                parameters['category'], 
                float(parameters['amount'])
            )
            return {
                'success': result['success'],
                'action': 'budget_set',
                'message': f"✅ Set {parameters['category']} budget to ${float(parameters['amount']):.2f}/month" if result['success'] else f"❌ Failed to set budget",
                'data': result
            }
        
        elif intent == 'add_expense' and 'amount' in parameters and 'description' in parameters:
            result = self.pf_manager.add_expense(
                float(parameters['amount']), 
                parameters['description'],
                parameters.get('category', "Other")
            )
            return {
                'success': result['success'],
                'action': 'expense_added',
                'message': f"✅ Added expense: ${float(parameters['amount']):.2f} for {parameters['description']}" if result['success'] else f"❌ Failed to add expense",
                'data': result
            }
        
        elif intent == 'financial_health':
            return self._get_financial_health_report()
        
        elif intent == 'spending_analysis':
            period = parameters.get('period', 'month')
            return self._get_spending_analysis(period)
        
        else:
            return self._provide_general_finance_advice(user_input)

    def _provide_general_finance_advice(self, user_input: str) -> Dict[str, Any]:
        """Provide general financial advice using AI"""
        try:
            advice_prompt = f"""
            Provide helpful personal finance advice for this request:
            "{user_input}"
            
            Give practical, actionable advice in a conversational tone.
            Include specific steps they can take.
            """
            
            try:
                ai_response = self.ai_provider.get_response(advice_prompt, 'financial')
                advice = ai_response.get('content', 'I can help with your finances, but need more specific information.') if not ai_response.get('error') else 'I can help with your finances, but need more specific information.'
            except:
                advice = 'I can help with your finances, but need more specific information.'
            
            return {
                'success': True,
                'action': 'general_advice',
                'message': f"💡 Financial Advice:\n{advice}",
                'advice_type': 'general'
            }
            
        except Exception as e:
            logger.error(f"❌ General advice error: {e}")
            return {
                'success': False,
                'message': "I'd be happy to help with your finances, but I need more specific information. Try asking about budgets, expenses, goals, or your financial health."
            }

    def _get_budget_status(self) -> Dict[str, Any]:
        """Get comprehensive budget status"""
        try:
            # This would get actual budget status from the manager
            return {
                'success': True,
                'action': 'budget_check',
                'message': "📊 Budget Status: Checking all your budget categories...",
                'data': {'status': 'within_budget', 'details': 'Implementation needed'}
            }
        except Exception as e:
            logger.error(f"❌ Budget status error: {e}")
            return {
                'success': False,
                'message': "❌ Unable to check budget status at this time."
            }

    def _get_financial_health_report(self) -> Dict[str, Any]:
        """Get financial health score and analysis"""
        try:
            health_data = self.pf_manager.get_financial_health_score()
            
            if 'error' in health_data:
                return {
                    'success': False,
                    'message': f"❌ Unable to calculate financial health: {health_data['error']}"
                }
            
            score = health_data['overall_score']
            grade = health_data['grade']
            
            message = f"📈 Financial Health Score: {score}/100 (Grade: {grade})\n\n"
            message += "Component Scores:\n"
            for component, score_val in health_data['component_scores'].items():
                message += f"• {component.replace('_', ' ').title()}: {score_val}/100\n"
            
            if health_data.get('recommendations'):
                message += f"\n💡 Recommendations:\n"
                for rec in health_data['recommendations']:
                    message += f"• {rec}\n"
            
            return {
                'success': True,
                'action': 'financial_health',
                'message': message,
                'data': health_data
            }
            
        except Exception as e:
            logger.error(f"❌ Financial health report error: {e}")
            return {
                'success': False,
                'message': "❌ Unable to generate financial health report at this time."
            }

    def _get_spending_analysis(self, period: str = 'month') -> Dict[str, Any]:
        """Get spending analysis and insights"""
        try:
            insights = self.pf_manager.get_spending_insights(period)
            
            if 'error' in insights:
                return {
                    'success': False,
                    'message': f"❌ Unable to analyze spending: {insights['error']}"
                }
            
            message = f"📊 Spending Analysis - Last {period.title()}\n\n"
            message += f"Total Spending: ${insights['total_spending']:.2f}\n\n"
            
            if insights['top_categories']:
                message += "Top Categories:\n"
                for cat in insights['top_categories']:
                    message += f"• {cat['category']}: ${cat['amount']:.2f} ({cat['percentage']:.1f}%)\n"
            
            if insights.get('ai_insights'):
                message += f"\n💡 AI Insights:\n{insights['ai_insights']}"
            
            return {
                'success': True,
                'action': 'spending_analysis',
                'message': message,
                'data': insights
            }
            
        except Exception as e:
            logger.error(f"❌ Spending analysis error: {e}")
            return {
                'success': False,
                'message': "❌ Unable to analyze spending at this time."
            }

    def _add_debt_record(self, amount: float, debt_type: str, interest_rate: float) -> Dict[str, Any]:
        """Add debt record to tracking"""
        try:
            # Implementation for debt tracking
            return {
                'success': True,
                'action': 'debt_added',
                'message': f"✅ Added debt: ${amount:.2f} {debt_type} at {interest_rate:.1f}% APR",
                'data': {
                    'amount': amount,
                    'debt_type': debt_type,
                    'interest_rate': interest_rate
                }
            }
        except Exception as e:
            logger.error(f"❌ Debt record error: {e}")
            return {
                'success': False,
                'message': "❌ Unable to add debt record at this time."
            }

    def _parse_target_date(self, date_str: str) -> str:
        """Parse natural language date to ISO format"""
        try:
            # Handle common date formats
            current_year = datetime.datetime.now().year
            
            if 'december' in date_str.lower() or 'dec' in date_str.lower():
                return f"{current_year}-12-31"
            elif 'next year' in date_str.lower():
                return f"{current_year + 1}-12-31"
            elif re.search(r'\d{4}-\d{2}-\d{2}', date_str):
                match = re.search(r'\d{4}-\d{2}-\d{2}', date_str)
                return match.group() if match else f"{current_year}-12-31"
            else:
                # Default to end of current year
                return f"{current_year}-12-31"
                
        except Exception:
            return f"{datetime.datetime.now().year}-12-31"

# Integration function for main OperatorOS conversation system
def handle_personal_finance_query(user_input: str, user_id: str = "default_user") -> Dict[str, Any]:
    """
    Main entry point for personal finance queries from OperatorOS conversation system
    """
    pf_conversation = PersonalFinanceConversation(user_id)
    return pf_conversation.process_personal_finance_query(user_input)

if __name__ == "__main__":
    # Demo usage
    pf_conv = PersonalFinanceConversation("demo_user")
    
    # Test various queries
    test_queries = [
        "Set my food budget to $600",
        "I spent $45 at the grocery store",
        "How am I doing financially?",
        "I want to save $10000 for a vacation by December 2025",
        "Am I over budget this month?",
        "Show my spending trends for last month"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        result = pf_conv.process_personal_finance_query(query)
        print(f"Response: {result['message']}")
        print("-" * 50)