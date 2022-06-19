import requests as req
import json
from datetime import datetime, timedelta

def get_date():
    # getting the date of the monday of this week
    now = datetime.now()
    monday = now - timedelta(days = now.weekday())
    return monday.strftime('%d-%m')

WISHES = ['ah kleine salades en pastasalades', 'amandeldrink', 'quaker havermout', 'bramen', 'breaker']

url = 'https://www.ah.nl/gql'

headers = {'client-name':'ah-bonus', 
    'client-version':'3.195.0', 
    'Content-Type': 'application/json'
}

payload = "{\"query\":\"query bonusSegments($promotionType: BonusPromotionType, $segmentType: BonusSegmentType, $hideVariants: Boolean, $periodStart: String, $periodEnd: String, $orderId: Int, $viewDate: String) {\\n  bonusSegments(\\n    promotionType: $promotionType\\n    segmentType: $segmentType\\n    hideVariants: $hideVariants\\n    periodStart: $periodStart\\n    periodEnd: $periodEnd\\n    orderId: $orderId\\n    viewDate: $viewDate\\n  ) {\\n    title\\n  }\\n}\",\"variables\":{\"segmentType\":\"NEGATE_PREMIUM\",\"hideVariants\":true,\"orderId\":null}}"

page = req.post(headers=headers, data=payload, url=url)
data = json.loads(page.content)
discounts = [el['title'].lower() for el in data['data']['bonusSegments']]
for d in discounts:
    for w in WISHES:
        if w in d:
            print(d)

title = f'bonus-{get_date()}.txt'
f = open(title, 'w')
for d in discounts:
    f.write(d+'\n')
f.close()