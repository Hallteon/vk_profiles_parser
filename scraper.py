import random
import vk_api

from config import TOKEN


def users_parser(id, session):
    try:
        user = session.method('users.get', {'user_ids': f'{id}', 'fields': 'bdate,status,relation,followers_count'})
        # print(session.method('groups.get', {'user_ids': id}))
        user[0]['friends'] = session.method('friends.get', {'user_id': f'{id}'})['count']
        print(user)
    except:
        return False
    else:
        return user


def get_data(number):
    ids = random.sample(range(1, 100000), number)
    users = []

    for id in ids:
        user = users_parser(id, api_session)

        if user:
            users.append(user)

    if users:
        return users


if __name__ == '__main__':
    api_session = vk_api.VkApi(token=TOKEN)
    vk = api_session.get_api()

    print(get_data(1000))