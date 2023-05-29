"""Count how many claims submitted in December 2021 are still pending. 
A claim is pending when it has neither an acceptance nor rejection date."""

import pandas as pd
from datetime import datetime

# Start writing code
#cvs_claims.head()
data=cvs_claims[(cvs_claims['date_accepted'].isnull())&(cvs_claims['date_rejected'].isnull())]
data=data.loc[pd.to_datetime(data['date_submitted']).dt.to_period('M')=='2021-12']
print(len(data))