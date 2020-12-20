from datetime import datetime, timedelta


def isPeriod(df_page):

    today = datetime.today()
    today_30 = today - timedelta(days=31)

    day_to_search = df_page["date"].min() # <--- "date"를 빼는게 좋을 것 같다

    condition = day_to_search > today_30

    return condition