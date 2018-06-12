import time
def hak(food_name):
    if food_name == '• 향설 1 관':
        food_name = 'hyang1'
    elif food_name =='• 향설 2 관':
        food_name = 'hyang2'
    elif food_name =='• 향설 3 관':
        food_name = 'hyang3'
    elif food_name == '• 학생회관':
        food_name = 'student'
    elif food_name == '• 교직원 식당':
        food_name = 'teacher'
    now = time.localtime()
    week = ('mon','tue','wen','thu','fri','sat','sun')
    today = week[now.tm_wday]
    today = '/kakobot/test/data/food/'+food_name+'/'+today+'.txt'
    file = open(today)
    a = file.read()
    file.close()
    return a
