"""
DeathSec333 OSINT Engine
Advanced multi-threaded OSINT data collection (Termux Compatible)
"""

import asyncio
import httpx
import time
import importlib
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

class DeathSecOSINTEngine:
    def __init__(self, modules=None, delay=2, verbose=False):
        self.author = "DeathSec333"
        self.version = "1.0"
        self.delay = delay
        self.verbose = verbose
        self.client = None
        
        # Available modules
        self.available_modules = {
            'CarrierLookup': 'modules.carrier_lookup',
            'TruecallerSearch': 'modules.truecaller',
            'WhatsAppChecker': 'modules.whatsapp_checker',
            'SocialScanner': 'modules.social_scanner',
            'LocationLookup': 'modules.location_lookup',
            'DatabaseScanner': 'modules.database_scanner'
        }
        
        # Load selected modules
        self.modules = self._load_modules(modules)
        
        print(f"{Fore.RED}[🔥] DeathSec333 OSINT Engine v{self.version}")
        print(f"{Fore.YELLOW}[⚡] Created by {self.author}")
        print(f"{Fore.CYAN}[📊] Loaded {len(self.modules)} modules")
    
    def _load_modules(self, selected_modules=None):
        """Load OSINT modules"""
        modules = {}
        
        module_list = selected_modules if selected_modules else list(self.available_modules.keys())
        
        for module_name in module_list:
            if module_name in self.available_modules:
                try:
                    module_path = self.available_modules[module_name]
                    module = importlib.import_module(module_path)
                    module_class = getattr(module, module_name)
                    modules[module_name] = module_class
                    
                    if self.verbose:
                        print(f"{Fore.GREEN}[✅] Loaded: {module_name}")
                        
                except Exception as e:
                    print(f"{Fore.RED}[❌] Failed to load {module_name}: {str(e)}")
        
        return modules
    
    async def gather_info(self, phone_number):
        """Main OSINT gathering function"""
        start_time = time.time()
        
        results = {
            'phone_number': phone_number,
            'scan_info': {
                'author': self.author,
                'version': self.version,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'modules_used': list(self.modules.keys())
            },
            'findings': {}
        }
        
        # Create httpx client
        async with httpx.AsyncClient(timeout=30.0) as client:
            self.client = client
            
            # Run modules sequentially with progress tracking
            print(f"{Fore.YELLOW}[🔍] Running {len(self.modules)} modules...")
            
            for module_name, module_class in self.modules.items():
                try:
                    print(f"{Fore.CYAN}[⏳] Running {module_name}...")
                    
                    # Create module instance and run
                    module_instance = module_class()
                    result = await self._run_module_safe(module_instance, phone_number)
                    
                    results['findings'][module_name] = result
                    
                    if 'error' in result:
                        print(f"{Fore.RED}[❌] {module_name}: {result['error']}")
                    else:
                        print(f"{Fore.GREEN}[✅] {module_name}: Completed")
                    
                except Exception as e:
                    results['findings'][module_name] = {'error': str(e)}
                    print(f"{Fore.RED}[❌] {module_name}: Exception - {str(e)}")
                
                # Rate limiting
                await asyncio.sleep(self.delay)
        
        # Calculate scan time
        scan_time = time.time() - start_time
        results['scan_info']['duration'] = f"{scan_time:.2f} seconds"
        
        return results
    
    async def _run_module_safe(self, module_instance, phone_number):
        """Safely run a module with timeout"""
        try:
            if hasattr(module_instance, 'search'):
                if asyncio.iscoroutinefunction(module_instance.search):
                    return await asyncio.wait_for(module_instance.search(phone_number), timeout=30)
                else:
                    loop = asyncio.get_event_loop()
                    return await loop.run_in_executor(None, module_instance.search, phone_number)
            else:
                return {'error': 'Module does not have search method'}
        except asyncio.TimeoutError:
            return {'error': 'Module timeout (30s)'}
        except Exception as e:
            return {'error': str(e)}
