import requests
url_guru ='https://api.gnavi.co.jp/RestSearchAPI/v3/'

#コメント挿入
params = {}
val = input('ぐるなびに聞きたいことを何でも記入してください　：')
params['keyid'] = '0bfdeadbcd27a20b0aca3581b7e0eb42'
params['freeword'] = val

response = requests.get(url_guru, params)
results = response.json()
restaurants = results['rest']
print(len(restaurants))
i = 0
while i < len(restaurants):
    print(restaurants[i]['name'])
    i = i + 1
print("End")