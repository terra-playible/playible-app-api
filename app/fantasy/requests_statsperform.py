import datetime
import hashlib
import os
import re
import sys
import time

import requests
from requests.exceptions import HTTPError
from django.conf import settings

HOST = 'http://api.stats.com/v1/stats/basketball/nba/'
PUBLIC_KEY = os.environ.get('STATSPERFORM_PUBLIC_KEY', '')
SECRET_KEY = os.environ.get('STATSPERFORM_PRIVATE_KEY', '')

def get(url, args=[], stream=False):
  try:
    if args:
      params = dict(f.split('=') for f in args)
    else:
      params = {}

    params.update(get_sig())

    url = HOST + url
    response = requests.get(
      url,
      params=params,
      stream=stream
    )
    response.raise_for_status()

    return {
      'status': settings.RESPONSE['STATUS_OK'],
      'response': response.json().get('apiResults')[0]
    }

  except requests.Timeout:
    return {
      'status': settings.RESPONSE['STATUS_ERROR'],
      'response': f'HTTP timeout when downloading: {url}'
    }
  except requests.exceptions.ConnectionError as e:
    return {
      'status': settings.RESPONSE['STATUS_ERROR'],
      'response': f'HTTP Connection Error when downloading: {url}'
    }
  except HTTPError as http_err:
    return {
      'status': settings.RESPONSE['STATUS_ERROR'],
      'response': f'HTTP error occurred: {http_err}'
    }

def get_sig():
  timestamp = repr(int(time.time()))
  all = str.encode(PUBLIC_KEY + SECRET_KEY + timestamp)
  signature = hashlib.sha256(all).hexdigest()
  params = {
    'content-type': 'application/json',
    'api_key': PUBLIC_KEY,
    'sig': signature 
  }
  
  return params
