import urllib.request
import urllib.parse

def result_book(book_name):
    apple = str(book_name)
    apple = urllib.parse.quote_plus(apple)
    page = urllib.request.urlopen('https://library.sch.ac.kr/search/caz/result?st=KWRD&si=TOTAL&q='+apple+'&folder_id=null')
    pizza = page.read().decode('utf8')
    result = '총 <strong>'
    result2 = '</strong>건 중 <strong>'
    result3 = '</strong>건 출력'
    where = pizza.find(result)
    where2 = pizza.find(result2)
    where3 = pizza.find(result3)
    firt_book = pizza[where+len(result):where2]
    last_book = pizza[where2+len(result2):where3]
    return '총 ' +firt_book+ '건 중' + last_book +'건의 검색 결과가 존재합니다.\n• 자세한 사항은 아래 url 을 확인해주세요.'
