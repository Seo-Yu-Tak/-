#웹스크래핑 라이브러리 beautiful soup 가져오기
import requests 
from bs4 import BeautifulSoup 

#타깃과 접속상태확인, soup변수 내부에는 타깃의 html doc 내용이 첨부
url = "https://www.gnu.ac.kr/main/ad/fm/foodmenu/selectFoodMenuView.do?mi=1341&restSeq=5/robots.txt" 
res = requests.get(url) 
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
#soup = soup.prettify()
#print(type(soup))


#접속상태 확인 코드
string_object_of_res = str(res)
slicing_res = string_object_of_res[-5:-2]
if slicing_res == "200":
    print("접속상태 정상")
else:
    print("접속상태 불량")


# <td>태그 모두 찾아 내기
Menu_data = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2)")
mon_Menu = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
tue_Menu = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2) > td:nth-child(3)")
wed_Menu = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2) > td:nth-child(4)")
thu_Menu = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2) > td:nth-child(5)")
fri_Menu = soup.select_one("#detailForm > div > table > tbody > tr:nth-child(2) > td:nth-child(6)")

mon_Menu_text = mon_Menu.get_text()
tue_Menu_text = tue_Menu.get_text()
wed_Menu_text = wed_Menu.get_text()
thu_Menu_text = thu_Menu.get_text()
fri_Menu_text = fri_Menu.get_text()
#print(Menu_data.get_text())
#print(type(Menu_data))
print(fri_Menu_text)
#test1
#test2