def calander():
    import time
    now = time.localtime()
    weeks = ('월요일','화요일','수요일','목요일','금요일','토요일','일요일')
    year = now.tm_year
    month = str(now.tm_mon)
    date = str(now.tm_mday)
    day = weeks[now.tm_wday]
    if len(month) == 1 :
        month = "0" + month
    if len(date) == 1 :
        date = "0" + date
    return (str(year) + '년 '+ str(month) + '월 ' + str(date) + '일 ' + day)
