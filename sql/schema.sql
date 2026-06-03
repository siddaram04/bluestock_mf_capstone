
-- 1. Dimension Tables
CREATE TABLE IF NOT EXISTS dim_fund (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    fund_house TEXT NOT NULL,
    category TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id TEXT PRIMARY KEY, -- format: YYYY-MM-DD
    year INTEGER,
    month INTEGER,
    day INTEGER,
    quarter INTEGER,
    is_weekend INTEGER
);

-- 2. Fact Tables
CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    date TEXT,
    nav REAL NOT NULL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code),
    FOREIGN KEY (date) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id TEXT PRIMARY KEY,
    scheme_code INTEGER,
    date TEXT,
    transaction_type TEXT, -- SIP, Lumpsum, Redemption
    amount REAL,
    kyc_status TEXT,
    state TEXT,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code),
    FOREIGN KEY (date) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    expense_ratio REAL,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER,
    date TEXT,
    aum_crores REAL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code),
    FOREIGN KEY (date) REFERENCES dim_date(date_id)
);