import pandas as pd
import numpy as np
from scipy import stats

def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith(('.xlsx', '.xls')):
        return pd.read_excel(file)
    else:
        raise ValueError("Unsupported file type. Use CSV or Excel.")

def clean_data(df):
    # Handle missing values (fill with mean for numeric, mode for categorical)
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown', inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Detect and remove outliers (using Z-score for numeric columns)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        z_scores = np.abs(stats.zscore(df[col]))
        df = df[z_scores < 3]  # Remove rows with Z-score > 3
    
    return df

def transform_data(df, rename_dict=None, type_changes=None, encode_categoricals=False):
    # Rename columns
    if rename_dict:
        df.rename(columns=rename_dict, inplace=True)
    
    # Change data types
    if type_changes:
        for col, dtype in type_changes.items():
            df[col] = df[col].astype(dtype)
    
    # Encode categoricals (one-hot encoding)
    if encode_categoricals:
        categorical_cols = df.select_dtypes(include=['object']).columns
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

def analyze_data(df):
    # Summary statistics
    summary = df.describe(include='all')
    
    # Correlations (for numeric columns)
    numeric_df = df.select_dtypes(include=[np.number])
    correlations = numeric_df.corr() if not numeric_df.empty else None
    
    # Patterns (e.g., value counts for categoricals)
    patterns = {}
    for col in df.select_dtypes(include=['object']).columns:
        patterns[col] = df[col].value_counts()
    
    return summary, correlations, patterns
