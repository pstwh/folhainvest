
# coding: utf-8

# In[1]:

import pandas as pd
import os

import requests


# In[7]:

session = requests.Session()
#session.auth = 

url = "https://login.folha.com.br/login"

params = {"done":"http://folhainvest.folha.uol.com.br/carteira","service":"folhainvest"}

#data = {
#}

#headers = {
    
#   }

auth = session.request("POST", url, data, headers, params)

print(auth.cookies)


# In[28]:

url = "https://folhainvest.folha.uol.com.br/cotacoes"

querystring = {"tsv":"yes"}

#headers = {
#}

r = requests.request("GET", url, headers=headers, params=querystring)

file = r.headers['Content-Disposition'][43:-5]

if r.status_code == 200:
    with open('/folhainvest/data/{}'.format(file), 'wb') as f:
        for chunk in r:
            f.write(chunk)


# In[29]:

"""
table = pd.read_csv(file, sep='\t', header=1, encoding='latin-1')

print(table['Ação'])
"""

