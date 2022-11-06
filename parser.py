import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


def parse_profiles(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    page_exists = soup.find('h1', {'id': 'owner_page_name'})

    if page_exists:
        age = soup.find('span', {'class': 'ProfileModalInfoLink'}).get_text()
        status = soup.find('span', {'class': 'kuiCaption'}).get_text()

        return True
    else:
        return False


def get_data(number):
    id = 1

    while number > 0:
        user = parse_profiles(f'https://vk.com/id{id}')
        id += 1

        if user:
            print(user)
            number -= 1

        else:
            continue

    return 'The End!'


get_data(10000)