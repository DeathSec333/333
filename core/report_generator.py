"""
DeathSec333 Report Generator
Advanced reporting with multiple output formats
"""

import json
import html
import csv
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

class DeathSecReporter:
    def __init__(self):
        self.author = "DeathSec333"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def generate(self, results, output_file=None, format_type='txt'):
        """Generate report in specified format"""
        if output_file:
            if format_type == 'json':
                self._save_json(results, output_file)
            elif format_type == 'html':
                self._save_html(results, output_file)
            elif format_type == 'csv':
                self._save_csv(results, output_file)
            else:
                self._save_txt(results, output_file)
        
        # Always display console output
        self._display_console(results)
    
    def _display_console(self, results):
        """Display results in console with DeathSec333 styling"""
        print(f"\n{Fore.RED}{'='*70}")
        print(f"{Fore.RED}🔥 DEATHSEC333 PHONE INFOGA RESULTS 🔥")
        print(f"{Fore.YELLOW}⚡ Created by {self.author}")
        print(f"{Fore.RED}{'='*70}")
        print(f"{Fore.CYAN}📱 Target: {results['phone_number']}")
        print(f"{Fore.CYAN}🕒 Scan Time: {results['scan_info']['timestamp']}")
        print(f"{Fore.CYAN}⏱️  Duration: {results['scan_info'].get('duration', 'Unknown')}")
        print(f"{Fore.RED}{'='*70}\n")
        
        # Summary
        total_modules = len(results['findings'])
        successful_modules = sum(1 for data in results['findings'].values() if 'error' not in data)
        
        print(f"{Fore.GREEN}📊 SCAN SUMMARY")
        print(f"{Fore.YELLOW}{'─'*50}")
        print(f"{Fore.BLUE}Total Modules: {total_modules}")
        print(f"{Fore.GREEN}Successful: {successful_modules}")
        print(f"{Fore.RED}Failed: {total_modules - successful_modules}")
        print(f"{Fore.YELLOW}{'─'*50}\n")
        
        # Detailed results
        for module_name, data in results['findings'].items():
            print(f"{Fore.RED}[🔥] {module_name.upper()}")
            print(f"{Fore.YELLOW}{'─'*50}")
            
            if 'error' in data:
                print(f"{Fore.RED}❌ Error: {data['error']}\n")
                continue
            
            self._format_module_output(module_name, data)
            print()
        
        print(f"{Fore.RED}{'='*70}")
        print(f"{Fore.YELLOW}🔥 DeathSec333 Phone Infoga - Advanced Mobile OSINT")
        print(f"{Fore.CYAN}⚡ Created by {self.author}")
        print(f"{Fore.RED}{'='*70}")
    
    def _format_module_output(self, module_name, data):
        """Format module output for console display"""
        if isinstance(data, dict) and data:
            table_data = []
            for key, value in data.items():
                if isinstance(value, (list, dict)):
                    value = str(value)[:100] + "..." if len(str(value)) > 100 else str(value)
                table_data.append([key.replace('_', ' ').title(), value])
            
            if table_data:
                print(tabulate(table_data, headers=['Field', 'Value'], tablefmt='grid'))
            else:
                print(f"{Fore.YELLOW}ℹ️  No data available")
        else:
            print(f"{Fore.YELLOW}ℹ️  No data available")
    
    def _save_json(self, results, filename):
        """Save results as JSON"""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"{Fore.GREEN}✅ JSON report saved to {filename}")
    
    def _save_html(self, results, filename):
        """Save results as HTML with DeathSec333 styling"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>DeathSec333 Phone Infoga Report</title>
            <style>
                body {{ 
                    font-family: 'Courier New', monospace; 
                    margin: 20px; 
                    background: #0a0a0a; 
                    color: #00ff00; 
                }}
                .header {{ 
                    background: linear-gradient(45deg, #ff0000, #8b0000); 
                    color: white; 
                    padding: 20px; 
                    text-align: center;
                    border-radius: 10px;
                    margin-bottom: 20px;
                }}
                .module {{ 
                    margin: 20px 0; 
                    padding: 15px; 
                    border: 2px solid #ff0000; 
                    background: #1a1a1a;
                    border-radius: 5px;
                }}
                .error {{ color: #ff4444; }}
                .success {{ color: #44ff44; }}
                table {{ 
                    width: 100%; 
                    border-collapse: collapse; 
                    background: #2a2a2a;
                }}
                th, td {{ 
                    border: 1px solid #ff0000; 
                    padding: 8px; 
                    text-align: left; 
                }}
                th {{ background-color: #ff0000; color: white; }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding: 20px;
                    border-top: 2px solid #ff0000;
                    color: #ff0000;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🔥 DEATHSEC333 PHONE INFOGA REPORT 🔥</h1>
                <h2>⚡ Created by DeathSec333</h2>
                <p>📱 Target: {html.escape(results['phone_number'])}</p>
                <p>🕒 Generated: {self.timestamp}</p>
            </div>
        """
        
        for module_name, data in results['findings'].items():
            html_content += f'<div class="module"><h2>🔥 {module_name}</h2>'
            
            if 'error' in data:
                html_content += f'<p class="error">❌ Error: {html.escape(str(data["error"]))}</p>'
            else:
                html_content += '<table><tr><th>Field</th><th>Value</th></tr>'
                for key, value in data.items():
                    html_content += f'<tr><td><strong>{html.escape(str(key))}</strong></td><td>{html.escape(str(value))}</td></tr>'
                html_content += '</table>'
            
            html_content += '</div>'
        
        html_content += '''
            <div class="footer">
                <h3>🔥 DeathSec333 Phone Infoga - Advanced Mobile OSINT</h3>
                <p>⚡ Created by DeathSec333</p>
                <p>⚠️ Use responsibly and legally only!</p>
            </div>
        </body></html>
        '''
        
        with open(filename, 'w') as f:
            f.write(html_content)
        print(f"{Fore.GREEN}✅ HTML report saved to {filename}")
    
    def _save_txt(self, results, filename):
        """Save results as plain text"""
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("🔥 DEATHSEC333 PHONE INFOGA RESULTS 🔥\n")
            f.write(f"⚡ Created by {self.author}\n")
            f.write("="*70 + "\n")
            f.write(f"📱 Target: {results['phone_number']}\n")
            f.write(f"🕒 Scan Time: {results['scan_info']['timestamp']}\n")
            f.write("="*70 + "\n\n")
            
            for module_name, data in results['findings'].items():
                f.write(f"[🔥] {module_name.upper()}\n")
                f.write("-"*50 + "\n")
                
                if 'error' in data:
                    f.write(f"❌ Error: {data['error']}\n\n")
                else:
                    for key, value in data.items():
                        f.write(f"{key}: {value}\n")
                    f.write("\n")
        
        print(f"{Fore.GREEN}✅ Text report saved to {filename}")
    
    def _save_csv(self, results, filename):
        """Save results as CSV"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Module', 'Field', 'Value'])
            
            for module_name, data in results['findings'].items():
                if 'error' in data:
                    writer.writerow([module_name, 'Error', data['error']])
                else:
                    for key, value in data.items():
                        writer.writerow([module_name, key, value])
        
        print(f"{Fore.GREEN}✅ CSV report saved to {filename}")
