import random
import vk_api


def users_parser(ids, session):
    users = session.method('users.get', {'user_ids': ids, 'fields': 'bdate,status,counters,relation,'})

    return users


def divide_list(lst, n):
    for x in range(0, len(lst), n):
        e_c = lst[x:n + x]

        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c


def get_data(number):
    ids = random.sample(range(1, 100000), number)
    samples = divide_list(ids, 500)
    users = []

    for sample in samples:
        sample = [str(id) for id in sample]
        str_sample = ','.join(sample)
        user = users_parser(str_sample, api_session)
        users.append(user)

    if users:
        return users


if __name__ == '__main__':
    api_session = vk_api.VkApi(token='vk1.a.3QmRiAaVUfLTCfAyMf2MiBJu1ZSR3SNHNpcwYMmorsLHvqA_EU7bvZ-ufB2X9FeHECO_zORAF6PsUw3dXE3fRqVQncbwDGACdaHLPmw8fQUitqIZaAQUhITgYPtea_ovPSjWBWE2j-F-aAkW8-tY2jEF3kDPMxqjMi5604oeAUKAwrfarj_ovi10OTDcMWeqLd8wj97XTRg6ghgSccF57w')
    vk = api_session.get_api()

    print(get_data(1000))