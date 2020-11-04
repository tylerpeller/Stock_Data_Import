from datetime import datetime
import numpy as np
import pandas_datareader.data as web
import pandas as pd
import os
import time as t
import sys


#Go to Alpha Vantage website to recieve your free API key and fill in the key into the "" marks below
API_Key = ""        #Insert your API key here

def FillDatareader (ticker,startdate, enddate):

    Stock = web.DataReader(ticker, "av-daily", startdate,enddate, api_key=API_Key)
    return Stock

def UserValues():
    stocks_to_add=[]
    stock_tickers=[]
    add=True
    average = input('For this data would you like (1) daily average or (2) daily adjusted average? [1/2]: ')
    if(average=="1"):
        average = 'av-daily'
    elif(average=="2"):
        average='av-daily-adjusted'
    else:
        print ("invalid type. Please run again")
        sys.exit()

    # add a do while (equivalent) to do first and then check condition of if they want another input
    while (add):
        ticker = input("What ticker symbol would you like to look up? ")
        start = input("What start date would you like? [dd/mm/yyyy] :")
        end = input("What end date would you like? [dd/mm/yyyy]: ")
        try:
            day1 = int(start.split("/")[0])
            month1 = int(start.split("/")[1])
            year1= int(start.split("/")[2])
            day2 = int(end.split("/")[0])
            month2 = int(end.split("/")[1])
            year2= int(end.split("/")[2])
        except:
            print("invalid input,try again")
            continue

        try:
            value =FillDatareader(ticker,datetime(year1,month1,day1),datetime(year2,month2,day2))
            stocks_to_add.append(value)
            stock_tickers.append(ticker)
        except:
            print("error retrieving, try again")
        
        next_ = input("would you like to add another stock [y/n] ?")
        if (next_ ==  'n'):
            add = False



    return stocks_to_add,stock_tickers,valid



new_stocks,tiks,valid = UserValues()


# for i in new_stocks:
#     print(i.head(5))

filename = input("Plase gove a name to your excel file (without extension)")
filename += ".xlsx"
with pd.ExcelWriter(filename) as writer: 
    for i in range(len(new_stocks)):
        new_stocks[i].to_excel(writer, sheet_name = tiks[i])

print("excel file has been saved in path" + os.getcwd() + filename)
t.sleep(10.0)
print("Goodbye")
t.sleep(10.0)


