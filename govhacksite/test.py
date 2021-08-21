import requests
import io
import pandas as pd
url = "https://api.data.abs.gov.au/data/ABS,ABS_REGIONAL_LGA2020/INCOME_2+INCOME_21+HELP_2+LF_6+LF_3+ERP_P_20+ERP_23...?startPeriod=2016"

payload={}
headers = {
  'Accept': 'text/csv'
}

response = requests.request("GET", url, headers=headers, data=payload)

urlData = response.content
rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
print(rawData['DATAFLOW'][0])