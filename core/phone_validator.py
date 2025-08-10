"""
DeathSec333 Phone Validator
Advanced phone number validation and information extraction
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style

class DeathSecPhoneValidator:
    def __init__(self):
        self.author = "DeathSec333"
        self.parsed_number = None
        self.phone_info = {}
    
    def is_valid(self, number, country_code=None):
        """Validate phone number format"""
        try:
            self.parsed_number = phonenumbers.parse(number, country_code)
            is_valid = phonenumbers.is_valid_number(self.parsed_number)
            
            if is_valid:
                self._extract_info()
            
            return is_valid
            
        except phonenumbers.NumberParseException as e:
            print(f"{Fore.RED}[❌] Parse Error: {str(e)}")
            return False
    
    def _extract_info(self):
        """Extract detailed information from phone number"""
        if not self.parsed_number:
            return
        
        try:
            self.phone_info = {
                'country': geocoder.description_for_number(self.parsed_number, "en"),
                'carrier': carrier.name_for_number(self.parsed_number, "en"),
                'timezone': list(timezone.time_zones_for_number(self.parsed_number)),
                'international_format': phonenumbers.format_number(
                    self.parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
                ),
                'national_format': phonenumbers.format_number(
                    self.parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL
                ),
                'e164_format': phonenumbers.format_number(
                    self.parsed_number, phonenumbers.PhoneNumberFormat.E164
                ),
                'number_type': self._get_number_type(),
                'is_possible': phonenumbers.is_possible_number(self.parsed_number),
                'is_valid': phonenumbers.is_valid_number(self.parsed_number),
                'country_code': self.parsed_number.country_code,
                'national_number': self.parsed_number.national_number
            }
        except Exception as e:
            print(f"{Fore.YELLOW}[⚠️] Info extraction error: {str(e)}")
    
    def _get_number_type(self):
        """Get human-readable number type"""
        if not self.parsed_number:
            return "Unknown"
        
        number_type = phonenumbers.number_type(self.parsed_number)
        type_mapping = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.UAN: "UAN",
            phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
            phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
        }
        
        return type_mapping.get(number_type, "Unknown")
    
    def get_info(self):
        """Return extracted phone information"""
        return self.phone_info
