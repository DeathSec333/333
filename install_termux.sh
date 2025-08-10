#!/bin/bash

echo "🔥 Installing DeathSec333 Phone Infoga for Termux..."
echo "⚡ Created by DeathSec333"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Update Termux
echo -e "${YELLOW}[🔧] Updating Termux packages...${NC}"
pkg update -y && pkg upgrade -y

# Install required packages
echo -e "${YELLOW}[📦] Installing required packages...${NC}"
pkg install -y python git clang make libjpeg-turbo libpng zlib openssl libffi nodejs chromium wget curl

# Install Python packages
echo -e "${YELLOW}[🐍] Installing Python packages...${NC}"
pip install --upgrade pip wheel setuptools

# Install requirements
echo -e "${YELLOW}[📋] Installing Python requirements...${NC}"
pip install -r requirements.txt

# Create necessary directories
echo -e "${YELLOW}[📁] Creating directories...${NC}"
mkdir -p data/{cache,reports,logs}
mkdir -p ~/.config/DeathSec333-Phone-Infoga

# Set permissions
echo -e "${YELLOW}[🔐] Setting permissions...${NC}"
chmod +x deathsec_main.py
chmod +x install_termux.sh

# Create config file
echo -e "${YELLOW}[⚙️] Creating configuration...${NC}"
cat > ~/.config/DeathSec333-Phone-Infoga/config.json << 'CONFIG_EOF'
{
    "author": "DeathSec333",
    "version": "1.0",
    "default_delay": 2,
    "max_threads": 5,
    "output_dir": "data/reports",
    "cache_enabled": true,
    "user_agent": "DeathSec333-Phone-Infoga/1.0",
    "modules": {
        "carrier_lookup": true,
        "truecaller": true,
        "whatsapp_checker": true,
        "social_scanner": true,
        "location_lookup": true,
        "database_scanner": true
    },
    "apis": {
        "numverify_key": "",
        "truecaller_key": "",
        "hibp_key": "",
        "dehashed_key": ""
    }
}
CONFIG_EOF

# Create alias
echo -e "${YELLOW}[🔗] Creating alias...${NC}"
echo 'alias deathsec-phone="python ~/DeathSec333-Phone-Infoga/deathsec_main.py"' >> ~/.bashrc

echo ""
echo -e "${GREEN}✅ DeathSec333 Phone Infoga installation completed!${NC}"
echo -e "${CYAN}🔥 Created by DeathSec333${NC}"
echo ""
echo -e "${YELLOW}Usage Examples:${NC}"
echo -e "${CYAN}  python deathsec_main.py -n '+1234567890'${NC}"
echo -e "${CYAN}  python deathsec_main.py -n '+1234567890' -f html -o report.html${NC}"
echo -e "${CYAN}  python deathsec_main.py -n '+1234567890' --modules CarrierLookup TruecallerSearch${NC}"
echo ""
echo -e "${RED}⚠️  Remember: Use responsibly and legally only!${NC}"
