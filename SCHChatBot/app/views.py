from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request
from addon import student_food
from addon import train
from addon import find_book
from addon import weather_edit
from addon import asanbus
from addon import calander
from module.buttons import *
from module import process
from module.message import *
import time

# =================== process.py (사용자에게 전달할 내용 모듈) ================

# process.Json_Return(msg,buttons)
# 사용자에게 전송할 정보가 메세지, 키보드일경우
# msg = 전달할 메세지 / buttons = 전달할 키보드 값
# 두가지를 인수로 받는다.

# process.Json_Map_Return(msg,url)
# 사용자에게 전송할 정보가 건물 정보일때 사용
# msg = 전달할 메세지 / url = 전달할 이미지의 이름
# 두가지를 인수로 받는다. 반환해주는 buttons 는 building_button 버튼

# process.Json_Error_Return(msg)
# 사용자에게 전송할 정보가 도서관 책 검색 내역일떄 사용
# msg = 전달할 메세지
# 사용자에게 받은 메세지 타입이 (사진, 메세지, 음성 등) 무엇인지에 따라 오류처리를 해야함
# 반환해주는 buttons 타입은 text 로 사용자가 입력 가능한 내용
# 사용 내역은 ==디버깅== 항목 아래에서 찾을수 있음

# process.Json_Library_Return(msg, url)
# 사용자에게 전송할 정보가 도서관 좌석 정보일떄 사용
# msg = 전달할 메세지 / url = 장소 이름으로 전달할 사진 이름
# msg, url 을 인수로 받고 반환해주는 버튼은 reading_zone_button 버튼

# =============================================================================

# =================== buttons.py (버튼 리스트 모듈) ===========================

# weeks = ('mon','tue','wen','thu','fri','sat','sun')
# library_button = ['도서검색','열람실 좌석 보기','처음으로']
# reading_zone_button = ['제1 열람실','제2 열람실','제3 열람실','멀티존','인터넷존','프리미어존','처음으로']
# basic_button = ['학식 정보','도서관 서비스','교통 정보','신창 날씨','건물정보','보건실 이용시간','처음으로','문의하기']
# school_food_button = ['향설 1관','향설 2관','향설 3관','학생회관','교직원 식당','처음으로']
# building_button = ['편의시설 위치','학교 지도','학교 건물 번호','처음으로']
# traffic_button = ['신창행 버스','신창역 기차 출발 시간','신창 시외버스 터미널 시간표','처음으로']

#==============================================================================

# =================== times.py (시간 관련 모듈) ===============================

# times.now_day() / 오늘 요일을 확인 후 mon,tue,wen,thu,fri,sat,sun 문자로 반환
# times.now_time_hour() / 현재 시를 24 단위로 반환 Ex : 오후 1시면 13 , 자정이면 0반환
# times.now_time_minute() / 현재 시를 제외한 분을 반환 EX : 1시 50분이면 50 반환
# times.now_time_for_min() / 현재 시와 분을 분으로 표기하여 반환
# EX : 13시 50분이면 (13 * 60) + 50 을 하여  830 반환

# =============================================================================


# =================== train.py (전철, 버스 모듈) ==============================

# train.train_time() 반환되는 정보는 다음과 같다
# 주말인지 평일인지 구별을 하고 그에 맞는 조건식을 실행을 한다
# 반환되는 정보는 리스트 형으로 반환된다.
# first_time ( 출발 남은 시간), first_goal (가장 빠른 기차의 어디 행 열차 )
# second_time ( 두번쨰로 빠른 기차 남은 시간) , second_goal (두번쨰 빠른 기차 목적지)

# train.bus_time() 은 신창역에서 출발하는 기차의 시간을 기준으로
# 주말이닞 평일인지 구별을 하고 그에 맞는 조건식을 실행을 한다.
# 반환되는 정보는 문자열 형으로
# 가장 빨리 출발하는 기차 시간 - 10, -5 을 하여 빠른 시간내로 출발하는 버스의 남은 시간,
# 그 다음 시간내로 출발하는 버스의 남은 시간을 알려준다
# 남은 시간이 0 분일 경우 다음 기차를 고려하여 남은 시간을 알려준다.

