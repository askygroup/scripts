# 查询IP属地信息
查询IP属地信息


---


#### 脚本迭代记录

##### query_ip_geolocation.py

|脚本迭代版本|描述|
|---|---|
|query_ip_geolocation-1.py|查询单个IP（IPV4 地址、IPV6 地址）属地信息，多途径查询|
|||


##### nginx_query_ip_geolocation.py

|脚本迭代版本|描述|
|---|---|
|nginx_query_ip_geolocation-1.py|读取 nginx 来源IP地址，查询IP属地信息，读取 all_ip.list 文件中的数据进行匹配查询，读取的IP属地信息数据为字典类型；速度较慢，两千个IP用时 286 秒|
|nginx_query_ip_geolocation-1-1.py|读取 nginx 来源IP地址，查询IP属地信息，读取 all_ip.list 文件中的数据进行匹配查询，将读取的IP属地信息数据转换成字典类型；查询速度秒级|
|nginx_query_ip_geolocation-2.py|读取 nginx 来源IP地址，查询IP属地信息，使用 ip信息 API 查询；速度较慢，两千个IP用时 365 秒|
|nginx_query_ip_geolocation-3.py|读取 nginx 来源IP地址，查询IP属地信息，使用 ip信息 API 查询，使用 threading 模块开启多线程；50 个线程，两千个IP用时 12 秒|
|nginx_query_ip_geolocation-4.py|读取 nginx 来源IP地址，查询IP属地信息，使用本地缓存查询，使用 ip信息 API 查询，使用 threading 模块开启多线程，优化系统最大线程池限制，增加过滤境外IP的top30；查询时先查找本地缓存是否有属地信息，有直接写入到结果文件中，没有则添加到任务列表中，然后读取任务列表，开启多线程使用 ip信息 API 查询，然后将查询后的数据写入到结果文件中，最后更新本地IP属地信息缓存 all_ip.json 文件，方便后续查询；如果本地有缓存，查询速度秒级|
|||


---


#### 其他文件

|文件|描述|
|---|---|
|all_ip.list|IP属地信息表|
|all_ip.json|IP属地信息表，历史查询本地缓存文件|
|---|---|
|./files/nginx_ip.*.list|IP地址信息|
|./files/nginx_ip.*.txt|IP地址和属地信息|
|---|---|
|./files/test_ip.list|IP地址信息，测试数据|
|./files/test_ip.txt|IP地址和属地信息，测试数据|
|test_ip-使用本地list缓存查询.txt|IP地址和属地信息，测试数据|
|./files/test_ip-使用API单线程查询.txt|IP地址和属地信息，测试数据|
|./files/test_ip-使用API多线程查询.txt|IP地址和属地信息，测试数据|
|---|---|
|./files/overseas_ip-*.list|当天境外IP的top30数据|

---


#### 查询IP属地的网站

##### ip信息 IPV4 API

https://ip.useragentinfo.com/json?ip=125.119.233.10

支持查询本机IP地址属地信息，不传 "ip" 参数即可；不支持 IPV6 地址

返回：

```json
{
    "country": "中国",
    "short_name": "CN",
    "province": "浙江省",
    "city": "杭州市",
    "area": "西湖区",
    "isp": "电信",
    "net": "",
    "ip": "125.119.233.10",
    "code": 200,
    "desc": "success"
}
```

##### ip信息 IPV6 API

https://ip.useragentinfo.com/ipv6/240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a

不支持查询本机IP地址属地信息；支持 IPV6 地址；还可以查询IP地址的经纬度

返回：

```json
{
    "iso2": "CN",
    "country": "China",
    "region": "Zhejiang",
    "city": "Quzhou",
    "latitude": "28.959440",
    "longitude": "118.868610",
    "zip_code": "324000",
    "time_zone": "+08:00",
    "ipv6": "240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a",
    "code": 200,
    "desc": "success"
}
```

##### 百度 API

http://opendata.baidu.com/api.php?query=125.119.233.10&co=&resource_id=6006&oe=utf8

http://opendata.baidu.com/api.php?query=125.119.233.10&co=&resource_id=6006&oe=utf8&format=json

不支持查询本机IP地址属地信息；不支持 IPV6 地址

返回：

```json
{
    "status": "0",
    "t": "",
    "set_cache_time": "",
    "data": [
        {
            "ExtendedLocation": "",
            "OriginQuery": "125.119.233.10",
            "appinfo": "",
            "disp_type": 0,
            "fetchkey": "125.119.233.10",
            "location": "浙江省杭州市 电信",
            "origip": "125.119.233.10",
            "origipquery": "125.119.233.10",
            "resourceid": "6006",
            "role_id": 0,
            "shareImage": 1,
            "showLikeShare": 1,
            "showlamp": "1",
            "titlecont": "IP地址查询",
            "tplt": "ip"
        }
    ]
}
```

##### 太平洋 API

http://whois.pconline.com.cn/ipJson.jsp?ip=125.119.233.10&json=true

支持查询本机IP地址属地信息，不传 "ip" 参数即可；不支持 IPV6 地址

返回：

```json
{
    "ip": "125.119.233.10",
    "pro": "浙江省",
    "proCode": "330000",
    "city": "杭州市",
    "cityCode": "330100",
    "region": "",
    "regionCode": "0",
    "addr": "浙江省杭州市 电信ADSL",
    "regionNames": "",
    "err": ""
}
```

