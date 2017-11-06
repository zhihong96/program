# -*- coding: utf-8 -*-

import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

def basic_auth():
    # 基本认证
    response = requests.get(construct_url('user'), auth=('zhihong96','zdvhi93tg'))
    print response.text
    print response.request.headers

def basic_oauth():
    headers = {'Authorization': 'token 2917be95313eb780e6cc68ad8eb552d00902362f'}
    # user/emails
    response = requests.get(construct_url('user/eamils'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code

from requests.auth import AuthBase

class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # requests add headers
        r.headers['authorization'] = ' '.join(['token', self.token])
        return r 

def oauth_advanced():
    auth = GithubAuth('2917be95313eb780e6cc68ad8eb552d00902362f')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.request.headers
    print response.text
    print response.status_code

  
if __name__=='__main__':
    oauth_advanced()