# =============================================================================

def keyboard(request):
    return JsonResponse(
        {
            'type': 'buttons',
            'buttons' : basic_button
        }
    )

@csrf_exempt
def message(request):


    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    type_name = received_json['type']

#===================도서관 좌석보기 ================================
    if content_name == '• 도서관':
        msg = '• 도서관에 관한 정보를 확인하실 수 있습니다.\n• 원하는 버튼을 눌러주세요.'
        return process.JsonReturn(msg,library_button)

    elif content_name == '• 도서관 이용 정보':
        return process.JsonReturn(library_info_msg,library_button)

    elif content_name == '• 열람실 좌석 확인':
        msg = content_name+' 항목입니다. \n좌석을 볼때 오류가 많으니 가급적 전송해주는 링크에 접속하여 정확하게 확인해주세요.\n갱신 주기는 15초 내외입니다.'
        return process.JsonReturn(msg,reading_zone)

    elif content_name == '• 제 1 열람실':
        return process.JsonLibraryReturn(first_reading_msg ,'first',1060,502)

    elif content_name == '• 제 2 열람실':
        return process.JsonLibraryReturn(second_reading_msg,'second',1059,458)

    elif content_name == '• 제 3 열람실':
        return process.JsonLibraryReturn(third_reading_msg,'third',1053,406)

    elif content_name == '• 멀티존':
        return process.JsonLibraryReturn(multi_reading_msg,'multi',565,282)

    elif content_name == '• 인터넷존':
        return process.JsonLibraryReturn(internet_reading_msg,'internet',168,436)

    elif content_name == '• 프리미어존':
        return process.JsonLibraryReturn(pre_reading_msg,'pre',294,281)

    elif content_name == '• 처음으로' or content_name == '처음으로' :
        msg = '• 처음으로 돌아갑니다.'
        return process.JsonReturn(msg,basic_button)
    elif content_name == '• 문의사항':
        return process.JsonReturn(developer_question_msg,basic_button)
#==================날씨코드==================
    elif content_name == '• 날씨':
        msg = weather_edit.weather()
        return process.JsonReturn(msg,basic_button)

#=======================학식 구현 코드===========
    elif content_name == '• 학식':
        msg ='• 학식에 관한 정보를 확인 하실수 있습니다.\n• 원하는 식당을 선택하세요.'
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 1 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 향설 1 관 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 2 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 향설 2 관 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 향설 3 관':
        msg = student_food.hak(content_name)
        msg = calander.calander() +'\n■ 향설 3 관 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 학생회관':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 학생회관 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)

    elif content_name == '• 교직원 식당':
        msg = student_food.hak(content_name)
        msg = calander.calander() + '\n■ 교직원 식당 학식 정보 ■\n\n' + msg
        return process.JsonReturn(msg,food)
    
    elif content_name == '• 학식 이용 시간':
        return process.JsonReturn(student_food_info_msg,food)
    

