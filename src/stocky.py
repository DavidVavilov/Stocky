import yfinance 
import datetime


'''
Idea - 
Create a Discord bot that gives stock info and notifies when stock falls or gets up
'''
def getStocks(company):
   data = yfinance.download(company, start="2020-08-01", end="2020-08-20")
   dataList = list(data["Close"])
   dateKeyList = list(data["Close"].keys())
   dateList = []
   lastDateList = []
   for dateKey in dateKeyList:
      date_time_obj = dateKey.to_pydatetime()
      dateList.append(str(date_time_obj))
   
   for date in dateList:
      lastDateList.append(date[:10])

   return (dataList, lastDateList)

def todayStock(company):
   data = yfinance.Ticker(company)
   dat = data.history()
   before = dat.tail(2)['Close'][0]
   last_quote = dat.tail(1)['Close']
   
   price = last_quote[0]
   if(before > price):
      emote = ":arrow_down:"
   else:
      emote = ":arrow_up:"

   date = str(list(dat.tail(1)['Close'].keys().to_pydatetime())[0])[:10]
   
   return (date, price, emote)


