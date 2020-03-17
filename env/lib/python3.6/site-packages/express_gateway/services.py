import logging

import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from rest_framework.exceptions import ValidationError

log = logging.getLogger('django')


def get_headers() -> dict:
    api_key = settings.EXPRESS_GATEWAY.get('API_KEY', None)
    if not api_key:
        raise ImproperlyConfigured('Express Gateway: API_KEY is required.')
    return {'Authorization': f'apiKey {api_key}'}


def get_endpoint(key_name):
    base_url = settings.EXPRESS_GATEWAY.get('URL', None)
    endpoint = settings.EXPRESS_GATEWAY.get('ENDPOINTS', None)
    if not base_url or not endpoint:
        raise ImproperlyConfigured('URL or ENDPOINTS is required')

    endpoint = endpoint.get(key_name, None)
    if not endpoint:
        raise ImproperlyConfigured(f'Cannot find endpoint name {key_name}.')

    return base_url + endpoint


def handle_error(url, data, response):
    if response.status_code not in range(200, 299):
        log.error(url)
        log.error(get_headers())
        log.error(data)
        raise ValidationError(response.json())


def create_user(**kwargs):
    """
    Expected kwargs are firstName, lastName, email, password
    """
    assert kwargs.get('firstName')
    assert kwargs.get('lastName')
    assert kwargs.get('email')
    assert kwargs.get('password')

    url = get_endpoint('register')
    response = requests.post(url=url, headers=get_headers(), json=kwargs)
    log.info(f'creating {kwargs}')
    handle_error(url, kwargs, response)

    return response.json()


def authenticate_user(username: str, password: str):
    url = get_endpoint('token')
    data = {'username': username, 'password': password}
    response = requests.post(url=url, json=data)
    log.info(f'authentication {data}')
    handle_error(url, data, response)

    return response.json()
