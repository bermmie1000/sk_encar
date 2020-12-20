from datetime import datetime, timedelta


def isPeriod(df_page):

    today = datetime.today()
    today_30 = today - timedelta(days=31)

    day_to_search = df_page["date"].min()

    condition = day_to_search > today_30

    return condition