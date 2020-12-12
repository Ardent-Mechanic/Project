# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup as bs

from datetime import datetime, timedelta


class Parser:
    def __init__(self):
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                     " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                       "accept": "*/*"}

        self.date_dict = {'сегодня': datetime.today().date().strftime("%d-%m-%Y"),
                          'вчера': (datetime.today().date() - timedelta(days=1)).strftime("%d-%m-%Y"),
                          'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                          'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

    def get_html(self, url):  # Получение html страницы
        text_link = requests.get(url, self.header)

        return text_link

    def get_page(self, n, link):  # Создание ссылок на нужное колличество страниц

        return map(lambda val: f"{link}page{val}", range(1, n + 1))

    def get_article(self, html):  # Парсинг статей
        soup = bs(html, 'lxml')

        return soup.find_all('article', class_="post post_preview")

    def get_content(self, arr):  # Получение данных в виде html кода

        return [[val.header.contents,
                 val.find('h2', class_="post__title").find('a'),
                 list(map(lambda i: i.a.text, val.find('ul', class_="post__hubs inline-list").find_all('li'))),
                 list(filter(lambda i: i['class'][-1] in ("post-stats__item", "post-stats__item_views"),
                             val.footer.ul.find_all('li')))] for val in arr]

    def date_and_time(self, string):

        def create_date(dd):
            return f"{dd[0]}-{self.date_dict[dd[1]]}-{dd[2]}"

        date, time = string.split(' в ')

        return self.date_dict[date] if date in ('сегодня', 'вчера') else create_date(date.split()), time

    def content_filtering(self, box, gnr):  # Получение данных в более приятном виде
        all_data = []
        for art in box:
            article_name, article_link = art[1].get_text(), art[1]['href']  # Название статьи и ссылка на неё

            author_name, author_link, datatime = art[0][1].get_text().strip(), art[0][1]['href'], art[0][
                3].get_text()  # Имя автора, ссылка на его профиль дата поста

            # Рейтинг и просмотры
            rate, viwe = art[3][0].get_text().strip(), art[3][1].get_text().strip().replace(',', '.')

            rate = rate.replace('–', '-') if '–' in rate else rate

            viwe = float(viwe[:-1]) * 1000 if 'k' in viwe else float(viwe)

            date, time = self.date_and_time(datatime)  # Дата и время

            all_data.append([article_name, author_name, date, viwe, gnr, article_link, author_link, time, rate])

        return all_data

    def manual_parse(self, name, page):
        html = self.get_html(page)

        if html.status_code == 200:
            nxt = self.get_article(html.text)
            box = self.get_content(nxt)
            filter_box = self.content_filtering(box, name)
            return filter_box

        else:
            print('Error')
            return

    def auto_parse(self, name, i):
        html = self.get_html(f'https://habr.com/{name}/page{i}/')

        if html.status_code == 200:
            nxt = self.get_article(html.text)
            box = self.get_content(nxt)
            filter_box = self.content_filtering(box, name)
            return filter_box
        else:
            print('Error')
            return
