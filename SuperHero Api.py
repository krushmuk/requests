import requests


superman_names = ['Hulk', 'Captain America', 'Thanos']
token = '2619421814940190'
superman_intelligence = dict()
for superman_name in superman_names:
    res = requests.get(f'https://superheroapi.com/api/{token}/search/{superman_name}')
    superman_intelligence[res.json()['results'][0]['powerstats']['intelligence']] = superman_name
print(f'The highest intelligence has {superman_intelligence[max(superman_intelligence.keys())]}')