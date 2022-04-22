from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    html = urlopen("https://www.mju.ac.kr/mjukr/488/subview.do")
    source = html.read()
    html.close()

    tasty_soup = BeautifulSoup(source, "html.parser")
    week_diet_tbody = tasty_soup.find("tbody")
    diet = {}
    tmp_day = ""
    for week in week_diet_tbody.find_all("tr"):
        day = ""
        try:
            day = week.find("th").get_text()
            tmp_day = day
        except:
            day = tmp_day
        week_td = week.find_all("td")
        t = week_td[2].get_text().replace("\r", ", ")
        t = t[:-2] if t[-2:] == ", " else t
        diet[f"{day} - {week_td[0].get_text()}"] = {
            "식단제목": week_td[1].get_text(),
            "식단내용": t,
        }

    for d in diet:
        print(d)
        print(diet[d])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
