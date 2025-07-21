#!/usr/bin/env python3
"""
xAI Grok AI Provider for OperatorOS
Integrates Grok models for advanced AI analysis and decision support
"""

import os
import logging
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from openai import OpenAI

class GrokProvider:
    """
    xAI Grok provider for advanced AI analysis and reasoning
    """
    
    def __init__(self):
        self.api_key = os.environ.get('XAI_API_KEY')
        self.base_url = "https://api.x.ai/v1"
        self.default_model = "grok-2-1212"
        self.vision_model = "grok-2-vision-1212"
        self.available = bool(self.api_key)
        
        if self.available:
            try:
                # Create a custom OpenAI client with the X.AI endpoint
                self.client = OpenAI(
                    base_url=self.base_url,
                    api_key=self.api_key
                )
                logging.info(f"Grok Provider initialized with API key: {self.api_key[:8]}...")
            except Exception as e:
                logging.error(f"Failed to initialize Grok client: {e}")
                self.available = False
        else:
            logging.warning("XAI_API_KEY not found - Grok features disabled")
            self.client = None
    
    def is_available(self) -> bool:
        """Check if Grok API is available"""
        return self.available and self.client is not None
    
    def business_analysis(self, query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Perform comprehensive business analysis using Grok
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            # Construct business analysis prompt
            system_prompt = """You are an expert business analyst with deep expertise in:
            - Strategic planning and business development
            - Market analysis and competitive intelligence
            - Financial modeling and business valuation
            - Operational efficiency and process optimization
            - Technology integration and digital transformation
            
            Provide comprehensive business insights with practical recommendations,
            data-driven analysis, and clear strategic guidance."""
            
            # Add context if provided
            context_str = ""
            if context:
                if 'company_data' in context:
                    context_str += f"Company data: {context['company_data']}\n"
                if 'market_conditions' in context:
                    context_str += f"Market conditions: {context['market_conditions']}\n"
                if 'financial_metrics' in context:
                    context_str += f"Financial metrics: {context['financial_metrics']}\n"
            
            user_prompt = f"{context_str}\n\nBusiness Query: {query}"
            
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2000,
                temperature=0.3
            )
            
            response_content = response.choices[0].message.content if response.choices else "No response generated"
            
            return {
                "analysis": response_content,
                "model": self.default_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat(),
                "context_used": bool(context),
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else None,
                    "completion_tokens": response.usage.completion_tokens if response.usage else None,
                    "total_tokens": response.usage.total_tokens if response.usage else None
                }
            }
            
        except Exception as e:
            logging.error(f"Grok business analysis failed: {e}")
            return {"error": f"Grok analysis failed: {str(e)}", "fallback": True}
    
    def investment_strategy(self, investment_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate investment strategy recommendations using Grok
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            system_prompt = """You are a sophisticated investment strategist with expertise in:
            - Portfolio construction and asset allocation
            - Alternative investments and hedge fund strategies
            - Global macro investing and currency strategies
            - ESG investing and sustainable finance
            - Quantitative analysis and algorithmic trading
            
            Provide detailed investment strategies with specific allocations,
            risk considerations, and implementation timelines."""
            
            profile_summary = json.dumps(investment_profile, indent=2)
            user_prompt = f"""Design an investment strategy based on the following profile:

{profile_summary}

Please provide:
1. Recommended asset allocation (specific percentages)
2. Investment vehicles and instruments
3. Geographic and sector diversification
4. Risk management approach
5. Performance benchmarks and targets
6. Rebalancing strategy and timeline
7. Tax optimization considerations"""
            
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2500,
                temperature=0.2
            )
            
            response_content = response.choices[0].message.content if response.choices else "No strategy generated"
            
            return {
                "investment_strategy": response_content,
                "model": self.default_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat(),
                "investment_profile": investment_profile
            }
            
        except Exception as e:
            logging.error(f"Grok investment strategy failed: {e}")
            return {"error": f"Investment strategy failed: {str(e)}", "fallback": True}
    
    def competitive_analysis(self, company: str, industry: str) -> Dict[str, Any]:
        """
        Perform competitive analysis using Grok
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            system_prompt = """You are a competitive intelligence analyst with expertise in:
            - Industry analysis and market positioning
            - Competitive benchmarking and SWOT analysis
            - Strategic threats and opportunities assessment
            - Market share and growth trend analysis
            - Technology disruption and innovation tracking
            
            Provide comprehensive competitive analysis with actionable insights
            and strategic recommendations."""
            
            user_prompt = f"""Perform a competitive analysis for {company} in the {industry} industry.

