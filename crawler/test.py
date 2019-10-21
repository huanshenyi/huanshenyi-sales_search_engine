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

# x = "株式会社プロディライト　 東京支店"
# y = re.sub("\s*","", x)
# print(y)
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

# x = """
# <td class="rnn-col-10 rnn-offerDetail__text">
#                 650万円／月給33万8000円＋賞与＋役職手当／32歳・入社8年目<br>480万円／月給31万8000円＋賞与／28歳・入社3年目<br>390万円／月給28万円＋賞与／25歳・入社1年目
#               </td>
# """
#
# y = re.sub("<.*>", "", x) # 650万円／月給33万8000円＋賞与＋役職手当／32歳・入社8年目390万円／月給28万円＋賞与／25歳・入社1年目
# xx = re.compile("(\d+)万円／")
#
# xxx = re.findall(xx,y,)
#  #['650', '390']
# xxx = ['850', '450', '600', '850']
# n = len(xxx)
# print(n)
# for i in range(n-1):
#     print(i)
#     if int(xxx[i]) > int(xxx[i+1]):
#         xxx[i] , xxx[i + 1] = xxx[i + 1], xxx[i]
# print(xxx)

# text = """
#
#
#               正社員／全国の各事業所◎転勤なし★急募地域 北海道／札幌 東北／仙台、青…
#
# """
#
# text = text.strip()
# print(text)

# text =['株式会社レッド・フリップ　★ゼロからプロになれる研修制度あり　★メリハリのある風土で残業ほぼなし　★GW・夏季・冬季には長期休暇あり',
#        'PayPay株式会社（株主：ソフトバンクグループ株式会社、ソフトバンク株式会社、ヤフー株式会社）',
#        '■東証一部上場■6期連続で過去最高の連結売上高、利益を更新中！「日本一」を本気で目指す会社■休日出勤ナシ■残業少なめ・残業抑制を徹底　【株式会社オープンハウス】',
#        '住友不動産株式会社◆東証一部上場企業◆土日面接可◆UIターン歓迎 ',
#        '【東証一部上場】【提携先JA（農協）の取り扱い企業】【2020年に創業50周年】【転勤なし／全国60ヶ所に営業所あり】株式会社アサンテ',
#        '株式会社りらく　◆週3日～＆1日3時間～という働き方が可能！働く時間や休日は自由設定　◆プロの技術が習得できる無料レッスンあり',
#        '東建コーポレーション株式会社　■東証・名証一部上場企業　■全国571拠点　■連結売上高3,285億2,400万円 （2019年4月期）',
#        '富士冷熱株式会社【設立以来58年の歴史を刻み、長年経験を積んだベテランはもちろん20～30代の若手社員が活躍中の会社です】',
#        '佐川急便株式会社★東証一部上場SGホールディングス（株）のグループ企業★子育てサポートのくるみんマーク認定企業',
#        '株式会社yell　☆リクルートトップパートナー／人材業界に特化した広告代理店　★土日祝休み'
#        ]
# re_text = re.compile("(\w*)株式会社(\w*)")
# for i in text:
#     x = re.search(re_text, i)
#     print(x.group())

# text = """
# # <div class="listDate">
# # 			<span class="listDateMark listDateMark--new">NEW</span>
# # 			<span class="item">掲載期間</span>19/10/17 ～ 19/10/30</div>
# # """
# # pattern = re.compile(r'<[^>]+>', re.S)
# # result = pattern.sub('', text)
# # result = result.split()
# # result = result[1]
# # print(result)

# text = ['<div class="categoryData">32歳・4年目／1233万円（月給51万円＋業績給621万円）<br>34歳・3年目／758万円（月給36万円＋業績給326万円）<br>28歳・2年目／523万円（月給21万円＋業績給271万円）</div>',
#  '<div class="categoryData">520万円／入社2年目・27歳<br>400万円／入社1年目・23歳</div>']
# result = '<div class="categoryData">32歳・4年目／1233万円（月給51万円＋業績給621万円）<br>34歳・3年目／758万円（月給36万円＋業績給326万円）<br>28歳・2年目／523万円（月給21万円＋業績給271万円）</div>'
#
# pattern = re.compile(r'<[^>]+>', re.S)
# result = pattern.sub('', result)# 520万円／入社2年目・27歳400万円／入社1年目・23歳
# xx = re.compile("(\d{3,4})万円")
#
# xxx = re.findall(xx, result)
#
# n = len(xxx)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if int(xxx[j]) > int(xxx[j+1]):
#             xxx[j], xxx[j + 1] = xxx[j + 1], xxx[j]
# print(xxx)

# import requests
#
# url = "https://mynavi.agentsearch.jp/jobList/"
#
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"occ\"\r\n\r\n11105\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'postman-token': "ecab0de4-ab0d-fc6e-413f-6f66bbbbf681"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)

