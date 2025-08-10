"""
DeathSec333 Social Scanner Module
Advanced social media presence detection (Termux Compatible)
"""

import requests
import re
import time
import html5lib
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore

class SocialScanner:
    def __init__(self):
        self.author = "DeathSec333"
        self.module_name = "Social Scanner"
        self.ua = UserAgent()
        self.session = requests.Session()
        
        # Social media platforms to check
        self.platforms = {
            'telegram': self._check_telegram,
            'viber': self._check_viber,
            'signal': self._check_signal,
            'facebook': self._check_facebook,
            'twitter': self._check_twitter,
            'linkedin': self._check_linkedin
        }
    
    def search(self, phone_number):
        """Scan multiple social media platforms"""
        try:
            clean_number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
            
            results = {
                'phone_number': phone_number,
                'clean_number': clean_number,
                'platforms_checked': [],
                'found_on': [],
                'platform_results': {}
            }
            
            # Check each platform
            for platform_name, checker_func in self.platforms.items():
                try:
                    platform_result = checker_func(clean_number)
                    results['platform_results'][platform_name] = platform_result
                    results['platforms_checked'].append(platform_name)
                    
                    if platform_result.get('found', False):
                        results['found_on'].append(platform_name)
                    
                    # Rate limiting
                    time.sleep(1)
                    
                except Exception as e:
                    results['platform_results'][platform_name] = {
                        'found': False,
                        'error': str(e)
                    }
            
            # Summary
            results['total_platforms'] = len(results['platforms_checked'])
            results['found_count'] = len(results['found_on'])
            results['success_rate'] = f"{(results['found_count'] / results['total_platforms'] * 100):.1f}%" if results['total_platforms'] > 0 else "0%"
            
            return results
            
        except Exception as e:
            return {'error': f'Social scanner failed: {str(e)}'}
    
    def _check_telegram(self, phone_number):
        """Check Telegram presence"""
        return {
            'found': False,
            'method': 'api_check',
            'message': 'Telegram API required',
            'note': 'Requires Telegram API access for phone number lookup'
        }
    
    def _check_viber(self, phone_number):
        """Check Viber presence"""
        return {
            'found': False,
            'method': 'api_check',
            'message': 'Viber API required',
            'note': 'Viber does not provide public phone lookup'
        }
    
    def _check_signal(self, phone_number):
        """Check Signal presence"""
        return {
            'found': False,
            'method': 'privacy_focused',
            'message': 'Signal prioritizes privacy',
            'note': 'Signal does not allow phone number lookups for privacy'
        }
    
    def _check_facebook(self, phone_number):
        """Check Facebook presence"""
        try:
            search_url = f"https://www.facebook.com/search/people/?q={phone_number}"
            
            headers = {'User-Agent': self.ua.random}
            response = self.session.get(search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                if "No results found" in response.text or "no results" in response.text.lower():
                    return {
                        'found': False,
                        'method': 'web_search',
                        'message': 'No results found'
                    }
                else:
                    return {
                        'found': True,
                        'method': 'web_search',
                        'message': 'Possible results found',
                        'note': 'Manual verification required'
                    }
            else:
                return {
                    'found': False,
                    'method': 'web_search',
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_twitter(self, phone_number):
        """Check Twitter presence"""
        try:
            search_url = f"https://twitter.com/search?q={phone_number}"
            
            headers = {'User-Agent': self.ua.random}
            response = self.session.get(search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                if phone_number in response.text:
                    return {
                        'found': True,
                        'method': 'web_search',
                        'message': 'Phone number mentioned in tweets',
                        'note': 'May be in public tweets or profiles'
                    }
                else:
                    return {
                        'found': False,
                        'method': 'web_search',
                        'message': 'No mentions found'
                    }
            else:
                return {
                    'found': False,
                    'method': 'web_search',
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_linkedin(self, phone_number):
        """Check LinkedIn presence"""
        return {
            'found': False,
            'method': 'blocked',
            'message': 'LinkedIn blocks automated searches',
            'note': 'LinkedIn requires authentication for searches'
        }
