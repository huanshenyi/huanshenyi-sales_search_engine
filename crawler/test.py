# import requests
# import re
# str="大東建託株式会社（東証・名証一部上場）"
# string = re.sub("（(.*?)）", "", str)
# print(string)

"""
品川本社・全国にある拠点での勤務となります。
本社（さいたま市）、各事業所（さいたま市・越谷市・上尾市・蓮田市・桶川市・久喜市・幸手市　ほか）
東京、横浜、名古屋、さいたま、静岡、金沢、仙台のいずれかの支店　★希望考慮。主要繁華街の中心部です。
山口県・福岡県・埼玉県の各支店のいずれか（希望に応じて決定いたします）
大阪市西区新町1丁目5番7号 四ツ橋ビルディング502／「四ツ橋駅」より徒歩2分
本社／東京都渋谷区円山町5-5 NAVI渋谷V　※転勤なし。「渋谷駅」より徒歩2分とアクセス良好！
仙台、新潟、福岡の営業所（いずれも主要駅からのアクセス良好！）　★希望を考慮します
東北・関東・関西・東海・中国・四国・九州　※U・Iターン歓迎！希望勤務地考慮
＜転勤ナシ／希望を考慮します＞東京（豊島区）、大阪（淀川区）、名古屋（中区）　※いずれも駅チカ！
東京支店／東京都中央区日本橋箱崎町25-7　ヤマキビル5F　※転勤なし！「水天宮前駅」徒歩1分
西東京・埼玉エリアの13店舗（埼玉県入間市・狭山市・所沢市、東京都練馬区、武蔵野市、国分寺市など）
本社／東京都墨田区押上2丁目18-12 東武館1F ★「押上駅」A3出口より徒歩1分　★転勤なし
東京都世田谷区祖師谷（12月オープン予定）★最寄り駅徒歩4分　※オープンまでは立川の本社勤務
東宝ハウス新小岩／東京都葛飾区新小岩１丁目５１－１８　★転勤ナシ
関西支店／大阪府吹田市江坂町2-6-10　江坂DAプラザビル601号
本社または第2工場（東京都杉並区）★転勤なし。自転車通勤OK！第2工場は昨年完成したキレイな工場！
"""
import re

# y = re.compile("【(.*?)】")
# xx = re.sub("【(.*?)】", "", "株式会社IDOM【東証一部上場企業】")
# print(xx)

x = "株式会社プロディライト　 東京支店"
y = re.sub("\s*","", x)
print(y)
# y = re.sub("\D*", "", "年収：400～700万円")
# y = re.compile("\d*～\d*")
# x = re.search(y, "年収：400～700万円")
# x = x.group()
# xx = x.split("～")
# print(xx)


# xx = re.sub("【(.*?)】|\（(.*?)\）", "", "ＧＭＯ　ＴＥＣＨ株式会社 【マザーズ】 (GMOインターネットグループ)")
# # xx = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()★?転勤なし／【】本社：“”■！，。？、~@#￥%……&*（）]+", "",
# #             "本社または第2工場（東京都杉並区）★転勤なし。自転車通勤OK！第2工場は昨年完成したキレイな工場！")
# print(xx)
# xx = "ＧＭＯ　ＴＥＣＨ株式会社  (GMOインターネットグループ)"
# y = re.sub("　", "", xx)
# print(y)

# url = "https://www.wantedly.com/projects/308370?filter_params%5Bauthorized%5D=true&filter_params%5Bcategory%5D=normal&filter_params%5Bcountry%5D=japan&filter_params%5Boccupation_types%5D%5B%5D=sales&filter_type=mixed&list=2&page=1"
#
# y = re.compile("https://www.wantedly.com/projects/(\d+)?")
#
# x = re.match(y,url)
# print(x.group())

# x = "東京都港区海岸3-3-18 芝浦日新ビル6階"
# x = re.sub(" ",'',x)
# print(x)