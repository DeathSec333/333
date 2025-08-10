"""
DeathSec333 Phone Infoga Setup
Advanced Mobile OSINT Framework
"""

from setuptools import setup, find_packages

def read_requirements():
    try:
        with open("requirements.txt", "r") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except:
        return [
            "phonenumbers>=8.13.0",
            "requests>=2.31.0",
            "colorama>=0.4.6",
            "tabulate>=0.9.0",
            "fake-useragent>=1.4.0",
            "beautifulsoup4>=4.12.0",
            "lxml>=4.9.0",
            "aiohttp>=3.8.0"
        ]

setup(
    name="deathsec333-phone-infoga",
    version="1.0.0",
    author="DeathSec333",
    description="Advanced Mobile OSINT Framework for Phone Number Intelligence",
    url="https://github.com/DeathSec333/DeathSec333-Phone-Infoga",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "deathsec-phone=deathsec_main:main",
        ],
    },
    keywords="osint, phone, intelligence, security, termux, mobile, investigation",
)
