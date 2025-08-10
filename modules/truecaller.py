"""
DeathSec333 Truecaller Search Module
Advanced Truecaller OSINT gathering
"""

import requests
import json
import time
from fake_useragent import UserAgent
from colorama import Fore

class TruecallerSearch:
    def __init__(self):
        self.author = "DeathSec333"
        self.module_name = "Truecaller Search"
        self.ua = UserAgent()
        self.session = requests.Session()
        self.base_url = "https://www.truecaller.com"
    
    def search(self, phone_number):
        """Search phone number on Truecaller"""
        try:
            # Clean phone number
            clean_number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
            
            # Method 1: Try web search
            web_result = self._web_search(clean_number)
            
            # Method 2: Try API search (if available)
            api_result = self._api_search(clean_number)
            
            # Combine results
            result = {
                'web_search': web_result,
                'api_search': api_result,
                'found': web_result.get('found', False) or api_result.get('found', False)
            }
            
            # Extract best available data
            if web_result.get('found'):
                result.update(web_result)
            elif api_result.get('found'):
                result.update(api_result)
            
            return result
            
        except Exception as e:
            return {'error': f'Truecaller search failed: {str(e)}'}
    
    def _web_search(self, phone_number):
        """Search via Truecaller web interface"""
        try:
            headers = {
                'User-Agent': self.ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            # Search URL
            search_url = f"{self.base_url}/search?q={phone_number}"
            
            response = self.session.get(search_url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                # Parse response for phone number info
                # This is a simplified parser - actual implementation would need
                # more sophisticated HTML parsing
                if phone_number in response.text and "name" in response.text.lower():
                    return {
                        'found': True,
                        'method': 'web_search',
                        'source': 'Truecaller Web',
                        'note': 'Data found but requires manual verification'
                    }
                else:
                    return {
                        'found': False,
                        'method': 'web_search',
                        'message': 'No data found via web search'
                    }
            else:
                return {
                    'found': False,
                    'method': 'web_search',
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {
                'found': False,
                'method': 'web_search',
                'error': str(e)
            }
    
    def _api_search(self, phone_number):
        """Search via Truecaller API (requires authentication)"""
        try:
            # Note: This requires Truecaller API access
            # For educational purposes, returning placeholder
            return {
                'found': False,
                'method': 'api_search',
                'message': 'API access required',
                'note': 'Truecaller API requires authentication'
            }
            
        except Exception as e:
            return {
                'found': False,
                'method': 'api_search',
                'error': str(e)
            }
