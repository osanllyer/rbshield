'''
Created on Jul 12, 2021

@author: osanllyer
'''
import json
import requests

import time
import urllib

class Shield(object):
    
    key_comm = 'xy-common-params'
    key_paltform = 'xy-platform-info'
    key_shield = 'shield'
    
    url_shield = 'http://localhost:8080/shield?token=%s'
    
    def __init__(self):
      pass  
      
    
    
    '计算获取一个shield'
    def calc_shiled(self, params):
        headers = {
            'Content-type': 'application/json'
            }
        res = requests.post(Shield.url_shield, headers=headers, json=params)
        print(res.text)
        return res

if __name__ == '__main__':
    sh = Shield()
    params =  {
        "fid":"1626258960109c8bc04eb3fce98b58486a871ad317d6",
        "sid":"session.1626415361335602341925",
        "deviceid":"20c164f1-e52b-338f-b964-710fd601f2ea",
        "finger":"20180724153319c43fc0e95c6412cfb093cfa21ac613470114a3c43dee00c6",
        "hmac":"/m9n/Mbb/9y7aFxkHaVhyZOBceYi1E68SsVtSAezZxHftDwmszBaA+/UoKTwN3APTyfvE+m91M8jtD0q0iCm0rXjKjPrduWNXZkajeTrifq3N2vH4Kt5Ew2tUUD3PSW2",
        "url": "https://www.xiaohongshu.com/api/sns/v4/note/user/posted?user_id=5efdeba4000000000101e7e6&sub_tag_id=&cursor=607578f6000000000102b606&num=10&use_cursor=true&pin_note_id=&pin_note_ids=&deviceId=20c164f1-e52b-338f-b964-710fd601f2ea&identifier_flag=0&fid=1626258960109c8bc04eb3fce98b58486a871ad317d6&device_fingerprint1=20180724153319c43fc0e95c6412cfb093cfa21ac613470114a3c43dee00c6&uis=light&device_fingerprint=20180724153319c43fc0e95c6412cfb093cfa21ac613470114a3c43dee00c6&versionName=6.60.0.1&platform=android&sid=session.1626415361335602341925&t=1626415425&x_trace_page_current=user_page&lang=zh-Hans&channel=PMgdt11437564",
        "xy_common_params": "deviceId=20c164f1-e52b-338f-b964-710fd601f2ea&identifier_flag=0&fid=1626258960109c8bc04eb3fce98b58486a871ad317d6&device_fingerprint1=20180724153319c43fc0e95c6412cfb093cfa21ac613470114a3c43dee00c6&uis=light&device_fingerprint=20180724153319c43fc0e95c6412cfb093cfa21ac613470114a3c43dee00c6&versionName=6.60.0.1&platform=android&sid=session.1626415361335602341925&t=1626415425&x_trace_page_current=user_page&lang=zh-Hans&channel=PMgdt11437564",
        "xy_platfrom_info": "platform=android&build=6600125&deviceId=20c164f1-e52b-338f-b964-710fd601f2ea",
        "method": "get",
        "data": ""
    }
    sh.calc_shiled(params)
    pass
