#!/usr/bin/env python
#-*- coding:utf-8 -*-
import  json
import os
import  requests
import  configparser
import pysnooper

# path = os.path.dirname(os.path.dirname(__file__))
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(path)
config_file = configparser.ConfigParser()
config_file.read(path + r"\configuration_file\necessary_information.config")
email = config_file.get("user_login_info","email")
password = config_file.get("user_login_info","password")


#获取sessionid
@pysnooper.snoop()
def get_device_session():
    url ="https://iot-test.sensoro.com/sensoroapi/signin"
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    payload = {
        "email": email,
        "password": password
    }
    payload = json.dumps(payload)
    response = requests.post(url,headers = headers,data = payload)
    response = json.loads(response.text)
    sessionid = response["sessionId"]
    print(sessionid)
    return sessionid
get_device_session()

#根据设备SN号，获取设备信息。
