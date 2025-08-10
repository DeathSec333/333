"""
DeathSec333 Database Scanner Module
Advanced breach and leak database scanning
"""

import requests
import hashlib
import json
import sqlite3
import os
from pathlib import Path
from colorama import Fore

class DatabaseScanner:
    def __init__(self):
        self.author = "DeathSec333"
        self.module_name = "Database Scanner"
        self.cache_dir = Path.home() / "DeathSec333-Phone-Infoga" / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.cache_dir / "phone_cache.db"
        
        # Initialize cache database
        self._init_cache_db()
        
        # Available leak databases and APIs
        self.leak_sources = {
            'haveibeenpwned': self._check_hibp,
            'dehashed': self._check_dehashed,
            'leakcheck': self._check_leakcheck,
            'intelx': self._check_intelx,
            'local_cache': self._check_local_cache
        }
    
    def search(self, phone_number):
        """Scan multiple breach databases"""
        try:
            clean_number = phone_number.replace('+', '').replace('-', '').replace(' ', '')
            
            results = {
                'phone_number': phone_number,
                'clean_number': clean_number,
                'databases_checked': [],
                'breaches_found': [],
                'total_breaches': 0,
                'database_results': {}
            }
            
            # Check cache first
            cached_result = self._get_cached_result(clean_number)
            if cached_result:
                results['cached_data'] = cached_result
                results['cache_hit'] = True
            else:
                results['cache_hit'] = False
            
            # Check each database
            for db_name, checker_func in self.leak_sources.items():
                try:
                    print(f"{Fore.CYAN}[🔍] Checking {db_name.title()}...")
                    
                    db_result = checker_func(clean_number)
                    results['database_results'][db_name] = db_result
                    results['databases_checked'].append(db_name)
                    
                    if db_result.get('found', False):
                        results['breaches_found'].append(db_name)
                        breach_count = db_result.get('breach_count', 0)
                        results['total_breaches'] += breach_count
                    
                except Exception as e:
                    results['database_results'][db_name] = {
                        'found': False,
                        'error': str(e)
                    }
            
            # Cache results
            self._cache_result(clean_number, results)
            
            # Summary
            results['summary'] = {
                'databases_checked': len(results['databases_checked']),
                'breaches_found': len(results['breaches_found']),
                'total_breaches': results['total_breaches'],
                'risk_level': self._assess_risk_level(results['total_breaches'])
            }
            
            return results
            
        except Exception as e:
            return {'error': f'Database scanner failed: {str(e)}'}
    
    def _check_hibp(self, phone_number):
        """Check Have I Been Pwned"""
        try:
            # Note: HIBP API requires API key for phone number searches
            return {
                'found': False,
                'method': 'hibp_api',
                'message': 'API key required',
                'note': 'Have I Been Pwned requires API key for phone searches',
                'breach_count': 0
            }
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_dehashed(self, phone_number):
        """Check DeHashed database"""
        try:
            # Note: DeHashed requires API credentials
            return {
                'found': False,
                'method': 'dehashed_api',
                'message': 'API credentials required',
                'note': 'DeHashed provides comprehensive breach data',
                'breach_count': 0
            }
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_leakcheck(self, phone_number):
        """Check LeakCheck database"""
        try:
            # LeakCheck public API (limited)
            url = "https://leakcheck.io/api/public"
            params = {'check': phone_number}
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                found = data.get('found', False)
                
                return {
                    'found': found,
                    'method': 'leakcheck_public',
                    'sources': data.get('sources', []),
                    'breach_count': len(data.get('sources', [])),
                    'note': 'Public API - limited results'
                }
            else:
                return {
                    'found': False,
                    'method': 'leakcheck_public',
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_intelx(self, phone_number):
        """Check IntelX phonebook"""
        try:
            # IntelX phonebook search
            url = "https://2.intelx.io/phonebook/search"
            params = {'term': phone_number}
            
            response = requests.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                selectors = data.get('selectors', [])
                
                return {
                    'found': len(selectors) > 0,
                    'method': 'intelx_phonebook',
                    'results': selectors[:10],  # Limit results
                    'breach_count': len(selectors),
                    'note': 'IntelX phonebook data'
                }
            else:
                return {
                    'found': False,
                    'method': 'intelx_phonebook',
                    'error': f'HTTP {response.status_code}'
                }
                
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _check_local_cache(self, phone_number):
        """Check local cache database"""
        try:
            cached = self._get_cached_result(phone_number)
            if cached:
                return {
                    'found': True,
                    'method': 'local_cache',
                    'cached_data': cached,
                    'note': 'Data from local cache'
                }
            else:
                return {
                    'found': False,
                    'method': 'local_cache',
                    'message': 'No cached data'
                }
        except Exception as e:
            return {'found': False, 'error': str(e)}
    
    def _init_cache_db(self):
        """Initialize cache database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS phone_cache (
                    phone_number TEXT PRIMARY KEY,
                    results TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"{Fore.YELLOW}[⚠️] Cache DB init error: {str(e)}")
    
    def _get_cached_result(self, phone_number):
        """Get cached result from database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT results FROM phone_cache WHERE phone_number = ?', (phone_number,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return json.loads(result[0])
            return None
        except Exception:
            return None
    
    def _cache_result(self, phone_number, results):
        """Cache result in database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                'INSERT OR REPLACE INTO phone_cache (phone_number, results) VALUES (?, ?)',
                (phone_number, json.dumps(results, default=str))
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"{Fore.YELLOW}[⚠️] Cache save error: {str(e)}")
    
    def _assess_risk_level(self, breach_count):
        """Assess risk level based on breach count"""
        if breach_count == 0:
            return "Low"
        elif breach_count <= 2:
            return "Medium"
        elif breach_count <= 5:
            return "High"
        else:
            return "Critical"
