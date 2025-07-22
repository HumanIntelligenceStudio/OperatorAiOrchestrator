"""
OpenFDA Data Provider
Integrates FDA drug, device, and food safety data for analysis
"""

import os
import requests
import json
from typing import Dict, List, Optional
import logging
from datetime import datetime, timedelta

class OpenFDAProvider:
    def __init__(self):
        self.api_key = os.environ.get('OPEN_FDA_KEY')
        self.base_url = "https://api.fda.gov"
        
        if not self.api_key:
            logging.warning("OPEN_FDA_KEY not found in environment variables")
    
    def test_connection(self) -> bool:
        """Test OpenFDA API connection"""
        try:
            # Test with drug adverse events endpoint
            url = f"{self.base_url}/drug/event.json"
            params = {
                'api_key': self.api_key,
                'limit': 1
            }
            
            response = requests.get(url, params=params, timeout=10)
            return response.status_code == 200
            
        except Exception as e:
            logging.error(f"OpenFDA connection test failed: {e}")
            return False
    
    def get_drug_adverse_events(self, drug_name: Optional[str] = None, limit: int = 10) -> Dict:
        """Get drug adverse event reports"""
        try:
            url = f"{self.base_url}/drug/event.json"
            params = {
                'api_key': self.api_key,
                'limit': limit
            }
            
            if drug_name:
                # Search for drug name in patient.drug.medicinalproduct
                params['search'] = f'patient.drug.medicinalproduct:"{drug_name}"'
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'drug_searched': drug_name,
                    'total_records': len(data.get('results', [])),
                    'analysis_type': 'drug_adverse_events'
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
                'message': 'Failed to retrieve drug adverse event data'
            }
    
    def get_drug_recalls(self, classification: Optional[str] = None, limit: int = 10) -> Dict:
        """Get drug recall information"""
        try:
            url = f"{self.base_url}/drug/enforcement.json"
            params = {
                'api_key': self.api_key,
                'limit': limit
            }
            
            if classification:
                # Class I, II, or III recalls
                params['search'] = f'classification:"{classification}"'
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'classification_filter': classification,
                    'total_records': len(data.get('results', [])),
                    'analysis_type': 'drug_recalls'
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
                'message': 'Failed to retrieve drug recall data'
            }
    
    def get_device_adverse_events(self, device_name: Optional[str] = None, limit: int = 10) -> Dict:
        """Get medical device adverse event reports"""
        try:
            url = f"{self.base_url}/device/event.json"
            params = {
                'api_key': self.api_key,
                'limit': limit
            }
            
            if device_name:
                params['search'] = f'device.generic_name:"{device_name}"'
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'device_searched': device_name,
                    'total_records': len(data.get('results', [])),
                    'analysis_type': 'device_adverse_events'
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
                'message': 'Failed to retrieve device adverse event data'
            }
    
    def get_food_recalls(self, limit: int = 10) -> Dict:
        """Get food recall information"""
        try:
            url = f"{self.base_url}/food/enforcement.json"
            params = {
                'api_key': self.api_key,
                'limit': limit
            }
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'status': 'success',
                    'data': data,
                    'total_records': len(data.get('results', [])),
                    'analysis_type': 'food_recalls'
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
                'message': 'Failed to retrieve food recall data'
            }
    
    def analyze_safety_trends(self, focus_area: str = "drugs") -> Dict:
        """Comprehensive safety trends analysis using FDA data"""
        try:
            results = {}
            
            if focus_area in ["drugs", "all"]:
                # Get drug adverse events
                drug_events = self.get_drug_adverse_events(limit=15)
                results['drug_adverse_events'] = drug_events
                
                # Get drug recalls
                drug_recalls = self.get_drug_recalls(limit=10)
                results['drug_recalls'] = drug_recalls
            
            if focus_area in ["devices", "all"]:
                # Get device adverse events
                device_events = self.get_device_adverse_events(limit=10)
                results['device_adverse_events'] = device_events
            
            if focus_area in ["food", "all"]:
                # Get food recalls
                food_recalls = self.get_food_recalls(limit=8)
                results['food_recalls'] = food_recalls
            
            total_records = sum([
                results.get('drug_adverse_events', {}).get('total_records', 0),
                results.get('drug_recalls', {}).get('total_records', 0),
                results.get('device_adverse_events', {}).get('total_records', 0),
                results.get('food_recalls', {}).get('total_records', 0)
            ])
            
            return {
                'status': 'success',
                'analysis_type': 'comprehensive_safety_trends',
                'focus_area': focus_area,
                'data_sources': list(results.keys()),
                'results': results,
                'total_data_points': total_records,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': 'Failed to perform comprehensive safety trends analysis'
            }
    
    def search_drug_interactions(self, drug_name: str, limit: int = 5) -> Dict:
        """Search for drug interaction data and adverse events"""
        try:
            # Get adverse events for specific drug
            adverse_events = self.get_drug_adverse_events(drug_name=drug_name, limit=limit)
            
            # Get recalls for the drug if any
            recalls = self.get_drug_recalls(limit=limit)
            
            return {
                'status': 'success',
                'drug_name': drug_name,
                'analysis_type': 'drug_safety_profile',
                'adverse_events': adverse_events,
                'recalls': recalls,
                'safety_assessment': 'Available for AI analysis',
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'message': f'Failed to analyze drug interactions for {drug_name}'
            }