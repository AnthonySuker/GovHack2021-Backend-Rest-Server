from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

import requests
import io
import pandas as pd

#help debt by age bracket
dataHelpByAge=0
#Aus income by LGA (we're just getting the mean value)
ausIncome=0
#Help debt repayments based on income
dataHelpRepay=0

def getData():
    global dataHelpByAge, ausIncome, dataHelpRepay
    dataHelpByAge = pd.read_csv('govhacksite/rsc/HelpStats.csv')
    dataHelpRepay = pd.read_csv('govhacksite/rsc/HelpRepaymentByIncome.csv')

    print(dataHelpByAge)
    #Australia mean income
    url = "https://api.data.abs.gov.au/data/ABS,ABS_REGIONAL_LGA2020/INCOME_2+INCOME_21+HELP_2+LF_6+LF_3+ERP_P_20+ERP_23...?startPeriod=2016"
    payload={}
    headers = {
        'Accept': 'text/csv'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    urlData = response.content
    ausIncome = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    print('data loaded')
    

class getHelpDebtComparison(APIView):
    def get(self,request):
        global dataHelpByAge
        userAge = request.data['age']

        for index, row in dataHelpByAge.iterrows():
            if int(userAge) > int(row['hiAge']):
                continue
            else:
                return Response(row.Debt)


        return Response(False)

class getHelpRepayments(APIView):
    def get(self,request):
        global dataHelpRepay
        userIncome = request.data['income']

        for index, row in dataHelpByAge.iterrows():
            if int(userIncome) > int(row['RIH']):
                continue
            else:
                return Response(row.RR)


        return Response(False)


# class getDebtAvg(APIView):


