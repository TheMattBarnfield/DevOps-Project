from requests import get, post, put, delete

class ApiClient:
    def get(self, url, params):
        return get(url, params=params)

    def post(self, url, params):
        return post(url, params=params)

    def put(self, url, params):
        return put(url, params=params)

    def delete(self, url, params):
        return delete(url, params=params)
