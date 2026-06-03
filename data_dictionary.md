## 1. Table: dim_fund (Dimension Table)
| Column Name | Data Type | Key Type | Business Definition |
| :--- | :--- | :--- | :--- |
| `scheme_code` | INTEGER | Primary Key | Unique 6-digit structural identification key issued by AMFI. |
| `scheme_name` | TEXT | None | Complete marketing name designation for the retail mutual fund unit. |
| `fund_house` | TEXT | None | Financial institution handling fund distributions (AMC). |

## 2. Table: fact_nav (Fact Ledger Table)
| Column Name | Data Type | Key Type | Business Definition |
| :--- | :--- | :--- | :--- |
| `id` | INTEGER | Primary Key | Auto-incrementing line item key. |
| `scheme_code` | INTEGER | Foreign Key | Relates to target asset profile record inside `dim_fund`. |
| `date` | TEXT | Foreign Key | Calendar tracking timestamp (YYYY-MM-DD). |
| `nav` | REAL | None | Net Asset Value pricing computed per unit. |

## 3. Table: fact_transactions (Fact Ledger Table)
| Column Name | Data Type | Key Type | Business Definition |
| :--- | :--- | :--- | :--- |
| `transaction_id` | TEXT | Primary Key | Ledger registration invoice identifier. |
| `scheme_code` | INTEGER | Foreign Key | Targeted fund schema mapping index code. |
| `date` | TEXT | Foreign Key | Day action occurred on. |
| `transaction_type`| TEXT | None | Method categorization format tags: [SIP, Lumpsum, Redemption]. |
| `amount` | REAL | None | Nominal value of the trade ledger order. |
| `kyc_status` | TEXT | None | User compliance evaluation index level: [Y, N, PENDING]. |
| `state` | TEXT | None | Origin province geographic area of the investor. |