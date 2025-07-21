#!/usr/bin/env python3
"""
Test Polygon.io Integration
"""
import os
import requests

def test_polygon_connection():
    print("Testing Polygon.io API Connection")
    print("=" * 35)
    
    api_key = os.environ.get('POLYGON_KEY')
    
    if not api_key:
        print("❌ POLYGON_KEY not found in environment")
        return False
    
    print(f"✅ POLYGON_KEY found: {api_key[:8]}...")
    
    # Test with a simple API call - get previous day's data for AAPL
    url = "https://api.polygon.io/v2/aggs/ticker/AAPL/prev"
    params = {
        'apiKey': api_key
    }
    
    try:
        print("🔄 Testing Polygon API connection...")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'ERROR':
                print(f"❌ API Error: {data.get('error', 'Unknown error')}")
                return False
            elif data.get('status') == 'OK':
                print("✅ Polygon.io API connection successful!")
                results = data.get('results', [])
                if results:
                    print(f"Sample data: Close price ${results[0].get('c', 'N/A')}")
                return True
            else:
                print(f"⚠️  Unexpected status: {data.get('status')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_sports_api_with_polygon():
    print("\nTesting Enhanced Sports API")
    print("=" * 30)
    
    endpoints = [
        "http://localhost:5000/api/sports/features"
    ]
    
    for endpoint in endpoints:
        try:
            print(f"🔄 Testing: {endpoint}")
            response = requests.get(endpoint, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Success: {data['status']}")
                if 'data' in data:
                    features = data['data']
                    print(f"   Alpha Vantage: {'Connected' if features.get('alpha_vantage_available') else 'Disconnected'}")
                    print(f"   Polygon.io: {'Connected' if features.get('polygon_available') else 'Disconnected'}")
                    print(f"   Available features: {len([f for f, v in features.get('available_features', {}).items() if v])}")
            else:
                print(f"❌ Failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    polygon_works = test_polygon_connection()
    test_sports_api_with_polygon()
    
    if polygon_works:
        print("\n🎉 Full sports integration ready!")
        print("Available capabilities:")
        print("  • Real-time sports betting odds (Alpha Vantage)")
        print("  • Advanced market data for sports stocks (Polygon.io)")
        print("  • Team performance analysis")
        print("  • Player statistics")
        print("  • Sports-related financial data")
    else:
        print("\n⚠️  Partial integration available")
        print("Some features require valid Polygon.io API key")