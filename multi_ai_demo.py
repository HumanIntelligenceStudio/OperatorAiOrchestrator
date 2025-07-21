#!/usr/bin/env python3
"""
Multi-Provider AI Integration Demo for OperatorOS
Demonstrates Claude, Grok, and OpenAI integration for comprehensive financial analysis
"""

import json
import logging
from datetime import datetime
from ai_providers_enhanced import AIProviderManager
from claude_provider import get_claude_provider
from grok_provider import get_grok_provider

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MultiAIDemoRunner:
    """Demo runner for multi-provider AI analysis"""
    
    def __init__(self):
        self.ai_manager = AIProviderManager()
        self.claude_provider = get_claude_provider()
        self.grok_provider = get_grok_provider()
        
    def test_provider_connectivity(self):
        """Test connectivity to all AI providers"""
        print("\n🔌 Testing AI Provider Connectivity")
        print("=" * 50)
        
        result = self.ai_manager.test_enhanced_providers()
        
        for provider, status in result['providers'].items():
            if status.get('connected'):
                print(f"✅ {provider.upper()}: Connected")
                if 'model' in status:
                    print(f"   Model: {status['model']}")
                if 'response' in status:
                    print(f"   Response: {status['response'][:100]}...")
            else:
                print(f"❌ {provider.upper()}: {status.get('error', 'Not available')}")
        
        return result
    
    def demo_financial_analysis(self):
        """Demonstrate multi-provider financial analysis"""
        print("\n💰 Multi-Provider Financial Analysis Demo")
        print("=" * 50)
        
        # Sample financial query
        query = """Analyze the investment potential of renewable energy sector stocks for Q2 2025. 
        Consider market trends, regulatory changes, and geopolitical factors affecting clean energy investments."""
        
        context = {
            'currency_data': {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75},
            'market_data': {
                'sector': 'renewable_energy',
                'market_cap': '2.5T',
                'growth_rate': '15%',
                'volatility': 'moderate'
            },
            'portfolio_info': {
                'risk_tolerance': 'moderate',
                'investment_horizon': '3-5 years',
                'current_allocation': '10% clean energy'
            }
        }
        
        print(f"Query: {query[:100]}...")
        print(f"Context: Market data, currency rates, portfolio info")
        
        # Get multi-provider analysis
        result = self.ai_manager.get_multi_provider_analysis(query, 'financial', context)
        
        print(f"\nResults from {len(result['providers'])} providers:")
        
        for provider, analysis in result['providers'].items():
            if analysis.get('status') == 'success':
                print(f"\n🤖 {provider.upper()} Analysis:")
                response = analysis.get('response', analysis.get('analysis', ''))
                print(f"Model: {analysis.get('model', 'Unknown')}")
                print(f"Response: {response[:200]}...")
                print("-" * 40)
            else:
                print(f"\n❌ {provider.upper()}: {analysis.get('error', 'Analysis failed')}")
        
        return result
    
    def demo_risk_assessment(self):
        """Demonstrate multi-provider risk assessment"""
        print("\n⚠️  Multi-Provider Risk Assessment Demo")
        print("=" * 50)
        
        investment_data = {
            'asset_class': 'Technology Stocks',
            'allocation': {
                'AAPL': 15,
                'MSFT': 20,
                'GOOGL': 15,
                'NVDA': 25,
                'TSLA': 25
            },
            'total_value': 500000,
            'time_horizon': '5 years',
            'risk_tolerance': 'aggressive',
            'geographic_exposure': {
                'US': 80,
                'International': 20
            },
            'market_conditions': {
                'volatility_index': 22.5,
                'interest_rates': '4.5%',
                'inflation_rate': '3.2%'
            }
        }
        
        print(f"Investment Portfolio: {investment_data['asset_class']}")
        print(f"Total Value: ${investment_data['total_value']:,}")
        print(f"Risk Tolerance: {investment_data['risk_tolerance']}")
        
        # Get risk assessment from multiple providers
        result = self.ai_manager.get_risk_assessment_analysis(investment_data)
        
        print(f"\nRisk Assessment from {len(result['providers'])} providers:")
        
        for provider, analysis in result['providers'].items():
            if analysis.get('status') == 'success':
                print(f"\n🔍 {provider.upper()} Risk Assessment:")
                content = analysis.get('assessment', analysis.get('strategy', analysis.get('analysis', '')))
                print(f"Model: {analysis.get('model', 'Unknown')}")
                print(f"Assessment: {content[:200]}...")
                print("-" * 40)
            else:
                print(f"\n❌ {provider.upper()}: {analysis.get('error', 'Assessment failed')}")
        
        return result
    
    def demo_market_sentiment(self):
        """Demonstrate multi-provider market sentiment analysis"""
        print("\n📊 Multi-Provider Market Sentiment Analysis")
        print("=" * 50)
        
        market_data = {
            'indices': {
                'S&P_500': {'value': 5800, 'change': '+1.2%'},
                'NASDAQ': {'value': 18500, 'change': '+0.8%'},
                'DOW': {'value': 43000, 'change': '+0.5%'}
            },
            'sectors': {
                'Technology': {'performance': '+15%', 'sentiment': 'bullish'},
                'Healthcare': {'performance': '+8%', 'sentiment': 'neutral'},
                'Energy': {'performance': '+12%', 'sentiment': 'bullish'},
                'Finance': {'performance': '+6%', 'sentiment': 'neutral'}
            },
            'economic_indicators': {
                'GDP_growth': '2.8%',
                'unemployment': '3.9%',
                'consumer_confidence': 'high',
                'inflation_trend': 'declining'
            },
            'news_sentiment': {
                'positive': 65,
                'neutral': 25,
                'negative': 10
            }
        }
        
        print(f"Market Indices: S&P 500: {market_data['indices']['S&P_500']['value']}")
        print(f"Top Performing Sector: Technology (+15%)")
        print(f"Economic Indicators: GDP Growth {market_data['economic_indicators']['GDP_growth']}")
        
        # Get market sentiment analysis
        result = self.ai_manager.get_market_sentiment_multi_analysis(market_data)
        
        print(f"\nSentiment Analysis from {len(result['providers'])} providers:")
        
        for provider, analysis in result['providers'].items():
            if analysis.get('status') == 'success':
                print(f"\n📈 {provider.upper()} Sentiment Analysis:")
                
                if 'rating' in analysis and 'confidence' in analysis:
                    # Grok sentiment with numerical scores
                    print(f"Model: {analysis.get('model', 'Unknown')}")
                    print(f"Rating: {analysis['rating']}/5 stars")
                    print(f"Confidence: {analysis['confidence']:.2f}")
                else:
                    # Claude/other detailed analysis
                    content = analysis.get('analysis', '')
                    print(f"Model: {analysis.get('model', 'Unknown')}")
                    print(f"Analysis: {content[:200]}...")
                print("-" * 40)
            else:
                print(f"\n❌ {provider.upper()}: {analysis.get('error', 'Analysis failed')}")
        
        return result
    
    def demo_compliance_analysis(self):
        """Demonstrate Claude-specific compliance analysis"""
        print("\n📋 Compliance Analysis Demo (Claude)")
        print("=" * 50)
        
        scenario = """
        A US-based fintech company is planning to launch a cryptocurrency trading platform
        that will offer retail and institutional trading services. The platform will:
        
        1. Support trading of major cryptocurrencies (BTC, ETH, etc.)
        2. Offer margin trading with up to 5:1 leverage
        3. Provide custody services for digital assets
        4. Target both US and European markets
        5. Process payments in multiple fiat currencies
        
        What are the key regulatory compliance requirements?
        """
        
        jurisdiction = "US"
        
        print(f"Scenario: Fintech cryptocurrency trading platform")
        print(f"Jurisdiction: {jurisdiction}")
        print(f"Services: Trading, custody, margin trading, multi-currency")
        
        # Get compliance analysis (Claude speciality)
        result = self.ai_manager.get_compliance_analysis(scenario, jurisdiction)
        
        if result.get('status') == 'success':
            print(f"\n⚖️  Claude Compliance Analysis:")
            print(f"Model: {result.get('model', 'Unknown')}")
            print(f"Analysis: {result.get('compliance_analysis', '')[:500]}...")
        else:
            print(f"\n❌ Compliance Analysis Failed: {result.get('error', 'Unknown error')}")
        
        return result
    
    def demo_provider_status(self):
        """Show status of all AI providers"""
        print("\n📋 AI Provider Status Summary")
        print("=" * 50)
        
        status = self.ai_manager.get_provider_status()
        
        for provider, info in status['providers'].items():
            print(f"\n🤖 {provider.upper()} Provider:")
            print(f"   Available: {'✅' if info.get('available') else '❌'}")
            
            if 'model' in info:
                print(f"   Model: {info['model']}")
            elif 'models' in info:
                print(f"   Models: {info['models']}")
            elif 'assistants' in info:
                print(f"   Assistants: {info['assistants']}")
            
            if 'capabilities' in info:
                print(f"   Capabilities: {', '.join(info['capabilities'][:3])}...")
        
        return status
    
    def run_full_demo(self):
        """Run the complete multi-provider AI demo"""
        print("\n🚀 OperatorOS Multi-Provider AI Integration Demo")
        print("=" * 60)
        print("Showcasing Claude, Grok, and OpenAI integration for comprehensive analysis")
        print("=" * 60)
        
        demo_results = {}
        
        try:
            # Test connectivity
            demo_results['connectivity'] = self.test_provider_connectivity()
            
            # Financial analysis demo
            demo_results['financial_analysis'] = self.demo_financial_analysis()
            
            # Risk assessment demo
            demo_results['risk_assessment'] = self.demo_risk_assessment()
            
            # Market sentiment demo
            demo_results['market_sentiment'] = self.demo_market_sentiment()
            
            # Compliance analysis demo
            demo_results['compliance'] = self.demo_compliance_analysis()
            
            # Provider status
            demo_results['provider_status'] = self.demo_provider_status()
            
            print("\n🎉 Demo Completed Successfully!")
            print("=" * 50)
            print("Multi-provider AI integration is operational with:")
            
            # Count successful providers
            connected_providers = []
            if demo_results['connectivity']['providers'].get('openai', {}).get('connected'):
                connected_providers.append('OpenAI GPT-4o')
            if demo_results['connectivity']['providers'].get('claude', {}).get('connected'):
                connected_providers.append('Claude Sonnet-4')
            if demo_results['connectivity']['providers'].get('grok', {}).get('connected'):
                connected_providers.append('Grok-2')
            
            for provider in connected_providers:
                print(f"✅ {provider}")
            
            print(f"\nTotal AI Models Available: {len(connected_providers)}")
            print("Enhanced capabilities: Financial analysis, Risk assessment, Market sentiment, Compliance analysis")
            
        except Exception as e:
            print(f"\n❌ Demo failed with error: {e}")
            logging.error(f"Demo error: {e}")
            demo_results['error'] = str(e)
        
        return demo_results

def main():
    """Main demo execution"""
    demo = MultiAIDemoRunner()
    results = demo.run_full_demo()
    
    # Save results to file for reference
    with open('multi_ai_demo_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nDemo results saved to: multi_ai_demo_results.json")

if __name__ == "__main__":
    main()