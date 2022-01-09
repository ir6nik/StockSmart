# By Carter Wong and Ronik Agarwal

from numpy import double
import yfinance as yf #importing API to pull data from 
ticker=yf.Ticker(str(input("Ticker: "))) #getting user input to find ticker
data=ticker.info #getting data
#assigning variables to use for analysis
rating=0
numofcriteria=17
currentprice=data['currentPrice']
profitmargins=data['profitMargins']
targetmedianprice=data['targetMedianPrice']
currentratio=data['currentRatio']
roe=data['returnOnEquity']
quickratio=data['quickRatio']
enterprisetorevenue=data['enterpriseToRevenue']
sharesoutstanding=data['sharesOutstanding']
sharesshort=data['sharesShort']
pb=data['priceToBook']
beta=data['beta']
payoutratio=data['payoutRatio']
earningsquarterlygrowth=data['earningsQuarterlyGrowth']
pegratio=data['pegRatio']
twohundreddayavg=data['twoHundredDayAverage']
volume=data['volume']
avgdailyvolumetenday=data['averageDailyVolume10Day']
fiftydayavg=data['fiftyDayAverage']
fiftytwoH=data['fiftyTwoWeekHigh']
fiftytwoL=data['fiftyTwoWeekLow']
#analysis
try:
    if profitmargins>=0.2:
        rating+=1
    elif profitmargins<=0.05:
        rating-=1
    if currentprice<targetmedianprice:
        rating+=1
    elif currentprice>targetmedianprice:
        rating-=1
    if currentratio>1:
        rating+=1
    elif currentratio<1:
        rating-=1
    if roe>0.15:
        rating+=1
    elif roe<0.15:
        rating-=1
    if quickratio>1:
        rating+=1
    elif quickratio<1:
        rating-=1
    if enterprisetorevenue>2:
        rating+=1
    elif enterprisetorevenue<0:
        rating-=1
    if sharesoutstanding/sharesshort<0.05:
        rating+=1
    elif sharesoutstanding/sharesshort>0.05:
        rating-=1
    if pb<2:
        rating+=1
    elif pb>5:
        rating-=1
    try:
        if beta>-0.05 and beta<0.05:
            rating+=1
        elif beta>0.75 or beta<-0.75:
            rating-=1
    except:
        print("no beta")
    if earningsquarterlygrowth>0:
        rating+=1
    elif earningsquarterlygrowth<0:
        rating-=1
    if pegratio<1:
        rating+=1
    elif pegratio>1:
        rating-=1
    if currentprice<twohundreddayavg:
        rating+=1
    elif currentprice>twohundreddayavg:
        rating-=1
    if payoutratio>0:
        rating+=1
    elif payoutratio<0:
        rating-=1
    if volume<avgdailyvolumetenday:
        rating+=1
    elif volume>avgdailyvolumetenday:
        rating-=1
    if currentprice<fiftydayavg:
        rating+=1
    elif currentprice>fiftydayavg:
        rating-=1
    if currentprice/fiftytwoH>2.5:
        rating+=1
    elif currentprice/fiftytwoH<1.5:
        rating-=1
    if currentprice/fiftytwoL<0.25:
        rating+=1
    elif currentprice/fiftytwoL>0.75:
        rating-=1
except:
    rating+=0
#rating
if rating>int(numofcriteria*0.5):
     print("Buy, rating: ",rating)
elif rating<int((numofcriteria*-1)*.5):
    print("Sell, rating:",rating)
else:
    print("Neutral, rating: ",rating)
