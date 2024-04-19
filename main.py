from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout
from random import shuffle
class O_Object():
    def __init__(self,question,ra,wa1,wa2,wa3):
        self.question = question
        self.ra = ra
        self.wa1 = wa1
        self.wa2 = wa2
        self.wa3 = wa3
Ql = []
Ql.append(O_Object('2+2',"4","22","1","5"))
Ql.append(O_Object('342-27*532',"167580","274385","787234675","723428208470384238490249023826785738295782350"))
Ql.append(O_Object('√3',"1.732","1.932","1.432","1.132"))




def ask(q: O_Object):
    pon.setText(q.question)
    shuffle(but_l)
    but_l[0].setText(q.ra)
    but_l[1].setText(q.wa1)
    but_l[2].setText(q.wa2)
    but_l[3].setText(q.wa3)

def ca():
    if but_l[0].isChecked():
        pon2.setText('правельно')
    else:
        pon2.setText('неправельно')
    r_a.setText(but_l[0].text())

def nq():
    ask(Ql[main_win.counter])
    main_win.counter += 1
    if main_win.counter >= len(Ql):
        main_win.counter = 0



def bq():
    if ab.text() == 'Ответить':
        ca()
        rgbrb.hide()
        rgq.show()
        ab.setText("Следующий вопрос")
    else:
        nq()
        rgbrb.show()
        rgq.hide()
        rb()
        ab.setText("Ответить")

def rb():
    for btn in but_l:
        btn.setAutoExclusive(False)
        btn.setChecked(False)
        btn.setAutoExclusive(True)

app = QApplication([])
main_win = QWidget()
rgbrb = QGroupBox('вопросы')
main_win.counter = 0
main_win.setWindowTitle('Memory card')
main_win.resize(400,200)
pon = QLabel("Какой национальности не существует?")
but_1 = QRadioButton('Смурфы')
but_2 = QRadioButton('Чулымци')
but_3 = QRadioButton('Энци')
but_4 = QRadioButton('Алеуты')
but_l = [but_1,but_2,but_3,but_4]

ab = QPushButton('Ответить')
h = QVBoxLayout()

lh1 = QVBoxLayout()
lh2 = QHBoxLayout()
lh3 = QHBoxLayout()
lh2.addWidget(but_1, alignment = Qt.AlignCenter)
lh2.addWidget(but_2, alignment = Qt.AlignCenter)
lh3.addWidget(but_3, alignment = Qt.AlignCenter)
lh3.addWidget(but_4, alignment = Qt.AlignCenter)
lh1.addLayout(lh2)
lh1.addLayout(lh3)
rgbrb.setLayout(lh1)

at = ('')
pon2 = QLabel("Прально / Непрльно")
rgq = QGroupBox("Ответ")
r_a = QLabel('правильный ответ')
lay = QVBoxLayout()
lay.addWidget(pon2)
lay.addWidget(r_a)
rgq.setLayout(lay)








h.addWidget(pon, alignment=Qt.AlignCenter)
h.addWidget(rgbrb)
h.addWidget(rgq)
h.addWidget(ab)



main_win.setLayout(h)
ab.clicked.connect(bq)

rgq.hide()
nq()
main_win.show()
app.exec_()
