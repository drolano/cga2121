import re

import html2text
from bs4 import BeautifulSoup

h = html2text.HTML2Text()
h.body_width = 0



regex_device_modal = re.compile(
    r'(?P<name>[\w\-_]+) ?\|'
    r' ?(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})? ?\|'
    r' ?(?P<mac>\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})')




def get_device_modal(content):
    data = []
    soup = BeautifulSoup(content, features="lxml")
    
    devices = soup.find_all('table', { 'class' : 'table table-condensed table-striped rsp-table' })
    rows = soup.find_all('tr')
    if len(devices) > 0:
        get_data_from_devices(data, devices)




def get_data_from_devices(data, devices):
    for device in devices:
        device_contents = device.contents

        for contador in range (3, len(device_contents[1])-3):
            fila_datos = device_contents[1].contents[contador]
            print (device_contents[1].contents[contador])
            name = fila_datos.contents[1].text
            ip_address = fila_datos.contents[5].text
            mac = fila_datos.contents[3].text
            data.append({'name': name, 'ip': ip_address, 'mac': mac})