Please analyze:
1. Market position and competitive advantages
2. Key competitors and their strengths/weaknesses  
3. Market trends and disruption threats
4. Growth opportunities and strategic options
5. Recommended competitive strategies
6. Key performance indicators to monitor"""
            
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2000,
                temperature=0.4
            )
            
            response_content = response.choices[0].message.content if response.choices else "No analysis generated"
            
            return {
                "competitive_analysis": response_content,
                "company": company,
                "industry": industry,
                "model": self.default_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Grok competitive analysis failed: {e}")
            return {"error": f"Competitive analysis failed: {str(e)}", "fallback": True}
    
    def market_opportunity_analysis(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze market opportunities using Grok
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            system_prompt = """You are a market opportunity analyst with expertise in:
            - Market sizing and growth potential assessment
            - Customer segmentation and demand analysis
            - Emerging market trends and opportunities
            - Technology adoption and innovation cycles
            - Regulatory environment and policy impacts
            
            Provide detailed market opportunity analysis with quantified potential
            and clear go-to-market recommendations."""
            
            market_summary = json.dumps(market_data, indent=2)
            user_prompt = f"""Analyze market opportunities based on the following data:

{market_summary}

Please provide:
1. Market size and growth potential (TAM, SAM, SOM)
2. Key customer segments and their needs
3. Emerging trends and opportunities
4. Barriers to entry and competitive threats
5. Go-to-market strategy recommendations
6. Revenue potential and timeline
7. Key success factors and risks"""
            
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=2500,
                temperature=0.3
            )
            
            response_content = response.choices[0].message.content if response.choices else "No analysis generated"
            
            return {
                "opportunity_analysis": response_content,
                "model": self.default_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat(),
                "market_data": market_data
            }
            
        except Exception as e:
            logging.error(f"Grok opportunity analysis failed: {e}")
            return {"error": f"Opportunity analysis failed: {str(e)}", "fallback": True}
    
    def sentiment_analysis(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment using Grok with structured output
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a sentiment analysis expert. Analyze the sentiment of the text and provide a rating from 1 to 5 stars and a confidence score between 0 and 1. Respond with JSON in this format: {'rating': number, 'confidence': number}"
                    },
                    {"role": "user", "content": text}
                ],
                response_format={"type": "json_object"},
                max_tokens=200,
                temperature=0.1
            )
            
            result = json.loads(response.choices[0].message.content)
            
            return {
                "rating": max(1, min(5, round(result["rating"]))),
                "confidence": max(0, min(1, result["confidence"])),
                "model": self.default_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Grok sentiment analysis failed: {e}")
            return {"error": f"Sentiment analysis failed: {str(e)}", "fallback": True}
    
    def analyze_image(self, base64_image: str, query: str = "Analyze this image") -> Dict[str, Any]:
        """
        Analyze image using Grok Vision
        """
        if not self.is_available():
            return {"error": "Grok API not available", "fallback": True}
        
        try:
            response = self.client.chat.completions.create(
                model=self.vision_model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": query},
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                            }
                        ]
                    }
                ],
                max_tokens=500,
                temperature=0.3
            )
            
            response_content = response.choices[0].message.content if response.choices else "No analysis generated"
            
            return {
                "analysis": response_content,
                "model": self.vision_model,
                "provider": "grok",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Grok image analysis failed: {e}")
            return {"error": f"Image analysis failed: {str(e)}", "fallback": True}
    
    def test_connection(self) -> Dict[str, Any]:
        """Test Grok API connection"""
        if not self.is_available():
            return {"connected": False, "error": "API key not configured"}
        
        try:
            response = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "user", "content": "Hello, please confirm you are Grok and ready to assist with business analysis."}
                ],
                max_tokens=100,
                temperature=0.1
            )
            
            response_content = response.choices[0].message.content if response.choices else "No response"
            
            return {
                "connected": True,
                "model": self.default_model,
                "response": response_content,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Grok connection test failed: {e}")
            return {"connected": False, "error": str(e)}
    
    def get_status(self) -> Dict[str, Any]:
        """Get Grok provider status"""
        return {
            "provider": "grok",
            "available": self.is_available(),
            "models": {
                "text": self.default_model,
                "vision": self.vision_model
            },
            "api_key_configured": bool(self.api_key),
            "capabilities": [
                "business_analysis",
                "investment_strategy",
                "competitive_analysis", 
                "market_opportunity_analysis",
                "sentiment_analysis",
                "image_analysis"
            ],
            "timestamp": datetime.now().isoformat()
        }

# Global provider instance
_grok_provider = None

def get_grok_provider():
    """Get singleton Grok provider instance"""
    global _grok_provider
    if _grok_provider is None:
        _grok_provider = GrokProvider()
    return _grok_provider