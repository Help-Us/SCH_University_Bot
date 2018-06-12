SCH University Chatbot
=====================
순천향대 봇
----------------------
<br/>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Generic badge](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://shields.io/)
<br/>

## 헬퍼스(HelpUs)
순천향대학교 창업 동아리 소속<br/>
<img src="images/Logo2.jpg" width="30%"></img>

Developing Team<br/>
- 김민수(컴퓨터 소프트웨어 공학과 17학번)<br/>
- 김도현(컴퓨터 공학과 18학번)<br/>

Design Team<br/>
- 김두연(디지털 애니메이션 학과 18학번)<br/>
- 김연수(디지털 애니메이션 학과 18학번)<br/>
<br/>


## 제작자
[김민수](https://github.com/alstn2468)<br/>Soonchunhyang University<br/>Department of Computer Software Engineering<br/>
[ [Facebook](https://www.facebook.com/profile.php?id=100003769223078) ]
[ [Github](https://github.com/alstn2468) ]
[ [LinkedIn](https://www.linkedin.com/in/minsu-kim-336289160/) ]
[[Webpage](https://kimminsu.ml) ]<br/><br/>

[김도현](https://github.com/wookoo)<br/>Soonchunhyang University<br/>Department of Computer Science Engineering<br/>
[ [Facebook](https://www.facebook.com/profile.php?id=100008326148155) ]
[ [Github](https://github.com/wookoo) ]<br/>
<br/>


## 개요
Python과 Django 웹 프레임워크를 사용하여 제작한 자동 응답형 카카오톡 챗봇입니다.<br/>
[(순천향대 봇)](https://pf.kakao.com/_lxmrmC)에서 친구 추가가 가능합니다.<br/>
순천향대 봇 다음 [문서](https://github.com/plusfriend/auto_reply)를 기반으로 제작되었습니다.<br/>
<br/>

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
<br/>


## 구조
```
├─ library_screenshot.py
├─ upload.txt
│
└─ SCHChatBot
   ├─ db.sqlite3
   ├─ manage.py
   │
   ├─ addon
   │  ├─ asanbus.py
   │  ├─ calander.py
   │  ├─ find_book.py
   │  ├─ student_food.py
   │  ├─ train.py
   │  └─ weather_edit.py
   │
   ├─ app
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ views.py
   │  ├─ __pycache__
   │  └─ migrations
   │
   ├─ data
   │  └─ food
   │      ├─ hyang1
   │      │   ├─ mon.txt
   │      │   ├─ tue.txt
   │      │   ├─ wen.txt
   │      │   ├─ thu.txt
   │      │   ├─ fri.txt
   │      │   ├─ sat.txt
   │      │   └─ sun.txt
   │      │
   │      ├─ hyang2
   │      │   ├─ mon.txt
   │      │   ├─ tue.txt
   │      │   ├─ wen.txt
   │      │   ├─ thu.txt
   │      │   ├─ fri.txt
   │      │   ├─ sat.txt
   │      │   └─ sun.txt
   │      │
   │      ├─ hyang3
   │      │   ├─ mon.txt
   │      │   ├─ tue.txt
   │      │   ├─ wen.txt
   │      │   ├─ thu.txt
   │      │   ├─ fri.txt
   │      │   ├─ sat.txt
   │      │   └─ sun.txt
   │      │
   │      ├─ student
   │      │   ├─ mon.txt
   │      │   ├─ tue.txt
   │      │   ├─ wen.txt
   │      │   ├─ thu.txt
   │      │   ├─ fri.txt
   │      │   ├─ sat.txt
   │      │   └─ sun.txt
   │      │
   │      └─ teacher
   │          ├─ mon.txt
   │          ├─ tue.txt
   │          ├─ wen.txt
   │          ├─ thu.txt
   │          ├─ fri.txt
   │          ├─ sat.txt
   │          └─ sun.txt
   │      
   └─ module
       ├─ apple.py
       ├─ buttons.py
       ├─ message.py
       ├─ process.py
       └─ __pycache__
```

## 기능


## 버전
2018/05/13<br/>
- Version (1.0.0) Released<br/>
