import json
from pprint import pprint

with open('C:\MyData\Office Work\CodeBase\experimental\input.json') as df:
    data = json.loads(df)
pprint(data)
