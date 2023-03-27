"""The column 'perc_viewed' in the table 'post_views' denotes the percentage of the session duration time 
the user spent viewing a post. Using it, calculate the total time that each post was viewed by users.
 Output post ID and the total viewing time in seconds, but only for posts with a total viewing time of over 5 seconds.

"""
import pandas as pd

# Start writing code
user_sessions.head()
data=user_sessions.merge(post_views,how="inner",left_on="session_id",right_on="session_id")
data=data.loc[data['perc_viewed']<=5]
data=data.groupby(data['post_id'])['perc_viewed'].sum().reset_index(name="total_time")