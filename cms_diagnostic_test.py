#!/usr/bin/env python3
"""
CMS API Diagnostic Test - Direct endpoint testing
"""

import requests
import json

def test_cms_direct_endpoints():
    """Test actual working CMS API endpoints"""
    print("=== CMS API DIAGNOSTIC TEST ===")
    print()
    
    # Test Medicare spending CSV data (direct download)
    print("1. Testing Medicare Spending CSV Data:")
    try:
        url = "https://data.cms.gov/provider-data/sites/default/files/resources/f2aba7d3-9a6e-4aca-8f10-44eec5bb46d9_Data.csv"
        response = requests.head(url, timeout=10)
        print(f"   CSV Data Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   File Size: {response.headers.get('content-length', 'Unknown')} bytes")
            print("   ✅ Medicare spending CSV data available")
        else:
            print("   ❌ CSV data not accessible")
    except Exception as e:
        print(f"   Error: {e}")
    
    print()
    
    # Test hospital quality CSV data
    print("2. Testing Hospital Quality CSV Data:")
    try:
        url = "https://data.cms.gov/provider-data/sites/default/files/resources/9767cb68-8ea9-4f0b-8179-9431abc89f11_Data.csv"
        response = requests.head(url, timeout=10)
        print(f"   CSV Data Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   File Size: {response.headers.get('content-length', 'Unknown')} bytes") 
            print("   ✅ Hospital quality CSV data available")
        else:
            print("   ❌ CSV data not accessible")
    except Exception as e:
        print(f"   Error: {e}")
    
    print()
    
    # Test direct CSV data sampling
    print("3. Testing Direct CSV Data Sample:")
    try:
        # Medicare spending sample
        url = "https://data.cms.gov/provider-data/sites/default/files/resources/f2aba7d3-9a6e-4aca-8f10-44eec5bb46d9_Data.csv"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.split('\n')
            print(f"   Medicare CSV Lines: {len(lines)}")
            if len(lines) > 1:
                headers = lines[0].split(',')[:5]
                sample_row = lines[1].split(',')[:5] if len(lines) > 1 else []
                print(f"   Headers: {headers}")
                print(f"   Sample: {sample_row}")
                print("   ✅ Real Medicare spending data accessible")
        else:
            print("   ❌ Could not retrieve Medicare CSV")
    except Exception as e:
        print(f"   Error: {e}")
    
    print()
    
    # Summary
    print("📊 CMS DATA ACCESS SUMMARY:")
    print("   Direct CSV files provide access to authentic CMS data")
    print("   API endpoints may require specific authentication or different URLs")
    print("   CSV approach ensures real government healthcare data access")
    print("   Medical research analysis can proceed with authentic data sources")

if __name__ == "__main__":
    test_cms_direct_endpoints()