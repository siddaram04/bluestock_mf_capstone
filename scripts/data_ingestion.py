import os
import glob
import pandas as pd

def audit_all_csv_datasets():
    raw_dir = "data/raw"
    
    # Target every CSV file present in the raw folder
    csv_files = glob.glob(os.path.join(raw_dir, "*.csv"))
    
    if not csv_files:
        print(" No CSV datasets found in data/raw/. Please add your 10 files first!")
        return

    print(f" Found {len(csv_files)} total CSV files inside '{raw_dir}'. Starting Data Profiling & Audit...\n")
    
    # Loop through each file to inspect properties
    for idx, file_path in enumerate(sorted(csv_files), 1):
        file_name = os.path.basename(file_path)
        print("=" * 60)
        print(f" DATASET {idx}: {file_name}")
        print("=" * 60)
        
        try:
            # Load file
            df = pd.read_csv(file_path)
            
            # 1. Print Shape
            print(f" Dimensionality (.shape): {df.shape[0]} rows, {df.shape[1]} columns")
            print("-" * 40)
            
            # 2. Print Data Types
            print(" Column Names & Data Types (.dtypes):")
            print(df.dtypes)
            print("-" * 40)
            
            # 3. Print Head
            print(" First 3 Preview Rows (.head()):")
            print(df.head(3))
            print("-" * 40)
            
            # 4. Anomaly Scanner
            print(" Automated Data Quality & Anomaly Notes:")
            has_anomalies = False
            
            # Check for missing values
            missing_counts = df.isnull().sum()
            total_missing = missing_counts.sum()
            if total_missing > 0:
                has_anomalies = True
                print(f"   MISSING DATA: Found {total_missing} null fields.")
                for col, count in missing_counts.items():
                    if count > 0:
                        print(f"     - Column '{col}': {count} missing rows")
            
            # Check for exact duplicate rows
            duplicate_count = df.duplicated().sum()
            if duplicate_count > 0:
                has_anomalies = True
                print(f"  DUPLICATES: Found {duplicate_count} exact duplicate rows.")
                
            if not has_anomalies:
                print("  CLEAN: Structure looks solid with zero null cells or duplicates.")
                
        except Exception as e:
            print(f" Failed to complete audit for {file_name} due to error: {str(e)}")
            
        print("\n" + "•" * 60 + "\n")

if __name__ == "__main__":
    audit_all_csv_datasets()