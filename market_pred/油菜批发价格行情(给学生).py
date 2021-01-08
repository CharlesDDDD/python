
import codecs
import re
import time
import datetime
import os
import requests
import json
from requests.packages import urllib3

urllib3.disable_warnings()

#------------------------------------------------------------------------------#
# root_dir
root_dir = '/Users/weihangsun/Desktop/cif.mofcom.gov.cn/'

# date_record
date_record = root_dir + 'date_record.txt'
if os.path.exists(date_record) == True:
    with codecs.open(date_record, 'r', 'UTF-8') as f:
        data = f.read()
    if data == '':
        searchDate = datetime.date(2015, 1, 1)
    else:
        searchDate = datetime.datetime.strptime(data, "%Y-%m-%d").date()
else:
    searchDate = datetime.date(2015, 1, 1)

# writefile
writefile = root_dir + '油菜批发价格行情.txt'
row_exist = []
if os.path.exists(writefile) == True:
    print(f'已存在 {writefile}')
    with codecs.open(writefile, 'r', 'UTF-8') as f:
        data = f.readlines()
        for line in data:
            row_exist.append(re.sub(r'\s+', '', line))
row_exist_set = set(row_exist)

# headers
# headers = { 
#             }

# LOOP
this_round_add = 0

while searchDate <= datetime.date(2020,1,31):

    # url
    url = url = 'https://cif.mofcom.gov.cn/cif/getEnterpriseListForDate.fhtml'
    this_page_add = 0
    print(f'now {searchDate}:')

    # FormData
    # FormData = {
    #             }

    # get
    while True:
        try:
            response = requests.post(url, ？？？=？？？, ？？？=？？？, timeout=30)
            break
        except:
            time.sleep(0.1)

    # r_json
    r_json = json.loads(response.text)

    # date
    date = r_json['date']
    print(f'-- date = {date}')
    title = r_json['title']
    print(f'-- title = {title}')

    # item
    for item in ？？？:
        
        try:
            ？？？ = ？？？
        except:
            ？？？ = ''

        # row_to_write
        row_to_write = '' 
        row_to_write += date + ','
        ？？？

        # write
        writer = codecs.open(writefile, 'a', 'UTF-8')
        writer.write(row_to_write + '\n')
        writer.close()

        this_page_add += 1
        this_round_add += 1

    # date_record
    record_writer = codecs.open(date_record, 'w', 'UTF-8')
    record_writer.write(str(searchDate))
    record_writer.close()

    # 报告进度, 更新 searchDate
    print(f'date {searchDate} finished ({this_page_add} added this page, {this_round_add} added this round). \n')
    searchDate += datetime.timedelta(days = 1)