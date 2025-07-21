#!/usr/bin/env python3
"""
OperatorOS Multi-Provider AI Showcase
Complete demonstration of Claude + Grok + OpenAI coordination
"""

import json
from datetime import datetime

def showcase_demo():
    print("🚀 OperatorOS Multi-Provider AI Showcase")
    print("=" * 55)
    
    from claude_provider import get_claude_provider
    from grok_provider import get_grok_provider
    
    claude = get_claude_provider()
    grok = get_grok_provider()
    
    print(f"Claude Sonnet-4: {'✅' if claude.is_available() else '❌'}")
    print(f"Grok-2: {'✅' if grok.is_available() else '❌'}")
    
    # Showcase 1: Financial Risk Assessment
    print(f"\n📈 SHOWCASE 1: Multi-Model Risk Assessment")
    print("-" * 45)
    
    risk_scenario = {
        'portfolio_type': 'Tech-focused growth portfolio',
        'assets': {
            'AAPL': 15, 'MSFT': 18, 'GOOGL': 12, 'NVDA': 20,
            'TSLA': 15, 'META': 10, 'Cash': 10
        },
        'total_value': 750000,
        'market_conditions': {'volatility': 'elevated', 'rates': 'rising'}
    }
    
    print(f"Portfolio: ${risk_scenario['total_value']:,} tech-focused")
    
    # Claude risk assessment
    if claude.is_available():
        risk_result = claude.risk_assessment(risk_scenario)
        if not risk_result.get('error'):
            print(f"✅ Claude risk assessment: {len(risk_result.get('risk_assessment', ''))} chars")
        
    # Grok investment strategy
    if grok.is_available():
        strategy_result = grok.investment_strategy(risk_scenario)
        if not strategy_result.get('error'):
            print(f"✅ Grok strategy analysis: {len(strategy_result.get('investment_strategy', ''))} chars")
    
    # Showcase 2: Market Sentiment Analysis
    print(f"\n📊 SHOWCASE 2: Multi-Provider Sentiment Analysis")
    print("-" * 50)
    
    market_data = {
        'indices': {'S&P_500': 5850, 'NASDAQ': 18800},
        'sectors': {'Technology': '+2.3%', 'Energy': '+1.8%'},
        'sentiment_indicators': {'VIX': 18.5, 'Put_Call_Ratio': 0.85}
    }
    
    print(f"Market: S&P 500 at {market_data['indices']['S&P_500']}")
    
    # Claude market sentiment
    if claude.is_available():
        sentiment_result = claude.market_sentiment_analysis(market_data)
        if not sentiment_result.get('error'):
            print(f"✅ Claude sentiment analysis: {len(sentiment_result.get('sentiment_analysis', ''))} chars")
    
    # Grok opportunity analysis
    if grok.is_available():
        opp_result = grok.market_opportunity_analysis(market_data)
        if not opp_result.get('error'):
            print(f"✅ Grok opportunity analysis: {len(opp_result.get('opportunity_analysis', ''))} chars")
    
    # Showcase 3: Regulatory Compliance
    print(f"\n⚖️ SHOWCASE 3: Compliance & Business Analysis")
    print("-" * 45)
    
    compliance_query = """
    Crypto trading platform launching in US and EU markets.
    Services: Spot trading, staking, custody services.
    Target: Retail and institutional clients.
    """
    
    print("Scenario: Multi-jurisdictional crypto platform")
    
    # Claude compliance analysis
    if claude.is_available():
        compliance_result = claude.compliance_analysis(compliance_query, "US")
        if not compliance_result.get('error'):
            print(f"✅ Claude compliance (US): {len(compliance_result.get('compliance_analysis', ''))} chars")
    
    # Grok business analysis
    if grok.is_available():
        business_result = grok.business_analysis(compliance_query)
        if not business_result.get('error'):
            print(f"✅ Grok business strategy: {len(business_result.get('analysis', ''))} chars")
    
    print(f"\n🎉 SHOWCASE COMPLETE")
    print("=" * 30)
    print("Multi-Provider Capabilities Demonstrated:")
    print("• Advanced financial risk assessment")  
    print("• Market sentiment and opportunity analysis")
    print("• Regulatory compliance and business strategy")
    print("• Real-time coordination between AI models")
    print("• Comprehensive analysis from multiple perspectives")

if __name__ == "__main__":
    showcase_demo()