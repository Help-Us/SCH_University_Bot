def goals_week(line):
    if line == 578 or line == 897 or line == 1219:
        where = '용산(급)'
    elif line == 1267 or line == 1390:
        where = '병점'
    elif line == 1305 or line == 1335:
        where = '구로'
    elif line == 1342 or line == 1420 or line == 8:
        where = '천안'
    else:
        where = '청량리'
    return where

def goals(line):
    if line == 365 or line == 389 or line == 1268:
        where = '광운대'
    elif line == 433:
        where = '서울역(급)'
    elif line == 470 or line == 1030 or line == 1230:
        where = '용산(급)'
    elif line == 488 or line == 530 or line == 770 or line == 1220 or line == 1390:
        where = '병점'
    elif line == 1305 or line == 1330 or line == 1349:
        where = '구로'
    elif line == 1427 or line == 9:
        where = '천안'
    else:
        where = '청량리'
    return where

def train_time():
    import time
    now = time.localtime()
    week = ('mon','tue','wen','thu','fri','sat','sun')
    today = week[now.tm_wday]
    time = (int(now.tm_hour)*60)+int(now.tm_min)
    if today == 'sun' or today == 'sat':
        train_list = [8,330,375,401,433,460,482,520,556,578,598,622,656,694,739,781,814,859,897,928,949,977,1022,1062,1093,1126,1145,1162,1186,1219,1244,1267,1305,1335,1353,1390,1420]
        for line in train_list:
            if time > 1420:
                first_time = abs(time - 1448)
                first_goal = goals_week(8)
                second_time = abs(time-(330+1440))
                second_goal = goals_week(330)
                break
            else:
                if time < line:
                    time_where = train_list.index(line) + 1
                    first_time = (line-time)
                    first_goal = goals_week(line)
                    second_time = train_list[time_where] - time
                    second_goal = goals_week(train_list[time_where])
                    break
    else:
        train_list=[9,318,365,389,420,433,470,488,501,530,580,598,640,675,693,718,739,770,780,817,859,902,931,979,1030,1059,1093,1125,1145,1162,1197,1220,1230,1268,1305,1330,1349,1390,1427]
        for line in train_list:
            if time > 1390:
                first_time = abs(time - 1449)
                first_goal = goals(9)
                second_time = abs(time - 1758)
                second_goal = goals(318)
                break
            else:
                if time < line:
                    time_where = train_list.index(line) + 1
                    first_time = line-time
                    first_goal = goals(line)
                    second_time = train_list[time_where] - time
                    second_goal = goals(train_list[time_where])
                    break
    return first_time,first_goal,second_time,second_goal
def bus_time():
    bus = train_time()
    first_bus = int(bus[0]) - 10
    second_bus = int(bus[0]) - 5
    if first_bus <=  0 and second_bus >= 0:
        return '■ 순천향대학교 →  신창역 ■\n\n• 이번 버스는 ' + str(second_bus) + '분 후 출발 예정입니다.\n• 다음 버스는 '+ str(int(bus[2]) - 10 ) + '분 후 출발 예정입니다.'
    elif first_bus >= 0:
        return '■ 순천향대학교 →  신창역 ■\n\n• 이번 버스는 ' + str(first_bus) + '분 후 출발 예정입니다.\n• 다음 버스는 '+ str(second_bus ) + '분 후 출발 예정입니다.'
    elif first_bus <= 0 and second_bus <= 0:
        return '■ 순천향대학교 →  신창역 ■\n\n• 이번 버스는 ' + str(int(bus[2]) - 10) + '분 후 출발 예정입니다.\n• 다음 버스는 '+ str(int(bus[2]) - 5 ) + '분 후 출발 예정입니다.'
