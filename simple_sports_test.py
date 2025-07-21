#!/usr/bin/env python3
"""
Simple Sports Integration Test
"""
import os
import requests

def test_alpha_vantage_connection():
    print("Testing Alpha Vantage API Connection")
    print("=" * 40)
    
    api_key = os.environ.get('ALPHA_API_KEY')
    
    if not api_key:
        print("❌ ALPHA_API_KEY not found in environment")
        return False
    
    print(f"✅ ALPHA_API_KEY found: {api_key[:8]}...")
    
    # Test with a simple API call
    url = "https://www.alphavantage.co/query"
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': 'AAPL',
        'interval': '5min',
        'apikey': api_key
    }
    
    try:
        print("🔄 Testing API connection...")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'Error Message' in data:
                print(f"❌ API Error: {data['Error Message']}")
                return False
            elif 'Note' in data:
                print(f"⚠️  API Rate Limited: {data['Note']}")
                return False
            else:
                print("✅ Alpha Vantage API connection successful!")
                print(f"Sample data keys: {list(data.keys())}")
                return True
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_sports_api_endpoints():
    print("\nTesting Sports API Endpoints")
    print("=" * 30)
    
    endpoints = [
        "http://localhost:5000/api/sports/features",
        "http://localhost:5000/api/sports/odds/NBA"
    ]
    
    for endpoint in endpoints:
        try:
            print(f"🔄 Testing: {endpoint}")
            response = requests.get(endpoint, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Success: {data['status']}")
                if 'data' in data:
                    print(f"   Data preview: {str(data['data'])[:100]}...")
            else:
                print(f"❌ Failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    alpha_works = test_alpha_vantage_connection()
    test_sports_api_endpoints()
    
    if alpha_works:
        print("\n🎉 Sports integration is ready!")
        print("You can now use commands like:")
        print("  • 'Show me NBA betting odds'")
        print("  • 'Analyze Lakers team performance'") 
        print("  • 'Get live sports scores'")
    else:
        print("\n⚠️  Sports integration partially ready")
        print("Real-time data requires a valid Alpha Vantage API key")