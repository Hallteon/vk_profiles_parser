import random
import re

import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


def parse_profile(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    page_exists = soup.find('h1', {'class': 'page_name'})

    if page_exists:
        try:
            name = page_exists.text
            age = int(soup.find_all('a', {'href': re.compile(r'^/search(.*?)byear(.*?)$')})[0].text.split()[0])
            status = soup.find('span', {'class': 'current_text'}).text
            groups = []
            groups_links = []

            for group in soup.find_all('div', {'class': 'group_name'}):
                link = group.find('a')
                groups.append(link.text)
                groups_links.append(link.get('href'))

            groups = '\n'.join(groups)
            groups_links = '\n'.join(groups_links)

        except:
            return False
        else:
            return {'name': name, 'age': age, 'status': status, 'groups': groups, 'groups_links': groups_links}


def get_data(number):
    for id in random.sample(range(1, 100000), number):
        user = parse_profile(f'https://vk.com/id{id}')

        if user:
            print(id, user['name'], user['age'], user['status'], user['groups'], user['groups_links'])


print(get_data(10000))