text= """
<li>
            <span class="icon-salary"></span>
            800万円〜1000万円<br>
          </li>
"""
# pattern = re.compile(r'<[^>]+>', re.S)
# result = pattern.sub('', text)
# result = result.strip()
# xx = re.compile("(\d{3,4})万円")
#
# result = re.findall(xx, result)
# print(result)

"""
<dd>月給25万円～50万円※経験・年齢・スキルを考慮の上、決定します。※月給にはみなし残業代（60時間分／7万5…</dd>
<dd>【年収例】<br>400万円～500万円／30歳…</dd>
<dd>1387万円／40歳・入社2年目（月給55万円+賞与）※営業経験者</dd>
<dd>年収800万円／28歳／経験6年／月給50万円＋歩合給＋賞与</dd>
<dd>年収例730万円（入社4年目）<br>年収例400万円（入社3年目）</dd>
<dd>【総合不動産業】（1）ビルの開発・賃貸（2）マンション・戸建住宅の開発・分譲（3）宅地の造成・分譲（4）…</dd>
<dd>年収414万円／25歳 経験3年／配偶者、子1人<br>年収489万円／28歳 経験7年／配偶者、子2人</dd>
<dd>・水まわりの緊急メンテナンス・水道衛生設備工事・給水設備工事・排水設備工事・住宅設備機器の販売、施工…</dd>
<dd>■年収922万円（33歳）月給46万840円、賞与369万3460円<br>■年収740万円（28歳）月給37万7510円、賞与287万1290円</dd>
<dd>サントリー清涼飲料水の販売＜関連会社＞サントリーホールディングス株式会社サントリー食品インターナショ…</dd>
<dd>【年収3000万円以上も可能】月給30万円～50万円＋出来高成果給＋報奨金 ◎月給には外勤手当（11万5000円～1…</dd>
<dd>【月収例】<br>22歳／月収24万4,085円～28万3,000円</dd>
<dd>■ホテルの運営・管理・開発■高級感のあるインテリア、広々としたベッド、足を伸ばせるバスタブ、行き届い…</dd>
<dd>年収672万円／29歳・課長・入社5年（月給56万円＋各種手当＋イン…<br>年収492万円／26歳・主任・入社3年（月給41万円＋各種手当＋イン…</dd>
<dd>【年収】670万円（入社3年目／賞与・歩合給含む）<br>【年収】950万円（入社6年目／賞与・歩合給含む）</dd>
<dd>年収400万円／入社2年目・30歳<br>年収300万円／入社1年目・25歳</dd>
<dd>【月収例】<br>22歳／月収21万4,010円～26万3,000円</dd>
<dd>【年収3000万円以上も可能】月給30万円～50万円＋出来高成果給＋報奨金 ◎月給には外勤手当（11万5000円～1…</dd>
<dd>年収485万円／25歳（入社3年）<br>年収606万円／32歳（入社6年）</dd>
"""

# text = "【年収例】<br>400万円～500万円／30歳…"
# pattern = re.compile(r'<[^>]+>', re.S)
# result = pattern.sub('', text)
# xx = re.compile("(\d{3,4})万円")
#
# result = re.findall(xx, result)
#
#
#
#
# print(result)

from urllib.parse import urlencode

# test = ("------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"occ\"\r\n\r\n11105\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--")
# print(test)

# import requests
#
# url = "https://mynavi.agentsearch.jp/jobList/"
#
# querystring = {"page":"1"}
#
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"occ\"\r\n\r\n11105\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"hiddenOcc\"\r\n\r\n11105\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"selectPageIndex\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'postman-token': "a3320a33-6ded-f7e2-a90d-223e1168d2dc"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#
# print(response.text)
"""
<Selector xpath="//div[@class='detail cf']/dl[4]/dd" data='<dd>東京都\r<br>港区西新橋1丁目16-3 1東洋海事ビル５階</dd>'>
"""

# text = """
# <Selector xpath="//div[@class='detail cf']/dl[4]/dd" data='<dd>＜福岡本社＞\u3000福岡市博多区東比恵3-1-2\u3000東比恵ビジネスセ…</dd>'>
# """
# pattern = re.compile(r'<[^>]+>', re.S)
# result = pattern.sub('', text)
# result = result.strip()
# result= result.replace("　","")
# result = re.sub("[＜＞…'>]", "", result)
# print(result)

text = """
<p class="job-name">
																	福祉機器トップシェア企業のルート営業職｜関西採用｜福利厚生充実<span class="employment-situation-new">正社員</span>
																	</p>
"""
pattern = re.compile(r'<[^>]+>', re.S)
result = pattern.sub('', text)
print(result.strip())