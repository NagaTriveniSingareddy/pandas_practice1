"""Find the number of account registrations according to the signup date. 
Output the months and their corresponding number of registrations."""


import pandas as pd
from datetime import datetime

# Start writing code
#noom_signups.head()
data=noom_signups.groupby(pd.to_datetime(noom_signups['started_at']).dt.to_period('M'))['plan_id'].count().reset_index(name='regestratin_count')