##### ip API

http://ip-api.com/json/125.119.233.10?lang=zh-CN

http://ip-api.com/json/240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a?lang=zh-CN

支持查询本机IP地址属地信息，不传 "ip" 参数即可；支持 IPV6 地址；还可以查询IP地址的经纬度

查询速度较慢，容易超时；每分钟限制45次查询

IPV4 地址返回：

```json
{
    "status": "success",
    "country": "中国",
    "countryCode": "CN",
    "region": "ZJ",
    "regionName": "浙江省",
    "city": "杭州",
    "zip": "",
    "lat": 30.2994,
    "lon": 120.1612,
    "timezone": "Asia/Shanghai",
    "isp": "Chinanet",
    "org": "",
    "as": "AS4134 CHINANET-BACKBONE",
    "query": "125.119.233.10"
}
```

IPV6 地址返回：

```json
{
    "status": "success",
    "country": "中国",
    "countryCode": "CN",
    "region": "BJ",
    "regionName": "北京市",
    "city": "北京",
    "zip": "",
    "lat": 39.9042,
    "lon": 116.407,
    "timezone": "Asia/Shanghai",
    "isp": "CHINANET",
    "org": "China Telecom",
    "as": "AS4134 CHINANET-BACKBONE",
    "query": "240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a"
}
```

##### vore IPV4 API

https://api.vore.top/api/IPv4?v4=125.119.233.10

支持查询本机IP地址属地信息，不传 "ip" 参数即可；不支持 IPV6 地址

查询速度较慢，容易超时

返回：

```json
{
    "code": "200",
    "msg": "SUCCESS",
    "ipdata": {
        "info1": "浙江省",
        "info2": "杭州市",
        "info3": "西湖区",
        "isp": "电信"
    },
    "time": "1669793947"
}
```

##### vore IPV6 API

https://api.vore.top/api/IPv6?v6=240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a

支持查询本机IP地址属地信息，不传 "ip" 参数即可，如果本机没有 IPV6 地址，返回为空；支持 IPV6 地址

查询速度较慢，容易超时

返回：

```json
{
    "code": 200,
    "msg": "SUCCESS",
    "ipdata": {
        "info1": "云南省",
        "info2": "昆明市",
        "info3": "西山区",
        "isp": "电信"
    },
    "time": 1669798281
}
```

##### vore API

https://api.vore.top/api/IPdata?ip=125.119.233.10

https://api.vore.top/api/IPdata?ip=44c:300:b0a3:c4e9:3eb9:6cb6:1a8a

支持查询本机IP地址属地信息，不传 "ip" 参数即可；支持 IPV6 地址

查询速度较慢，容易超时

IPV4 地址返回：

```json
{
    "code": 200,
    "msg": "SUCCESS",
    "ipinfo": {
        "type": "ipv4",
        "text": "125.119.233.10",
        "cnip": true
    },
    "ipdata": {
        "info1": "浙江省",
        "info2": "杭州市",
        "info3": "西湖区",
        "isp": "电信"
    },
    "adcode": {
        "o": "浙江省杭州市西湖区 - 电信",
        "p": "浙江",
        "c": "杭州",
        "n": "浙江-杭州",
        "r": "浙江-杭州",
        "a": "330100",
        "i": true
    },
    "tips": "接口由VORE-API(https://api.vore.top/)免费提供",
    "time": 1669792959
}
```

IPV6 地址返回：

```json
{
    "code": 200,
    "msg": "SUCCESS",
    "ipinfo": {
        "type": "ipv6",
        "text": "240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a",
        "cnip": true
    },
    "ipdata": {
        "info1": "云南省",
        "info2": "昆明市",
        "info3": "西山区",
        "isp": "电信"
    },
    "adcode": {
        "o": "云南省昆明市西山区 - 电信",
        "p": "云南",
        "c": "昆明",
        "n": "云南-昆明",
        "r": "云南-昆明",
        "a": "530100",
        "i": true
    },
    "tips": "接口由VORE-API(https://api.vore.top/)免费提供",
    "time": 1669797859
}
```

##### zxinc API

https://ip.zxinc.org/api.php?type=json&ip=125.119.233.10

不支持查询本机IP地址属地信息，会返回本机IP地址；支持 IPV6 地址

IPV4 地址返回：

```json
{
    "code": 0,
    "data": {
        "myip": "117.149.10.42",
        "ip": {
            "query": "125.119.233.10",
            "start": "",
            "end": ""
        },
        "location": "浙江省杭州市 电信",
        "country": "浙江省杭州市",
        "local": "电信"
    }
}
```

IPV6 地址返回：

```json
{
    "code": 0,
    "data": {
        "myip": "117.149.10.42",
        "ip": {
            "query": "240e:44c:300:b0a3:c4e9:3eb9:6cb6:1a8a",
            "start": "",
            "end": ""
        },
        "location": "中国\t云南省\t昆明市\t西山区 中国电信\t无线基站网络",
        "country": "中国\t云南省\t昆明市\t西山区",
        "local": "中国电信\t无线基站网络"
    }
}
```

##### 淘宝 API

https://ip.taobao.com

https://ip.taobao.com/service/getIpInfo.php?ip=125.119.233.10

查询功能已于2022年3月31日永久关停，已无法使用


---

