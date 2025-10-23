import requests
from random import randint
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'c199eb86-ce24-4a0d-8007-1ab517cf083f',
}

json_data = {
    'url': 'https://viikqoye.com/dc/?blockID=399115',
    'proxyType': 'residential',
    'proxyCountry': 'US',
    'blockResources': False,
    'blockAds': False,
    'blockUrls': [],
    'wait': randint(10000,25000),
    'jsScenario': [
        {
            'click': 'button',
        },
        {
            'wait': f"{randint(1000,5000)}",
        },
    ],
    'extractRules': {
        'title': 'h1',
    },
    'screenshot': True,
    'jsRendering': True,
    'extractEmails': True,
    'includeOnlyTags': [],
    'excludeTags': [],
    'outputFormat': [],
}
for i in range(1000):

	response = requests.post('https://api.hasdata.com/scrape/web', headers=headers, json=json_data)
	print(i)
