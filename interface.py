import os
import sys

from os.path import isfile

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QMessageBox

from db_worker import DateBaseW

from window.MainWindow import Ui_MainWindow as mainwindow

from window.dialog_one import Ui_Dialog as DialogObj

from script_for_parse import Parser

import time

from PyQt5 import Qt, QtWidgets

from PyQt5 import QtCore

import sqlite3

import datetime as dt


class WorkThread1(Qt.QThread):
    threadSignal = Qt.pyqtSignal(int)

    def __init__(self, box, database_name):

        self.database_name = database_name

        self.mode, self.name, self.cm, self.srpt = box
        super().__init__()

    def filling_database(self, all_data):
        database = sqlite3.connect(self.database_name)
        cur = database.cursor()

        for data in all_data:
            cur.execute(f"INSERT INTO article (article_name, author_name,"
                        f" date, viwe, genre) VALUES (?, ?, ?, ?, ?)", data[:5])
            database.commit()

            cur.execute(f"INSERT INTO dop_info (article_link, author_link, time, rate) VALUES (?, ?, ?, ?)",
                        data[5:])
            database.commit()
        database.close()

    def chek_article(self, new_article_name):
        database = sqlite3.connect(self.database_name)
        cur = database.cursor()
        chek = cur.execute(f'SELECT id FROM article WHERE article_name = "{new_article_name}"').fetchone()
        database.close()
        return chek

    def run(self, *args, **kwargs):
        if self.mode == 1:
            flag = False
            i = 1
            while True:
                box = self.srpt.auto_parse(self.name, i)
                for j in range(len(box)):
                    if self.chek_article(box[j][0]):
                        box = box[:j]
                        flag = True
                        break

                self.filling_database(box)

                if flag:
                    flag = False
                    i = 0
                    time.sleep(self.cm)

                if len(box) == 0:
                    i = 0
                i += 1
        else:
            for page in self.srpt.get_page(self.cm, f'https://habr.com/{self.name}/'):
                self.filling_database(self.srpt.manual_parse(self.name, page))
            self.quit()


class WorkThread2(Qt.QThread):
    threadSignal = Qt.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self, *args, **kwargs):
        c = 0
        while True:
            time.sleep(1)
            c += 1
            self.threadSignal.emit(c)


class DialogWindowTableForQuestion(QDialog, DialogObj):
    def __init__(self, mainwindow):
        QDialog.__init__(self)

        self.com = None

        self.setupUi(self)
        self.mainwindow = mainwindow

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

    @QtCore.pyqtSlot()
    def accept_data(self):
        self.com = True
        self.accept()

    @QtCore.pyqtSlot()
    def reject_data(self):
        self.com = False
        self.accept()


class MsgBox(Qt.QDialog):
    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self)
        self.label = Qt.QLabel("")
        layout.addWidget(self.label)
        close_btn = Qt.QPushButton("Close")
        layout.addWidget(close_btn)

        close_btn.clicked.connect(self.close)

        self.setGeometry(900, 65, 400, 80)
        self.setWindowTitle('MsgBox to display time')


