import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

class Program():
    URL_ENDP: str = "https://www.santodelgiorno.it/"

    def __init__(self):
        self

    def run(self):
        self.santo_del_giorno(self.parse())

    def test(self):
        print("MI chiamo pippo")

    def parse(self):
        resp = requests.get(self.URL_ENDP)
        if not resp.ok:
            print("Error")
            os.exit(-1)
        return resp.content

    def santo_del_giorno(self, html: str):
        saint = Saint()
        soup = BeautifulSoup(html, 'html.parser')
        saint.name = soup.find("div", class_="NomeSantoDiOggi").text
        saint.description = soup.find("div", class_="TipologiaSantoDiOggi").text
        saint.print_saint()
        saint.print_saints_list(self.other_saint_list(soup, html))

    def other_saint_list(self, soup, html: str):
        saint_list = []
        for s in soup.find_all("a", class_="NomeSantoEl"):
            new_saint = Saint()
            new_saint.name = s.text
            new_saint.description = None
            saint_list.append(new_saint)
        return saint_list


class Saint():
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def print_saint(self):
        print(f"{self.print_today_date()}\n-------SAINT-------\n{self.name}\n{self.description}\n")

    def print_saints_list(self, saint_list):
        print("-------OTHER SAINT LIST-------")
        print([f"{saint.name}" for saint in saint_list])

    def print_today_date(self):
        now = dt.now()
        print(now.strftime("%A %-m %Y"))


if __name__ == "__main__":
    p = Program()
    p.run()
