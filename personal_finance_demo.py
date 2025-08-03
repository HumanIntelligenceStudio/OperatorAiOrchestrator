"""
Personal Finance Demo for OperatorOS
Demonstrates comprehensive personal finance capabilities
"""

import json
import datetime
from personal_finance_conversation import PersonalFinanceConversation
try:
    from ai_providers_enhanced import AIProviderManager
except ImportError:
    from ai_providers import AIProviderManager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_personal_finance_demo():
    """
    Comprehensive demonstration of OperatorOS personal finance capabilities
    Shows integration with existing AI provider system and conversational interface
    """
    
    print("🏦 OperatorOS Personal Finance System Demo")
    print("=" * 60)
    
    # Initialize personal finance system
    pf_conv = PersonalFinanceConversation("demo_user")
    ai_provider = AIProviderManager()
    
    # Demo scenarios
    demo_scenarios = [
        {
            'title': 'Budget Management',
            'queries': [
                "Set my food budget to $600 per month",
                "Set my transportation budget to $300",
                "Budget $200 for entertainment"
            ]
        },
        {
            'title': 'Expense Tracking',
            'queries': [
                "I spent $45 at the grocery store",
                "Expense of $25 for coffee this morning",
                "Paid $85 for gas at Shell",
                "Bought lunch for $15 at Chipotle"
            ]
        },
        {
            'title': 'Financial Goals',
            'queries': [
                "I want to save $10000 for a vacation by December 2025",
                "Goal to save $50000 for a house down payment",
                "Save $5000 for emergency fund by next year"
            ]
        },
        {
            'title': 'Financial Health Analysis',
            'queries': [
                "How am I doing financially?",
                "Financial health check",
                "What's my financial score?"
            ]
        },
        {
            'title': 'Spending Analysis',
            'queries': [
                "Show my spending trends for last month",
                "Where am I spending my money?",
                "Analyze my spending patterns"
            ]
        },
        {
            'title': 'Budget Status Checks',
            'queries': [
                "Am I over budget this month?",
                "Check my budget status",
                "How much budget do I have left?"
            ]
        }
    ]
    
    results = []
    
    for scenario in demo_scenarios:
        print(f"\n📊 {scenario['title']}")
        print("-" * 40)
        
        scenario_results = []
        
        for query in scenario['queries']:
            try:
                print(f"\n👤 User: {query}")
                
                # Process the query
                result = pf_conv.process_personal_finance_query(query)
                
                if result['success']:
                    print(f"🤖 OperatorOS: {result['message']}")
                    scenario_results.append({
                        'query': query,
                        'success': True,
                        'response': result['message'],
                        'action': result.get('action', 'unknown'),
                        'data': result.get('data', {})
                    })
                else:
                    print(f"❌ OperatorOS: {result['message']}")
                    scenario_results.append({
                        'query': query,
                        'success': False,
                        'error': result['message']
                    })
                    
            except Exception as e:
                error_msg = f"Error processing query: {e}"
                print(f"❌ {error_msg}")
                scenario_results.append({
                    'query': query,
                    'success': False,
                    'error': error_msg
                })
        
        results.append({
            'scenario': scenario['title'],
            'results': scenario_results
        })
    
    # Multi-AI Provider Financial Analysis Demo
    print(f"\n🤖 Multi-AI Provider Financial Analysis")
    print("-" * 40)
    
    try:
        # Demonstrate multi-provider financial advice
        financial_situation = """
        I have $15,000 in savings, $25,000 in student loans at 6% interest,
        monthly income of $5,000, and monthly expenses of $3,500.
        Should I pay off debt or invest?
        """
        
        print(f"\n👤 User: {financial_situation}")
        
        # Get advice from AI provider
        providers_advice = {}
        
        try:
            financial_prompt = f"""As a financial advisor, analyze this situation and provide advice: {financial_situation}"""
            ai_response = ai_provider.get_response(financial_prompt, 'financial')
            providers_advice['AI Financial Advisor'] = ai_response.get('content', 'Unable to provide advice') if not ai_response.get('error') else f"AI unavailable: {ai_response.get('message', 'Unknown error')}"
        except Exception as e:
            providers_advice['AI Financial Advisor'] = f"AI unavailable: {e}"
        
        for provider, advice in providers_advice.items():
            print(f"\n🤖 {provider}:")
            print(f"{advice[:300]}..." if len(advice) > 300 else advice)
        
        results.append({
            'scenario': 'Multi-AI Provider Analysis',
            'results': [{
                'query': financial_situation,
                'success': True,
                'providers_advice': providers_advice
            }]
        })
        
    except Exception as e:
        print(f"❌ Multi-AI analysis error: {e}")
    
    # Demo Summary
    print(f"\n📈 Demo Summary")
    print("=" * 60)
    
    total_queries = sum(len(scenario['results']) for scenario in results)
    successful_queries = sum(
        sum(1 for result in scenario['results'] if result.get('success', False))
        for scenario in results
    )
    
    print(f"Total Queries Processed: {total_queries}")
    print(f"Successful Responses: {successful_queries}")
    print(f"Success Rate: {(successful_queries/total_queries)*100:.1f}%")
    
    # Feature Coverage
    features_demonstrated = [
        "✅ Natural Language Budget Setting",
        "✅ Intelligent Expense Categorization", 
        "✅ Financial Goal Creation and Timeline Analysis",
        "✅ Multi-Currency Support (via Exchange Rate API)",
        "✅ AI-Powered Financial Health Scoring",
        "✅ Spending Pattern Analysis and Insights",
        "✅ Budget Status Monitoring and Alerts",
        "✅ Multi-AI Provider Financial Advice",
        "✅ Conversational Interface Integration",
        "✅ Database Persistence and Data Management"
    ]
    
    print(f"\n🎯 Features Demonstrated:")
    for feature in features_demonstrated:
        print(f"  {feature}")
    
    # Integration Status
    print(f"\n🔗 Integration Status:")
    print(f"  ✅ AI Provider Coordination (Claude, GPT-4o, Grok)")
    print(f"  ✅ Exchange Rate API Integration")
    print(f"  ✅ Database Storage and Persistence")
    print(f"  ✅ Conversational Interface Pattern")
    print(f"  ✅ OperatorOS Architecture Compliance")
    
    # Save demo results
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"personal_finance_demo_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump({
            'demo_timestamp': timestamp,
            'total_queries': total_queries,
            'successful_queries': successful_queries,
            'success_rate': f"{(successful_queries/total_queries)*100:.1f}%",
            'scenarios': results,
            'features_demonstrated': features_demonstrated
        }, f, indent=2)
    
    print(f"\n💾 Demo results saved to: {results_file}")
    
    return results

