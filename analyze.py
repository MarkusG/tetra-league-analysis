import pandas as pd
import matplotlib.pyplot as plt

rank_index = {
    'd': 16
}

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
league = pd.json_normalize(raw['league'])
data = pd.concat([raw[['_id', 'username', 'country']], league])

ranks = data.groupby(['rank']).size().reset_index(name='count')
ranks['rank_num'] = ranks['rank'].map(rank_mapping['index'])
ranks = ranks.sort_values('rank_num')

plt.bar(ranks['rank'], ranks['count'])
plt.show()