class MainWindow(QMainWindow, mainwindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = mainwindow

        self.table = []

        self.setupUi(self)

        self.initUi()

    def initUi(self):
        self.btn.clicked.connect(self.chek)

        self.run.clicked.connect(self.parse_articles)

        self.run_2.clicked.connect(self.delete_database)

        self.run_3.clicked.connect(self.cleare_tables)

        self.run_4.clicked.connect(self.disconnect_from_db)

        self.show_btn_acc.clicked.connect(self.show_table)

        self.filter_btn_acc.clicked.connect(self.filter)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText("Section not selected")
        self.msg.setWindowTitle("Warning")

        self.msg2 = QMessageBox()
        self.msg2.setIcon(QMessageBox.Warning)
        self.msg2.setText("No additional argument entered")
        self.msg2.setWindowTitle("Warning")

        self.msg3 = MsgBox()
        self.thread1 = None
        self.thread2 = None

        self.msg4 = QMessageBox()
        self.msg4.setIcon(QMessageBox.Warning)
        self.msg4.setWindowTitle("Warning")

    def open_dialog(self):
        dialog_for_question = DialogWindowTableForQuestion(self.mainwindow)
        if dialog_for_question.exec_() == QtWidgets.QDialog.Accepted:
            if dialog_for_question.com:
                database = DateBaseW(self.input_s.text())
                database.create_table()
                database.exit()

    def chek(self):
        if not isfile(self.input_s.text()):
            self.open_dialog()

        else:
            """Открытие окна о нахождении такой бд"""
            pass

    def startExecuting1(self, *args):
        if args[0] == 2:
            self.thread1 = WorkThread1(args, self.input_s.text())
            self.thread2 = WorkThread2()

            self.thread1.start()


        else:
            if self.thread1 is None:

                self.thread1 = WorkThread1(args, self.input_s.text())
                self.thread2 = WorkThread2()
                self.thread1.start()

                self.thread2.threadSignal.connect(self.on_threadSignal)
                self.thread2.start()

                self.run.setText("STOP")

            else:

                self.thread1.terminate()
                self.thread2.terminate()

                self.thread1 = None
                self.thread2 = None

                self.run.setText("RUN")

    def on_threadSignal(self, second):
        hour = minute = 0
        if second // 3600 != 0:
            hour, second = second // 3600, second - hour * 3600
            second -= hour * 3600
        if second // 60 != 0:
            minute = second // 60
            second -= minute * 60
        self.msg3.label.setText(f"{hour}:{minute}:{second}")
        if not self.msg3.isVisible():
            self.msg3.show()

    def parse_articles(self):
        if any([self.type1.isChecked(), self.type2.isChecked(), self.type3.isChecked()]):

            action = Parser()

            box = list(
                map(lambda val: val.text(), filter(lambda val: val.isChecked(), [self.type1, self.type2, self.type3])))

            box = list(map(lambda val: val.split('_')[0].lower(), box))

            if not self.st1.text() and not self.st2.text():
                self.msg2.show()
            elif self.mode1.isChecked():
                for name in box:
                    self.startExecuting1(1, name, int(self.st1.text()), action)
            else:
                for name in box:
                    self.startExecuting1(2, name, int(self.st2.text()), action)

        else:
            self.msg.show()

    def show_table(self):
        row = [self.show_1, self.show_2, self.show_3,
               self.show_4, self.show_5, self.show_6,
               self.show_7, self.show_8, self.show_9]

        rows_string = [i.text().lower() for i in row if i.isChecked()]

        database = DateBaseW(self.input_s.text())

        result = database.show_rows(rows_string)

        database.exit()

        if not result:
            return

        if not self.table:
            self.table.append([i.text().lower() for i in row])
            self.table.append(result)
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        # Устанавливаем заголовки таблицы
        self.tableWidget.setHorizontalHeaderLabels(rows_string)

        # Заполнили таблицу полученными элементами
        [[self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
          for j, val in enumerate(elem)] for i, elem in enumerate(result)]

    def filter(self):

        row = [self.show_1, self.show_2, self.show_3,
               self.show_4, self.show_5, self.show_6,
               self.show_7, self.show_8, self.show_9]

        rows_string = [i.text().lower() for i in row]

        database = DateBaseW(self.input_s.text())

        data = database.show_rows(rows_string)

        database.exit()

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(rows_string))

        # Устанавливаем заголовки таблицы
        self.tableWidget.setHorizontalHeaderLabels(rows_string)

        params = [i.text().lower() for i in [self.fil_1, self.fil_2, self.fil_3, self.fil_4] if i.isChecked()][0]

        [print(i[-1]) for i in data if type(i[-1]) != int]

        n = rows_string.index(params)

        if params == 'date':
            data.sort(key=lambda val: (
                dt.datetime.strptime(val[3], '%d-%m-%Y').date(), dt.datetime.strptime(val[7], '%H:%M').time(), val[4]))
        else:
            data.sort(key=lambda val: val[n], reverse=True)

        # Заполнили таблицу полученными элементами
        [[self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
          for j, val in enumerate(elem)] for i, elem in enumerate(data)]

    def delete_database(self):
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), self.input_s.text())
            os.remove(path)
        except Exception as ex:
            print(ex)
            self.msg4.setText(f"Error:{ex}")
            self.msg4.show()

    def cleare_tables(self):
        database = DateBaseW(self.input_s.text())
        database.clear_table()
        database.exit()

    def disconnect_from_db(self):
        self.input_s.setText('')
        self.tableWidget.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
