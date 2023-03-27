"""Which hour has the highest average order volume per day? Your output should have the hour which satisfies that condition, and average order volume."""
import pandas as pd
from datetime import datetime
# Start writing code
postmates_orders.head()
postmates_orders['hours']=pd.to_datetime(postmates_orders['order_timestamp_utc']).dt.hour+(pd.to_datetime(postmates_orders['order_timestamp_utc']).dt.minute)/60+(pd.to_datetime(postmates_orders['order_timestamp_utc']).dt.second)/3600
postmates_orders['average_amount']=postmates_orders['amount']/24
data=postmates_orders.groupby(pd.to_datetime(postmates_orders['order_timestamp_utc']).dt.to_period('D')).first()