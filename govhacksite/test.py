import requests
import io
import pandas as pd
url = "https://api.data.abs.gov.au/data/ABS,ABS_REGIONAL_LGA2020/INCOME_21...?startPeriod=2016&endPeriod=2016"

payload={}
headers = {
  'Accept': 'text/csv'
}

pd.set_option('display.max_columns', None)
response = requests.request("GET", url, headers=headers, data=payload)

urlData = response.content
rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
print(rawData.mean(axis=0, skipna= False)['OBS_VALUE'])