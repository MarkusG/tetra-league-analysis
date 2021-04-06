import pandas as pd
import matplotlib.pyplot as plt

# this is to properly order the ranking data
df_rank_mapping = pd.DataFrame({
    'rank': [
        'x',
        'u',
        'ss',
        's+',
        's',
        's-',
        'a+',
        'a',
        'a-',
        'b+',
        'b',
        'b-',
        'c+',
        'c',
        'c-',
        'd+'
    ]
})
rank_mapping = df_rank_mapping.reset_index().set_index('rank')

raw = pd.read_json('data.json')

# each player's league data is stored as a nested 'league' object
league = pd.json_normalize(raw['league'])
data = pd.concat([raw[['_id', 'username', 'country']], league])

# count by rank
ranks = data.groupby(['rank']).size().reset_index(name='count')

# fix ordering
ranks['rank_num'] = ranks['rank'].map(rank_mapping['index'])
ranks = ranks.sort_values('rank_num')

# create and show the bar chart
plt.bar(ranks['rank'], ranks['count'])
plt.show()
