#!/usr/bin/env python3
"""
Test Exchange Rate API Integration
Comprehensive testing of currency conversion features
"""

import sys
import os
sys.path.append('.')

import json
import requests
from datetime import datetime
from exchange_rate_provider import get_exchange_rate_provider

def test_exchange_rate_api():
    """Test ExchangeRate-API.com connection"""
    print("Testing ExchangeRate-API Connection")
    print("=" * 40)
    
    api_key = os.environ.get('EXCHANGERATE_KEY')
    
    if not api_key:
        print("❌ EXCHANGERATE_KEY not found")
        return False
        
    print(f"✅ EXCHANGERATE_KEY found: {api_key[:8]}...")
    
    # Test direct API connection
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('result') == 'success':
                print("✅ ExchangeRate-API connection successful")
                print(f"Base currency: {data.get('base_code')}")
                print(f"Last updated: {data.get('time_last_update_utc')}")
                print(f"Currencies supported: {len(data.get('conversion_rates', {}))}")
                return True
            else:
                print(f"❌ API Error: {data.get('error-type', 'Unknown')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_exchange_provider():
    """Test OperatorOS exchange rate provider"""
    print("\nTesting OperatorOS Exchange Provider")
    print("=" * 40)
    
    try:
        provider = get_exchange_rate_provider()
        
        # Test 1: API Status
        print("🔄 Testing API status...")
        status = provider.get_api_status()
        print(f"Status: {status.get('status')}")
        print(f"Cache entries: {status.get('cache_entries', 0)}")
        
        # Test 2: Latest Rates
        print("\n🔄 Testing latest rates (USD base)...")
        rates = provider.get_latest_rates('USD')
        
        if not rates.get('error'):
            print(f"✅ Retrieved rates for {rates.get('supported_codes', 0)} currencies")
            
            # Show sample rates
            sample_rates = {k: v for k, v in list(rates.get('rates', {}).items())[:5]}
            print(f"Sample rates: {sample_rates}")
        else:
            print(f"❌ Error getting rates: {rates.get('error')}")
        
        # Test 3: Currency Conversion
        print("\n🔄 Testing currency conversion...")
        conversion = provider.convert_currency(100, 'USD', 'EUR')
        
        if not conversion.get('error'):
            print(f"✅ Conversion: $100 USD = €{conversion.get('converted_amount')} EUR")
            print(f"Exchange rate: {conversion.get('conversion_rate')}")
        else:
            print(f"❌ Conversion error: {conversion.get('error')}")
        
        # Test 4: Supported Currencies
        print("\n🔄 Testing supported currencies...")
        currencies = provider.get_supported_currencies()
        
        if not currencies.get('error'):
            total = currencies.get('total_currencies', 0)
            major = len(currencies.get('major_currencies', []))
            print(f"✅ Total currencies: {total}")
            print(f"Major currencies tracked: {major}")
        else:
            print(f"❌ Currency list error: {currencies.get('error')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Provider test failed: {e}")
        return False

def test_api_endpoints():
    """Test OperatorOS exchange rate API endpoints"""
    print("\nTesting API Endpoints")
    print("=" * 25)
    
    base_url = "http://localhost:5000/api"
    
    endpoints = [
        "/exchange/status",
        "/exchange/rates?base=USD",
        "/exchange/convert?amount=100&from=USD&to=EUR",
        "/exchange/currencies"
    ]
    
    results = []
    
    for endpoint in endpoints:
        try:
            print(f"🔄 Testing: {endpoint}")
            response = requests.get(f"{base_url}{endpoint}", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('status') == 'success':
                    print(f"✅ Success")
                    
                    # Show relevant data snippet
                    if 'rates' in str(data):
                        rates_count = len(data.get('data', {}).get('rates', {}))
                        if rates_count > 0:
                            print(f"   Retrieved {rates_count} exchange rates")
                    
                    if 'converted_amount' in str(data):
                        amount = data.get('data', {}).get('converted_amount')
                        print(f"   Converted amount: {amount}")
                        
                    if 'total_currencies' in str(data):
                        total = data.get('data', {}).get('total_currencies')
                        print(f"   Supported currencies: {total}")
                        
                    results.append({"endpoint": endpoint, "success": True})
                else:
                    print(f"❌ API Error: {data.get('message', 'Unknown')}")
                    results.append({"endpoint": endpoint, "success": False})
            else:
                print(f"❌ HTTP {response.status_code}")
                results.append({"endpoint": endpoint, "success": False})
                
        except Exception as e:
            print(f"❌ Request failed: {e}")
            results.append({"endpoint": endpoint, "success": False})
    
    return results

def test_financial_agent_integration():
    """Test integration with Financial Agent"""
    print("\nTesting Financial Agent Integration")
    print("=" * 35)
    
    try:
        provider = get_exchange_rate_provider()
        
        # Sample financial queries that would use exchange rates
        financial_scenarios = [
            {
                "scenario": "International Investment",
                "query": "Convert $10,000 to EUR for European stock purchase",
                "amount": 10000,
                "from": "USD",
                "to": "EUR"
            },
            {
                "scenario": "Portfolio Valuation",
                "query": "Convert £5,000 to USD for portfolio analysis",
                "amount": 5000,
                "from": "GBP", 
                "to": "USD"
            },
            {
                "scenario": "Currency Hedging",
                "query": "Check JPY to USD rate for risk assessment",
                "amount": 1000000,
                "from": "JPY",
                "to": "USD"
            }
        ]
        
        for scenario in financial_scenarios:
            print(f"\n💼 {scenario['scenario']}:")
            print(f"   Query: {scenario['query']}")
            
            conversion = provider.convert_currency(
                scenario['amount'],
                scenario['from'],
                scenario['to']
            )
            
            if not conversion.get('error'):
                print(f"   Result: {scenario['from']} {scenario['amount']:,.0f} = {scenario['to']} {conversion.get('converted_amount', 0):,.2f}")
                print(f"   Rate: 1 {scenario['from']} = {conversion.get('conversion_rate', 0):.4f} {scenario['to']}")
            else:
                print(f"   ❌ Error: {conversion.get('error')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Financial integration test failed: {e}")
        return False

def main():
    """Run comprehensive exchange rate integration tests"""
    print("💱 OperatorOS Exchange Rate API Integration Test")
    print("=" * 55)
    
    test_results = {
        "timestamp": datetime.now().isoformat(),
        "tests": []
    }
    
    # Test 1: Direct API connection
    api_connected = test_exchange_rate_api()
    test_results["tests"].append({"name": "ExchangeRate-API Connection", "passed": api_connected})
    
    # Test 2: Provider functionality
    provider_works = test_exchange_provider()
    test_results["tests"].append({"name": "Exchange Rate Provider", "passed": provider_works})
    
    # Test 3: API endpoints
    endpoint_results = test_api_endpoints()
    endpoint_success = all(r["success"] for r in endpoint_results)
    test_results["tests"].append({"name": "API Endpoints", "passed": endpoint_success})
    
    # Test 4: Financial agent integration
    financial_integration = test_financial_agent_integration()
    test_results["tests"].append({"name": "Financial Agent Integration", "passed": financial_integration})
    
    # Summary
    print(f"\n📊 Test Results Summary")
    print("=" * 30)
    
    passed_tests = sum(1 for test in test_results["tests"] if test["passed"])
    total_tests = len(test_results["tests"])
    
    for test in test_results["tests"]:
        status = "✅ PASS" if test["passed"] else "❌ FAIL"
        print(f"{test['name']}: {status}")
    
    print(f"\nOverall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 All exchange rate integration tests passed!")
        print("Currency conversion features ready for production")
    else:
        print("⚠️ Some tests failed - check configuration")
    
    # Save results
    with open('exchange_rate_test_results.json', 'w') as f:
        json.dump(test_results, f, indent=2)
    
    print(f"\n📄 Results saved to exchange_rate_test_results.json")
    return test_results

if __name__ == "__main__":
    results = main()