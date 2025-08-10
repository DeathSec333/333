#!/usr/bin/env python3
"""
DeathSec333 Phone Infoga Test Script
"""

from core.phone_validator import DeathSecPhoneValidator
from colorama import Fore

def test_validator():
    print(f"{Fore.RED}🔥 Testing DeathSec333 Phone Validator...")
    
    validator = DeathSecPhoneValidator()
    
    # Test valid numbers
    test_numbers = [
        "+15551234567",  # US
        "+447700900123", # UK  
        "+33123456789",  # France
        "+919876543210"  # India
    ]
    
    for number in test_numbers:
        print(f"\n{Fore.CYAN}Testing: {number}")
        if validator.is_valid(number):
            info = validator.get_info()
            print(f"{Fore.GREEN}✅ Valid - Country: {info.get('country', 'Unknown')}")
            print(f"{Fore.YELLOW}   Carrier: {info.get('carrier', 'Unknown')}")
            print(f"{Fore.YELLOW}   Type: {info.get('number_type', 'Unknown')}")
        else:
            print(f"{Fore.RED}❌ Invalid")

if __name__ == "__main__":
    test_validator()
