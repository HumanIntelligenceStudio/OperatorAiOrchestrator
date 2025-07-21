#!/usr/bin/env python3
"""
Test Sports Integration with Alpha Vantage API
"""

import sys
import os
sys.path.append('.')

from sports_data_provider import SportsDataProvider
from agent_pools import SpecializedAgentPools
import json

def test_sports_integration():
    print("🏈 Testing Sports Integration with Alpha Vantage API")
    print("=" * 50)
    
    # Initialize sports data provider
    sports_provider = SportsDataProvider()
    
    # Test 1: Check available features
    print("\n📋 Available Features:")
    features = sports_provider.get_available_features()
    print(json.dumps(features, indent=2))
    
    # Test 2: Test betting odds (if Alpha Vantage key available)
    print("\n🎲 Testing Sports Betting Odds:")
    if features['alpha_vantage_available']:
        odds_data = sports_provider.get_sports_betting_odds("NBA")
        print(f"Betting odds result: {json.dumps(odds_data, indent=2)[:200]}...")
    else:
        print("❌ Alpha Vantage API key required for betting odds")
    
    # Test 3: Test agent pool integration
    print("\n🤖 Testing Agent Pool Integration:")
    agent_pools = SpecializedAgentPools()
    
    # Test sports query routing
    test_queries = [
        "Show me NBA betting odds for tonight",
        "What are the live scores for Lakers vs Warriors?",
        "Analyze the Patriots performance this season"
    ]
    
    for query in test_queries:
        print(f"\n📝 Query: '{query}'")
        # This would normally route to AI, but we'll just test the context building
        try:
            context = agent_pools._get_sports_data_context(query)
            print(f"   Context generated: {json.dumps(context, indent=4)[:300]}...")
        except Exception as e:
            print(f"   Error: {e}")
    
    print("\n✅ Sports Integration Test Complete!")
    print("🔑 Note: Full functionality requires Alpha Vantage and Polygon.io API keys")

if __name__ == "__main__":
    test_sports_integration()