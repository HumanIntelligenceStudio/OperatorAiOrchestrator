import logging
import random
from typing import Dict, List, Optional, Any
from datetime import datetime
from ai_providers_enhanced import AIProviderManager

class SpecializedAgentPools:
    """
    Specialized domain agents accessible through Replit Agent
    Each pool handles specific types of queries and provides domain expertise
    """
    
    def __init__(self):
        self.ai_provider_manager = AIProviderManager()
        
        # Pool configurations
        self.pool_configs = {
            'healthcare': {
                'name': 'Healthcare AI Specialists',
                'description': 'Medical advice, symptom analysis, and health guidance',
                'specialties': ['symptom_analysis', 'medication_info', 'health_screening', 'wellness_advice', 'mental_health'],
                'response_style': 'professional_medical'
            },
            'financial': {
                'name': 'Financial Analysis Team',
                'description': 'Investment advice, market analysis, and financial planning',
                'specialties': ['stock_analysis', 'investment_strategy', 'market_trends', 'financial_planning', 'risk_assessment'],
                'response_style': 'analytical_financial'
            },
            'sports': {
                'name': 'Sports Analytics Experts',
                'description': 'Game predictions, player analysis, and betting strategies',
                'specialties': ['game_predictions', 'player_stats', 'team_analysis', 'betting_strategy', 'fantasy_advice'],
                'response_style': 'analytical_sports'
            },
            'business': {
                'name': 'Business Automation Consultants',
                'description': 'Process optimization, workflow automation, and strategic planning',
                'specialties': ['process_automation', 'workflow_optimization', 'strategic_planning', 'team_management', 'efficiency_analysis'],
                'response_style': 'professional_business'
            },
            'general': {
                'name': 'General Knowledge Specialists',
                'description': 'Comprehensive assistance across various topics',
                'specialties': ['information_retrieval', 'research_assistance', 'problem_solving', 'creative_thinking', 'general_advice'],
                'response_style': 'conversational'
            }
        }
        
        logging.info("🏥💰🏈💼📚 Specialized Agent Pools initialized")

    def route_query(self, query: str, user_id: int, preferred_pool: Optional[str] = None) -> Dict[str, Any]:
        """Route query to appropriate agent pool based on content analysis or user preference"""
        try:
            # Use preferred pool if specified
            if preferred_pool and preferred_pool in self.pool_configs:
                pool_type = preferred_pool
            else:
                # Auto-detect appropriate pool based on query content
                pool_type = self._analyze_query_type(query)
            
            logging.info(f"🎯 Routing query to {pool_type} pool: {query[:100]}...")
            
            # Process query through specialized agent
            result = self._process_specialized_query(query, pool_type, user_id)
            
            return {
                'pool_used': pool_type,
                'pool_name': self.pool_configs[pool_type]['name'],
                'result': result
            }
            
        except Exception as e:
            logging.error(f"Error routing query: {e}")
            return {
                'error': True,
                'message': f"Query routing failed: {str(e)}"
            }

    def _analyze_query_type(self, query: str) -> str:
        """Analyze query content to determine best agent pool"""
        query_lower = query.lower()
        
        # Healthcare keywords
        healthcare_keywords = [
            'pain', 'symptom', 'doctor', 'medical', 'health', 'sick', 'hurt', 'medication',
            'headache', 'fever', 'chest', 'stomach', 'back', 'joint', 'muscle', 'blood',
            'pressure', 'diabetes', 'heart', 'lung', 'kidney', 'liver', 'brain', 'anxiety',
            'depression', 'mental', 'therapy', 'treatment', 'diagnosis', 'disease', 'infection'
        ]
        
        # Financial keywords
        financial_keywords = [
            'invest', 'stock', 'money', 'finance', 'portfolio', 'market', 'trading', 'buy',
            'sell', 'price', 'return', 'profit', 'loss', 'dividend', 'bond', 'fund',
            'retirement', 'savings', 'budget', 'loan', 'mortgage', 'insurance', 'tax',
            'crypto', 'bitcoin', 'ethereum', 'nasdaq', 'sp500', 'dow', 'recession'
        ]
        
        # Sports keywords
        sports_keywords = [
            'game', 'team', 'player', 'score', 'bet', 'odds', 'prediction', 'fantasy',
            'football', 'basketball', 'baseball', 'soccer', 'hockey', 'tennis', 'golf',
            'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'stats', 'season', 'playoffs', 'championship'
        ]
        
        # Business keywords
        business_keywords = [
            'business', 'company', 'workflow', 'process', 'automation', 'management',
            'strategy', 'team', 'project', 'efficiency', 'productivity', 'operations',
            'marketing', 'sales', 'customer', 'revenue', 'growth', 'startup', 'enterprise',
            'optimize', 'scale', 'leadership', 'meeting', 'deadline', 'budget', 'roi'
        ]
        
        # Count keyword matches
        scores = {
            'healthcare': sum(1 for keyword in healthcare_keywords if keyword in query_lower),
            'financial': sum(1 for keyword in financial_keywords if keyword in query_lower),
            'sports': sum(1 for keyword in sports_keywords if keyword in query_lower),
            'business': sum(1 for keyword in business_keywords if keyword in query_lower),
            'general': 0  # Default fallback
        }
        
        # Return pool with highest score, or general if no clear match
        best_pool = max(scores.items(), key=lambda x: x[1])
        return best_pool[0] if best_pool[1] > 0 else 'general'

    def _process_specialized_query(self, query: str, pool_type: str, user_id: int) -> Dict[str, Any]:
        """Process query through specialized agent with domain-specific enhancements"""
        try:
            # Get enhanced context based on pool type
            context = self._build_pool_context(pool_type, query)
            
            # Get AI response using enhanced provider with assistants
            ai_response = self.ai_provider_manager.get_assistant_response(
                query=query,
                user_id=user_id,
                agent_type=pool_type,
                context=context
            )
            
            if ai_response.get('error'):
                raise Exception(ai_response.get('message', 'AI processing failed'))
            
            # Format response for conversational display
            formatted_response = self._format_pool_response(
                ai_response['response'], 
                pool_type, 
                query
            )
            
            return {
                'success': True,
                'response': formatted_response,
                'ai_metadata': {
                    'provider': ai_response.get('provider'),
                    'model': ai_response.get('model'),
                    'conversation_id': ai_response.get('conversation_id')
                }
            }
            
        except Exception as e:
            logging.error(f"Error processing {pool_type} query: {e}")
            return {
                'success': False,
                'error': str(e),
                'fallback_response': self._get_fallback_response(pool_type)
            }

    def _build_pool_context(self, pool_type: str, query: str) -> Dict[str, Any]:
        """Build specialized context for each agent pool"""
        base_context = {
            'pool_type': pool_type,
            'timestamp': datetime.utcnow().isoformat(),
            'response_format': 'conversational_replit'
        }
        
        if pool_type == 'healthcare':
            base_context.update({
                'medical_disclaimers': True,
                'professional_consultation_reminder': True,
                'empathy_level': 'high',
                'evidence_based': True
            })
        elif pool_type == 'financial':
            base_context.update({
                'risk_disclaimers': True,
                'data_sources': ['market_data', 'financial_reports'],
                'analysis_depth': 'comprehensive',
                'investment_risks_emphasis': True
            })
        elif pool_type == 'sports':
            base_context.update({
                'statistical_analysis': True,
                'confidence_levels': True,
                'responsible_gambling': True,
                'current_season_context': True
            })
        elif pool_type == 'business':
            base_context.update({
                'actionable_advice': True,
                'roi_consideration': True,
                'implementation_steps': True,
                'scalability_focus': True
            })
        
        return base_context

    def _format_pool_response(self, response: str, pool_type: str, original_query: str) -> str:
        """Format AI response for conversational display through Replit Agent"""
        
        # Pool-specific formatting
        pool_icons = {
            'healthcare': '🏥',
            'financial': '💰',
            'sports': '🏈',
            'business': '💼',
            'general': '🤖'
        }
        
        pool_names = {
            'healthcare': 'Healthcare AI Specialist',
            'financial': 'Financial Analysis Expert',
            'sports': 'Sports Analytics Expert',
            'business': 'Business Automation Consultant',
            'general': 'General Knowledge Assistant'
        }
        
        icon = pool_icons.get(pool_type, '🤖')
        name = pool_names.get(pool_type, 'AI Assistant')
        
        formatted_response = f"{icon} **{name} Response**\n"
        formatted_response += "=" * 50 + "\n\n"
        formatted_response += response
        
        # Add pool-specific footers
        if pool_type == 'healthcare':
            formatted_response += "\n\n⚠️ **Medical Disclaimer**: This information is for educational purposes only and should not replace professional medical advice. Please consult with healthcare professionals for medical concerns."
            
        elif pool_type == 'financial':
            formatted_response += "\n\n⚠️ **Investment Disclaimer**: Past performance does not guarantee future results. All investments carry risk. Consider your financial situation and consult with financial advisors before making investment decisions."
            
        elif pool_type == 'sports':
            formatted_response += "\n\n⚠️ **Sports Betting Disclaimer**: Predictions are based on analysis and statistics. Gambling involves risk. Please bet responsibly and within your means."
            
        elif pool_type == 'business':
            formatted_response += "\n\n💡 **Implementation Note**: Consider your specific business context, resources, and goals when implementing these recommendations. Test changes incrementally when possible."
        
        formatted_response += f"\n\n🎯 **Query processed by**: {name} Pool\n"
        formatted_response += f"⏰ **Response time**: {datetime.now().strftime('%H:%M:%S')}"
        
        return formatted_response

    def _get_fallback_response(self, pool_type: str) -> str:
        """Provide fallback response when AI processing fails"""
        fallbacks = {
            'healthcare': "I'm temporarily unable to provide medical information. Please consult with a healthcare professional for your medical concerns.",
            'financial': "I'm temporarily unable to provide financial analysis. Please consult financial resources or advisors for investment decisions.",
            'sports': "I'm temporarily unable to provide sports analysis. Please check current sports news and statistics from reliable sources.",
            'business': "I'm temporarily unable to provide business consulting. Please consider consulting with business professionals or resources.",
            'general': "I'm temporarily unable to process your request. Please try again or rephrase your question."
        }
        
        return fallbacks.get(pool_type, fallbacks['general'])

    def get_pool_status(self) -> Dict[str, Any]:
        """Get status of all agent pools for system monitoring"""
        status = {}
        
        for pool_type, config in self.pool_configs.items():
            # Mock pool metrics (in real implementation, these would be actual metrics)
            status[pool_type] = {
                'name': config['name'],
                'description': config['description'],
                'specialties': config['specialties'],
                'active_agents': random.randint(2, 8),
                'total_agents': random.randint(5, 12),
                'avg_response_time': round(random.uniform(1.2, 4.8), 1),
                'success_rate': round(random.uniform(92, 98), 1),
                'requests_today': random.randint(15, 150),
                'health_status': 'healthy'
            }
        
        return status

    def get_pool_capabilities(self) -> Dict[str, Any]:
        """Get detailed capabilities of each agent pool"""
        capabilities = {}
        
        for pool_type, config in self.pool_configs.items():
            capabilities[pool_type] = {
                'name': config['name'],
                'description': config['description'],
                'specialties': config['specialties'],
                'response_style': config['response_style'],
                'sample_queries': self._get_sample_queries(pool_type)
            }
        
        return capabilities

    def _get_sample_queries(self, pool_type: str) -> List[str]:
        """Get sample queries for each pool type"""
        samples = {
            'healthcare': [
                "I have persistent headaches and fatigue, what could this mean?",
                "What are the symptoms of diabetes?",
                "How can I improve my sleep quality?",
                "What should I know about this medication?",
                "I'm feeling anxious lately, what can help?"
            ],
            'financial': [
                "Should I invest in tech stocks right now?",
                "Analyze AAPL stock performance for me",
                "What's the best retirement savings strategy?",
                "How should I diversify my portfolio?",
                "Is this a good time to buy real estate?"
            ],
            'sports': [
                "Predict tonight's NBA games",
                "Who should I start in fantasy football this week?",
                "What are the odds for the Super Bowl?",
                "Analyze LeBron James' recent performance",
                "Create a betting strategy for tonight's games"
            ],
            'business': [
                "Help me optimize my team's workflow",
                "How can I automate our customer service?",
                "What's the best project management approach?",
                "Analyze our sales process for inefficiencies",
                "Create a growth strategy for our startup"
            ],
            'general': [
                "What's the weather like in New York?",
                "Explain quantum computing in simple terms",
                "Help me plan a trip to Europe",
                "What are the latest technology trends?",
                "How do I learn a new programming language?"
            ]
        }
        
        return samples.get(pool_type, [])

    def process_demo_request(self, pool_type: str, user_id: int) -> Dict[str, Any]:
        """Process a demo request for a specific agent pool"""
        try:
            if pool_type not in self.pool_configs:
                return {'error': f'Unknown pool type: {pool_type}'}
            
            # Get sample query for demo
            sample_queries = self._get_sample_queries(pool_type)
            demo_query = random.choice(sample_queries)
            
            # Process the demo query
            result = self._process_specialized_query(demo_query, pool_type, user_id)
            
            # Format as demo response
            demo_response = f"🎬 **{self.pool_configs[pool_type]['name']} Demo**\n"
            demo_response += "=" * 50 + "\n\n"
            demo_response += f"**Demo Query**: {demo_query}\n\n"
            demo_response += f"**Response**:\n{result.get('response', result.get('fallback_response', 'Demo failed'))}\n\n"
            demo_response += f"✨ **This demonstrates**: {self.pool_configs[pool_type]['description']}\n"
            demo_response += f"🎯 **Specialties**: {', '.join(self.pool_configs[pool_type]['specialties'])}"
            
            return {
                'success': True,
                'demo_response': demo_response,
                'pool_type': pool_type
            }
            
        except Exception as e:
            logging.error(f"Error processing demo for {pool_type}: {e}")
            return {
                'error': True,
                'message': f"Demo failed: {str(e)}"
            }
