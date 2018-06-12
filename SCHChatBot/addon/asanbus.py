import urllib.request
from bs4 import BeautifulSoup
import re
def get_xml(stop_id):
    url = 'http://openapi.tago.go.kr/openapi/service/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList?serviceKey='
    url = url + str(stop_id)
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
    error_checker = text.find('<item>')
    soup = BeautifulSoup(text, 'html.parser')
    if error_checker != -1:
        items = soup.find_all('item')
        return items
    else:
        return None

def parsing(line_number,bus_id,xml):
    index = 0
    for s in xml :
        s = str(s)
        if bus_id in s:
            index = index
            break
        else:
            index = index + 1

    if len(xml) != index:
        need_parsing = str(xml[index])
        soup = BeautifulSoup(need_parsing,'html.parser')
        arrprevstationcnt = soup.find_all('arrprevstationcnt')
        arrtime = soup.find_all('arrtime')
        arrprevstationcnt = str(re.sub('<.+?>', '', str(arrprevstationcnt[0])))
        arrtime = str( int(re.sub('<.+?>', '', str(arrtime[0]))) // 60 )
        return ('• ' + str(line_number) +'번 버스\n약 ' + arrtime + '분 후 도착예정 (' + arrprevstationcnt + '개 전 정류장)')
    else:
        return ('• ' + str(line_number) +'번 버스\n현재 배차 된 버스가 없습니다.')

def start(line_number,bus_id,xml):
    if xml == []:
        return '• ' + str(line_number) +'번 버스\n현재 배차 된 버스가 없습니다.'

    else:
        return parsing(line_number,bus_id,xml)

def xml_checker ( xml ) :
    if xml == None :
        xml = []
    else :
        xml = list(xml)
    return xml
