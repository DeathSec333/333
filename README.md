# 🔥 DeathSec333 Phone Infoga

**Advanced Mobile OSINT Framework**  
*Created by DeathSec333*

## 🎯 Overview

DeathSec333 Phone Infoga is an advanced phone number OSINT (Open Source Intelligence) framework designed for security researchers, penetration testers, and digital investigators. This tool provides comprehensive phone number intelligence gathering capabilities.

### ⚡ Features

- **Multi-Module OSINT Collection**
  - Carrier & Network Information
  - Truecaller Database Search
  - WhatsApp Presence Detection
  - Social Media Scanning
  - Location & Timezone Analysis
  - Breach Database Scanning

- **Advanced Reporting**
  - HTML Reports with DeathSec333 Styling
  - JSON Export for Further Analysis
  - CSV Format for Spreadsheet Import
  - Console Output with Color Coding

- **Termux Optimized**
  - Designed specifically for Android/Termux
  - Lightweight and Fast
  - Async Processing
  - Rate Limiting & Error Handling

## 🚀 Installation

### Quick Install (Termux)
```bash
# Clone repository
git clone https://github.com/DeathSec333/DeathSec333-Phone-Infoga.git
cd DeathSec333-Phone-Infoga

# Run installation script
chmod +x install_termux.sh
./install_termux.sh

Manual Install

# Update Termux
pkg update && pkg upgrade

# Install dependencies
pkg install python git clang make libjpeg-turbo libpng zlib openssl libffi

# Install Python packages
pip install -r requirements.txt

# Set permissions
chmod +x deathsec_main.py
Insert at cursor


📱 Usage

Basic Usage

# Basic phone number scan
python deathsec_main.py -n "+1234567890"

# Scan with country code
python deathsec_main.py -n "1234567890" -c US

# Verbose output
python deathsec_main.py -n "+1234567890" -v
Insert at cursor


Advanced Usage

# Generate HTML report
python deathsec_main.py -n "+1234567890" -f html -o report.html

# Run specific modules only
python deathsec_main.py -n "+1234567890" --modules CarrierLookup TruecallerSearch

# Custom delay between requests
python deathsec_main.py -n "+1234567890" --delay 5
Insert at cursor


Output Formats


txt - Plain text report (default)

json - JSON format for APIs

html - Styled HTML report

csv - CSV for spreadsheets


🔧 Modules



Module
Description
Status




CarrierLookup
Network & carrier information

✅ Active


TruecallerSearch
Truecaller database lookup

✅ Active


WhatsAppChecker
WhatsApp presence detection

✅ Active


SocialScanner
Social media presence scan

✅ Active


LocationLookup
Geographic information

✅ Active


DatabaseScanner
Breach database search

✅ Active




⚙️ Configuration
Configuration file: ~/.config/DeathSec333-Phone-Infoga/config.json

{
    "author": "DeathSec333",
    "version": "1.0",
    "default_delay": 2,
    "modules": {
        "carrier_lookup": true,
        "truecaller": true,
        "whatsapp_checker": true,
        "social_scanner": true,
        "location_lookup": true,
        "database_scanner": true
    }
}
Insert at cursor


📊 Sample Output

╔══════════════════════════════════════════════════════════════════╗
║                🔥 DEATHSEC333 PHONE INFOGA 🔥                    ║
║              Advanced Mobile OSINT Framework                     ║
║                    Created by DeathSec333                        ║
║                     Termux Optimized                            ║
╚══════════════════════════════════════════════════════════════════╝

[🔥] DeathSec333 Phone Infoga Starting...
[📱] Target: +1234567890
[🔍] Validating phone number...
[✅] Phone number validated
[📍] Country: United States
[📡] Carrier: Verizon Wireless
[⚡] Initializing DeathSec OSINT Engine...
[🔥] DeathSec333 OSINT Engine v1.0
[⚡] Created by DeathSec333
[📊] Loaded 6 modules
[🔥] Starting OSINT scan...
Insert at cursor


⚠️ Legal Disclaimer
IMPORTANT: This tool is for educational and authorized testing purposes only.

Only use on phone numbers you own or have explicit permission to investigate
Respect privacy laws (GDPR, CCPA, etc.)
Do not use for harassment, stalking, or illegal activities
The author (DeathSec333) is not responsible for misuse


🛡️ Ethical Usage


Authorized Testing Only - Only test numbers you own or have permission

Respect Privacy - Follow local privacy laws and regulations

No Harassment - Do not use for stalking or harassment

Educational Purpose - Use for learning and authorized security testing


🔗 API Keys (Optional)
For enhanced functionality, you can add API keys:


NumVerify: Phone validation API

Truecaller: Enhanced caller ID data

HaveIBeenPwned: Breach database access

DeHashed: Comprehensive breach data

Add keys to config file: ~/.config/DeathSec333-Phone-Infoga/config.json

🐛 Troubleshooting

Common Issues


Module Import Errors

pip install -r requirements.txt
Insert at cursor



Permission Denied

chmod +x deathsec_main.py
Insert at cursor



Network Timeouts

python deathsec_main.py -n "+1234567890" --delay 5
Insert at cursor




📈 Roadmap


 Telegram API Integration

 Advanced Social Media Scanning

 GUI Interface

 Batch Processing

 Export to MISP

 Docker Support


🤝 Contributing

Fork the repository
Create feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open Pull Request


📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

👨‍💻 Author
DeathSec333

GitHub: [@DeathSec333](https://github.com/DeathSec333)

Created for educational and authorized security testing


🙏 Acknowledgments

PhoneNumbers library contributors
OSINT community
Security researchers worldwide


🔥 DeathSec333 Phone Infoga - Advanced Mobile OSINT Framework
Use responsibly and legally only!

## 🌟 GitHub Repository

[![GitHub stars](https://img.shields.io/github/stars/deathsec333/DeathSec333-Phone-Infoga?style=social)](https://github.com/deathsec333/DeathSec333-Phone-Infoga/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/deathsec333/DeathSec333-Phone-Infoga?style=social)](https://github.com/deathsec333/DeathSec333-Phone-Infoga/network)
[![GitHub issues](https://img.shields.io/github/issues/deathsec333/DeathSec333-Phone-Infoga)](https://github.com/deathsec333/DeathSec333-Phone-Infoga/issues)
[![GitHub license](https://img.shields.io/github/license/deathsec333/DeathSec333-Phone-Infoga)](https://github.com/deathsec333/DeathSec333-Phone-Infoga/blob/main/LICENSE)

### 🚀 Quick Start from GitHub

```bash
# Clone the repository
git clone https://github.com/deathsec333/DeathSec333-Phone-Infoga.git
cd DeathSec333-Phone-Infoga

# Install dependencies
pip install -r requirements_termux.txt

# Run your first scan
python deathsec_main.py -n "+YOUR_NUMBER" -v

📈 Project Stats


Language: Python 3.8+

Platform: Termux/Linux optimized

Modules: 6 OSINT modules

Reports: 4 formats (HTML, JSON, CSV, TXT)

Performance: Sub-6 second targeted scans

Creator: deathsec333


🔗 Links


Repository: https://github.com/deathsec333/DeathSec333-Phone-Infoga


Issues: https://github.com/deathsec333/DeathSec333-Phone-Infoga/issues


Releases: https://github.com/deathsec333/DeathSec333-Phone-Infoga/releases



⭐ If you find this tool useful, please give it a star on GitHub!
🔥 Created with ❤️ by deathsec333
