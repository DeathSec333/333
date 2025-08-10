"""
DeathSec333 Configuration Manager
"""

import json
import os
from pathlib import Path

class DeathSecConfig:
    def __init__(self, config_path=None):
        self.author = "DeathSec333"
        
        if config_path:
            self.config_path = Path(config_path)
        else:
            self.config_path = Path.home() / ".config" / "DeathSec333-Phone-Infoga" / "config.json"
        
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from file"""
        default_config = {
            "author": "DeathSec333",
            "version": "1.0",
            "default_delay": 2,
            "max_threads": 5,
            "output_dir": "data/reports",
            "cache_enabled": True,
            "user_agent": "DeathSec333-Phone-Infoga/1.0",
            "modules": {
                "carrier_lookup": True,
                "truecaller": True,
                "whatsapp_checker": True,
                "social_scanner": True,
                "location_lookup": True,
                "database_scanner": True
            },
            "apis": {
                "numverify_key": "",
                "truecaller_key": "",
                "hibp_key": "",
                "dehashed_key": ""
            }
        }
        
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
            else:
                self.config_path.parent.mkdir(parents=True, exist_ok=True)
                self._save_config(default_config)
            
            return default_config
            
        except Exception as e:
            print(f"Config load error: {e}")
            return default_config
    
    def _save_config(self, config):
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"Config save error: {e}")
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value
        self._save_config(self.config)
