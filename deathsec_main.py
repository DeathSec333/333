#!/usr/bin/env python3
"""
DeathSec333 Phone Infoga - Advanced Mobile OSINT Framework
Created by: DeathSec333
Version: 1.0
Optimized for Termux
"""

import os
import sys
import argparse
import asyncio
import time
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def deathsec_banner():
    banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════╗
{Fore.RED}║                🔥 DEATHSEC333 PHONE INFOGA 🔥                    ║
{Fore.RED}║              Advanced Mobile OSINT Framework                     ║
{Fore.YELLOW}║                    Created by DeathSec333                        ║
{Fore.CYAN}║                     Termux Optimized                            ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}[⚡] Version: 1.0
{Fore.YELLOW}[🎯] Target: Mobile Phone Intelligence
{Fore.YELLOW}[⚠️]  Legal Use Only - Created by DeathSec333
"""
    print(banner)

def main():
    deathsec_banner()
    
    parser = argparse.ArgumentParser(
        description='DeathSec333 Phone Infoga - Advanced Mobile OSINT',
        epilog='Created by DeathSec333 - Use responsibly and legally only!',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Main arguments
    parser.add_argument('-n', '--number', required=True, 
                       help='Phone number to investigate (e.g., +1234567890)')
    parser.add_argument('-c', '--country', 
                       help='Country code (e.g., US, UK, IN)')
    parser.add_argument('-o', '--output', 
                       help='Output file for results')
    parser.add_argument('-f', '--format', 
                       choices=['json', 'html', 'txt', 'csv'], 
                       default='txt', help='Output format (default: txt)')
    
    # Advanced options
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help='Enable verbose output')
    parser.add_argument('--modules', nargs='+', 
                       help='Specific modules to run (space-separated)')
    parser.add_argument('--delay', type=int, default=2, 
                       help='Delay between requests in seconds (default: 2)')
    
    args = parser.parse_args()
    
    print(f"{Fore.GREEN}[🔥] DeathSec333 Phone Infoga Starting...")
    print(f"{Fore.CYAN}[📱] Target: {args.number}")
    
    try:
        asyncio.run(process_single(args))
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[❌] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[❌] Error: {str(e)}")
        sys.exit(1)

async def process_single(args):
    from core.phone_validator import DeathSecPhoneValidator
    from core.osint_engine import DeathSecOSINTEngine
    from core.report_generator import DeathSecReporter
    
    # Validate phone number
    print(f"{Fore.YELLOW}[🔍] Validating phone number...")
    validator = DeathSecPhoneValidator()
    
    if not validator.is_valid(args.number, args.country):
        print(f"{Fore.RED}[❌] Invalid phone number format")
        return
    
    phone_info = validator.get_info()
    print(f"{Fore.GREEN}[✅] Phone number validated")
    print(f"{Fore.CYAN}[📍] Country: {phone_info.get('country', 'Unknown')}")
    print(f"{Fore.CYAN}[📡] Carrier: {phone_info.get('carrier', 'Unknown')}")
    
    # Initialize OSINT engine
    print(f"{Fore.YELLOW}[⚡] Initializing DeathSec OSINT Engine...")
    engine = DeathSecOSINTEngine(
        modules=args.modules,
        delay=args.delay,
        verbose=args.verbose
    )
    
    # Run scan
    print(f"{Fore.RED}[🔥] Starting OSINT scan...")
    results = await engine.gather_info(args.number)
    
    # Generate report
    print(f"{Fore.YELLOW}[📊] Generating report...")
    reporter = DeathSecReporter()
    
    if args.output:
        output_file = args.output
    else:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        clean_number = args.number.replace('+', '').replace('-', '').replace(' ', '')
        output_file = f"data/reports/DeathSec333_Report_{clean_number}_{timestamp}.{args.format}"
    
    reporter.generate(results, output_file, args.format)
    
    print(f"{Fore.GREEN}[🔥] DeathSec333 scan completed successfully!")

if __name__ == "__main__":
    main()
