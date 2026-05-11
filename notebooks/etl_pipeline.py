import pandas as pd
import numpy as np

np.random.seed(10)

rows = 5000

customer_ids = np.random.randint(1000, 2000, rows)

transaction_amount = np.random.randint(100, 10000, rows)

transaction_type = np.random.choice(
    ['Shopping', 'Travel', 'Bills', 'Food'],
    rows
)

raw_df = pd.DataFrame({
    'Customer_ID': customer_ids,
    'Transaction_Amount': transaction_amount,
    'Transaction_Type': transaction_type
})

raw_df.to_csv('raw_transactions.csv', index=False)

segment_conditions = [
    raw_df['Transaction_Amount'] > 7000,
    raw_df['Transaction_Amount'] > 3000,
]

segment_values = ['High Value', 'Medium Value']

raw_df['Customer_Segment'] = np.select(
    segment_conditions,
    segment_values,
    default='Low Value'
)

raw_df.to_csv('cleaned_transactions.csv', index=False)

print('ETL pipeline completed successfully!')
