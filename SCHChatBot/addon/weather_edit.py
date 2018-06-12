#import korean
import pyowm

def weather_parshing(API_KEY):
    City_ID = 1839726
    owm = pyowm.OWM(API_KEY)
    obs = owm.weather_at_id(City_ID)
    w = obs.get_weather()
    temperature = w.get_temperature(unit='celsius')
    humidity = w.get_humidity()  #습도
    humidity = '현재 습도 : ' + str(humidity) + ' %' #습도 퍼센트
    cloud = w.get_clouds()
    cloud = '구름 퍼센트 : ' + str(cloud) + ' %' #구름 퍼센트
    high_temp ='최고 기온 : ' + str( temperature['temp_max'] ) + ' ℃'#최고기온
    low_temp ='최저 기온 : ' + str( temperature['temp_min'] ) + ' ℃'#최저기온
    now_temp = '현재 기온 : ' + str( temperature['temp'] ) + ' ℃' #현재 기온
    now_sky = w.get_status()
    now_sky = now_sky.replace("Clear","맑음")
    now_sky = now_sky.replace("Clouds","구름")
    now_sky = now_sky.replace("Rain","비")
    now_sky = now_sky.replace("Haze","안개")
    now_sky = '현재 날씨 : ' + now_sky
    air = air_status()
    result = '■ 충남 아산시 신창면 날씨 ■\n\n• '+now_sky + '\n• ' + now_temp  + '\n• ' + high_temp + '\n• ' + low_temp
    result = result + air
    return result

def weather():
    try :
        return weather_parshing('')

    except:
        return weather_parshing('')

def air_status():
    import urllib.request
    from bs4 import BeautifulSoup
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=&pageSize=999&pageNo=1&startPage=1&sidoName=%EC%B6%A9%EB%82%A8&ver=1.3'
    page = urllib.request.urlopen(url)
    text = page.read().decode('utf8')
    soup = BeautifulSoup(text, 'html.parser')
    error_checker = text.find('도고면')
    if error_checker != -1:
        items = soup.find_all('item')
        items = list(items)
        index = 0
        for s in items:
            s = str(s)
            if s.find('도고면') != -1:
                index = index
                break
            else:
                index = index + 1

        if len(items) != index:
            need_parsing = str(items[index])
            start_so2value = need_parsing.find('<so2value>')
            end_so2value = need_parsing.find('</so2value>')
            so2value = need_parsing[start_so2value + len('<so2value>') : end_so2value]
            start_covalue = need_parsing.find('<covalue>')
            end_covalue = need_parsing.find('</covalue>')
            covalue = need_parsing[start_covalue + len('<covalue>') : end_covalue]
            start_o3value = need_parsing.find('<o3value>')
            end_o3value = need_parsing.find('</o3value>')
            o3value = need_parsing[start_o3value + len('<o3value>') : end_o3value]
            start_no2value = need_parsing.find('<no2value>')
            end_no2value = need_parsing.find('</no2value>')
            no2value = need_parsing[start_no2value + len('<no2value>') : end_no2value]
            start_pm10value = need_parsing.find('<pm10value>')
            end_pm10value = need_parsing.find('</pm10value>')
            pm10value = need_parsing[start_pm10value + len('<pm10value>') : end_pm10value]
            start_pm25value = need_parsing.find('<pm25value>')
            end_pm25value = need_parsing.find('</pm25value>')
            pm25value = need_parsing[start_pm25value + len('<pm25value>') : end_pm25value]
            #print(so2value) #아황산가스
            #print(covalue) #일산화탄소 농도
            #print(o3value) #오존농도
            #print(no2value) #이산화질소
            #print(pm10value) #미세먼지
            #print(pm25value) #초 미세먼지
            so2valu = float(so2value)
            covalu = float(covalue)
            o3valu = float(o3value)
            no2valu = float(no2value)
            pm10valu = float(pm10value)
            pm25valu = float(pm25value)
            so2 = ''
            co = ''
            o3 = ''
            pm10 = ''
            pm25 = ''
            if so2valu > 0.15 :
                so2 = '매우나쁨'
            elif so2valu > 0.05:
                so2 = '나쁨'
            elif so2valu > 0.02:
                so2 = '보통'
            else :
                so2 = '좋음'

            if covalu > 15 :
                co = '매우나쁨'
            elif covalu > 9:
                co = '나쁨'
            elif covalu > 2:
                co = '보통'
            else :
                co = '좋음'

            if o3valu > 0.15 :
                o3 = '매우나쁨'
            elif o3valu > 0.09:
                o3 = '나쁨'
            elif o3valu > 0.03:
                o3 = '보통'
            else :
                o3 = '좋음'

            if no2valu > 0.2 :
                no2 = '매우나쁨'
            elif no2valu > 0.06:
                no2 = '나쁨'
            elif no2valu > 0.03:
                no2 = '보통'
            else :
                no2 = '좋음'

            if pm10valu > 150 :
                pm10 = '매우나쁨'
            elif pm10valu > 80:
                pm10 = '나쁨'
            elif pm10valu > 30:
                pm10 = '보통'
            else :
                pm10 = '좋음'

            if pm25valu > 75 :
                pm25 = '매우나쁨'
            elif pm25valu > 35:
                pm25 = '나쁨'
            elif pm25valu > 15:
                pm25 = '보통'
            else :
                pm25 = '좋음'

            return ('\n• 오존 : ' + o3 +'\n• 미세먼지 : ' + pm10 + '\n• 초미세먼지 : ' + pm25 + '\n• 아황산가스 : ' + so2 +'\n• 일산화탄소 : ' + co +  '\n• 이산화질소 : ' + no2 )
print(weather())
