import requests
import re
str="■:福岡オフィス／福岡県福岡市博多区中洲4-5-6"
string = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?／【】:“”■！，。？、~@#￥%……&*（）]+", "", str)
print(string)