"""
CMS (Centers for Medicare & Medicaid Services) Data Provider
Integrates healthcare data from CMS APIs for analysis
"""

import os
import requests
import json
from typing import Dict, List, Optional
import logging

class CMSProvider:
    def __init__(self):
        self.api_key = os.environ.get('CMS_KEY')
        self.base_url = "https://data.cms.gov/api/1"
        
        if not self.api_key:
            logging.warning("CMS_KEY not found in environment variables")
    
    def test_connection(self) -> bool:
        """Test CMS API connection"""
        try:
            # Test with a simple dataset query
            url = f"{self.base_url}/datastore/query"
            headers = {
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json'
            }
            
            # Simple test query
            params = {
                'limit': 1
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            return response.status_code == 200
            
        except Exception as e:
            logging.error(f"CMS connection test failed: {e}")
            return False
    
    def get_hospital_quality_data(self, state: Optional[str] = None, limit: int = 10) -> Dict:
        """Get hospital quality and safety data"""
        try:
            url = f"{self.base_url}/datastore/query"
            headers = {
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json'
            }
            
            params = {
                'limit': limit,
                'offset': 0
            }
            
            if state:
                state_filter = json.dumps({
                    'state': state.upper()
                })
                params['filters'] = state_filter
            
            response = requests.get(url, headers=headers, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'total_records': len(data.get('results', [])),
                    'query_parameters': params
                }
            else:
                return {
                    'status': 'error',
                    'error': f"API returned status {response.status_code}",
                    'message': response.text
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Failed to retrieve CMS hospital quality data'
            }
    
    def get_medicare_spending_data(self, year: Optional[str] = None, limit: int = 10) -> Dict:
        """Get Medicare spending per beneficiary data"""
        try:
            # CMS Medicare Spending Per Beneficiary dataset
            url = f"{self.base_url}/datastore/query"
            headers = {
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json'
            }
            
            params = {
                'limit': limit,
                'offset': 0
            }
            
            if year:
                year_filter = json.dumps({
                    'year': year
                })
                params['filters'] = year_filter
            
            response = requests.get(url, headers=headers, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'total_records': len(data.get('results', [])),
                    'analysis_type': 'medicare_spending',
                    'query_parameters': params
                }
            else:
                return {
                    'status': 'error',
                    'error': f"API returned status {response.status_code}",
                    'message': response.text
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Failed to retrieve Medicare spending data'
            }
    
    def get_provider_comparison_data(self, provider_type: str = "hospital", limit: int = 5) -> Dict:
        """Get provider comparison data for quality metrics"""
        try:
            url = f"{self.base_url}/datastore/query"
            headers = {
                'X-API-Key': self.api_key,
                'Content-Type': 'application/json'
            }
            
            params = {
                'limit': limit,
                'offset': 0
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'provider_type': provider_type,
                    'total_records': len(data.get('results', [])),
                    'analysis_focus': 'provider_quality_comparison'
                }
            else:
                return {
                    'status': 'error',
                    'error': f"API returned status {response.status_code}",
                    'message': response.text
                }
                
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Failed to retrieve provider comparison data'
            }

    def analyze_healthcare_trends(self, focus_area: str = "quality") -> Dict:
        """Comprehensive healthcare trends analysis using CMS data"""
        try:
            results = {}
            
            # Get hospital quality data
            quality_data = self.get_hospital_quality_data(limit=20)
            results['quality_metrics'] = quality_data
            
            # Get Medicare spending data
            spending_data = self.get_medicare_spending_data(limit=15)
            results['spending_analysis'] = spending_data
            
            # Get provider comparison
            comparison_data = self.get_provider_comparison_data(limit=10)
            results['provider_comparison'] = comparison_data
            
            return {
                'status': 'success',
                'analysis_type': 'comprehensive_healthcare_trends',
                'focus_area': focus_area,
                'data_sources': ['hospital_quality', 'medicare_spending', 'provider_comparison'],
                'results': results,
                'total_data_points': sum([
                    quality_data.get('total_records', 0),
                    spending_data.get('total_records', 0),
                    comparison_data.get('total_records', 0)
                ])
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Failed to perform comprehensive healthcare trends analysis'
            }