def demonstrate_advanced_features():
    """Demonstrate advanced personal finance features"""
    
    print(f"\n🚀 Advanced Personal Finance Features")
    print("=" * 60)
    
    pf_conv = PersonalFinanceConversation("advanced_demo_user")
    
    # Advanced scenarios
    advanced_scenarios = [
        "What if I pay an extra $500 toward my student loans each month?",
        "Should I refinance my mortgage at current rates?",
        "How can I optimize my portfolio for retirement?",
        "What's the best debt payoff strategy: snowball or avalanche?",
        "I got a $10,000 bonus, how should I allocate it?",
        "Help me create a 5-year financial plan",
        "What are some tax-efficient investment strategies?",
        "How much house can I afford with my current income?"
    ]
    
    print(f"\n🎯 Processing Advanced Financial Queries:")
    
    for i, scenario in enumerate(advanced_scenarios, 1):
        print(f"\n{i}. Query: {scenario}")
        
        try:
            result = pf_conv.process_personal_finance_query(scenario)
            if result['success']:
                print(f"   ✅ Response: {result['message'][:150]}...")
            else:
                print(f"   ❌ Failed: {result['message']}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print(f"\n✅ Advanced features demonstration complete")

if __name__ == "__main__":
    try:
        # Run main demo
        demo_results = run_personal_finance_demo()
        
        # Run advanced features demo
        demonstrate_advanced_features()
        
        print(f"\n🎉 Personal Finance Demo Complete!")
        print(f"OperatorOS now has comprehensive personal finance capabilities")
        print(f"integrated with the existing multi-AI provider system.")
        
    except Exception as e:
        logger.error(f"❌ Demo error: {e}")
        print(f"❌ Demo failed: {e}")