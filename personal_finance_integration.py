"""
Personal Finance Integration for OperatorOS Main Conversation System
Extends the main conversation manager with personal finance capabilities
"""

import re
import logging
from typing import Dict, Any, Optional
from personal_finance_conversation import handle_personal_finance_query

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonalFinanceIntegration:
    """
    Integration layer between main OperatorOS conversation system and personal finance capabilities
    """
    
    def __init__(self):
        # Personal finance keywords and patterns
        self.finance_keywords = [
            'budget', 'expense', 'spent', 'save', 'saving', 'money', 'financial', 'finance',
            'debt', 'loan', 'investment', 'portfolio', 'goal', 'bank', 'payment', 'cost',
            'price', 'income', 'salary', 'emergency fund', 'retirement', 'mortgage'
        ]
        
        # Specific finance command patterns
        self.finance_patterns = [
            r'set.*budget',
            r'i spent',
            r'expense of',
            r'paid.*for',
            r'save.*for',
            r'financial health',
            r'budget status',
            r'spending.*trend',
            r'how.*doing.*financial',
            r'debt.*payoff',
            r'investment.*advice'
        ]
        
        logger.info("💰 Personal Finance Integration initialized")

    def is_personal_finance_query(self, user_input: str) -> bool:
        """
        Determine if a user query is related to personal finance
        """
        user_input_lower = user_input.lower()
        
        # Check for specific finance patterns first
        for pattern in self.finance_patterns:
            if re.search(pattern, user_input_lower):
                return True
        
        # Check for finance keywords
        for keyword in self.finance_keywords:
            if keyword in user_input_lower:
                return True
        
        return False

    def handle_finance_query(self, user_input: str, user_id: str = "default_user") -> Dict[str, Any]:
        """
        Handle personal finance query and return formatted response for main conversation system
        """
        try:
            # Process the finance query
            finance_result = handle_personal_finance_query(user_input, user_id)
            
            if finance_result['success']:
                return {
                    'handled': True,
                    'response_type': 'personal_finance',
                    'message': finance_result['message'],
                    'action': finance_result.get('action', 'unknown'),
                    'data': finance_result.get('data', {}),
                    'suggestion': self._get_follow_up_suggestion(finance_result)
                }
            else:
                return {
                    'handled': True,
                    'response_type': 'personal_finance_error',
                    'message': finance_result['message'],
                    'suggestion': "Try rephrasing your financial query or ask for specific help with budgets, expenses, or financial goals."
                }
                
        except Exception as e:
            logger.error(f"❌ Personal finance integration error: {e}")
            return {
                'handled': False,
                'error': str(e),
                'message': "I encountered an issue processing your financial request. Please try again or ask for help with specific finance topics."
            }

    def _get_follow_up_suggestion(self, finance_result: Dict[str, Any]) -> str:
        """
        Generate follow-up suggestions based on the finance action taken
        """
        action = finance_result.get('action', '')
        
        if action == 'budget_set':
            return "You can now add expenses with 'I spent $X on Y' or check your budget status with 'Am I over budget?'"
        elif action == 'expense_added':
            return "Try asking 'Show my spending trends' or 'How am I doing financially?' to see insights."
        elif action == 'goal_set':
            return "Ask 'How can I reach my goal faster?' or set another financial goal."
        elif action == 'financial_health':
            return "You can ask for specific advice like 'How can I improve my financial score?' or set new goals."
        elif action == 'spending_analysis':
            return "Try asking 'How can I reduce spending?' or 'What should I budget for next month?'"
        else:
            return "Ask me about budgets, expenses, financial goals, or spending analysis anytime!"

    def get_finance_capabilities_summary(self) -> str:
        """
        Return a summary of personal finance capabilities for help/info requests
        """
        return """
🏦 Personal Finance Capabilities:

Budget Management:
• "Set my food budget to $600"
• "Budget $300 for transportation"

Expense Tracking:
• "I spent $45 at the store"
• "Expense of $25 for coffee"

Financial Goals:
• "I want to save $10,000 for vacation by December"
• "Save $5,000 for emergency fund"

Financial Health:
• "How am I doing financially?"
• "What's my financial health score?"

Spending Analysis:
• "Show my spending trends"
• "Where am I spending my money?"

General Advice:
• "Should I pay off debt or invest?"
• "How can I save more money?"
"""

# Factory function for easy integration
def create_personal_finance_integration() -> PersonalFinanceIntegration:
    """Create and return PersonalFinanceIntegration instance"""
    return PersonalFinanceIntegration()

# Main integration function for conversation manager
def process_personal_finance_if_relevant(user_input: str, user_id: str = "default_user") -> Optional[Dict[str, Any]]:
    """
    Main integration point for conversation manager
    Returns None if not a finance query, otherwise returns processed result
    """
    pf_integration = PersonalFinanceIntegration()
    
    if pf_integration.is_personal_finance_query(user_input):
        return pf_integration.handle_finance_query(user_input, user_id)
    
    return None

if __name__ == "__main__":
    # Test the integration
    pf_integration = PersonalFinanceIntegration()
    
    test_queries = [
        "Set my food budget to $500",
        "I spent $30 on lunch",
        "How are my finances looking?",
        "What is the weather today?",  # Non-finance query
        "Help me save money for a car"
    ]
    
    print("🧪 Testing Personal Finance Integration")
    print("=" * 50)
    
    for query in test_queries:
        is_finance = pf_integration.is_personal_finance_query(query)
        print(f"\nQuery: {query}")
        print(f"Is Finance Query: {is_finance}")
        
        if is_finance:
            result = pf_integration.handle_finance_query(query)
            print(f"Response: {result['message']}")
            if result.get('suggestion'):
                print(f"Suggestion: {result['suggestion']}")
        print("-" * 30)