import requests
from bs4 import BeautifulSoup

BASE_URL = "https://soshlinky.bakalari.cz/Timetable/Public/Actual/Class"

def get_timetable(class_name="3O"):
    """Stáhne veřejný rozvrh z Bakalářů a převede ho do slovníku"""
    url = f"{BASE_URL}/{class_name}"
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    days = soup.select("div.card")
    timetable = {}

    for day in days:
        day_name = day.select_one("h5.card-header").text.strip()
        lessons = []
        for row in day.select("tr")[1:]:
            cols = [td.text.strip() for td in row.select("td")]
            if cols and len(cols) >= 4:
                lessons.append({
                    "hour": cols[0],
                    "subject": cols[1],
                    "teacher": cols[2],
                    "room": cols[3],
                })
        timetable[day_name] = lessons
    return timetable
