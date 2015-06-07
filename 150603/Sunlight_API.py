# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:48:47 2015
@author: erinboyle

Trying to access Sunlight Congress API with Codeacademy tutorial. See:
https://sunlightlabs.github.io/congress/
http://www.codecademy.com/courses/python-intermediate-en-D56TP/0/2?curriculum_id=50ecbb00306689057a000188
"""

import requests
import pprint
import json
import numpy as np
import pandas as pd
import sklearn as sk

""" The endpoint (line 8) usually determines what type of data you will get back, while the query parameters (line 4) act as 
filters on that data. Code academy code verbatim first: 
Note codeacadmey just shows .json not .json() ""

query_params = { 'apikey': 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
		         'phrase': 'conservation' 
		       }

endpoint = 'http://capitolwords.org/api/text.json'

response = requests.get( endpoint, params=query_params)
data = response.json()

pprint.pprint(data)

"""

query_params = {'apikey': 'dacd349b474440e1937181079fdf1619'} #, 'phrase': 'guns'}

endpoint = 'https://congress.api.sunlightfoundation.com/votes?fields=roll_id,result,breakdown.total'
#endpoint = 'https://congress.api.sunlightfoundation.com/bills?bill_type=hr&congress=112'

response = requests.get( endpoint, params=query_params)
data = response.json()

pprint.pprint(data)

out = pd.read_json()
#print data[count]

"""
out = json.loads(data)
print out

""
out = []
for line in data:
    out.append(json.loads(line))
print out

"""