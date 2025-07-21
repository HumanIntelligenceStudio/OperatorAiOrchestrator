#!/usr/bin/env python3
"""
Enhanced AI Demo showcasing Claude and Grok integration
Demonstrates multi-provider financial analysis capabilities
"""

import json
import logging
from datetime import datetime
from claude_provider import get_claude_provider
from grok_provider import get_grok_provider

logging.basicConfig(level=logging.INFO)

def demo_multi_provider_financial_analysis():
    """Demonstrate financial analysis using both Claude and Grok"""
    print("\n💰 Multi-Provider Financial Analysis")
    print("=" * 50)
    
    # Sample investment scenario
    scenario = """
    Portfolio Analysis Request:
    - Current portfolio: $500K in tech stocks (AAPL 25%, MSFT 20%, GOOGL 20%, NVDA 15%, TSLA 20%)
    - Investment horizon: 3-5 years
    - Risk tolerance: Moderate to aggressive
    - Goals: Growth with some income generation
    - Considering: Adding international exposure and clean energy sector
    """
    
    context = {
        'portfolio_value': 500000,
        'current_allocation': {
            'AAPL': 0.25,
            'MSFT': 0.20, 
            'GOOGL': 0.20,
            'NVDA': 0.15,
            'TSLA': 0.20
        },
        'market_conditions': {
            'VIX': 18.5,
            'ten_year_yield': 4.2,
            'inflation_rate': 3.1
        }
    }
    
    print(f"Scenario: {scenario.strip()}")
    print(f"Portfolio Value: ${context['portfolio_value']:,}")
    
    # Get Claude analysis (financial specialist)
    claude = get_claude_provider()
    if claude.is_available():
        print(f"\n🤖 Claude Financial Analysis:")
        claude_result = claude.financial_analysis(scenario, context)
        if not claude_result.get('error'):
            analysis = claude_result.get('analysis', '')
            print(f"Model: {claude_result.get('model')}")
            print(f"Analysis: {analysis[:300]}...")
            print(f"Token Usage: Input: {claude_result.get('token_usage', {}).get('input_tokens', 'N/A')}, "
                  f"Output: {claude_result.get('token_usage', {}).get('output_tokens', 'N/A')}")
    
    # Get Grok analysis (business strategist)
    grok = get_grok_provider()
    if grok.is_available():
        print(f"\n🤖 Grok Business Analysis:")
        grok_result = grok.business_analysis(scenario, context)
        if not grok_result.get('error'):
            analysis = grok_result.get('analysis', '')
            print(f"Model: {grok_result.get('model')}")
            print(f"Analysis: {analysis[:300]}...")
            print(f"Token Usage: Total: {grok_result.get('usage', {}).get('total_tokens', 'N/A')}")

def demo_risk_assessment():
    """Demonstrate advanced risk assessment capabilities"""
    print("\n⚠️  Advanced Risk Assessment Demo")
    print("=" * 50)
    
    investment_data = {
        'portfolio_type': 'Growth-focused equity portfolio',
        'assets': {
            'US_Large_Cap': 40,  # %
            'US_Small_Cap': 15,
            'International_Developed': 20,
            'Emerging_Markets': 10,
            'Clean_Energy_ETF': 10,
            'Cash': 5
        },
        'total_value': 750000,
        'leverage': None,
        'investment_horizon': '7-10 years',
        'investor_profile': {
            'age': 35,
            'risk_tolerance': 'aggressive',
            'income_stability': 'high',
            'liquidity_needs': 'low'
        },
        'market_environment': {
            'economic_cycle': 'late_expansion',
            'interest_rate_trend': 'rising',
            'geopolitical_risk': 'moderate'
        }
    }
    
    print(f"Portfolio Value: ${investment_data['total_value']:,}")
    print(f"Asset Allocation: {dict(list(investment_data['assets'].items())[:3])}...")
    print(f"Risk Profile: {investment_data['investor_profile']['risk_tolerance']}")
    
    # Claude risk assessment (regulatory and compliance focus)
    claude = get_claude_provider()
    if claude.is_available():
        print(f"\n🔍 Claude Risk Assessment:")
        risk_result = claude.risk_assessment(investment_data)
        if not risk_result.get('error'):
            assessment = risk_result.get('risk_assessment', '')
            print(f"Model: {risk_result.get('model')}")
            print(f"Assessment: {assessment[:400]}...")
    
    # Grok investment strategy (strategic planning focus)
    grok = get_grok_provider()
    if grok.is_available():
        print(f"\n📈 Grok Investment Strategy:")
        strategy_result = grok.investment_strategy(investment_data)
        if not strategy_result.get('error'):
            strategy = strategy_result.get('investment_strategy', '')
            print(f"Model: {strategy_result.get('model')}")
            print(f"Strategy: {strategy[:400]}...")

