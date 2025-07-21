import os
import logging
import json
from typing import Dict, List, Optional, Any
from openai import OpenAI
# Models will be imported dynamically to avoid circular imports
from datetime import datetime

# Import enhanced AI providers
try:
    from claude_provider import get_claude_provider
    from grok_provider import get_grok_provider
except ImportError as e:
    logging.warning(f"Enhanced AI providers not available: {e}")
    get_claude_provider = None
    get_grok_provider = None

class AIProviderManager:
    """Enhanced AI provider integration with OpenAI Assistants, Claude, Grok, and persistent conversations"""
    
    def __init__(self):
        # Initialize OpenAI client
        # The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # Do not change this unless explicitly requested by the user
        self.openai_api_key = os.environ.get('OPENAI_API_KEY')
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable must be set")
            
        self.openai_client = OpenAI(api_key=self.openai_api_key)
        
        # Initialize enhanced AI providers
        self.claude_provider = get_claude_provider() if get_claude_provider else None
        self.grok_provider = get_grok_provider() if get_grok_provider else None
        
        # Domain-specific assistant configurations
        self.assistant_configs = {
            'healthcare': {
                'name': 'Healthcare Specialist',
                'instructions': """You are a professional healthcare AI assistant specializing in medical information and health guidance. 

Key responsibilities:
- Provide accurate, evidence-based medical information
- Help users understand symptoms and conditions
- Suggest when to seek professional medical care
- Offer wellness and prevention advice
- Explain medical procedures and treatments

Important guidelines:
- Always emphasize that you cannot replace professional medical diagnosis
- Recommend consulting healthcare professionals for serious concerns
- Be empathetic and supportive in your responses
- Cite medical sources when possible
- Ask clarifying questions to better understand health concerns""",
                'model': 'gpt-4o',
                'tools': [{'type': 'code_interpreter'}]
            },
            
            'financial': {
                'name': 'Financial Analyst',
                'instructions': """You are an expert financial analyst and investment advisor with deep knowledge of markets, economics, and personal finance.

Key responsibilities:
- Analyze market trends and investment opportunities
- Provide portfolio recommendations based on risk tolerance
- Explain financial concepts and strategies
- Offer budgeting and financial planning advice
- Analyze stocks, bonds, and other financial instruments

Important guidelines:
- Always include appropriate risk disclaimers
- Consider user's financial situation and goals
- Provide data-driven analysis with sources
- Explain complex financial concepts clearly
- Recommend consulting financial advisors for major decisions""",
                'model': 'gpt-4o',
                'tools': [{'type': 'code_interpreter'}]
            },
            
            'sports': {
                'name': 'Sports Analytics Expert',
                'instructions': """You are a professional sports analyst with expertise in statistics, predictions, and sports betting strategy.

Key responsibilities:
- Analyze team and player performance data
- Provide game predictions with statistical backing
- Explain sports strategies and tactics
- Offer fantasy sports advice
- Create betting strategies (with responsible gambling emphasis)

Important guidelines:
- Use statistical analysis and historical data
- Explain your reasoning and methodology
- Include confidence levels in predictions
- Promote responsible gambling practices
- Stay updated on current team news and player status""",
                'model': 'gpt-4o',
                'tools': [{'type': 'code_interpreter'}]
            },
            
            'business': {
                'name': 'Business Automation Consultant',
                'instructions': """You are a senior business consultant specializing in process optimization, workflow automation, and operational efficiency.

Key responsibilities:
- Analyze business processes for automation opportunities
- Design efficient workflows and procedures
- Recommend tools and technologies for automation
- Create strategic business plans and analysis
- Help with project management and team coordination

Important guidelines:
- Focus on practical, implementable solutions
- Consider ROI and cost-benefit analysis
- Adapt recommendations to company size and industry
- Provide step-by-step implementation guidance
- Consider human factors in automation decisions""",
                'model': 'gpt-4o',
                'tools': [{'type': 'code_interpreter'}]
            },
            
            'general': {
                'name': 'General Knowledge Assistant',
                'instructions': """You are a knowledgeable and helpful AI assistant capable of providing information and assistance across a wide range of topics.

Key responsibilities:
- Answer questions on diverse subjects
- Provide detailed explanations and information
- Help with research and fact-checking
- Assist with problem-solving and decision-making
- Offer creative and analytical thinking

Important guidelines:
- Provide accurate and well-sourced information
- Admit when you don't know something
- Ask clarifying questions when needed
- Be conversational and engaging
- Tailor responses to the user's level of understanding""",
                'model': 'gpt-4o',
                'tools': [{'type': 'code_interpreter'}]
            }
        }
        
        # Cache for created assistants
        self.assistants = {}
        self._initialize_assistants()
        
        logging.info("🤖 Enhanced AI Provider Manager with OpenAI Assistants initialized")

    def _initialize_assistants(self):
        """Initialize OpenAI Assistants for each domain"""
        try:
            for domain, config in self.assistant_configs.items():
                try:
                    # Create or get existing assistant
                    assistant = self.openai_client.beta.assistants.create(
                        name=config['name'],
                        instructions=config['instructions'],
                        model=config['model'],
                        tools=config['tools']
                    )
                    self.assistants[domain] = assistant.id
                    logging.info(f"✅ Created {domain} assistant: {assistant.id}")
                except Exception as e:
                    logging.error(f"❌ Failed to create {domain} assistant: {e}")
                    
        except Exception as e:
            logging.error(f"Failed to initialize assistants: {e}")

    def get_or_create_conversation(self, user_id: int, conversation_type: str):
        """Get existing conversation or create new one for user and type"""
        try:
            # Import models dynamically to avoid circular imports
            from models import Conversation
            from app import db
            
            # Look for existing conversation
            conversation = Conversation.query.filter_by(
                user_id=user_id,
                conversation_type=conversation_type
            ).first()
            
            if not conversation:
                # Create new thread with OpenAI
                thread = self.openai_client.beta.threads.create()
                
                # Create conversation record
                conversation = Conversation(
                    user_id=user_id,
                    openai_thread_id=thread.id,
                    assistant_id=self.assistants.get(conversation_type),
                    conversation_type=conversation_type,
                    conversation_data={'created_via': 'replit_agent'}
                )
                db.session.add(conversation)
                db.session.commit()
                
                logging.info(f"Created new conversation for user {user_id}, type {conversation_type}")
            
            return conversation
            
        except Exception as e:
            logging.error(f"Error getting/creating conversation: {e}")
            raise e

    def get_assistant_response(self, query: str, user_id: int, agent_type: str = 'general', context: Optional[Dict] = None) -> Dict[str, Any]:
        """Get response from OpenAI Assistant with conversation context"""
        try:
            # Get or create conversation
            conversation = self.get_or_create_conversation(user_id, agent_type)
            
            if not conversation.openai_thread_id:
                raise Exception("No valid thread ID for conversation")
            
            # Add user message to thread
            message = self.openai_client.beta.threads.messages.create(
                thread_id=conversation.openai_thread_id,
                role="user",
                content=query
            )
            
            # Run the assistant
            run = self.openai_client.beta.threads.runs.create(
                thread_id=conversation.openai_thread_id,
                assistant_id=conversation.assistant_id,
                additional_instructions=self._build_context_instructions(context) if context else None
            )
            
            # Wait for completion
            import time
            while run.status in ['queued', 'in_progress', 'cancelling']:
                time.sleep(1)
                run = self.openai_client.beta.threads.runs.retrieve(
                    thread_id=conversation.openai_thread_id,
                    run_id=run.id
                )
            
            if run.status == 'completed':
                # Get the assistant's response
                messages = self.openai_client.beta.threads.messages.list(
                    thread_id=conversation.openai_thread_id,
                    order="desc",
                    limit=1
                )
                
                assistant_response = messages.data[0].content[0].text.value
                
                # Update conversation metadata
                conversation.last_message_at = datetime.utcnow()
                conversation.message_count += 1
                db.session.commit()
                
                return {
                    'error': False,
                    'response': assistant_response,
                    'provider': 'openai_assistant',
                    'model': self.assistant_configs[agent_type]['model'],
                    'conversation_id': conversation.id,
                    'thread_id': conversation.openai_thread_id
                }
            else:
                error_msg = f"Assistant run failed with status: {run.status}"
                if run.last_error:
                    error_msg += f" - {run.last_error.message}"
                raise Exception(error_msg)
                
        except Exception as e:
            logging.error(f"Error getting assistant response: {e}")
            return {
                'error': True,
                'message': f"Assistant processing error: {str(e)}",
                'provider': 'openai_assistant'
            }

    def _build_context_instructions(self, context: Dict[str, Any]) -> str:
        """Build additional context instructions for the assistant"""
        instructions = []
        
        if context.get('user_preferences'):
            instructions.append(f"User preferences: {context['user_preferences']}")
        
        if context.get('conversation_history'):
            instructions.append(f"Previous context: {context['conversation_history']}")
        
        if context.get('urgency'):
            instructions.append(f"Urgency level: {context['urgency']}")
        
        if context.get('specific_focus'):
            instructions.append(f"Focus specifically on: {context['specific_focus']}")
            
        return "\n".join(instructions) if instructions else ""

    def get_conversation_history(self, user_id: int, conversation_type: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get conversation history for a user and type"""
        try:
            conversation = Conversation.query.filter_by(
                user_id=user_id,
                conversation_type=conversation_type
            ).first()
            
            if not conversation or not conversation.openai_thread_id:
                return []
            
            # Get messages from OpenAI thread
            messages = self.openai_client.beta.threads.messages.list(
                thread_id=conversation.openai_thread_id,
                order="desc",
                limit=limit * 2  # Get more to account for both user and assistant messages
            )
            
            history = []
            for message in reversed(messages.data):
                history.append({
                    'role': message.role,
                    'content': message.content[0].text.value,
                    'timestamp': message.created_at
                })
            
            return history[-limit:] if len(history) > limit else history
            
        except Exception as e:
            logging.error(f"Error getting conversation history: {e}")
            return []

    def clear_conversation(self, user_id: int, conversation_type: str) -> bool:
        """Clear/reset a conversation by creating a new thread"""
        try:
            conversation = Conversation.query.filter_by(
                user_id=user_id,
                conversation_type=conversation_type
            ).first()
            
            if conversation:
                # Create new thread
                thread = self.openai_client.beta.threads.create()
                
                # Update conversation with new thread ID
                conversation.openai_thread_id = thread.id
                conversation.message_count = 0
                conversation.last_message_at = datetime.utcnow()
                db.session.commit()
                
                logging.info(f"Cleared conversation for user {user_id}, type {conversation_type}")
                return True
            
            return False
            
        except Exception as e:
            logging.error(f"Error clearing conversation: {e}")
            return False

    def get_assistant_capabilities(self) -> Dict[str, Any]:
        """Get capabilities of all available assistants"""
        capabilities = {}
        
        for domain, config in self.assistant_configs.items():
            assistant_id = self.assistants.get(domain)
            capabilities[domain] = {
                'name': config['name'],
                'model': config['model'],
                'tools': [tool['type'] for tool in config['tools']],
                'assistant_id': assistant_id,
                'available': bool(assistant_id)
            }
        
        return capabilities

    def test_assistants(self) -> Dict[str, bool]:
        """Test all assistants with a simple query"""
        results = {}
        
        for domain, assistant_id in self.assistants.items():
            try:
                # Create a temporary thread for testing
                thread = self.openai_client.beta.threads.create()
                
                # Add test message
                message = self.openai_client.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content="Hello, please respond with 'test successful'"
                )
                
                # Run assistant
                run = self.openai_client.beta.threads.runs.create(
                    thread_id=thread.id,
                    assistant_id=assistant_id
                )
                
                # Wait briefly for completion
                import time
                for _ in range(10):  # Max 10 seconds
                    time.sleep(1)
                    run = self.openai_client.beta.threads.runs.retrieve(
                        thread_id=thread.id,
                        run_id=run.id
                    )
                    if run.status not in ['queued', 'in_progress']:
                        break
                
                results[domain] = run.status == 'completed'
                
            except Exception as e:
                logging.error(f"Test failed for {domain} assistant: {e}")
                results[domain] = False
        
        return results
    
    # Enhanced AI Provider Methods - Multi-Model Analysis
    
    def get_multi_provider_analysis(self, query: str, domain: str = 'financial', context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Get analysis from multiple AI providers for comprehensive insights
        """
        results = {
            'query': query,
            'domain': domain,
            'providers': {},
            'timestamp': datetime.now().isoformat(),
            'context_used': bool(context)
        }
        
        # OpenAI GPT-4o analysis
        try:
            gpt_result = self.get_quick_response(query, domain, context)
            if not gpt_result.get('error'):
                results['providers']['openai'] = {
                    'response': gpt_result.get('response', ''),
                    'model': 'gpt-4o',
                    'status': 'success'
                }
        except Exception as e:
            results['providers']['openai'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Claude analysis for financial domain
        if domain in ['financial', 'business'] and self.claude_provider and self.claude_provider.is_available():
            try:
                claude_result = self.claude_provider.financial_analysis(query, context)
                if not claude_result.get('error'):
                    results['providers']['claude'] = {
                        'response': claude_result.get('analysis', ''),
                        'model': claude_result.get('model', 'claude-sonnet-4'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['claude'] = {
                    'status': 'error', 
                    'error': str(e)
                }
        
        # Grok analysis for business insights
        if domain in ['financial', 'business', 'general'] and self.grok_provider and self.grok_provider.is_available():
            try:
                grok_result = self.grok_provider.business_analysis(query, context)
                if not grok_result.get('error'):
                    results['providers']['grok'] = {
                        'response': grok_result.get('analysis', ''),
                        'model': grok_result.get('model', 'grok-2'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['grok'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        return results
    
    def get_risk_assessment_analysis(self, investment_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get comprehensive risk assessment from multiple AI providers
        """
        results = {
            'investment_data': investment_data,
            'providers': {},
            'timestamp': datetime.now().isoformat()
        }
        
        # Claude risk assessment (specialized)
        if self.claude_provider and self.claude_provider.is_available():
            try:
                claude_result = self.claude_provider.risk_assessment(investment_data)
                if not claude_result.get('error'):
                    results['providers']['claude_risk'] = {
                        'assessment': claude_result.get('risk_assessment', ''),
                        'model': claude_result.get('model', 'claude-sonnet-4'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['claude_risk'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        # Grok investment strategy
        if self.grok_provider and self.grok_provider.is_available():
            try:
                grok_result = self.grok_provider.investment_strategy(investment_data)
                if not grok_result.get('error'):
                    results['providers']['grok_strategy'] = {
                        'strategy': grok_result.get('investment_strategy', ''),
                        'model': grok_result.get('model', 'grok-2'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['grok_strategy'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        # OpenAI financial analysis
        try:
            query = f"Analyze investment risks for: {json.dumps(investment_data, indent=2)}"
            gpt_result = self.get_quick_response(query, 'financial')
            if not gpt_result.get('error'):
                results['providers']['openai_analysis'] = {
                    'analysis': gpt_result.get('response', ''),
                    'model': 'gpt-4o',
                    'status': 'success'
                }
        except Exception as e:
            results['providers']['openai_analysis'] = {
                'status': 'error',
                'error': str(e)
            }
        
        return results
    
    def get_market_sentiment_multi_analysis(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get market sentiment analysis from multiple AI providers
        """
        results = {
            'market_data': market_data,
            'providers': {},
            'timestamp': datetime.now().isoformat()
        }
        
        # Claude market sentiment
        if self.claude_provider and self.claude_provider.is_available():
            try:
                claude_result = self.claude_provider.market_sentiment_analysis(market_data)
                if not claude_result.get('error'):
                    results['providers']['claude_sentiment'] = {
                        'analysis': claude_result.get('sentiment_analysis', ''),
                        'model': claude_result.get('model', 'claude-sonnet-4'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['claude_sentiment'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        # Grok opportunity analysis
        if self.grok_provider and self.grok_provider.is_available():
            try:
                grok_result = self.grok_provider.market_opportunity_analysis(market_data)
                if not grok_result.get('error'):
                    results['providers']['grok_opportunity'] = {
                        'analysis': grok_result.get('opportunity_analysis', ''),
                        'model': grok_result.get('model', 'grok-2'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['grok_opportunity'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        # Grok sentiment analysis
        if self.grok_provider and self.grok_provider.is_available():
            try:
                market_summary = json.dumps(market_data)
                grok_sentiment = self.grok_provider.sentiment_analysis(market_summary)
                if not grok_sentiment.get('error'):
                    results['providers']['grok_sentiment'] = {
                        'rating': grok_sentiment.get('rating'),
                        'confidence': grok_sentiment.get('confidence'),
                        'model': grok_sentiment.get('model', 'grok-2'),
                        'status': 'success'
                    }
            except Exception as e:
                results['providers']['grok_sentiment'] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        return results
    
    def get_compliance_analysis(self, scenario: str, jurisdiction: str = "US") -> Dict[str, Any]:
        """
        Get compliance analysis using Claude (specialized for regulatory analysis)
        """
        results = {
            'scenario': scenario,
            'jurisdiction': jurisdiction,
            'timestamp': datetime.now().isoformat()
        }
        
        if self.claude_provider and self.claude_provider.is_available():
            try:
                claude_result = self.claude_provider.compliance_analysis(scenario, jurisdiction)
                if not claude_result.get('error'):
                    results['compliance_analysis'] = claude_result.get('compliance_analysis', '')
                    results['model'] = claude_result.get('model', 'claude-sonnet-4')
                    results['status'] = 'success'
                    results['provider'] = 'claude'
                else:
                    results['status'] = 'error'
                    results['error'] = claude_result.get('error', 'Unknown error')
            except Exception as e:
                results['status'] = 'error'
                results['error'] = str(e)
        else:
            results['status'] = 'error'
            results['error'] = 'Claude provider not available'
        
        return results
    
    def test_enhanced_providers(self) -> Dict[str, Any]:
        """
        Test all enhanced AI providers
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'providers': {}
        }
        
        # Test Claude
        if self.claude_provider:
            try:
                claude_test = self.claude_provider.test_connection()
                results['providers']['claude'] = claude_test
            except Exception as e:
                results['providers']['claude'] = {
                    'connected': False,
                    'error': str(e)
                }
        else:
            results['providers']['claude'] = {
                'connected': False,
                'error': 'Provider not initialized'
            }
        
        # Test Grok
        if self.grok_provider:
            try:
                grok_test = self.grok_provider.test_connection()
                results['providers']['grok'] = grok_test
            except Exception as e:
                results['providers']['grok'] = {
                    'connected': False,
                    'error': str(e)
                }
        else:
            results['providers']['grok'] = {
                'connected': False,
                'error': 'Provider not initialized'
            }
        
        # Test OpenAI (existing)
        try:
            openai_test = self.test_assistants()
            results['providers']['openai'] = {
                'assistants': openai_test,
                'connected': any(openai_test.values()),
                'status': 'success'
            }
        except Exception as e:
            results['providers']['openai'] = {
                'connected': False,
                'error': str(e)
            }
        
        return results
    
    def get_provider_status(self) -> Dict[str, Any]:
        """
        Get status of all AI providers
        """
        status = {
            'timestamp': datetime.now().isoformat(),
            'providers': {}
        }
        
        # OpenAI status
        status['providers']['openai'] = {
            'available': bool(self.openai_api_key),
            'assistants': len(self.assistants),
            'capabilities': list(self.assistant_configs.keys())
        }
        
        # Claude status
        if self.claude_provider:
            status['providers']['claude'] = self.claude_provider.get_status()
        else:
            status['providers']['claude'] = {
                'available': False,
                'error': 'Provider not initialized'
            }
        
        # Grok status  
        if self.grok_provider:
            status['providers']['grok'] = self.grok_provider.get_status()
        else:
            status['providers']['grok'] = {
                'available': False,
                'error': 'Provider not initialized'
            }
        
        return status
