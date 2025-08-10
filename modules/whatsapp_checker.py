"""
DeathSec333 WhatsApp Checker Module
Advanced WhatsApp presence detection
"""

import requests
import json
import time
from fake_useragent import UserAgent
from colorama import Fore

class WhatsAppChecker:
    def __init__(self):
        self.author = "DeathSec333"
        self.module_name = "WhatsApp Checker"
        self.ua = UserAgent()
        self.session = requests.Session()
    
    def search(self, phone_number):
        """Check WhatsApp presence"""
        try:
            clean_number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
            
            results = {
                'phone_number': phone_number,
                'clean_number': clean_number,
                'checks_performed': []
            }
            
            # Method 1: WhatsApp Web URL check
            web_check = self._check_whatsapp_web(clean_number)
            results['web_check'] = web_check
            results['checks_performed'].append('web_url')
            
            # Method 2: WhatsApp Business API check (placeholder)
            business_check = self._check_business_api(clean_number)
            results['business_check'] = business_check
            results['checks_performed'].append('business_api')
            
            # Method 3: Profile picture check (advanced)
            profile_check = self._check_profile_picture(clean_number)
            results['profile_check'] = profile_check
            results['checks_performed'].append('profile_picture')
            
            # Determine overall result
            registered = any([
                web_check.get('registered', False),
                business_check.get('registered', False),
                profile_check.get('registered', False)
            ])
            
            results['registered'] = registered
            results['confidence'] = self._calculate_confidence(results)
            
            return results
            
        except Exception as e:
            return {'error': f'WhatsApp check failed: {str(e)}'}
    
    def _check_whatsapp_web(self, phone_number):
        """Check via WhatsApp Web URL"""
        try:
            # WhatsApp Web URL format
            wa_url = f"https://wa.me/{phone_number}"
            
            headers = {
                'User-Agent': self.ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
            
            response = self.session.head(wa_url, headers=headers, timeout=10, allow_redirects=True)
            
            if response.status_code == 200:
                return {
                    'registered': True,
                    'method': 'wa_web_url',
                    'status_code': response.status_code,
                    'note': 'URL accessible - likely registered'
                }
            else:
                return {
                    'registered': False,
                    'method': 'wa_web_url',
                    'status_code': response.status_code,
                    'note': 'URL not accessible'
                }
                
        except Exception as e:
            return {
                'registered': False,
                'method': 'wa_web_url',
                'error': str(e)
            }
    
    def _check_business_api(self, phone_number):
        """Check via WhatsApp Business API"""
        try:
            # Note: This requires WhatsApp Business API access
            # Placeholder implementation
            return {
                'registered': False,
                'method': 'business_api',
                'message': 'Business API access required',
                'note': 'Requires WhatsApp Business API credentials'
            }
            
        except Exception as e:
            return {
                'registered': False,
                'method': 'business_api',
                'error': str(e)
            }
    
    def _check_profile_picture(self, phone_number):
        """Check for profile picture (advanced method)"""
        try:
            # This is a placeholder for advanced profile picture checking
            # Actual implementation would require WhatsApp Web automation
            return {
                'registered': False,
                'method': 'profile_picture',
                'message': 'Advanced method - requires automation',
                'note': 'Profile picture check needs WhatsApp Web automation'
            }
            
        except Exception as e:
            return {
                'registered': False,
                'method': 'profile_picture',
                'error': str(e)
            }
    
    def _calculate_confidence(self, results):
        """Calculate confidence level based on all checks"""
        positive_checks = 0
        total_checks = len(results['checks_performed'])
        
        if results.get('web_check', {}).get('registered'):
            positive_checks += 1
        if results.get('business_check', {}).get('registered'):
            positive_checks += 1
        if results.get('profile_check', {}).get('registered'):
            positive_checks += 1
        
        if total_checks == 0:
            return 0
        
        confidence = (positive_checks / total_checks) * 100
        return round(confidence, 2)
