import pandas as pd
import json

file_path = r"C:\Users\lucie\OneDrive\Documentos\Steam Games Analysis\archive\games.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='index')
df.index.name = 'AppID'
df = df.reset_index()

df_clean = df[[
    'AppID', 'name', 'release_date', 'price', 'estimated_owners',
    'peak_ccu', 'positive', 'negative', 'recommendations',
    'metacritic_score', 'user_score', 'genres', 'categories',
    'tags', 'developers', 'publishers',
    'average_playtime_forever', 'median_playtime_forever'
]].copy()

# Convert lists to comma-separated strings
for col in ['genres', 'categories', 'developers', 'publishers']:
    df_clean[col] = df_clean[col].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

# Tags is a dictionary - extract only the tag names
df_clean['tags'] = df_clean['tags'].apply(lambda x: ', '.join(x.keys()) if isinstance(x, dict) else x)

output_path = r"C:\Users\lucie\OneDrive\Documentos\Steam Games Analysis\archive\games_clean.csv"
df_clean.to_csv(output_path, index=False, encoding='utf-8')

print(f"Done! {df_clean.shape[0]} rows and {df_clean.shape[1]} columns.")
print(df_clean[['AppID', 'name', 'genres', 'tags']].head(3))