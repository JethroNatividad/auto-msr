from pytrends.request import TrendReq

def get_trending():
    pytrends = TrendReq(hl='en-PH', tz=480)
    trending = pytrends.trending_searches(pn='philippines')

    trending_list = []
    for trend in trending[0]:
        trending_list.append(trend)
    return trending_list

