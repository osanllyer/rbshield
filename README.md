# rbshield
小红书shield 6.6版本的分析

支持6.6版本的小红书shield算法
用法请直接参考python脚本

## 参数说明：

fid, hmac, deviceid, finger 可以从自己的手机上dump出来，也可以通过fiddler， charles等工具获取查看

如果需要更多的deviceid，可以联系开发人员

url 是需要获取的url，后面一般需要拼接xy_common_params这个参数
xy_common_params, xy_platform参考charles的请求发送的参数即可。
method 是请求方式，get，post两种
data 如果请求是post，那么需要把请求发送的数据使用form-encoded的方式编码成字符串

## 例子：

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
