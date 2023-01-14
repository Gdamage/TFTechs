from utils import resource_path
import shutil
import requests

current_path = '13.1'
store_location = resource_path('lang')
availiable_langs = ["en_US","cs_CZ","de_DE","el_GR","en_AU","en_GB","en_PH","en_SG","es_AR","es_ES","es_MX",
"fr_FR","hu_HU","id_ID","it_IT","ja_JP","ko_KR","pl_PL","pt_BR","ro_RO","ru_RU","th_TH","tr_TR","vn_VN",
"zh_CN","zh_MY","zh_TW"]

for lang in availiable_langs:
    endpoint = f'https://raw.communitydragon.org/{current_path}/cdragon/tft/{lang.lower()}.json'
    
    with open(f'{store_location}/{lang}.json', 'wb') as output:
        r = requests.get(endpoint)
        output.write(r.content)
        print(f'Saved {lang}.json - {endpoint}')