import logging
import random
from typing import Dict, Any, List
from datetime import datetime
from agent_pools import SpecializedAgentPools
from business_automation import BusinessAutomationEngine

class DemoRunner:
    """
    Interactive demonstration system for OperatorOS
    Showcases capabilities of each agent pool through Replit Agent
    """
    
    def __init__(self):
        self.agent_pools = SpecializedAgentPools()
        self.business_automation = BusinessAutomationEngine()
        
        # Demo scenarios for each domain
        self.demo_scenarios = {
            'healthcare': [
                {
                    'title': 'Symptom Analysis Demo',
                    'query': 'I have persistent headaches, fatigue, and occasional dizziness for the past week',
                    'description': 'Demonstrates medical symptom analysis and health guidance'
                },
                {
                    'title': 'Medication Information Demo',
                    'query': 'Can you tell me about ibuprofen side effects and proper dosage?',
                    'description': 'Shows medication information and safety guidance'
                },
                {
                    'title': 'Health Screening Demo',
                    'query': 'What health screenings should a 35-year-old male get annually?',
                    'description': 'Preventive health screening recommendations'
                }
            ],
            'financial': [
                {
                    'title': 'Stock Analysis Demo',
                    'query': 'Analyze Apple (AAPL) stock performance and provide investment recommendation',
                    'description': 'Comprehensive stock analysis with investment insights'
                },
                {
                    'title': 'Portfolio Diversification Demo',
                    'query': 'I have $10,000 to invest. How should I diversify my portfolio for moderate risk?',
                    'description': 'Portfolio allocation and diversification strategy'
                },
                {
                    'title': 'Market Trend Analysis Demo',
                    'query': 'What are the current trends in the tech sector and should I invest now?',
                    'description': 'Market analysis and sector-specific insights'
                }
            ],
            'sports': [
                {
                    'title': 'Game Prediction Demo',
                    'query': 'Predict the outcome of tonight\'s Lakers vs Warriors game with analysis',
                    'description': 'Statistical game prediction with reasoning'
                },
                {
                    'title': 'Fantasy Sports Demo',
                    'query': 'Who should I start in my fantasy football lineup this week?',
                    'description': 'Fantasy sports recommendations and player analysis'
                },
                {
                    'title': 'Sports Betting Strategy Demo',
                    'query': 'Create a betting strategy for this weekend\'s NFL games',
                    'description': 'Responsible betting strategy with odds analysis'
                }
            ],
            'business': [
                {
                    'title': 'Workflow Optimization Demo',
                    'query': 'Our customer service team takes too long to respond to tickets. How can we optimize this process?',
                    'description': 'Business process optimization and automation recommendations'
                },
                {
                    'title': 'Team Productivity Demo',
                    'query': 'How can I improve my remote team\'s productivity and collaboration?',
                    'description': 'Team management and productivity enhancement strategies'
                },
                {
                    'title': 'Business Automation Demo',
                    'query': 'What aspects of our sales process can be automated to increase efficiency?',
                    'description': 'Sales process automation and efficiency improvements'
                }
            ],
            'general': [
                {
                    'title': 'Research Assistant Demo',
                    'query': 'Explain the latest developments in artificial intelligence and their impact on society',
                    'description': 'Comprehensive research and analysis on complex topics'
                },
                {
                    'title': 'Problem Solving Demo',
                    'query': 'I\'m planning a trip to Japan for 2 weeks. Help me create an itinerary and budget',
                    'description': 'Complex planning and problem-solving assistance'
                },
                {
                    'title': 'Educational Demo',
                    'query': 'Teach me about quantum computing in a way that\'s easy to understand',
                    'description': 'Educational content with clear explanations'
                }
            ]
        }
        
        logging.info("🎬 Demo Runner initialized with interactive scenarios")

    def run_demo(self, demo_type: str, user_id: int, specific_scenario: Optional[int] = None) -> Dict[str, Any]:
        """Run interactive demonstration for specified agent type"""
        try:
            if demo_type not in self.demo_scenarios:
                return self._handle_invalid_demo_type(demo_type)
            
            # Select scenario
            scenarios = self.demo_scenarios[demo_type]
            if specific_scenario is not None and 0 <= specific_scenario < len(scenarios):
                scenario = scenarios[specific_scenario]
            else:
                scenario = random.choice(scenarios)
            
            logging.info(f"🎬 Running {demo_type} demo: {scenario['title']}")
            
            # Execute the demo scenario
            demo_result = self._execute_demo_scenario(demo_type, scenario, user_id)
            
            # Format the complete demo response
            demo_content = self._format_demo_response(demo_type, scenario, demo_result)
            
            return {
                'success': True,
                'demo_type': demo_type,
                'scenario_title': scenario['title'],
                'demo_content': demo_content,
                'execution_result': demo_result
            }
            
        except Exception as e:
            logging.error(f"Error running {demo_type} demo: {e}")
            return {
                'error': True,
                'message': f"Demo execution failed: {str(e)}",
                'demo_type': demo_type
            }

    def _execute_demo_scenario(self, demo_type: str, scenario: Dict[str, Any], user_id: int) -> Dict[str, Any]:
        """Execute the actual demo scenario"""
        try:
            if demo_type == 'business':
                # Use business automation engine for business demos
                result = self.business_automation.analyze_workflow(scenario['query'], user_id)
                if result.get('success'):
                    return {
                        'success': True,
                        'response': self.business_automation.format_business_analysis_for_display(result),
                        'analysis_data': result
                    }
                else:
                    raise Exception(result.get('error', 'Business analysis failed'))
            else:
                # Use agent pools for other demos
                result = self.agent_pools.route_query(scenario['query'], user_id, demo_type)
                
                if result.get('error'):
                    raise Exception(result.get('message', 'Agent pool processing failed'))
                
                return {
                    'success': True,
                    'response': result['result']['response'],
                    'pool_used': result.get('pool_used'),
                    'ai_metadata': result['result'].get('ai_metadata', {})
                }
                
        except Exception as e:
            logging.error(f"Error executing demo scenario: {e}")
            return {
                'success': False,
                'error': str(e),
                'fallback_response': self._get_demo_fallback(demo_type)
            }

    def _format_demo_response(self, demo_type: str, scenario: Dict[str, Any], demo_result: Dict[str, Any]) -> str:
        """Format complete demo response for conversational display"""
        try:
            # Demo icons
            demo_icons = {
                'healthcare': '🏥',
                'financial': '💰',
                'sports': '🏈',
                'business': '💼',
                'general': '🤖'
            }
            
            demo_names = {
                'healthcare': 'Healthcare AI Specialist',
                'financial': 'Financial Analysis Expert', 
                'sports': 'Sports Analytics Expert',
                'business': 'Business Automation Consultant',
                'general': 'General Knowledge Assistant'
            }
            
            icon = demo_icons.get(demo_type, '🎬')
            name = demo_names.get(demo_type, 'AI Assistant')
            
            formatted = f"{icon} **{name.upper()} DEMONSTRATION**\n"
            formatted += "=" * 60 + "\n\n"
            
            # Demo scenario info
            formatted += f"🎯 **Demo Scenario**: {scenario['title']}\n"
            formatted += f"📋 **Description**: {scenario['description']}\n"
            formatted += f"❓ **Sample Query**: \"{scenario['query']}\"\n\n"
            
            formatted += "🔄 **PROCESSING DEMONSTRATION...**\n"
            formatted += "-" * 50 + "\n\n"
            
            # Demo execution result
            if demo_result.get('success'):
                formatted += f"✅ **DEMO RESULT**:\n\n"
                formatted += demo_result['response']
                
                # Add metadata if available
                if demo_result.get('ai_metadata'):
                    metadata = demo_result['ai_metadata']
                    formatted += f"\n\n🔍 **Demo Technical Details**:\n"
                    formatted += f"├── AI Provider: {metadata.get('provider', 'N/A')}\n"
                    formatted += f"├── Model Used: {metadata.get('model', 'N/A')}\n"
                    if metadata.get('conversation_id'):
                        formatted += f"└── Conversation ID: {metadata['conversation_id']}\n"
            else:
                formatted += f"❌ **DEMO EXECUTION FAILED**:\n\n"
                formatted += demo_result.get('error', 'Unknown error occurred')
                
                if demo_result.get('fallback_response'):
                    formatted += f"\n\n📝 **Fallback Response**:\n{demo_result['fallback_response']}"
            
            # Demo conclusion
            formatted += f"\n\n" + "=" * 60 + "\n"
            formatted += f"🎬 **DEMONSTRATION COMPLETE**\n\n"
            
            # Provide next steps
            formatted += f"💡 **What you can do next**:\n"
            formatted += f"├── Try your own {demo_type} question\n"
            formatted += f"├── Run another demo: 'demo [type]'\n"
            formatted += f"├── View all capabilities: 'help'\n"
            formatted += f"└── Check system status: 'status'\n\n"
            
            # Additional demo scenarios
            other_scenarios = [s for s in self.demo_scenarios[demo_type] if s['title'] != scenario['title']]
            if other_scenarios:
                formatted += f"🎭 **Other {demo_type.title()} Demos Available**:\n"
                for i, other_scenario in enumerate(other_scenarios[:2], 1):
                    formatted += f"{i}. {other_scenario['title']}\n"
                formatted += "\n"
            
            formatted += f"⏰ **Demo completed at**: {datetime.now().strftime('%H:%M:%S')}"
            
            return formatted
            
        except Exception as e:
            logging.error(f"Error formatting demo response: {e}")
            return f"❌ Error formatting demo: {str(e)}"

    def _handle_invalid_demo_type(self, demo_type: str) -> Dict[str, Any]:
        """Handle invalid demo type request"""
        available_types = list(self.demo_scenarios.keys())
        
        error_response = f"❌ **Unknown Demo Type**: '{demo_type}'\n\n"
        error_response += f"🎬 **Available Demo Types**:\n"
        
        for demo_name in available_types:
            scenarios_count = len(self.demo_scenarios[demo_name])
            error_response += f"├── **{demo_name}**: {scenarios_count} demonstration scenarios\n"
        
        error_response += f"\n💡 **Usage Examples**:\n"
        error_response += f"• 'demo healthcare' - Run healthcare demonstration\n"
        error_response += f"• 'demo financial' - Run financial analysis demo\n"
        error_response += f"• 'demo sports' - Run sports analytics demo\n"
        error_response += f"• 'demo business' - Run business automation demo\n"
        error_response += f"• 'demo general' - Run general AI demo"
        
        return {
            'error': True,
            'message': error_response,
            'available_types': available_types
        }

    def _get_demo_fallback(self, demo_type: str) -> str:
        """Get fallback response when demo execution fails"""
        fallbacks = {
            'healthcare': "Healthcare AI Demo: This would demonstrate medical symptom analysis, medication information, and health guidance capabilities.",
            'financial': "Financial AI Demo: This would showcase stock analysis, investment recommendations, and market trend insights.",
            'sports': "Sports AI Demo: This would display game predictions, player analysis, and betting strategy recommendations.",
            'business': "Business AI Demo: This would show workflow optimization, process automation, and productivity enhancement strategies.",
            'general': "General AI Demo: This would exhibit research capabilities, problem-solving assistance, and educational content delivery."
        }
        
        return fallbacks.get(demo_type, f"Demo for {demo_type} is temporarily unavailable.")

    def list_available_demos(self) -> str:
        """List all available demonstration scenarios"""
        try:
            demo_list = "🎬 **AVAILABLE DEMONSTRATIONS**\n"
            demo_list += "=" * 50 + "\n\n"
            
            for demo_type, scenarios in self.demo_scenarios.items():
                demo_icons = {
                    'healthcare': '🏥',
                    'financial': '💰', 
                    'sports': '🏈',
                    'business': '💼',
                    'general': '🤖'
                }
                
                icon = demo_icons.get(demo_type, '🎬')
                demo_list += f"{icon} **{demo_type.upper()} DEMOS**:\n"
                
                for i, scenario in enumerate(scenarios, 1):
                    demo_list += f"{i}. {scenario['title']}\n"
                    demo_list += f"   └── {scenario['description']}\n"
                
                demo_list += "\n"
            
            demo_list += f"💡 **How to run demos**:\n"
            demo_list += f"• 'demo healthcare' - Random healthcare demo\n"
            demo_list += f"• 'demo financial' - Random financial demo\n"
            demo_list += f"• 'demo [type]' - Any available demo type\n\n"
            
            demo_list += f"🎯 **Interactive Features**:\n"
            demo_list += f"• Real AI processing with actual responses\n"
            demo_list += f"• Live system integration demonstration\n"
            demo_list += f"• Context-aware conversation handling\n"
            demo_list += f"• Multi-domain expertise showcase"
            
            return demo_list
            
        except Exception as e:
            logging.error(f"Error listing demos: {e}")
            return f"❌ Error listing demonstrations: {str(e)}"

    def run_interactive_demo_sequence(self, user_id: int) -> Dict[str, Any]:
        """Run an interactive sequence showing multiple capabilities"""
        try:
            sequence_content = "🎭 **INTERACTIVE DEMO SEQUENCE**\n"
            sequence_content += "=" * 50 + "\n\n"
            sequence_content += "🚀 **Welcome to OperatorOS Comprehensive Demo!**\n\n"
            sequence_content += "I'll demonstrate capabilities across all agent pools:\n\n"
            
            demo_results = []
            
            # Run one demo from each category
            for demo_type in ['healthcare', 'financial', 'sports', 'business']:
                try:
                    demo_result = self.run_demo(demo_type, user_id)
                    demo_results.append({
                        'type': demo_type,
                        'success': demo_result.get('success', False),
                        'title': demo_result.get('scenario_title', 'Unknown')
                    })
                    
                    sequence_content += f"\n{'='*30}\n"
                    sequence_content += demo_result.get('demo_content', f"{demo_type} demo failed")
                    sequence_content += f"\n{'='*30}\n"
                    
                except Exception as e:
                    demo_results.append({
                        'type': demo_type,
                        'success': False,
                        'error': str(e)
                    })
            
            # Sequence summary
            successful_demos = sum(1 for result in demo_results if result.get('success'))
            sequence_content += f"\n\n🎯 **DEMO SEQUENCE SUMMARY**:\n"
            sequence_content += f"├── Completed: {successful_demos}/{len(demo_results)} demonstrations\n"
            sequence_content += f"├── Coverage: {len(demo_results)} agent pools tested\n"
            sequence_content += f"└── Success Rate: {(successful_demos/len(demo_results)*100):.1f}%\n\n"
            
            sequence_content += f"✨ **What you've seen**:\n"
            sequence_content += f"• Multi-domain AI expertise\n"
            sequence_content += f"• Context-aware responses\n"
            sequence_content += f"• Real-time processing\n"
            sequence_content += f"• Enterprise-grade capabilities\n\n"
            
            sequence_content += f"🚀 **Ready to use OperatorOS?** Try asking your own questions!"
            
            return {
                'success': True,
                'demo_type': 'interactive_sequence',
                'demo_content': sequence_content,
                'demo_results': demo_results,
                'completion_rate': successful_demos / len(demo_results)
            }
            
        except Exception as e:
            logging.error(f"Error running interactive demo sequence: {e}")
            return {
                'error': True,
                'message': f"Interactive demo sequence failed: {str(e)}"
            }

    def get_demo_statistics(self) -> Dict[str, Any]:
        """Get statistics about available demonstrations"""
        try:
            stats = {
                'total_demo_types': len(self.demo_scenarios),
                'total_scenarios': sum(len(scenarios) for scenarios in self.demo_scenarios.values()),
                'scenarios_by_type': {},
                'demo_features': [
                    'Real AI processing',
                    'Live system integration', 
                    'Context-aware responses',
                    'Multi-domain expertise',
                    'Interactive demonstrations'
                ]
            }
            
            for demo_type, scenarios in self.demo_scenarios.items():
                stats['scenarios_by_type'][demo_type] = {
                    'count': len(scenarios),
                    'titles': [scenario['title'] for scenario in scenarios]
                }
            
            return stats
            
        except Exception as e:
            logging.error(f"Error getting demo statistics: {e}")
            return {'error': str(e)}

    def format_demo_help(self) -> str:
        """Format comprehensive demo help information"""
        help_text = "🎬 **DEMONSTRATION SYSTEM HELP**\n"
        help_text += "=" * 50 + "\n\n"
        
        help_text += "🎯 **Available Commands**:\n"
        help_text += "├── 'demo [type]' - Run specific demo type\n"
        help_text += "├── 'demo list' - List all available demos\n"
        help_text += "├── 'demo sequence' - Run interactive sequence\n"
        help_text += "└── 'demo help' - This help information\n\n"
        
        help_text += "🏥 **Demo Types**:\n"
        for demo_type, scenarios in self.demo_scenarios.items():
            help_text += f"├── **{demo_type}**: {len(scenarios)} scenarios available\n"
        help_text += "\n"
        
        help_text += "✨ **Demo Features**:\n"
        help_text += "• Real AI processing with live responses\n"
        help_text += "• Multiple scenarios per domain\n"
        help_text += "• Interactive system integration\n"
        help_text += "• Educational and practical examples\n"
        help_text += "• Context-aware demonstrations\n\n"
        
        help_text += "💡 **Example Usage**:\n"
        help_text += "• 'demo healthcare' - Medical analysis demo\n"
        help_text += "• 'demo financial' - Investment advice demo\n"
        help_text += "• 'demo sports' - Game prediction demo\n"
        help_text += "• 'demo business' - Workflow optimization demo\n"
        help_text += "• 'demo general' - Research assistance demo"
        
        return help_text

