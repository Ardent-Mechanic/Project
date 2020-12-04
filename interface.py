import sys

from os.path import isfile

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QMessageBox

from db_worker import DateBaseW

from window.MainWindow import Ui_MainWindow as mainwindow

from window.dialog_one import Ui_Dialog as DialogObj

from window.DialogForCreateDataBase import Ui_Dialog as DialogCreateObj

import script_for_parse

import time

from PyQt5 import Qt  # +


class WorkThread(Qt.QThread):
    threadSignal = Qt.pyqtSignal(int)

    def __init__(self, box):
        self.mode, self.name, self.cm, self.srpt = box
        super().__init__()

    def run(self, *args, **kwargs):
        if self.mode == 1:
            self.srpt.auto_parse(self.name, self.cm)
        else:
            self.srpt.manual_parse(self.name, self.cm)


class WorkThread1(Qt.QThread):
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
        self.setupUi(self)
        self.mainwindow = mainwindow

        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(self.reject_data)

    def accept_data(self):
        DateBaseW().create_table()
        self.close()

    def reject_data(self):
        self.close()


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

        self.database = None

        self.setupUi(self)

        self.initUi()

    def initUi(self):
        self.btn.clicked.connect(self.chek)

        # self.run.clicked.connect(self.parse_articles)
        self.run.clicked.connect(self.startExecuting1)

        # self.chek_status.clicked.connect(self.startExecuting2)

        self.input_s.setText('no_delete.db')

        self.show_btn_acc.clicked.connect(self.show_table)
        # print(self.show_1.text().lower())

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText("Section not selected")
        self.msg.setWindowTitle("Warning")

        self.msg2 = QMessageBox()
        self.msg2.setIcon(QMessageBox.Warning)
        self.msg2.setText("no additional argument entered")
        self.msg2.setWindowTitle("Warning")

        self.msg = MsgBox()
        self.thread1 = None
        self.thread2 = None

    def startExecuting1(self, *args):

        if self.thread1 is None:
            self.thread1 = WorkThread(args)
            self.thread2 = WorkThread1()
            # self.thread.threadSignal.connect(self.on_threadSignal)
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
        self.msg.label.setText(f"{hour}:{minute}:{second}")
        if not self.msg.isVisible():
            self.msg.show()

    def parse_articles(self):
        if any([self.type1.isChecked(), self.type2.isChecked(), self.type3.isChecked()]):
            print(self.input_s.text())
            action = script_for_parse.Parser(self.input_s.text())

            box = list(
                map(lambda val: val.text(), filter(lambda val: val.isChecked(), [self.type1, self.type2, self.type3])))

            box = list(map(lambda val: val.split('_')[0].lower(), box))

            if not self.st1.text() and not self.st2.text():
                self.msg2.show()
            elif self.mode1.isChecked():
                for name in box:
                    self.startExecuting1(1, name, int(self.st1.text()), action)
                    # action.auto_parse(name, int(self.st1.text()))
            else:
                # self.open_dialog()
                for name in box:
                    self.startExecuting1(2, name, int(self.st1.text()), action)
                    # action.manual_parse(name, int(self.st2.text()))

        else:
            self.msg.show()

    def show_table(self):
        row = [self.show_1, self.show_2, self.show_3,
               self.show_4, self.show_5, self.show_6,
               self.show_7, self.show_8, self.show_9]

        rows_string = [i.text().lower() for i in row if i.isChecked()]

        self.database = DateBaseW(self.input_s.text())

        result = self.database.show_rows(rows_string)

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        # Устанавливаем заголовки таблицы
        self.tableWidget.setHorizontalHeaderLabels(rows_string)

        # Заполнили таблицу полученными элементами
        [[self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
          for j, val in enumerate(elem)] for i, elem in enumerate(result)]

    def open_dialog(self):
        dialog_for_question = DialogWindowTableForQuestion(self.mainwindow)
        dialog_for_question.show()
        dialog_for_question.exec()

    def chek(self):
        if not isfile(self.input_s.text()):
            self.open_dialog()
            # self.create_db('boom')

    def filter(self):
        pass


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
