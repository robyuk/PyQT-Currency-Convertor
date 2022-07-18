# This one doesn't work on replit
#Use an IDE on your local computer with graphics

from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit,QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency='USD', out_currency='EUR'):
  url=f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content=requests.get(url).text
  soup=BeautifulSoup(content, 'html.parser')
  rate=soup.find("span", class_="ccOutputRslt").get_text()
  rate=float(rate[:-4])
  return rate

def show_currency():
  input_text=text.text()
  in_cur=in_combo.currentText()
  tgt_cur=tgt_combo.currentText()
  rate=get_currency(in_cur,tgt_cur)
  output=round(float(input_text) * rate, 2)
  message= f'{input_text} {in_cur} is {output} {tgt_cur}'
  output_label.setText(str(message))

app=QApplication([])
window=QWidget()
window.setWindowTitle('Currency Converter')

layout=QVBoxLayout()
currencies=['USD','EUR','GBP','INR']

layout1=QHbBoxLayout()
layout.addLayout(layout1)
output_label=QLabel('')
layout.addWidget(output_label)

layout2=QVBoxLayout()
layout1.addlayout(layout2)

layout3=QVBoxLayout()
layout1.addlayout(layout3)

in_combo=qComboBox()
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

tgt_combo=qComboBox()
tgt_combo.addItems(currencies)
layout2.addWidget(tgt_combo)

text=QLineEdit()
layout3.addWidget(text)

btn=QPushButton('Convert')
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(show_currency)

window.setLayout(layout)
window.show()
app.exec()