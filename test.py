import requests
import pprint
import json
from download_links import resource_ids
import numpy as np
import pandas as pd


pp = pprint.PrettyPrinter(indent=4)


def call_url(resource_ids):
    r = requests.get(url=resource_ids)
    data = r.json()
    pp.pprint(data)
    return data


# Getting the data
for link in resource_ids:
    # URL
    data = call_url()
    data = data['results']['records']

'https://www.data.qld.gov.au/api/3/action/datastore_search?q=jones&resource_id=5f67cc4a-04bf-4a03-b1bf-e383598395be'


# # Priority Route Link Details
r = requests.get(url=route_url)
data = r.json()
# # create a file
with open('resp.json', "w") as fp:
    json.dump(data, fp)


# Empty dict to store the data
pd_data = {}

# pp.pprint(data['result']['records'])
record_arr = data['result']['records']

# for record in record_arr:
#     pd_data['time'].append(record['INTERVAL_END'])
#     for key in record:
#         pd_data['time'] = record['INTERVAL_END']
#         if(key != 'INTERVAL_END' or key != '_id'):
#             pd_data[key] = record[key]


pp.pprint(pd.DataFrame(data=record_arr))

# data_url = 'https://www.data.qld.gov.au/api/3/action/datastore_search_sql?sql=SELECT SCHEMA_ID() AS Result'
# r = requests.get(url=data_url)
# data = r.json()

# # create a file
# with open('data.json', "w") as fp:
#     json.dump(data, fp)

# print(data)
