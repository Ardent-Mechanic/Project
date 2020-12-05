import sqlite3


class DateBaseW:
    def __init__(self, cur, database):
        self.cur = cur
        self.database = database

    def create_table(self, name1="article", name2="dop_info"):

        self.cur.execute(f"""CREATE TABLE {name1} (
    id           INTEGER PRIMARY KEY ON CONFLICT ROLLBACK NOT NULL,
    article_name TEXT,
    author_name  TEXT,
    date         DATE    NOT NULL,
    viwe         INTEGER
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

        return self.cur.execute(f"""SELECT {', '.join(rows_string)}
        FROM article JOIN dop_info ON article.id = dop_info.dop_id""").fetchall()

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