def demo_market_sentiment():
    """Demonstrate market sentiment analysis"""
    print("\n📊 Market Sentiment Analysis")
    print("=" * 50)
    
    market_data = {
        'date': '2025-07-21',
        'market_performance': {
            'S&P_500': {'price': 5850, 'change': '+1.8%', 'volume': 'high'},
            'NASDAQ': {'price': 18800, 'change': '+2.1%', 'volume': 'high'},
            'Russell_2000': {'price': 2180, 'change': '+0.9%', 'volume': 'moderate'}
        },
        'sector_rotation': {
            'Technology': '+2.3%',
            'Clean_Energy': '+4.1%', 
            'Healthcare': '+0.8%',
            'Financial': '+1.2%',
            'Consumer_Discretionary': '-0.3%'
        },
        'economic_indicators': {
            'jobs_report': 'strong (unemployment 3.8%)',
            'inflation_trend': 'declining (3.1% YoY)',
            'fed_policy': 'neutral stance',
            'consumer_confidence': 'high (112.5)'
        },
        'news_sentiment': 'positive AI earnings, strong consumer spending'
    }
    
    print(f"Market Date: {market_data['date']}")
    print(f"S&P 500: {market_data['market_performance']['S&P_500']['price']} ({market_data['market_performance']['S&P_500']['change']})")
    print(f"Top Sector: Clean Energy (+4.1%)")
    
    # Claude market sentiment (fundamental analysis focus)
    claude = get_claude_provider()
    if claude.is_available():
        print(f"\n📈 Claude Market Sentiment:")
        sentiment_result = claude.market_sentiment_analysis(market_data)
        if not sentiment_result.get('error'):
            sentiment = sentiment_result.get('sentiment_analysis', '')
            print(f"Model: {sentiment_result.get('model')}")
            print(f"Sentiment: {sentiment[:350]}...")
    
    # Grok opportunity analysis (trend and opportunity focus)
    grok = get_grok_provider()
    if grok.is_available():
        print(f"\n🎯 Grok Opportunity Analysis:")
        opportunity_result = grok.market_opportunity_analysis(market_data)
        if not opportunity_result.get('error'):
            opportunity = opportunity_result.get('opportunity_analysis', '')
            print(f"Model: {opportunity_result.get('model')}")
            print(f"Opportunities: {opportunity[:350]}...")

def demo_compliance_analysis():
    """Demonstrate regulatory compliance analysis"""
    print("\n⚖️  Regulatory Compliance Analysis")
    print("=" * 50)
    
    compliance_scenario = """
    Regulatory Compliance Scenario:
    
    A hedge fund is launching a new quantitative trading strategy that uses AI/ML algorithms to:
    1. Analyze alternative data sources (satellite imagery, social media sentiment)
    2. Execute high-frequency trades across multiple asset classes
    3. Use leverage up to 10:1 on certain positions
    4. Target institutional and accredited investors
    5. Plans to register as an investment advisor
    
    The fund will operate in the US and plans to expand to EU markets within 2 years.
    What are the key regulatory requirements and compliance considerations?
    """
    
    print(f"Scenario: AI-powered quantitative hedge fund")
    print(f"Key Features: Alternative data, HFT, leverage, institutional focus")
    print(f"Jurisdictions: US (immediate), EU (planned)")
    
    # Claude compliance analysis (regulatory specialist)
    claude = get_claude_provider()
    if claude.is_available():
        print(f"\n📋 Claude Compliance Analysis:")
        compliance_result = claude.compliance_analysis(compliance_scenario, "US")
        if not compliance_result.get('error'):
            compliance = compliance_result.get('compliance_analysis', '')
            print(f"Model: {compliance_result.get('model')}")
            print(f"Compliance Requirements: {compliance[:400]}...")

def main():
    """Run the enhanced AI demonstration"""
    print("🚀 OperatorOS Enhanced AI Integration Demo")
    print("=" * 60)
    print("Showcasing Claude Sonnet-4 and Grok-2 for comprehensive financial analysis")
    print("=" * 60)
    
    results = {}
    
    try:
        # Check provider availability
        claude = get_claude_provider()
        grok = get_grok_provider()
        
        claude_available = claude.is_available()
        grok_available = grok.is_available()
        
        print(f"\nProvider Status:")
        print(f"✅ Claude Sonnet-4: {'Available' if claude_available else 'Unavailable'}")
        print(f"✅ Grok-2: {'Available' if grok_available else 'Unavailable'}")
        
        if not claude_available and not grok_available:
            print("❌ No AI providers available. Please check API keys.")
            return
        
        # Run demonstrations
        demo_multi_provider_financial_analysis()
        demo_risk_assessment()
        demo_market_sentiment()
        demo_compliance_analysis()
        
        print("\n🎉 Enhanced AI Demo Completed Successfully!")
        print("=" * 50)
        print("Key Capabilities Demonstrated:")
        print("• Multi-provider financial analysis (Claude + Grok)")
        print("• Advanced risk assessment with regulatory focus")
        print("• Market sentiment and opportunity analysis")  
        print("• Regulatory compliance analysis")
        print("• Real-time AI model comparison and insights")
        
        results['status'] = 'success'
        results['providers_tested'] = {
            'claude': claude_available,
            'grok': grok_available
        }
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        logging.error(f"Enhanced AI demo error: {e}")
        results['status'] = 'failed'
        results['error'] = str(e)
    
    # Save results
    with open('enhanced_ai_demo_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nDemo results saved to: enhanced_ai_demo_results.json")

if __name__ == "__main__":
    main()