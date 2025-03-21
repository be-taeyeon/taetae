import requests

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드를 입력해줘 : ")

url = base_url + keyword
req = requests.get(url) #get요청 -> 주소를 들고 서버에게 가서 원화는 결과를 요청하는 행위
print(req.text)



