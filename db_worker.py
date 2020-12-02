import sqlite3


class DateBaseW:
    def __init__(self, name='no_delete.db'):
        self.name = name
        self.db = sqlite3.connect(name)
        self.cur = self.db.cursor()

    def create_table(self, name1="article", name2="dop_info"):

        self.cur.execute(f"""CREATE TABLE {name1} (
    id           INTEGER PRIMARY KEY ON CONFLICT ROLLBACK NOT NULL,
    article_name TEXT,
    author_name  TEXT,
    date         DATE    NOT NULL,
    viwe         INTEGER
    genre        TEXT    NOT NULL);""")  # main info
        self.db.commit()

        self.cur.execute(f"""CREATE TABLE {name2} (
    dop_id       INTEGER PRIMARY KEY ON CONFLICT ROLLBACK NOT NULL,
    article_link TEXT,
    author_link TEXT,
    time         TIME    NOT NULL,
    rate         INTEGER);""")  # dop info
        self.db.commit()

    def show_rows(self, rows_string):

        return self.cur.execute(f"""SELECT {', '.join(rows_string)}
        FROM article JOIN dop_info ON article.id = dop_info.dop_id""").fetchall()

    def clear_table(self, com):
        if com == 1:
            self.cur.execute("DELETE FROM article;")
            self.db.commit()

        elif com == 2:
            self.cur.execute("DELETE FROM dop_info;")
            self.db.commit()

        else:
            self.cur.execute("DELETE FROM article;")
            self.db.commit()

            self.cur.execute("DELETE FROM dop_info;")
            self.db.commit()
