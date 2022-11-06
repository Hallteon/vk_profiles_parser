import datetime
import random
import re
import vk_api
import csv

from config import TOKEN


def users_parser(ids, session):
    users = session.method('users.get', {'user_ids': ids, 'fields': 'bdate,status,counters,relation,followers_count'})

    for user in users:
        try:
            if re.match(r'^(.*?)\.(.*?)\.(.*?)$', user['bdate']):
                age = datetime.datetime.now().year - int(user['bdate'].split('.')[2])
                user['age'] = age
            else:
                continue

            user['frieds'] = session.method('friends.get', {'user_id': f'{user["id"]}'})['count']
            user['groups'] = []
            user['groups_links'] = []
            groups = session.method('groups.get', {'user_id': f'{user["id"]}', 'extended': '1'})['items']

            for group in groups:
                user['groups'].append(group['name'])
                user['groups_links'].append(group['screen_name'])

            user['groups'] = '\n'.join(user['groups'])
            user['groups_links'] = '\n'.join(user['groups_links'])
        except:
            continue

    return users


def divide_list(lst, n):
    for x in range(0, len(lst), n):
        e_c = lst[x:n + x]

        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c


def get_data(number):
    ids = random.sample(range(1, 100000), number)
    users = []

    if len(ids) > 1000:
        samples = divide_list(ids, 500)

        for sample in samples:
            sample = [str(id) for id in sample]
            str_sample = ','.join(sample)
            user = users_parser(str_sample, api_session)
            users.extend(user)
    else:
        ids = [str(id) for id in ids]
        str_ids = ','.join(ids)
        user = users_parser(str_ids, api_session)
        users.extend(user)

    if users:
        return users


# def create_dataset(data):
#     with open('data.csv', mode='w', encoding='utf-8') as w_file:
#         file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
#         file_writer.writerow(['ID', 'name', 'age', 'status', 'groups', 'groups_links', 'friends', 'followers', 'relationship'])
#
#         for user in data:
#             print(user)
#
#             file_writer.writerow([user['id'], user['first_name'], user['age'], user['status'], user['groups'],
#                                   user['groups_links'], user['friends'], user['followers'], user['relationship']])


if __name__ == '__main__':
    api_session = vk_api.VkApi(token=TOKEN)
    vk = api_session.get_api()

    print(get_data(20))