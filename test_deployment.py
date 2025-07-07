#!/usr/bin/env python3
"""
Script to test Azure App Service deployment
"""
import requests
import sys
from datetime import datetime

def test_url(url, timeout=10):
    """Test if a URL is accessible"""
    try:
        print(f"Testing: {url}")
        response = requests.get(url, timeout=timeout)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        if response.status_code == 200:
            print("✓ URL is accessible")
            return True
        else:
            print(f"✗ URL returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Error accessing URL: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def main():
    print(f"Azure App Service Deployment Test - {datetime.now()}")
    print("=" * 50)
    
    # Test various URL formats
    urls_to_test = [
        "https://studentperformancejk.azurewebsites.net",
        "https://studentperformancejk.azurewebsites.net/",
        "http://studentperformancejk.azurewebsites.net",
        "https://studentperformancejk.scm.azurewebsites.net",  # Kudu/SCM endpoint
    ]
    
    accessible_urls = []
    
    for url in urls_to_test:
        print()
        if test_url(url):
            accessible_urls.append(url)
    
    print()
    print("=" * 50)
    print("SUMMARY:")
    if accessible_urls:
        print("✓ Accessible URLs:")
        for url in accessible_urls:
            print(f"  - {url}")
    else:
        print("✗ No URLs were accessible")
        print("\nPossible issues:")
        print("1. Azure App Service not properly deployed")
        print("2. Container not running")
        print("3. DNS propagation delay")
        print("4. Azure App Service name is different")
        print("\nNext steps:")
        print("1. Check Azure Portal for actual App Service URL")
        print("2. Check Azure App Service logs")
        print("3. Verify container image is running")

if __name__ == "__main__":
    main()
