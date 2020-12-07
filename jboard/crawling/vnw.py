# -*- coding: utf-8 -*-
from logging import getLogger

from requests import Session


class VnWorks:
    _logger = getLogger(__name__)

    default_headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'origin': 'https://www.vietnamworks.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'content-type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.vietnamworks.com/'
    }

    _url = 'https://jf8q26wwud-dsn.algolia.net/1/indexes/*/' \
           'queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&' \
           'x-algolia-application-id=JF8Q26WWUD&' \
           'x-algolia-api-key=2bc790c0d4f44db9ab6267a597d17f1a'

    params = (
        ('x-algolia-agent', 'Algolia for JavaScript (3.35.1); Browser'),
        ('x-algolia-application-id', 'JF8Q26WWUD'),
        ('x-algolia-api-key', '2bc790c0d4f44db9ab6267a597d17f1a'),
    )

    data = '{"requests":[{"indexName":"vnw_job_v2","params":"query=python&hitsPerPage=200&attributesToRetrieve=%5B%22*%22%2C%22-jobRequirement%22%2C%22-jobDescription%22%5D&attributesToHighlight=%5B%5D&query=python&facetFilters=%5B%5B%22locationIds%3A29%22%5D%5D&filters=&numericFilters=%5B%5D&page=0&restrictSearchableAttributes=%5B%22jobTitle%22%2C%22skills%22%2C%22company%22%5D"}]}'

    _base_post_url = 'https://jf8q26wwud-dsn.algolia.net/1/indexes/*/queries'

    def __init__(self):
        self._session = Session()
        self._session.headers.update(self.default_headers)

    def get_python_jobs(self):
        self._logger.info('Getting python jobs')
        js = self._session.post(self._base_post_url, params=self.params, data=self.data)\
            .json()
        print(js)
        return []

    def get_jobs(self, keywords):
        raise NotADirectoryError


if __name__ == '__main__':
    for job in VnWorks().get_python_jobs():
        print(job)
