from config import conf
from os import system
import requests
from time import sleep
import re


def onu_reboot():
    # 光猫重启动
    try:
        login = requests.post(url=conf.ONU_LOGIN_URL, data=conf.ONU_LOGIN_POST_DATA)
        if login.status_code != 200:
            print('登陆失败')
        find_session_key = re.findall('sessionKey=(.*[0-9])', login.text)[0]
        if find_session_key == '':
            print('无法获取sessionKey')
        print('sessionKey: ' + find_session_key)
        reboot = requests.get(url=conf.ONU_REBOOT_URL.format(key=find_session_key), headers=conf.HEADERS)
        print('ONU重启中 Status:' + str(reboot.status_code))
    except TimeoutError:
        print('连接超时')
        exit(0)


def network_test(domain_name):
    # 网络恢复测试
    for i in range(1, 140):
        sleep(1)
        print('等待设备恢复' + str(i))
    system('chcp 65001')
    for i in domain_name:
        system('ping {domain_name}'.format(domain_name=i))


if __name__ == '__main__':
    # 执行
    onu_reboot()
    network_test(domain_name=conf.PING)
