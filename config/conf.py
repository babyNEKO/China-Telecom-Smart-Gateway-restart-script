# header信息
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

# 中国电信智能网关配置
ONU_LOGIN_URL = 'http://192.168.1.1:8080/login.cgi'
ONU_REBOOT_URL = 'http://192.168.1.1:8080/rebootinfo.cgi?sessionKey={key}'
ONU_LOGIN_POST_DATA = {
    'username': 'useradmin',
    'password': '',
}

# 网络连通测试
PING = [
    '192.168.31.1',
    '192.168.1.1',
    'www.taobao.com',
    'jd.com',
]
