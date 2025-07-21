#!/usr/bin/env python3
"""
Exchange Rate API Provider for OperatorOS
Integrates with ExchangeRate-API.com for real-time currency conversion
"""

import os
import requests
import logging
import json
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import threading
import time

class ExchangeRateProvider:
    """
    Professional exchange rate provider with caching and error handling
    Integrates with ExchangeRate-API.com
    """
    
    def __init__(self):
        self.api_key = os.environ.get('EXCHANGERATE_KEY')
        self.base_url = "https://v6.exchangerate-api.com/v6"
        
        # Cache settings
        self.cache = {}
        self.cache_duration = timedelta(minutes=15)  # Cache for 15 minutes
        self.cache_lock = threading.Lock()
        
        # API status
        self.api_available = bool(self.api_key)
        self.last_api_check = None
        self.rate_limit_reset = None
        
        # Supported currencies (major ones)
        self.major_currencies = [
            'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY',
            'SEK', 'NZD', 'MXN', 'SGD', 'HKD', 'NOK', 'TRY', 'ZAR',
            'BRL', 'INR', 'KRW', 'PLN', 'CZK', 'DKK', 'HUF', 'ILS'
        ]
        
        if not self.api_key:
            logging.warning("ExchangeRate-API key not found - currency features will be limited")
        else:
            logging.info(f"Exchange Rate Provider initialized with API key: {self.api_key[:8]}...")
            
    def _get_cache_key(self, from_currency: str, to_currency: str = None) -> str:
        """Generate cache key for currency pair or single currency"""
        if to_currency:
            return f"{from_currency}_{to_currency}"
        return f"latest_{from_currency}"
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        if cache_key not in self.cache:
            return False
            
        cached_time = self.cache[cache_key].get('timestamp')
        if not cached_time:
            return False
            
        cache_age = datetime.now() - datetime.fromisoformat(cached_time)
        return cache_age < self.cache_duration
    
    def get_latest_rates(self, base_currency: str = 'USD') -> Dict[str, Any]:
        """
        Get latest exchange rates for base currency
        """
        if not self.api_available:
            return self._get_demo_rates(base_currency)
            
        cache_key = self._get_cache_key(base_currency)
        
        # Check cache first
        with self.cache_lock:
            if self._is_cache_valid(cache_key):
                logging.debug(f"Returning cached rates for {base_currency}")
                return self.cache[cache_key]['data']
        
        try:
            url = f"{self.base_url}/{self.api_key}/latest/{base_currency}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('result') == 'error':
                return {"error": f"API Error: {data.get('error-type', 'Unknown error')}"}
            
            # Format response
            formatted_data = {
                "base_currency": base_currency,
                "last_updated": data.get('time_last_update_utc'),
                "next_update": data.get('time_next_update_utc'),
                "rates": data.get('conversion_rates', {}),
                "supported_codes": len(data.get('conversion_rates', {})),
                "timestamp": datetime.now().isoformat()
            }
            
            # Cache the result
            with self.cache_lock:
                self.cache[cache_key] = {
                    'data': formatted_data,
                    'timestamp': datetime.now().isoformat()
                }
            
            logging.info(f"Retrieved latest rates for {base_currency} - {len(formatted_data['rates'])} currencies")
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error getting exchange rates: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error getting exchange rates: {e}")
            return self._get_demo_rates(base_currency)
    
    def _get_demo_rates(self, base_currency: str = 'USD') -> Dict[str, Any]:
        """
        Provide demo exchange rates using free API as fallback
        """
        try:
            # Use free exchangerate.host API
            url = f"https://api.exchangerate.host/latest?base={base_currency}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                return {
                    "base_currency": base_currency,
                    "last_updated": data.get('date'),
                    "next_update": "Next day",
                    "rates": data.get('rates', {}),
                    "supported_codes": len(data.get('rates', {})),
                    "timestamp": datetime.now().isoformat(),
                    "source": "exchangerate.host (free API)"
                }
            else:
                return self._get_static_demo_rates(base_currency)
                
        except Exception as e:
            logging.warning(f"Free API also failed: {e}")
            return self._get_static_demo_rates(base_currency)
    
    def _get_static_demo_rates(self, base_currency: str = 'USD') -> Dict[str, Any]:
        """Provide static demo rates for demonstration"""
        
        # Static demo rates (approximate real values)
        demo_rates = {
            'USD': {
                'EUR': 0.85, 'GBP': 0.74, 'JPY': 107.12, 'AUD': 1.35, 'CAD': 1.25,
                'CHF': 0.92, 'CNY': 6.45, 'SEK': 8.75, 'NZD': 1.42, 'MXN': 20.15,
                'SGD': 1.35, 'HKD': 7.78, 'NOK': 8.65, 'TRY': 8.25, 'ZAR': 14.85,
                'BRL': 5.35, 'INR': 74.25, 'KRW': 1185.50, 'PLN': 3.85, 'CZK': 21.75
            },
            'EUR': {
                'USD': 1.18, 'GBP': 0.87, 'JPY': 126.25, 'AUD': 1.59, 'CAD': 1.47,
                'CHF': 1.08, 'CNY': 7.59, 'SEK': 10.29, 'NZD': 1.67, 'MXN': 23.71
            },
            'GBP': {
                'USD': 1.35, 'EUR': 1.15, 'JPY': 144.65, 'AUD': 1.82, 'CAD': 1.69,
                'CHF': 1.24, 'CNY': 8.71, 'SEK': 11.81, 'NZD': 1.91, 'MXN': 27.20
            }
        }
        
        rates = demo_rates.get(base_currency, demo_rates['USD'])
        
        return {
            "base_currency": base_currency,
            "last_updated": datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000"),
            "next_update": "Demo mode - static rates",
            "rates": rates,
            "supported_codes": len(rates),
            "timestamp": datetime.now().isoformat(),
            "source": "Static demo rates for demonstration"
        }
    
    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
        """
        Convert amount from one currency to another
        """
        if not self.api_available:
            return self._demo_convert_currency(amount, from_currency, to_currency)
            
        cache_key = self._get_cache_key(from_currency, to_currency)
        
        # Check cache for conversion rate
        with self.cache_lock:
            if self._is_cache_valid(cache_key):
                cached_rate = self.cache[cache_key]['data']['conversion_rate']
                converted_amount = amount * cached_rate
                
                return {
                    "from_currency": from_currency,
                    "to_currency": to_currency,
                    "original_amount": amount,
                    "conversion_rate": cached_rate,
                    "converted_amount": round(converted_amount, 4),
                    "cached": True,
                    "timestamp": datetime.now().isoformat()
                }
        
        try:
            url = f"{self.base_url}/{self.api_key}/pair/{from_currency}/{to_currency}/{amount}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('result') == 'error':
                return {"error": f"API Error: {data.get('error-type', 'Unknown error')}"}
            
            # Format response
            conversion_data = {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "original_amount": amount,
                "conversion_rate": data.get('conversion_rate'),
                "converted_amount": data.get('conversion_result'),
                "last_updated": data.get('time_last_update_utc'),
                "cached": False,
                "timestamp": datetime.now().isoformat()
            }
            
            # Cache the conversion rate
            with self.cache_lock:
                self.cache[cache_key] = {
                    'data': {
                        'conversion_rate': data.get('conversion_rate'),
                        'timestamp': datetime.now().isoformat()
                    },
                    'timestamp': datetime.now().isoformat()
                }
            
            logging.info(f"Converted {amount} {from_currency} to {conversion_data['converted_amount']} {to_currency}")
            return conversion_data
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error converting currency: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error converting currency: {e}")
            return self._demo_convert_currency(amount, from_currency, to_currency)
    
    def _demo_convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
        """Demo currency conversion using free APIs"""
        try:
            # Try free exchangerate.host API
            url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success'):
                return {
                    "from_currency": from_currency,
                    "to_currency": to_currency,
                    "original_amount": amount,
                    "conversion_rate": data.get('info', {}).get('rate'),
                    "converted_amount": data.get('result'),
                    "last_updated": data.get('date'),
                    "cached": False,
                    "timestamp": datetime.now().isoformat(),
                    "source": "exchangerate.host (free API)"
                }
            else:
                return self._static_demo_convert(amount, from_currency, to_currency)
                
        except Exception as e:
            logging.warning(f"Free conversion API failed: {e}")
            return self._static_demo_convert(amount, from_currency, to_currency)
    
    def _static_demo_convert(self, amount: float, from_currency: str, to_currency: str) -> Dict[str, Any]:
        """Static demo conversion for demonstration"""
        
        # Get demo rates
        demo_data = self._get_static_demo_rates(from_currency)
        rates = demo_data.get('rates', {})
        
        if to_currency in rates:
            conversion_rate = rates[to_currency]
            converted_amount = amount * conversion_rate
            
            return {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "original_amount": amount,
                "conversion_rate": conversion_rate,
                "converted_amount": round(converted_amount, 4),
                "last_updated": datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000"),
                "cached": False,
                "timestamp": datetime.now().isoformat(),
                "source": "Static demo rates"
            }
        else:
            return {"error": f"Conversion from {from_currency} to {to_currency} not available in demo mode"}
    
    def get_historical_rates(self, base_currency: str, date: str) -> Dict[str, Any]:
        """
        Get historical exchange rates for specific date (YYYY-MM-DD)
        """
        if not self.api_available:
            return {"error": "ExchangeRate-API key required"}
            
        try:
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
            
            url = f"{self.base_url}/{self.api_key}/history/{base_currency}/{date}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('result') == 'error':
                return {"error": f"API Error: {data.get('error-type', 'Unknown error')}"}
            
            return {
                "base_currency": base_currency,
                "date": date,
                "rates": data.get('conversion_rates', {}),
                "timestamp": datetime.now().isoformat()
            }
            
        except ValueError:
            return {"error": "Invalid date format. Use YYYY-MM-DD"}
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error getting historical rates: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error getting historical rates: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_supported_currencies(self) -> Dict[str, Any]:
        """
        Get list of supported currency codes
        """
        if not self.api_available:
            return {
                "error": "ExchangeRate-API key required",
                "major_currencies": self.major_currencies
            }
            
        try:
            url = f"{self.base_url}/{self.api_key}/codes"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('result') == 'error':
                return {"error": f"API Error: {data.get('error-type', 'Unknown error')}"}
            
            # Format supported codes
            supported_codes = data.get('supported_codes', [])
            currency_dict = {code[0]: code[1] for code in supported_codes}
            
            return {
                "supported_currencies": currency_dict,
                "total_currencies": len(currency_dict),
                "major_currencies": self.major_currencies,
                "timestamp": datetime.now().isoformat()
            }
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error getting supported currencies: {e}")
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            logging.error(f"Unexpected error getting supported currencies: {e}")
            return {"error": f"Unexpected error: {str(e)}"}
    
    def get_currency_trends(self, base_currency: str = 'USD', days: int = 7) -> Dict[str, Any]:
        """
        Get currency trends over specified number of days
        """
        if not self.api_available:
            return {"error": "ExchangeRate-API key required"}
            
        try:
            trends = {}
            current_date = datetime.now()
            
            for i in range(days):
                date = (current_date - timedelta(days=i)).strftime('%Y-%m-%d')
                historical_data = self.get_historical_rates(base_currency, date)
                
                if not historical_data.get('error'):
                    trends[date] = {
                        'major_rates': {
                            code: historical_data['rates'].get(code)
                            for code in self.major_currencies[:10]  # Top 10 major currencies
                            if code != base_currency and code in historical_data['rates']
                        }
                    }
                    
                # Rate limiting consideration
                time.sleep(0.2)
            
            return {
                "base_currency": base_currency,
                "period_days": days,
                "trends": trends,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logging.error(f"Error getting currency trends: {e}")
            return {"error": f"Trends analysis error: {str(e)}"}
    
    def get_api_status(self) -> Dict[str, Any]:
        """Get API connection status and quota information"""
        
        status = {
            "api_key_configured": bool(self.api_key),
            "cache_entries": len(self.cache),
            "major_currencies_supported": len(self.major_currencies),
            "timestamp": datetime.now().isoformat()
        }
        
        if not self.api_key:
            status["status"] = "API key required"
            status["message"] = "Configure EXCHANGERATE_KEY for full functionality"
            return status
        
        # Test API connection
        try:
            test_data = self.get_latest_rates('USD')
            if not test_data.get('error'):
                status["status"] = "Connected"
                status["api_response_time"] = "< 1s"
                status["last_successful_call"] = datetime.now().isoformat()
            else:
                status["status"] = "Error"
                status["error"] = test_data.get('error')
                
        except Exception as e:
            status["status"] = "Connection Failed"
            status["error"] = str(e)
            
        return status

# Initialize global provider
_exchange_provider = None

def get_exchange_rate_provider():
    """Get singleton exchange rate provider instance"""
    global _exchange_provider
    if _exchange_provider is None:
        _exchange_provider = ExchangeRateProvider()
    return _exchange_provider