
"""This program is an Instagram scraper that scrapes images based on user-defined keywords.

It requires a username and password to access your Instagram account, but it only requires the username to access a public Instagram account."""

import argparse
import json
import os
import urllib.request

import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Scrape Instagram')
parser.add_argument('-u', '--username', type=str, help='Instagram Username')
parser.add_argument('-p', '--password', type=str, help='Instagram Password')
parser.add_argument('-k', '--keywords', type=str, nargs='+', help='Keywords to scrape')
parser.add_argument('-l', '--limit', type=int, default=5, help='Max number of images to download')
args = parser.parse_args()


def main():
    if args.username and args.password:
        login(args.username, args.password)
    else:
        print('\nLogin is required\n')
        parser.print_help()

def login(username, password):
    if not os.path.exists('cookies'):
        os.makedirs('cookies')

    if not os.path.exists('./cookies/instagram_cookies.txt'):
        print('\nThere are no stored cookies for Instagram\n')
        print('Please enter your Instagram credentials\n')
        username = input('Username: ')
        password = input('Password: ')

        if username and password:
            print('\nLogging you in...\n')
            login_user(username, password)
        else:
            print('\nLogin is required\n')
            parser.print_help()
            return
    else:
        print('\nUsing stored cookies for Instagram\n')

    if args.keywords:
        print('\nScraping images...\n')
        scrape_images(args.keywords, args.limit)
    else:
        print('\nKeywords are required\n')
        parser.print_help()

def login_user(username, password):
    session = requests.Session()
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'referer': 'https://www.instagram.com/'
    }
    session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': '', 's_network': '', 'ds_user_id': ''})

    print('\nRequesting login page...\n')
    r = session.get('https://www.instagram.com/')

    print('\nParsing CSRF...\n')
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.body
    script = body.find('script')
    raw = script.text.strip().replace(';', '').replace('window._sharedData = ', '')
    json_data = json.loads(raw)
    csrf = json_data['config'].get('csrf_token')

    print('\nLogging in...\n')
    r = session.post('https://www.instagram.com/accounts/login/ajax/', data={'username': username, 'enc_password': password}, allow_redirects=True)
    session.headers.update({'X-CSRFToken': csrf})

    print('\nSetting cookies...\n')
    sessionid = r.cookies['sessionid']
    mid = r.cookies['mid']
    ig_pr = '1'
    ig_vw = '1920'
    csrftoken = r.cookies['csrftoken']
    s_network = '-'
    ds_user_id = r.cookies['ds_user_id']

    session.cookies.update({'sessionid': sessionid, 'mid': mid, 'ig_pr': ig_pr, 'ig_vw': ig_vw, 'csrftoken': csrftoken, 's_network': s_network, 'ds_user_id': ds_user_id})

    print('\nSuccessfully logged in\n')

def scrape_images(keywords, limit):
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    session = requests.Session()
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'referer': 'https://www.instagram.com/'
    }
    session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': '', 's_network': '', 'ds_user_id': ''})

    with open('./cookies/instagram_cookies.txt') as f:
        cookies = f.read().split(';')
        session.cookies.update({cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies})

    for keyword in keywords:
        print('\nScraping images for: {}\n'.format(keyword))

        if not os.path.exists('./downloads/{}'.format(keyword)):
            os.makedirs('./downloads/{}'.format(keyword))

        r = session.get('https://www.instagram.com/explore/tags/' + keyword)

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            body = soup.body
            script = body.find('script')
            raw = script.text.strip().replace(';', '').replace('window._sharedData = ', '')
            json_data = json.loads(raw)
            images = json_data['entry_data']['TagPage'][0]['tag']['media']['nodes']

            print('\nFound {} images\n'.format(len(images)))

            for i, image in enumerate(images):
                if i >= limit:
                    break

                image_url = image['display_src']
                image_name = image_url.split('/')[-1]
                print('Downloading image {}'.format(image_name))
                urllib.request.urlretrieve(image_url, './downloads/{}/{}'.format(keyword, image_name))
        else:
            print('Error occurred: {}'.format(r.status_code))

if __name__ == '__main__':
    main()