#교통정보 구현 =====================================
    elif content_name == '• 교통':
        msg = '학교에서 탑승하실수 있는 교통수단 정보입니다.'
        return process.JsonReturn(msg,ride)

    elif content_name == '학내순환 버스':

        nows = time.localtime()
        times = (int(nows.tm_hour)*60)+int(nows.tm_min)
        today_da = weeks[nows.tm_wday]

        if (times < 500 or times > 1080 or today_da =='sun' or today_da =='sat'):
            msg = '현재 학내 순환 버스가 운행중이지 않습니다.\n학내순환 버스는 평일 8:00 ~ 18:00 까지 운행합니다.'
            return process.JsonReturn(msg,ride)

        else:
            msg = '파란 핀은 정류소, 빨간 핀은 버스 위치입니다.\n현재 시범운행 진행중이기 때문에 버스 위치가 승강장에서 멈춰 있을수 있습니다. 그러나 운행은 정상적으로 되고 있는거에요.\n새로고침을 하시면 새 정보를 확인 가능합니다.\n http://bit.ly/2s41M7x'
            return process.JsonReturn(msg,ride)


    elif content_name == '• 순천향 대학교 → 신창역':
        nows = time.localtime()
        times = (int(nows.tm_hour)*60)+int(nows.tm_min)
        today_da = weeks[nows.tm_wday]
        if (times < 655 or times >  1349 or today_da == 'sat') and (today_da != 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg,ride)

        elif (times < 890 or times >  1360) and (today_da == 'sun'):
            return process.JsonReturn(bus_to_sin_error_msg,ride)

        else:
            msg = train.bus_time()
            msg = msg
            return process.JsonReturn(msg,ride)

    elif content_name == '• 신창역 지하철 출발시간':
        minute = train.train_time()
        msg = '■ 신창역 지하철 출발 시간 ■\n\n• 이번 지하철은 ' + str(minute[0]) +'분 후 출발 예정입니다. (' + minute[1] + '행)\n• 다음 지하철은 '+str(minute[2])+  '분 후 출발 예정입니다. (' + minute[3] + '행)\n\n• 지하철 시간표 데이터로 정보를 제공합니다.\n• 참고용으로만 사용해주세요.'
        return process.JsonReturn(msg,ride)

    elif content_name == '• 신창 시외버스 터미널':
        msg = '■ 신창 시외버스 터미널 ■\n\n• 사진을 크게 보실려면 아래 링크로 접속하세요.\n• http://bit.ly/2KXYBa3'
        return JsonResponse(
            {
                'message': {
                    'text': msg,
                    'photo':{
                        'url': 'http://211.229.250.54/photo/bus.jpg',
                        'width': 1280,
                        'height':1162

                }},
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ride
                }
            }
        )
    elif content_name == '• 학교 주변 시내버스':
        msg = '• 학교 주변에서 탑승하실수 있는 버스 정보 입니다.'
        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 순천향대학교 후문 (신창초 방향)':
        xml = asanbus.get_xml(288001690)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 순천향대학교 후문 (신창초) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404 
        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 순천향대학교 후문 (경희학성 방향)':
        xml = asanbus.get_xml(288001691)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000244',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 순천향대학교 후문 (경희학성) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 경희학성아파트 (순천향대 후문 방향)':
        xml = asanbus.get_xml(288000362)
        xml = asanbus.xml_checker(xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 경희학성 (순천향대후문) ■\n\n'
        msg = msg + bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 경희학성아파트 (창암1리 방향)':
        xml = asanbus.get_xml(288001578)
        xml = asanbus.xml_checker(xml)
        bus_350 = asanbus.start(350,'ASB288000240',xml)
        bus_352 = asanbus.start(352,'ASB288000041',xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 경희학성 (창암1리) ■\n\n'
        msg = msg + bus_350 + '\n\n'+ bus_352 + '\n\n'+ bus_402+ '\n\n'+ bus_403+ '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 순천향대학교 (와신1리 방향)':
        xml = asanbus.get_xml(288010276)
        xml = asanbus.xml_checker(xml)
        bus_430 = asanbus.start(430,'ASB288000048',xml)
        bus_450 = asanbus.start(450,'ASB288000050',xml)
        bus_451 = asanbus.start(451,'ASB288000051',xml)
        msg = '■ 순천향대학교 (외산1리) ■\n\n'
        msg = msg + bus_430 + '\n\n'+ bus_450 + '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop)
    
    elif content_name == '• 순천향대학교':
        xml = asanbus.get_xml(288000377)
        xml = asanbus.xml_checker(xml)
        bus_400 = asanbus.start(400,'ASB288000243',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        bus_450 = asanbus.start(450,'ASB288000248',xml)
        bus_451 = asanbus.start(451,'ASB288000249',xml)
        msg = '■ 순천향대학교 ■\n\n'
        msg = msg + bus_400 + '\n\n'+ bus_404 + '\n\n'+ bus_450+ '\n\n'+ bus_451

        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 신창역 (행목 1리 방향)':
        
        xml = asanbus.get_xml(288001943)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start(32,'ASB288000189',xml)
        bus_41 = asanbus.start(41,'ASB288000246',xml)
        bus_41_1 = asanbus.start('41-1','ASB288000300',xml)
        bus_402 = asanbus.start(402,'ASB288000244',xml)
        bus_403 = asanbus.start(403,'ASB288000245',xml)
        bus_404 = asanbus.start(404,'ASB288000246',xml)
        msg = '■ 신창역 (행목 1리) ■\n\n'
        msg = msg + bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404

        return process.JsonReturn(msg,bus_stop)

    elif content_name == '• 신창역 (행목리 방향)':
        xml = asanbus.get_xml(288001942)
        xml = asanbus.xml_checker(xml)
        bus_32 = asanbus.start(32,'ASB288000297',xml)
        bus_41 = asanbus.start(41,'ASB288000191',xml)
        bus_41_1 = asanbus.start('41-1','ASB288000192',xml)
        bus_402 = asanbus.start(402,'ASB288000044',xml)
        bus_403 = asanbus.start(403,'ASB288000045',xml)
        bus_404 = asanbus.start(404,'ASB288000209',xml)
        msg = '■ 신창역 (행목리) ■\n\n'
        msg = msg + '\n'+ bus_32 + '\n\n'+ bus_41 + '\n\n'+ bus_41_1 + '\n\n'+ bus_402 + '\n\n'+ bus_403 + '\n\n'+ bus_404
        return process.JsonReturn(msg,bus_stop)
#건물 정보 파트 ===============================================
    elif content_name == '• 순천향 건물':
        msg = '• 학교 건물 정보를 확인하실수 있습니다.'
        return process.JsonReturn(msg,building)

    elif content_name == '• 편의시설':
        return process.JsonMapReturn(building_comfortable_msg,'builging_a',1216,1294)

    elif content_name == '• 학교 지도':
        return process.JsonMapReturn(school_map_msg,'map',1280,719)

    elif content_name == '• 학교 건물 번호':
        return process.JsonMapReturn(building_number_msg,'builging_b',1280,1280)

#도서검색 파트 =================================================

    elif content_name == '• 도서 검색':
        return process.JsonErrorReturn(search_book_msg)

#보건실 이용시간 정보=========================================
    elif content_name == '• 보건실':
        return process.JsonReturn(health_room_msg,basic_button)

    elif content_name == '• WI-FI':
        return process.JsonReturn(wifi_msg,basic_button)
#택시 정보====================================
    elif content_name == '• 신창 택시 연락처 정보':
        return process.JsonReturn(taxi_msg,ride)

#미구현 상태 =====================
    elif content_name == '• 학사일정':
        return process.JsonReturn(ready_msg,basic_button)


#디버깅===================================================
    else:
        if type_name == 'photo':
            msg = '• 사진이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'video':
            msg = '• 영상이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'audio':
            msg = '• 음성 파일이 아닌 도서 제목을 입력하세요.'
            return process.JsonErrorReturn(msg)

        elif type_name == 'text':
            content_name2 = content_name.replace(" ","+")
            msge = find_book.result_book(content_name)
            research = "■ 도서관 도서 검색 ■\n\n• '"+ content_name + ' 에 대한 도서 검색 결과 입니다.\n• '+str(msge)
            search_url = 'https://library.sch.ac.kr/search/caz/result?st=KWRD&si=TOTAL&q='+content_name2+'&folder_id=null'
            msg = research + '\n• ' + search_url
            return process.JsonReturn(msg,library_button)



# Create your views here.
