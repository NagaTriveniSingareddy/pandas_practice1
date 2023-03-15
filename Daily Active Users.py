"""Find the average daily active users for January 2021 for each account. 
Your output should have account_id and the average daily count for that account."""
import pandas as pd
from datetime import datetime

# Start writing code
#sf_events.head()
data=sf_events.groupby(['date','account_id'])['user_id'].count().reset_index(name='count')
#pd.to_datetime(data['date']).dt.to_period('M')
data=data.loc[pd.to_datetime(data['date']).dt.to_period('M')=='2021-01']
#pd.to_datetime(data['date']).dt.to_period('M').dt.daysinmonth
data['avg_daily']=data['count']/(pd.to_datetime(data['date']).dt.to_period('M').dt.daysinmonth)
data