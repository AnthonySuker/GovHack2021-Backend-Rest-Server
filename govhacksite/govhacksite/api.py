from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

import requests
import io
import pandas as pd

class getIncomeHelp(APIView):


    def get(self,request):
        url = "https://api.data.abs.gov.au/data/ABS,ABS_REGIONAL_LGA2020/INCOME_2+INCOME_21+HELP_2+LF_6+LF_3+ERP_P_20+ERP_23...?startPeriod=2016"

        payload={}
        headers = {
            'Accept': 'text/csv'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        urlData = response.content
        rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))

        print(rawData.head())

        return Response(rawData['DATAFLOW'][0])

