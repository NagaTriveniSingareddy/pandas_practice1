"""For each city, find the number of rides in August 2021 that were not paid for using promotional codes. Output the city or cities where this number was the highest."""
import pandas as pd

# Start writing code
lyft_orders.head()
data=lyft_orders.merge(lyft_payments,how="left",left_on='order_id',right_on='order_id')
data=data.loc[(data['promo_code']==False)&(pd.to_datetime(data['order_date']).dt.to_period('M')=='2021-08')]
data=data.groupby('city')['order_id'].count().reset_index(name='rides_count')