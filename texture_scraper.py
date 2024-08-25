import requests
import pandas as pd
import numpy as np

vikram_tesla_id = 'clz7er1gi00r61075ifm7k0yx'
texture_api_key = 'api_94ec4ec5615af57af39beee883d9d948'
start_date = '2023-09-10T11:43:33.266Z'

# main

headers = {
    'Accept': 'application/json',
    'Texture-Api-Key': texture_api_key,
}

parent_df = pd.DataFrame()

for page in range(1, 44):
    params = {
        'from': start_date,
        'perPage': '100',
        'page': f'{page}'
    }

    response = requests.get(f'https://api.texturehq.com/v1/devices/{vikram_tesla_id}/history', params=params,
                            headers=headers)
    data_raw = response.json()
    data = data_raw['data']
    df = pd.DataFrame.from_records(data)
    parent_df = pd.concat([parent_df, df], axis=0)

parent_df.reset_index(drop=True, inplace=True)

parent_df.to_csv('Tesla_Charging_Data.csv')

print('hello')
