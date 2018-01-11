import requests
import json
from pandas import DataFrame

URL = 'https://coincheck.com/api/ticker'
coincheck = requests.get(URL).json()

#json形式のデータから、keyとリストをひっぱてきてデータを整形、
# 見やすいように文字数とフィールド幅を統一、
for key, item in coincheck.items():
    print("%-9s : %-10.9s " % (key, item))

