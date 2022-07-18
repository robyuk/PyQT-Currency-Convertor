# This one doesn't work on replit
#Use an IDE on your local computer with graphics

from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit,QComboBox
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

in_combo=qComboBox()
in_combo.addItems(currencies)
layout.addWidget(in_combo)

tgt_combo=qComboBox()
tgt_combo.addItems(currencies)
layout.addWidget(tgt_combo)

text=QLineEdit()
layout.addWidget(text)

btn=QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output_label=QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()