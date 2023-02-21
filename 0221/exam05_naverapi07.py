import urllib.request
import json

clientId = 'eKTacPu5QyP8sAAgDYzT'  # 자신의 ID
clientSecret = '5Q9ecvtew1'  # 자신의 Secret

def getRequestUrl(url):  # url에 접속해서 데이터를 가져와야하는 함수
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", clientId)
    req.add_header("X-Naver-Client-Secret", clientSecret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:   # 연결이 성공적이라면
            return response.read().decode('utf-8') # response값을 읽어와서 반환(utf-8로)
    except:
        return None


def getNaverSearch(node, srcText, start, display):
    # url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display) # %() : %s 위치에 값을 넣기 위해 사용
    url = base+node+parameters

    responseDecode = getRequestUrl(url)
    # print(responseDecode)
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)  # loads() : JSON문자열을 Python 객체로 변환시켜줌

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']
    pubDate = post['pubDate']
    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'originallink':originallink, 'link':link, 'pubDate':pubDate})

node = 'news'   # 'news'라는 탭에서
srcText = '선거'  # '선거'를 찾기 위해서 선언
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)  # 'news'라는 탭에서 '선거'라는 단어를 찾을 것임.(첫번째 게시물에서 100번째 게시물까지)
# print(jsonResponse)
# print(jsonResponse['total'])  # total의 값 출력
total = jsonResponse['total']
while((jsonResponse!=None) and (jsonResponse['display']!=0)) :
    for post in jsonResponse['items']:
        cnt += 1  # 몇개의 데이터가 출력되는지 알기 위해서 사용
        getPostData(post, jsonResult, cnt)
    start = jsonResponse['start'] + jsonResponse['display']  # 1 + 100 = 101
    jsonResponse = getNaverSearch(node, srcText, start, 10)

print('전체 검색 : %d 건'% (total))
print('가져온 데이터 : %d 건'% (cnt))

# json형태로 파일에 저장
with open('%s_naver_%s.json' %(srcText, node), 'w', encoding='utf-8-sig') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)  # dumps() : jsonResult를 json형태로 변환
    outfile.write(jsonFile)