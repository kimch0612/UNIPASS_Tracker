import requests
import datetime
from bs4 import BeautifulSoup

key = os.environ['CUSTOM_API_KEY']
year = datetime.date.today().year
url = 'https://unipass.customs.go.kr:38010/ext/rest/cargCsclPrgsInfoQry/retrieveCargCsclPrgsInfo?crkyCn=%d&blYy=%d&hblNo=%d' % (key, year, number)
result = requests.get(url)
soup = BeautifulSoup(result.text, "xml")
name = soup.find('prnm')
status = soup.find('csclPrgsStts')
process_time = datetime.datetime.strptime(str(soup.find('prcsDttm').text), "%Y%m%d%H%M%S").strftime("%Y.%m.%d %H:%M:%S")
strMessage = "/// 관세청 UNIPASS 통관 조회 ///\n\n품명: %s\n통관진행상태: %s\n처리일시: %s" % (name.text, status.text, process_time)