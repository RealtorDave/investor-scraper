import json
import requests
import pandas as pd

base_URL = "https://api.cilabs.com/conferences/cc20/lists/7b29fd4b-fbcf-4a21-bc64-1ccfe9d362af?per_page=50"
investors = []

for page in range(1, 50):
    if page != 1:
        URL = base_URL + str.format("&page={}", page)
    else:
        URL = base_URL

    print(str.format("Requesting data from {}", URL))

    response = requests.get(URL)

    try:
        data = response.json()

        # with open('data/raw_response.txt', 'w') as outfile:
        #     json.dump(data, outfile)

        for investor in data['data']:
            investors.append([
            investor['id'],
            investor['first_name'],
            investor['last_name'],
            investor['job_title'],
            investor['bio'],
            investor['company_name']])
    except:
        break

investors_df = pd.DataFrame.from_records(investors, columns=['id', 'first_name', 'last_name', 'job_title', 'bio', 'company_name'])

investors_df.to_csv('data/investors.csv')