SCH University Chatbot
=====================
순천향대 봇
----------------------


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version badge](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://shields.io/)
[![Add Friend badge](https://img.shields.io/badge/Add-Friend-yello.svg)](https://pf.kakao.com/_lxmrmC)

## 헬퍼스(HelpUs)
순천향대학교 창업 동아리 소속<br/>
<img src="images/Logo2.jpg" width="30%"></img>

Developing Team<br/>
- 김민수(컴퓨터 소프트웨어 공학과 17학번)<br/>
- 김도현(컴퓨터 공학과 18학번)<br/>

Design Team<br/>
- 김두연(디지털 애니메이션 학과 18학번)<br/>
- 김연수(디지털 애니메이션 학과 18학번)<br/>


## 제작자
[김민수](https://github.com/alstn2468)<br/>Soonchunhyang University<br/>Department of Computer Software Engineering<br/>
[ [Facebook](https://www.facebook.com/profile.php?id=100003769223078) ]
[ [Github](https://github.com/alstn2468) ]
[ [LinkedIn](https://www.linkedin.com/in/minsu-kim-336289160/) ]
[[Webpage](https://kimminsu.ml) ]<br/><br/>

[김도현](https://github.com/wookoo)<br/>Soonchunhyang University<br/>Department of Computer Science Engineering<br/>
[ [Facebook](https://www.facebook.com/profile.php?id=100008326148155) ]
[ [Github](https://github.com/wookoo) ]<br/>


## 개요
Python과 Django 웹 프레임워크를 사용하여 제작한 자동 응답형 카카오톡 챗봇입니다.<br/>
[(순천향대 봇)](https://pf.kakao.com/_lxmrmC)에서 친구 추가가 가능합니다.<br/>
순천향대 봇 다음 [문서](https://github.com/plusfriend/auto_reply)를 기반으로 제작되었습니다.<br/>

## 기술


### 언어
- Python (3.6.5)


### 프레임워크
- Django (2.0.5)


### 모듈
- beautifulsoup4 (4.6.0)
- certifi (2018.1.18)
- Django (2.0.5)
- folium (0.5.0)
- PyAutoGUI (0.9.36)
- pyowm (2.8.0)
- pytz (2018.4)
- requests (2.18.4)
- urllib3 (1.22)


### 서버
- Raspberry Pi 3b<br/>
- Ubuntu MATE


## 폴더 구조
```
├─ library_screenshot.py
└─ SCHChatBot
   ├─ db.sqlite3
   ├─ manage.py
   ├─ addon
   │  ├─ asanbus.py
   │  ├─ calander.py
   │  ├─ find_book.py
   │  ├─ student_food.py
   │  ├─ train.py
   │  └─ weather_edit.py
   ├─ app
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ views.py
   │  ├─ __pycache__
   │  └─ migrations
   ├─ data
   │  └─ food
   │      ├─ hyang1
   │      ├─ hyang2
   │      ├─ hyang3
   │      ├─ student
   │      └─ teacher
   └─ module
       ├─ apple.py
       ├─ buttons.py
       ├─ message.py
       ├─ process.py
       └─ __pycache__
```


## 기능


### 학식
- 월 ~ 토 요일별 `당일` 학식 메뉴 확인 가능<br/>
- 조식, 중식, 석식 한번에 확인 가능<br/>
- 학식이 없는 경우도 표시<br/>
- 식당 이용 가능 시간 확인 가능<br/>
- `일부` 식당 학식 가격 확인 가능<br/>


### 도서관
- 도서관 도서 검색 가능<br/>
- 열람실 좌석 확인 가능<br/>
- 도서관 이용 정보 확인 가능<br/>


### 교통
- 학교 주변 시내버스 정보 확인 가능<br/>
- 순천향대학교 -> 신창역 셔틀 버스 정보 확인 가능<br/>
- 신창역 지하철 출발 시간 확인 가능<br/>
- 신창 택시 연락처 정보 확인 가능<br/>
- 신창 시외버스 터미널 정보 확인 가능<br/>


### 날씨
- 신창면 `현재`날씨 확인 가능<br/>
- 현재 날씨, 현재 기온, 최고 기온, 최저 기온<br/>
오존, 미세먼지, 초미세먼지, 아황산 가스,<br/>
일산화탄소, 이산화탄소 정보 확인 가능<br/>


### WI-FI
- 교내 와이파이 사용 정보 확인 가능


### 순천향대학교 건물
- 학교 지도 확인 가능<br/>
- 학교 건물 번호 확인 가능<br/>
- 교내 편의 시설 확인 가능<br/>


### 보건실
- 보건실 위치, 이용 가능 시간 확인 가능<br/>
- 체성분 측정 가능 시간 확인 가능<br/>


## 버전
2018/05/13<br/>
- Version (1.0.0) Released<br/>

## 친구 추가 방법
