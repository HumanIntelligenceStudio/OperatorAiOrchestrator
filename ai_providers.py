import os
import logging
from typing import Dict, List, Optional, Any
from openai import OpenAI
import anthropic
from anthropic import Anthropic

class AIProviderManager:
    """Basic AI provider management for different models and services"""
    
    def __init__(self):
        # Initialize OpenAI client
        # The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # Do not change this unless explicitly requested by the user
        self.openai_api_key = os.environ.get('OPENAI_API_KEY')
        self.openai_client = OpenAI(api_key=self.openai_api_key) if self.openai_api_key else None
        
        # Initialize Anthropic client
        # The newest Anthropic model is "claude-sonnet-4-20250514"
        self.anthropic_api_key = os.environ.get('ANTHROPIC_API_KEY')
        self.anthropic_client = Anthropic(api_key=self.anthropic_api_key) if self.anthropic_api_key else None
        
        # Provider routing configuration
        self.provider_config = {
            'healthcare': {'provider': 'openai', 'model': 'gpt-4o'},
            'financial': {'provider': 'anthropic', 'model': 'claude-sonnet-4-20250514'},
            'sports': {'provider': 'openai', 'model': 'gpt-4o'},
            'business': {'provider': 'anthropic', 'model': 'claude-sonnet-4-20250514'},
            'general': {'provider': 'openai', 'model': 'gpt-4o'}
        }
        
        logging.info("🤖 AI Provider Manager initialized")

    def get_response(self, query: str, agent_type: str = 'general', context: Optional[Dict] = None) -> Dict[str, Any]:
        """Get AI response based on agent type and provider configuration"""
        try:
            config = self.provider_config.get(agent_type, self.provider_config['general'])
            provider = config['provider']
            model = config['model']
            
            if provider == 'openai' and self.openai_client:
                return self._get_openai_response(query, model, agent_type, context)
            elif provider == 'anthropic' and self.anthropic_client:
                return self._get_anthropic_response(query, model, agent_type, context)
            else:
                # Fallback to available provider
                if self.openai_client:
                    return self._get_openai_response(query, 'gpt-4o', agent_type, context)
                elif self.anthropic_client:
                    return self._get_anthropic_response(query, 'claude-sonnet-4-20250514', agent_type, context)
                else:
                    raise Exception("No AI providers available")
                    
        except Exception as e:
            logging.error(f"Error getting AI response: {e}")
            return {
                'error': True,
                'message': f"AI processing error: {str(e)}",
                'provider': provider,
                'model': model
            }

    def _get_openai_response(self, query: str, model: str, agent_type: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Get response from OpenAI"""
        try:
            # Build system prompt based on agent type
            system_prompt = self._build_system_prompt(agent_type, context)
            
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            return {
                'error': False,
                'response': response.choices[0].message.content,
                'provider': 'openai',
                'model': model,
                'tokens_used': response.usage.total_tokens if response.usage else 0
            }
            
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            raise e

    def _get_anthropic_response(self, query: str, model: str, agent_type: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """Get response from Anthropic Claude"""
        try:
            # Build system prompt based on agent type
            system_prompt = self._build_system_prompt(agent_type, context)
            
            response = self.anthropic_client.messages.create(
                model=model,
                max_tokens=2000,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": query}
                ]
            )
            
            return {
                'error': False,
                'response': response.content[0].text,
                'provider': 'anthropic',
                'model': model,
                'tokens_used': response.usage.output_tokens + response.usage.input_tokens
            }
            
        except Exception as e:
            logging.error(f"Anthropic API error: {e}")
            raise e

    def _build_system_prompt(self, agent_type: str, context: Optional[Dict] = None) -> str:
        """Build specialized system prompts for different agent types"""
        base_prompt = "You are a professional AI assistant specializing in "
        
        prompts = {
            'healthcare': base_prompt + """healthcare and medical information. You provide helpful, accurate medical information while being clear that you are not a doctor and cannot provide medical diagnoses. Always recommend consulting with healthcare professionals for medical concerns. Be empathetic and thorough in your responses.""",
            
            'financial': base_prompt + """financial analysis, investment advice, and economic insights. You provide data-driven financial recommendations while emphasizing the importance of personal financial situations and risk tolerance. Include appropriate disclaimers about investment risks.""",
            
            'sports': base_prompt + """sports analytics, statistics, and predictions. You analyze team performance, player statistics, and game outcomes using data-driven approaches. Provide insights for both casual fans and serious analysts.""",
            
            'business': base_prompt + """business strategy, operations, and automation. You help with process optimization, workflow design, strategic planning, and business automation solutions. Focus on practical, actionable advice.""",
            
            'general': base_prompt + """general knowledge and assistance. You provide helpful, accurate information across a wide range of topics while being conversational and engaging."""
        }
        
        prompt = prompts.get(agent_type, prompts['general'])
        
        # Add context if provided
        if context:
            prompt += f"\n\nAdditional context: {context.get('additional_info', '')}"
            
        return prompt

    def test_providers(self) -> Dict[str, bool]:
        """Test availability of AI providers"""
        results = {}
        
        # Test OpenAI
        try:
            if self.openai_client:
                response = self.openai_client.chat.completions.create(
                    model='gpt-4o',
                    messages=[{'role': 'user', 'content': 'Hello'}],
                    max_tokens=10
                )
                results['openai'] = True
            else:
                results['openai'] = False
        except Exception as e:
            logging.error(f"OpenAI test failed: {e}")
            results['openai'] = False
        
        # Test Anthropic
        try:
            if self.anthropic_client:
                response = self.anthropic_client.messages.create(
                    model='claude-sonnet-4-20250514',
                    max_tokens=10,
                    messages=[{'role': 'user', 'content': 'Hello'}]
                )
                results['anthropic'] = True
            else:
                results['anthropic'] = False
        except Exception as e:
            logging.error(f"Anthropic test failed: {e}")
            results['anthropic'] = False
        
        return results

    def get_provider_status(self) -> Dict[str, Any]:
        """Get status of all AI providers"""
        return {
            'openai': {
                'available': bool(self.openai_client),
                'api_key_configured': bool(self.openai_api_key),
                'default_model': 'gpt-4o'
            },
            'anthropic': {
                'available': bool(self.anthropic_client),
                'api_key_configured': bool(self.anthropic_api_key),
                'default_model': 'claude-sonnet-4-20250514'
            }
        }
