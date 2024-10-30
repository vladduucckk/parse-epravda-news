from operator import concat
import requests
import bs4
import csv
import datetime

day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year

url_news = "https://www.epravda.com.ua/rus/archives/date_{}{}{}/".format(day, month, year)


def get_url(url: str) -> bs4.BeautifulSoup:
    """Завантажує html код сторінки та повертає соуп об'єкт"""
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    if req.status_code == 200:
        with open("news.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        return soup
    else:
        raise requests.exceptions.HTTPError


def parse_news(soup: bs4.BeautifulSoup) -> tuple:
    """Парсить заголовки, посилання, дати, описи та поверстає список словників"""
    title = []
    link = []
    date = []
    summary = []
    # отримуємо div із стрічкою новин
    news_list = soup.find("div", {"class": "news_list"})
    # парсимо дані із стрічки новин
    list_title_link = news_list.find_all("a")
    list_date = news_list.find_all("div", {"class": "article__time"})
    list_summary = news_list.find_all("div", {"class": "article__subtitle"})
    # парсинг тексту тегів, значення атрибуту href та робимо шлях посилання абсолютним
    for data in list_title_link:
        title.append({"title": data.text})
        link.append({"link": concat("www.epravda.com.ua", data.get("href"))})

    for data in list_date:
        date.append({"date": data.text})

    for data in list_summary:
        summary.append({"summary": data.text})

    return title, link, date, summary


def save_to_csv(data: tuple) -> None:
    """Запис данних до csv файлу"""
    # розпаковка списків із словниками(був кортеж із списків)
    open_tuple_title = data[0]
    open_tuple_link = data[1]
    open_tuple_date = data[2]
    open_tuple_summary = data[3]

    with open("news.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link", "date", "summary"])
        writer.writeheader()
        for i in range(len(open_tuple_title)):
            writer.writerow({
                "title": open_tuple_title[i]["title"],
                "link": open_tuple_link[i]["link"],
                "date": open_tuple_date[i]["date"],
                "summary": open_tuple_summary[i]["summary"]
            })


# обробка виключень для 2 проблем із з'єднанням
try:
    download_page = get_url(url_news)
    news = parse_news(download_page)
    save_to_csv(news)
    print("Сторінка з новинами: news.html, завантажена!")
    print("CSV файл: news.csv, завантажений!")
except requests.ConnectionError as e:
    print("Сайту не існує!", e)
except requests.HTTPError:
    print("З'єднання з сторінкою прошло невдало!")
