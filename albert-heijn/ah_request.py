import requests

headers = {
    'authority': 'www.ah.nl',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'batch': 'True',
    'client-name': 'ah-bonus',
    'client-version': '3.382.0',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.ah.nl',
    'referer': 'https://www.ah.nl/bonus',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

json_data = [
  {
    "operationName": "bonusSegments",
    "variables": {
      "segmentType": "NEGATE_PREMIUM",
      "hideVariants": True,
      "periodStart": "2023-09-11",
      "periodEnd": "2023-09-17",
      "orderId": None,
      "testZeroSegments": False
    },
    "query": "query bonusSegments($promotionType: BonusPromotionType, $segmentType: BonusSegmentType, $hideVariants: Boolean, $periodStart: String, $periodEnd: String, $orderId: Int, $viewDate: String) {\n  bonusSegments(\n    promotionType: $promotionType\n    segmentType: $segmentType\n    hideVariants: $hideVariants\n    periodStart: $periodStart\n    periodEnd: $periodEnd\n    orderId: $orderId\n    viewDate: $viewDate\n  ) {\n    ...Segment\n    __typename\n  }\n}\n\nfragment Segment on BonusSegment {\n  ...BaseSegment\n  activationStatus\n  category\n  description\n  discountUnit {\n    count\n    __typename\n  }\n  images {\n    url\n    title\n    width\n    height\n    __typename\n  }\n  price {\n    label\n    now {\n      amount\n      formatted\n      __typename\n    }\n    was {\n      amount\n      formatted\n      __typename\n    }\n    __typename\n  }\n  productCount\n  promotionType\n  salesUnitSize\n  smartLabel\n  spotlight\n  type\n  __typename\n}\n\nfragment BaseSegment on BonusSegment {\n  id\n  hqId\n  availability {\n    startDate\n    endDate\n    description\n    __typename\n  }\n  discount {\n    type\n    title\n    description\n    extraDescriptions\n    theme\n    __typename\n  }\n  discountUnit {\n    count\n    __typename\n  }\n  discountLabels {\n    code\n    defaultDescription\n    price\n    actualCount\n    count\n    freeCount\n    amount\n    percentage\n    deliveryType\n    unit\n    __typename\n  }\n  promotionType\n  subtitle\n  title\n  type\n  description\n  storeOnly\n  __typename\n}"
  }
]

def get_bonus():
    response = requests.post('https://www.ah.nl/gql', headers=headers, json=json_data)
    return response