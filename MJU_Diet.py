from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import os



def main():
    html = urlopen("https://www.mju.ac.kr/mjukr/488/subview.do")
    source = html.read()
    html.close()

    tasty_soup = BeautifulSoup(source, "html5lib")
    tables = tasty_soup.find("table")
    menu = tables.find_all_next("td")
    mon =['월']
    tue = ['화']
    wed = ['수']
    thr = ['목']
    fri = ['금']

    counter = 0

    for day in [mon,tue,wed,thr,fri]:
        for i in [0,2,4,6]:
            day.append(menu[counter+i].get_text())#.replace("\n", ","))
        counter = counter + 8

    week=[mon,tue,wed,thr,fri]
    dateDict = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}

    print("-------------------------------")
    print("조회한 날짜 : ",datetime.today(),dateDict[datetime.today().weekday()])
    print("-------------------------------")

    for day in week :
        for i in range(len(day)):
            print(day[i])
        print("-------------------------------")
    os.system('pause')




if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      # do nothing here
      pass
