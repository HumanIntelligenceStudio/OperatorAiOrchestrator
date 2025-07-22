#!/usr/bin/env python3
"""
Healthcare API Integration Test
Tests the CMS and OpenFDA API endpoints directly
"""

import requests
import json
from cms_provider import CMSProvider
from openfda_provider import OpenFDAProvider

def test_healthcare_apis():
    """Test healthcare API integration directly"""
    print("=== OperatorOS Healthcare API Integration Test ===")
    print()
    
    # Test CMS Provider
    print("1. Testing CMS (Centers for Medicare & Medicaid Services)...")
    cms = CMSProvider()
    cms_status = cms.test_connection()
    print(f"   CMS API Status: {'✅ Connected' if cms_status else '❌ Failed'}")
    
    if cms_status:
        print("   Testing CMS hospital quality data...")
        quality_data = cms.get_hospital_quality_data(limit=3)
        print(f"   Status: {quality_data.get('status', 'unknown')}")
        print(f"   Records: {quality_data.get('total_records', 0)}")
    
    print()
    
    # Test OpenFDA Provider
    print("2. Testing OpenFDA (Food and Drug Administration)...")
    fda = OpenFDAProvider()
    fda_status = fda.test_connection()
    print(f"   FDA API Status: {'✅ Connected' if fda_status else '❌ Failed'}")
    
    if fda_status:
        print("   Testing FDA drug adverse events...")
        drug_data = fda.get_drug_adverse_events(limit=3)
        print(f"   Status: {drug_data.get('status', 'unknown')}")
        print(f"   Records: {drug_data.get('total_records', 0)}")
        
        if drug_data.get('status') == 'success':
            total_available = drug_data.get('data', {}).get('meta', {}).get('results', {}).get('total', 0)
            print(f"   Total FDA Records Available: {total_available:,}")
    
    print()
    
    # Summary
    print("3. Healthcare Integration Summary:")
    print(f"   CMS API: {'✅ Operational' if cms_status else '❌ Failed'}")
    print(f"   FDA API: {'✅ Operational' if fda_status else '❌ Failed'}")
    print(f"   Overall Status: {'✅ Healthcare APIs Ready' if (cms_status and fda_status) else '⚠️ Partial Integration'}")
    
    return {
        'cms_status': cms_status,
        'fda_status': fda_status,
        'overall_success': cms_status and fda_status
    }

if __name__ == "__main__":
    results = test_healthcare_apis()
    exit(0 if results['overall_success'] else 1)