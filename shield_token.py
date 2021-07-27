'''
Created on Jul 12, 2021

@author: osanllyer
'''
import pymysql
import json
import requests
# from xhs.xhs.tools.domains import *
from tools.domains import *

import time
import urllib

class Shield(object):
    
    key_comm = 'xy-common-params'
    key_paltform = 'xy-platform-info'
    key_shield = 'shield'
    
    url_shield = 'http://localhost:8080/shield'
    tmp_xy_common = 'deviceId=%s&identifier_flag=0&fid=%s&device_fingerprint1=%s&uis=light&device_fingerprint=%s&versionName=6.60.0.1&platform=android&sid=%s&t=%s&x_trace_page_current=&lang=zh-Hans&channel=PMgdt11437564'
    tmp_xy_platform = 'platform=android&build=6600125&deviceId=%s'
    
    def __init__(self):
        
        self.conn = pymysql.connect(
            host='127.0.0.1',#数据库地址
            port=3306,# 数据库端口
            db='xiaohongshu', # 数据库名
            user = 'osanllyer', # 数据库用户名
            passwd='12345qwert', # 数据库密码
            charset='utf8mb4', # 编码方式
            use_unicode=True)
        self.cursor = self.conn.cursor()
        
        pass
    
    
    
    '计算获取一个shield'
    def calc_shiled(self, params):
        headers = {
            'Content-type': 'application/json'
            }
        res = requests.post(Shield.url_shield, headers=headers, json=params)
        print(res.text)
        return res
    
    def get_encrypted_header_url(self, url, method, device_info = None):
        
        if device_info is None:
        
            sql = 'SELECT sid, uid, device_id, fid, finger, hmac FROM device_sid s, device_infos d WHERE s.device_info_id = d.id ORDER BY rand() LIMIT 1'
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            
            sid, uid, device_id, fid, finger, hmac = row
            
            device_info = PhoneDeviceInfo()
            device_info.device_id = device_id
            device_info.uid = uid
            device_info.sid = sid
            device_info.fid = fid
            device_info.finger = finger
            device_info.hmac = hmac
        
        timestamp = str(int(time.time()))
        xy_common = Shield.tmp_xy_common % (device_info.device_id, device_info.fid, device_info.finger, device_info.finger, device_info.sid, timestamp)
        xy_platform = Shield.tmp_xy_platform % device_info.device_id
        
        if method == 'get':
            url = url % xy_common
        
        data = {
            'deviceid': device_info.device_id,
            'finger': device_info.finger,
            'fid': device_info.fid,
            'sid': device_info.sid,
            'hmac': device_info.hmac,
            'url': url,
            'data': '',
            "xy_common_params": xy_common,
            "xy_platfrom_info": xy_platform,
            "method": method
            }
        
        shield_res = self.calc_shiled(data)
        shield_json = json.loads(shield_res.text)
        shield_val = shield_json['data'].strip()
        
        header = {
            Shield.key_comm: xy_common,
            Shield.key_paltform : xy_platform,
            Shield.key_shield : shield_val,
            'authority': 'edith.xiaohongshu.com',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; m3 note Build/NRD90M) Resolution/1080*1920 Version/6.60.0.1 Build/6600125 Device/(Meizu;m3 note) discover/6.60.0.1 NetType/WiFi'
        }    
        
        return {'header': header, 'url': url}
    
    
    def get_activate_params(self, deviceInfoList, activation_url):
        
        res = []

        for d in deviceInfoList:
            
            params = BasicParams()
            params.android_id = d.uid
            params.deviceId = d.device_id
            params.fid = d.fid
            params.device_fingerprint = d.finger
            params.t = str(int(time.time()))
            
            # realdata = urllib.parse.unquote('category=%E7%B4%A0%E6%9D%90%7C%E5%A4%B4%E5%83%8F%7C11437564&android_version=24&imsi=unknow&android_id=%s&mac=a4%3A44%3Ad1%3A8c%3Aa9%3A2f&deviceId=%s&identifier_flag=0&fid=%s&device_fingerprint1=&uis=light&device_fingerprint=%s&versionName=6.60.0.1&platform=android&sid=&t=%s&x_trace_page_current=&lang=zh-Hans&channel=PMgdt11437564')
            realdata = urllib.parse.unquote('category=%E7%B4%A0%E6%9D%90%7C%E5%A4%B4%E5%83%8F%7C11437564&android_version=24&imsi=unknow&android_id=%s&mac=9a%3A15%3Afc%3Ad7%3Af1%3Ad2&deviceId=%s&identifier_flag=0&fid=%s&device_fingerprint1=&uis=light&device_fingerprint=%s&versionName=6.60.0.1&platform=android&sid=&t=%s&x_trace_page_current=&lang=zh-Hans&channel=PMgdt11437564')

            params.data = realdata %  (d.uid, d.device_id, d.fid, d.finger, params.t)
            # params.xy_common = "deviceId=%s&identifier_flag=0&fid=%s&device_fingerprint1=&uis=light&device_fingerprint=%s&versionName=6.60.0.1&platform=android&sid=&t=%s&x_trace_page_current=&lang=zh-Hans&channel=PMgdt11437564" % ( d.device_id, d.fid, d.finger, params.t)
            params.xy_common = Shield.tmp_xy_common % ( d.device_id, d.fid, '', d.finger, '', params.t)

            params.xy_platform = Shield.tmp_xy_platform % d.device_id
            
            shield_res = self.calc_shiled({
                'deviceid': d.device_id,
                'finger': d.finger,
                'fid': d.fid,
                'sid': '',
                'hmac': d.hmac,
                'url': activation_url,
                'data': params.data,
                "xy_common_params": params.xy_common,
                "xy_platfrom_info": params.xy_platform,
                "method": "post"
                })
            
            shield_json = json.loads(shield_res.text)
            params.shield = shield_json['data'].strip()
            
            '转成一个dict'
            header = self.format(params)
            data = params.data
            res.append({'header': header, 'data': data, 'dinfoid': d.dinfoid})
        return res
    
    def format(self, params):
        
        return {
                Shield.key_comm: params.xy_common, 
                Shield.key_paltform: params.xy_platform, 
                Shield.key_shield: params.shield, 
                'user-agent': params.user_agent,
                'content-type': 'application/x-www-form-urlencoded',
                'authority': 'www.xiaohongshu.com'
            }        
    
    def get_device_phone_all(self, with_sid):
        res = []
        if with_sid:
            sql = 'SELECT zone, phone, url, uid, fid, device_id, finger, hmac, d.id as dinfoid FROM fakame f, device_infos d, device_sid s WHERE f.id = s.phone_id AND d.id = s.device_info_id'
        else:
            '其实不需要任何手机信息，就是激活一下而已'
            sql = 'SELECT -1, -1, "", uid, fid, device_id, finger, hmac, d.id as dinfoid FROM device_infos d'
            
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for r in rows:
            pd = PhoneDeviceInfo()
            pd.zone = r[0] 
            pd.phone = r[1]
            pd.url = r[2]
            pd.uid = r[3]
            pd.fid = r[4]
            pd.device_id = r[5]
            pd.finger = r[6]
            pd.hmac = r[7]
            pd.dinfoid = r[8]
            
            res.append(pd)
            
        return res
