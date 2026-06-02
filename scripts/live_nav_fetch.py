import os
import time
import requests
import pandas as pd

def fetch_and_save_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching: {scheme_name} ({scheme_code})...")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            json_data = response.json()
            meta = json_data.get('meta', {})
            nav_history = json_data.get('data', [])
            
            if not nav_history:
                print(f"Warning: No data found for {scheme_name}")
                return
            
            # Parse JSON data array to DataFrame
            df = pd.DataFrame(nav_history)
            
            # Map metadata fields as columns
            df['scheme_code'] = scheme_code
            df['scheme_name'] = meta.get('scheme_name', scheme_name)
            df['fund_house'] = meta.get('fund_house', 'Unknown')
            
            # Standardize column structure
            df = df[['date', 'nav', 'scheme_code', 'scheme_name', 'fund_house']]
            
            # Save file
            os.makedirs("data/raw", exist_ok=True)
            output_path = f"data/raw/live_nav_{scheme_code}.csv"
            df.to_csv(output_path, index=False)
            print(f"Success: Saved {len(df)} rows to {output_path}\n")
        else:
            print(f"Error: HTTP {response.status_code} for code {scheme_code}")
    except Exception as e:
        print(f"Exception for {scheme_code}: {str(e)}")

if __name__ == "__main__":
    # Combined target map from your prompt rules
    target_schemes = {
        "125497": "HDFC Top 100 Direct",
        "119551": "SBI Bluechip",
        "120503": "ICICI Bluechip",
        "118632": "Nippon Large Cap",
        "119092": "Axis Bluechip",
        "120841": "Kotak Bluechip"
    }
    
    print("Starting API Download Cycle...")
    for code, name in target_schemes.items():
        fetch_and_save_nav(code, name)
        time.sleep(1)  # Respect API rate limits