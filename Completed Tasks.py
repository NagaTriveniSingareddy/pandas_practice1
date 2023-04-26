"""Find the number of actions that ClassPass workers did for tasks completed in January 2022. The completed tasks are these rows in the asana_actions table with 'action_name' equal to CompleteTask. Note that each row in the dataset indicates how many actions of a certain type one user has performed in one day and the number of actions is stored in the 'num_actions' column.
Output the ID of the user and a total number of actions they performed for tasks they completed. If a user from this company did not complete any tasks in the given period of time, you should still output their ID and the number 0 in the second column."""
import pandas as pd
import datetime
# Start writing code
asana_users.head()
asana_users=asana_users.loc[asana_users['company']=='ClassPass']
finaldata=asana_users.merge(asana_actions,how='left',left_on='user_id',right_on='user_id')
finaldata=finaldata.loc[pd.to_datetime(finaldata['date']).dt.to_period('M')=='2022-01']
finaldata['num_actions']=finaldata.apply(lambda x: x['num_actions'] if x['action_name']=='CompleteTask' else 0,axis=1)
finaldata=finaldata.groupby('user_id')['num_actions'].sum().reset_index()