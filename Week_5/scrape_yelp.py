# example in python, functions from wrapper

import yelp as yelp

host = "api.yelp.com"
path = "/v2/search/"

url_params = {'term': 'gastropubs'}

yelp.request(host, path, url_params)