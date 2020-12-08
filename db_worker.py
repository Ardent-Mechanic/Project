import sqlite3


class DateBaseW:
    def __init__(self, name_database):
        self.database = sqlite3.connect(name_database)
        self.cur = self.database.cursor()
        # self.cur = cur
        # self.database = database

    def create_table(self, name1="article", name2="dop_info"):

        self.cur.execute(f"""CREATE TABLE {name1} (
    id           INTEGER PRIMARY KEY ON CONFLICT ROLLBACK NOT NULL,
    article_name TEXT,
    author_name  TEXT,
    date         DATE    NOT NULL,
    viwe         INTEGER,
    genre        TEXT    NOT NULL);""")  # main info
        self.database.commit()

        self.cur.execute(f"""CREATE TABLE {name2} (
    dop_id       INTEGER PRIMARY KEY ON CONFLICT ROLLBACK NOT NULL,
    article_link TEXT,
    author_link TEXT,
    time         TIME    NOT NULL,
    rate         INTEGER);""")  # dop info
        self.database.commit()

    def show_rows(self, rows_string):
        rows = self.cur.execute(f"""SELECT {', '.join(rows_string)}
        FROM article JOIN dop_info ON article.id = dop_info.dop_id""").fetchall()
        return rows

    def clear_table(self, com):
        if com == 1:
            self.cur.execute("DELETE FROM article;")
            self.database.commit()

        elif com == 2:
            self.cur.execute("DELETE FROM dop_info;")
            self.database.commit()

        else:
            self.cur.execute("DELETE FROM article;")
            self.database.commit()

            self.cur.execute("DELETE FROM dop_info;")
            self.database.commit()

    def filling_database(self, all_data):

        for data in all_data:
            self.cur.execute(f"INSERT INTO article (article_name, author_name,"
                             f" date, viwe, genre) VALUES (?, ?, ?, ?, ?)", data[:5])
            self.database.commit()

            self.cur.execute(f"INSERT INTO dop_info (article_link, author_link, time, rate) VALUES (?, ?, ?, ?)",
                             data[5:])
            self.database.commit()

    def chek_article(self, new_article_name):
        chek = self.cur.execute(f"""SELECT id FROM article WHERE article_name = '{new_article_name}'""").fetchone()
        return chek

    def exit(self):
        self.database.close()