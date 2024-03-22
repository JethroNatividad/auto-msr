from pytrends.request import TrendReq

# PH
# Limit 
pytrends = TrendReq(hl='en-PH', tz=480)
trending = pytrends.trending_searches(pn='philippines')

# convert trending dataframe to list
for trend in trending[0]:
    print(trend)