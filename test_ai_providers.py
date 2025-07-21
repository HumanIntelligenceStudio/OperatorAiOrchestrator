#!/usr/bin/env python3
"""
Simple test script for Claude and Grok AI providers
Tests the integration without circular import issues
"""

import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_claude_provider():
    """Test Claude provider directly"""
    print("\n🔍 Testing Claude Provider")
    print("=" * 40)
    
    try:
        from claude_provider import get_claude_provider
        
        claude = get_claude_provider()
        
        if not claude.is_available():
            print("❌ Claude provider not available")
            return False
        
        # Test connection
        print("Testing connection...")
        conn_test = claude.test_connection()
        if conn_test.get('connected'):
            print(f"✅ Claude connected: {conn_test.get('model', 'Unknown model')}")
        else:
            print(f"❌ Claude connection failed: {conn_test.get('error', 'Unknown error')}")
            return False
        
        # Test financial analysis
        print("\nTesting financial analysis...")
        query = "Analyze the current cryptocurrency market trends and provide investment recommendations."
        result = claude.financial_analysis(query)
        
        if result.get('error'):
            print(f"❌ Financial analysis failed: {result.get('error')}")
            return False
        else:
            print(f"✅ Financial analysis successful")
            print(f"   Model: {result.get('model', 'Unknown')}")
            print(f"   Response length: {len(result.get('analysis', ''))}")
        
        # Test risk assessment
        print("\nTesting risk assessment...")
        investment_data = {
            'asset_type': 'Technology Stocks',
            'allocation': {'AAPL': 30, 'MSFT': 25, 'GOOGL': 25, 'NVDA': 20},
            'total_value': 100000,
            'time_horizon': '5 years'
        }
        
        risk_result = claude.risk_assessment(investment_data)
        if risk_result.get('error'):
            print(f"❌ Risk assessment failed: {risk_result.get('error')}")
        else:
            print(f"✅ Risk assessment successful")
            print(f"   Model: {risk_result.get('model', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Claude test failed: {e}")
        logging.error(f"Claude test error: {e}")
        return False

def test_grok_provider():
    """Test Grok provider directly"""
    print("\n🔍 Testing Grok Provider")
    print("=" * 40)
    
    try:
        from grok_provider import get_grok_provider
        
        grok = get_grok_provider()
        
        if not grok.is_available():
            print("❌ Grok provider not available")
            return False
        
        # Test connection
        print("Testing connection...")
        conn_test = grok.test_connection()
        if conn_test.get('connected'):
            print(f"✅ Grok connected: {conn_test.get('model', 'Unknown model')}")
        else:
            print(f"❌ Grok connection failed: {conn_test.get('error', 'Unknown error')}")
            return False
        
        # Test business analysis
        print("\nTesting business analysis...")
        query = "Analyze the competitive landscape for AI-powered financial services startups in 2025."
        result = grok.business_analysis(query)
        
        if result.get('error'):
            print(f"❌ Business analysis failed: {result.get('error')}")
            return False
        else:
            print(f"✅ Business analysis successful")
            print(f"   Model: {result.get('model', 'Unknown')}")
            print(f"   Response length: {len(result.get('analysis', ''))}")
        
        # Test sentiment analysis
        print("\nTesting sentiment analysis...")
        text = "The market is showing strong bullish sentiment with record highs across major indices."
        sentiment_result = grok.sentiment_analysis(text)
        
        if sentiment_result.get('error'):
            print(f"❌ Sentiment analysis failed: {sentiment_result.get('error')}")
        else:
            print(f"✅ Sentiment analysis successful")
            print(f"   Rating: {sentiment_result.get('rating', 'Unknown')}/5")
            print(f"   Confidence: {sentiment_result.get('confidence', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Grok test failed: {e}")
        logging.error(f"Grok test error: {e}")
        return False

def test_api_endpoints():
    """Test the new API endpoints"""
    print("\n🔍 Testing API Endpoints")
    print("=" * 40)
    
    import requests
    
    base_url = "http://localhost:5000"
    
    endpoints_to_test = [
        "/ai/providers/status",
        "/ai/providers/test"
    ]
    
    for endpoint in endpoints_to_test:
        try:
            print(f"Testing {endpoint}...")
            response = requests.get(f"{base_url}{endpoint}", timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {endpoint} successful")
                if 'data' in data:
                    if 'providers' in data['data']:
                        providers = list(data['data']['providers'].keys())
                        print(f"   Available providers: {', '.join(providers)}")
            else:
                print(f"❌ {endpoint} failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ {endpoint} error: {e}")

def main():
    """Main test execution"""
    print("🚀 OperatorOS AI Provider Integration Test")
    print("=" * 50)
    print("Testing Claude and Grok AI provider integration")
    print("=" * 50)
    
    test_results = {
        'timestamp': datetime.now().isoformat(),
        'tests': {}
    }
    
    # Test Claude
    test_results['tests']['claude'] = test_claude_provider()
    
    # Test Grok
    test_results['tests']['grok'] = test_grok_provider()
    
    # Test API endpoints
    try:
        test_api_endpoints()
        test_results['tests']['api_endpoints'] = True
    except Exception as e:
        print(f"API endpoint tests failed: {e}")
        test_results['tests']['api_endpoints'] = False
    
    # Summary
    print("\n📊 Test Results Summary")
    print("=" * 30)
    
    successful_tests = sum(1 for result in test_results['tests'].values() if result)
    total_tests = len(test_results['tests'])
    
    for test_name, result in test_results['tests'].items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.upper()}: {status}")
    
    print(f"\nOverall: {successful_tests}/{total_tests} tests passed")
    
    if successful_tests == total_tests:
        print("🎉 All tests passed! Multi-provider AI integration is working.")
    else:
        print("⚠️  Some tests failed. Check the error messages above.")
    
    # Save results
    with open('ai_provider_test_results.json', 'w') as f:
        json.dump(test_results, f, indent=2, default=str)
    
    print(f"\nTest results saved to: ai_provider_test_results.json")

if __name__ == "__main__":
    main()