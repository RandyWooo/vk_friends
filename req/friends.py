import datetime
import requests

def calc_age(uid):
    url = 'https://api.vk.com/method/users.get?v=5.71&access_token='
    ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

    request = requests.get(url + ACCESS_TOKEN, params={'user_ids': uid})
    user_id = request.json()['response'][0]['id']

    url = 'https://api.vk.com/method/friends.get?v=5.71&access_token='
    r = requests.get(url + ACCESS_TOKEN, params={'user_id': user_id, 'fields': 'bdate'})
    user_friends = r.json()['response']['items']

    friends = []
    now = datetime.datetime.now()
    for i in user_friends:
        friends_bdate = i.get('bdate', '').split('.')
        if len(friends_bdate) == 3:
            friends.append(now.year - int(friends_bdate[2]))

    friends_result = list((x, friends.count(x)) for x in set(friends))
    friends_result = sorted(friends_result, key=lambda x:x[0], reverse=False)
    friends_result = sorted(friends_result, key=lambda x:x[1], reverse=True)

    return friends_result


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
