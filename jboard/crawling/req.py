# -*- coding: utf-8 -*-

import requests

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.vietnamworks.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.vietnamworks.com/',
    'Accept-Language': 'en-US,en;q=0.9,de;q=0.8,vi;q=0.7',
}

params = (
    ('x-algolia-agent', 'Algolia for JavaScript (3.35.1); Browser'),
    ('x-algolia-application-id', 'JF8Q26WWUD'),
    ('x-algolia-api-key', '2bc790c0d4f44db9ab6267a597d17f1a'),
)

data = {'{"requests":[{"indexName":"vnw_job_v2","params":"query': 'python',
        'hitsPerPage': '200',
        'attributesToRetrieve': '["*","-jobRequirement","-jobDescription"]',
        'attributesToHighlight': '[]',
        'query': 'python',
        'facetFilters': '[["locationIds:29"]]',
        'filters': '',
        'numericFilters': '[]',
        'page': '0',
        'restrictSearchableAttributes': '["jobTitle","skills","company"]"}]}'
        }

response = requests.post('https://jf8q26wwud-dsn.algolia.net/1/indexes/*/queries', headers=headers,
                         params=params, data=data)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.post('https://jf8q26wwud-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=JF8Q26WWUD&x-algolia-api-key=2bc790c0d4f44db9ab6267a597d17f1a', headers=headers, data=data)
print(response.json())
