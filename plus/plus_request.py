import requests

cookies = {
    'visid_incap_1876175': '5pQafGEiQRKPc9iMYi37XFI3F2UAAAAAQUIPAAAAAAAaFN/MopYH5EC49fGGFrnG',
    'incap_ses_1082_1876175': 'F0TsILLrkzVF49+K7goED1I3F2UAAAAAaKPLx1s9m6p0uDxS1yapnw==',
    'nlbi_1876175': 'f7F5BytsMjvSPvzgJuxx+QAAAACp9AJNLZh+wnJM/V2O4gg1',
    'reese84': '3:549C0o9KIUYr5AlqAnJeLQ==:q4Ac0D1O3M1JeYuS3KsA6aunxbOm+Sequ+/KpvzKqBpm7okMWFpuaC9NOCk6xMOkNytQpm+xVom93wRMd3omcbirWe1q6qU/1nl8keNn6uxpksiRmK6InjaiMQuBfOB2EqZ0iRI5Q4doBtumKTWK42AXoS7aWqGX+aEz4+1BMteuuhnzYYtaU8YrjoJVyykMWyHrwmG0KLi9o7LlqDryhmJhjbKgE9E26GlMt16ppgKfwYl/57XIC+xu3aHgq/N2zg7opu634yQhw7fk+8hd8ljJ836mLbPPoBB8cRtOk95FeVB4YqrJ3W6R6Pns30e+ebPLK7q2u6xETTLdW+mPtRItV27Jm5H2cs7+QZFbiGH+pPhA+griTsXv1C0W0DICyR6ChEbaMW4uA0PKwbHZBbwXJTE64ZSGJTVa5S3lbR90wdfZo4TONTdlx+URlKnmMyLZXUNZRokzuNU6KvdGjw==:cuNJArrKa1Ez+1JAT913EL3cR+/RramkMuAv3VnD+8s=',
    'SSLB': '1',
    'SSID': 'CQB9XB04AAAAAABUNxdlKuVAAFQ3F2UBAAAAAACAn9loVDcXZQD0DK0AAAFMGQAAVDcXZQEAyAAAAxgdAABUNxdlAQDCAAAB2hsAAFQ3F2UBAMcAAAFvHAAAVDcXZQEA',
    'SSSC': '1.G7284351756216100138.1|173.6476:194.7130:199.7279:200.7448',
    'SSRT': 'VDcXZQABAA',
    'sid': 'xESjvOXca0KAvIDL8xDHv8zWJZXfpgQNuF7kGpJy',
    'SecureSessionID-8lcKAygMZZ4AAAFFzHAngfeq': 'cc7a7c737b72bc99fb7cf8909b2ab5cb3aebbee6d7752733f1983260b688e5c4',
    'pgid-PLUS-website-Site': 'loZWaZo9dWFSRppQeDpemCWD0000QObqYlXc',
    'CES-Surveys': 'muted',
    'pageLoads': '1',
    'SSOD': 'ABkNAAAAEgD-HQAAAwAAAFQ3F2VpNxdlAwAAAA',
    'SSPV': 'J7MAAAAAAAMABgAAAAAAAAAAAAQAAAAAAAAAAAAA',
    'nlbi_1876175_2147483392': 'N7c4CclQDUt98A07Juxx+QAAAADv8fdthhVRRrS0EpgOgqff',
    'AWSALB': 'Boedp7ribryek9/16vagJeKLfB6f0Lt6oRCtDHZVxP1NA9NyCR32yk2JMoXds0xfPatr5xEpuEF2LuxXSrB9vxmHrLHj/K04HH6uppQHH/1hCbDbazLUOOM6Fo/h',
    'AWSALBCORS': 'Boedp7ribryek9/16vagJeKLfB6f0Lt6oRCtDHZVxP1NA9NyCR32yk2JMoXds0xfPatr5xEpuEF2LuxXSrB9vxmHrLHj/K04HH6uppQHH/1hCbDbazLUOOM6Fo/h',
}

headers = {
    'authority': 'www.plus.nl',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,nl;q=0.8,fr;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'visid_incap_1876175=5pQafGEiQRKPc9iMYi37XFI3F2UAAAAAQUIPAAAAAAAaFN/MopYH5EC49fGGFrnG; incap_ses_1082_1876175=F0TsILLrkzVF49+K7goED1I3F2UAAAAAaKPLx1s9m6p0uDxS1yapnw==; nlbi_1876175=f7F5BytsMjvSPvzgJuxx+QAAAACp9AJNLZh+wnJM/V2O4gg1; reese84=3:549C0o9KIUYr5AlqAnJeLQ==:q4Ac0D1O3M1JeYuS3KsA6aunxbOm+Sequ+/KpvzKqBpm7okMWFpuaC9NOCk6xMOkNytQpm+xVom93wRMd3omcbirWe1q6qU/1nl8keNn6uxpksiRmK6InjaiMQuBfOB2EqZ0iRI5Q4doBtumKTWK42AXoS7aWqGX+aEz4+1BMteuuhnzYYtaU8YrjoJVyykMWyHrwmG0KLi9o7LlqDryhmJhjbKgE9E26GlMt16ppgKfwYl/57XIC+xu3aHgq/N2zg7opu634yQhw7fk+8hd8ljJ836mLbPPoBB8cRtOk95FeVB4YqrJ3W6R6Pns30e+ebPLK7q2u6xETTLdW+mPtRItV27Jm5H2cs7+QZFbiGH+pPhA+griTsXv1C0W0DICyR6ChEbaMW4uA0PKwbHZBbwXJTE64ZSGJTVa5S3lbR90wdfZo4TONTdlx+URlKnmMyLZXUNZRokzuNU6KvdGjw==:cuNJArrKa1Ez+1JAT913EL3cR+/RramkMuAv3VnD+8s=; SSLB=1; SSID=CQB9XB04AAAAAABUNxdlKuVAAFQ3F2UBAAAAAACAn9loVDcXZQD0DK0AAAFMGQAAVDcXZQEAyAAAAxgdAABUNxdlAQDCAAAB2hsAAFQ3F2UBAMcAAAFvHAAAVDcXZQEA; SSSC=1.G7284351756216100138.1|173.6476:194.7130:199.7279:200.7448; SSRT=VDcXZQABAA; sid=xESjvOXca0KAvIDL8xDHv8zWJZXfpgQNuF7kGpJy; SecureSessionID-8lcKAygMZZ4AAAFFzHAngfeq=cc7a7c737b72bc99fb7cf8909b2ab5cb3aebbee6d7752733f1983260b688e5c4; pgid-PLUS-website-Site=loZWaZo9dWFSRppQeDpemCWD0000QObqYlXc; CES-Surveys=muted; pageLoads=1; SSOD=ABkNAAAAEgD-HQAAAwAAAFQ3F2VpNxdlAwAAAA; SSPV=J7MAAAAAAAMABgAAAAAAAAAAAAQAAAAAAAAAAAAA; nlbi_1876175_2147483392=N7c4CclQDUt98A07Juxx+QAAAADv8fdthhVRRrS0EpgOgqff; AWSALB=Boedp7ribryek9/16vagJeKLfB6f0Lt6oRCtDHZVxP1NA9NyCR32yk2JMoXds0xfPatr5xEpuEF2LuxXSrB9vxmHrLHj/K04HH6uppQHH/1hCbDbazLUOOM6Fo/h; AWSALBCORS=Boedp7ribryek9/16vagJeKLfB6f0Lt6oRCtDHZVxP1NA9NyCR32yk2JMoXds0xfPatr5xEpuEF2LuxXSrB9vxmHrLHj/K04HH6uppQHH/1hCbDbazLUOOM6Fo/h',
    'dnt': '1',
    'origin': 'https://www.plus.nl',
    'pragma': 'no-cache',
    'referer': 'https://www.plus.nl/aanbiedingen',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'PromotionUUID': '[krAKKQOWY88AAAGIwhQU1x9l, P68KKQOZlJQAAAGKQKxjUIaW, s3oKKQOZxJQAAAGKG6xjUIaW, WOEKKQOZLwAAAAGKuq1jUIaW, ypcKKQOZid0AAAGKSq9jUIaW, J54KKQKXYWgAAAGFKRFd2DX8, O18KKQKZ1wsAAAGFfBwkEDnZ, 2SYKKQOZ.m4AAAGKHa9jUIaW, yyUKKQOZYqkAAAGKaa9jUIaW, B8IKKQOZ45AAAAGKqTBLTa_J, rJMKKQOZjhcAAAGKj61jUIaW, VOQKKQOZcXYAAAGKczdLTa_J, l7UKKQOZ.ewAAAGKiTtLTa_J, 0mgKKQOZDIMAAAGKsjdLTa_J, lpoKKQOZhE0AAAGKb6tjUIaW, mBsKKQOZG0UAAAGK1TdLTa_J, _HoKKQOZ2oAAAAGKwTBLTa_J, IBgKKQOZIQgAAAGKlq5jUIaW, myAKKQOZSoUAAAGKiD5LTa_J, 8d0KKQOZq3gAAAGK5ThLTa_J, TnsKKQOZj_EAAAGKJDpLTa_J, 5vcKKQOZX8UAAAGK2zpLTa_J, 9RcKKQOZy3UAAAGKAjpLTa_J, eNEKKQOZt.EAAAGKH0BS_CS9, f2wKKQOZWzYAAAGKlzpLTa_J, h8AKKQOZ62IAAAGKuzlLTa_J, i5kKKQOZSDkAAAGKZTpLTa_J, Lz4KKQOZOq0AAAGKmztLTa_J, tKcKKQOZ9dUAAAGKIq5jUIaW, TxAKKQOZVMsAAAGK7z9S_CS9, UPkKKQOZzvwAAAGKn61jUIaW, giAKKQOZAe8AAAGK5jxLTa_J, s90KKQOZXZsAAAGKyjNLTa_J, FQcKKQOZpBIAAAGK0DRLTa_J, qhEKKQOZnHYAAAGKZ61jUIaW, 1PUKKQOZO9MAAAGKVkFLTa_J, ApMKKQOZZpEAAAGKCTRLTa_J, EekKKQOZaNwAAAGKNEFLTa_J, HbkKKQOZZuUAAAGK3q5jUIaW, nBcKKQOZXrMAAAGKIEFLTa_J, WO0KKQOZP68AAAGKajVLTa_J, G3YKKQOZRkoAAAGKAz9LTa_J, 0_gKKQOZwnYAAAGKhTJLTa_J, 1A4KKQOZG84AAAGKLjtLTa_J, gpwKKQOZjh0AAAGKCztLTa_J, QP4KKQOZu6EAAAGKG61jUIaW, ti4KKQOZjP8AAAGK3T5LTa_J, WNcKKQOZuUQAAAGKPq1jUIaW, AbAKKQOXunoAAAF_gnxx8SeA, B_IKKQOWgYkAAAF.TIFhaHgw, ahwKKQOWgjkAAAGK4ZAYaWpo, NskKKQOZBYIAAAGKFS9LTa_J, EoYKKQOZzp0AAAGKKy9LTa_J, haoKKQOZvi4AAAGKvT1LTa_J, BGwKKQOZDiUAAAGK.qxjUIaW, kaUKKQOZB08AAAGKCzNLTa_J, KZMKKQOZw.4AAAGKWaxjUIaW, m7EKKQOZh0IAAAGKBTJLTa_J, PUoKKQOZTK0AAAGKUDJLTa_J, bpUKKQKZ5gEAAAGFPYUkEDnl, rPQKKQOZMrAAAAGKdD5LTa_J, 7QgKKQOZ6nMAAAGKErtLTaqj, AhAKKQOZcosAAAGKVD9LTa_J, iv0KKQOZNvUAAAGKHjNLTa_J, O6YKKQOZVb0AAAGKLzdLTa_J, RqgKKQOZ_K0AAAGKnTRLTa_J, tY8KKQOZdREAAAGKSEBLTa_J, ztgKKQOZSrsAAAGKSTRLTa_J, PL0KKQOZkokAAAGKWTNLTa_J, RTgKKQOZHUkAAAGKKTRLTa_J, 6LIKKQOZjJwAAAGKbzNLTa_J]',
    'CurrentPrmoGroup': '25',
    'ViewContextUUID': '7QEKKQKWxnoAAAGCo0BPvVf_',
    'PromotionWeek': '202339',
    'SelectedWeek': '202339',
}

response = requests.post(
    'https://www.plus.nl/INTERSHOP/web/WFS/PLUS-website-Site/nl_NL/-/EUR/ViewPromotions-LoadNextPromotions',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)

# with open('plus.html', 'w') as file:
#   file.write(response.text)


import requests

cookies = {
    'visid_incap_1876175': '5pQafGEiQRKPc9iMYi37XFI3F2UAAAAAQUIPAAAAAAAaFN/MopYH5EC49fGGFrnG',
    'incap_ses_1082_1876175': 'F0TsILLrkzVF49+K7goED1I3F2UAAAAAaKPLx1s9m6p0uDxS1yapnw==',
    'nlbi_1876175': 'f7F5BytsMjvSPvzgJuxx+QAAAACp9AJNLZh+wnJM/V2O4gg1',
    'reese84': '3:549C0o9KIUYr5AlqAnJeLQ==:q4Ac0D1O3M1JeYuS3KsA6aunxbOm+Sequ+/KpvzKqBpm7okMWFpuaC9NOCk6xMOkNytQpm+xVom93wRMd3omcbirWe1q6qU/1nl8keNn6uxpksiRmK6InjaiMQuBfOB2EqZ0iRI5Q4doBtumKTWK42AXoS7aWqGX+aEz4+1BMteuuhnzYYtaU8YrjoJVyykMWyHrwmG0KLi9o7LlqDryhmJhjbKgE9E26GlMt16ppgKfwYl/57XIC+xu3aHgq/N2zg7opu634yQhw7fk+8hd8ljJ836mLbPPoBB8cRtOk95FeVB4YqrJ3W6R6Pns30e+ebPLK7q2u6xETTLdW+mPtRItV27Jm5H2cs7+QZFbiGH+pPhA+griTsXv1C0W0DICyR6ChEbaMW4uA0PKwbHZBbwXJTE64ZSGJTVa5S3lbR90wdfZo4TONTdlx+URlKnmMyLZXUNZRokzuNU6KvdGjw==:cuNJArrKa1Ez+1JAT913EL3cR+/RramkMuAv3VnD+8s=',
    'SSLB': '1',
    'SSID': 'CQB9XB04AAAAAABUNxdlKuVAAFQ3F2UBAAAAAACAn9loVDcXZQD0DK0AAAFMGQAAVDcXZQEAyAAAAxgdAABUNxdlAQDCAAAB2hsAAFQ3F2UBAMcAAAFvHAAAVDcXZQEA',
    'SSSC': '1.G7284351756216100138.1|173.6476:194.7130:199.7279:200.7448',
    'SSRT': 'VDcXZQABAA',
    'sid': 'xESjvOXca0KAvIDL8xDHv8zWJZXfpgQNuF7kGpJy',
    'SecureSessionID-8lcKAygMZZ4AAAFFzHAngfeq': 'cc7a7c737b72bc99fb7cf8909b2ab5cb3aebbee6d7752733f1983260b688e5c4',
    'pgid-PLUS-website-Site': 'loZWaZo9dWFSRppQeDpemCWD0000QObqYlXc',
    'CES-Surveys': 'muted',
    'pageLoads': '1',
    'SSOD': 'AFkeAAAAEgD-HQAAAgAAAFQ3F2VjNxdlAgAAAA',
    'SSPV': '07kAAAAAAAIABAAAAAAAAAAAAAMAAAAAAAAAAAAA',
    'nlbi_1876175_2147483392': 'wT3vFghSNwfLm11BJuxx+QAAAAAk63jDhIE5bvJrItmCP3rz',
    'AWSALB': '6jmSqdaXAc5km3VeuZPeXFmHhf+gL8hKtZaO+aHCnaWA6hWRmjlVd/6s5iHT1dGst/hVS+Brlrlo6gPxuQ2aUDguVg9Wj8heYVgeekcNNeRIKKIao+qD5xA1LMlf',
    'AWSALBCORS': '6jmSqdaXAc5km3VeuZPeXFmHhf+gL8hKtZaO+aHCnaWA6hWRmjlVd/6s5iHT1dGst/hVS+Brlrlo6gPxuQ2aUDguVg9Wj8heYVgeekcNNeRIKKIao+qD5xA1LMlf',
}

headers = {
    'authority': 'www.plus.nl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,nl;q=0.8,fr;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'visid_incap_1876175=5pQafGEiQRKPc9iMYi37XFI3F2UAAAAAQUIPAAAAAAAaFN/MopYH5EC49fGGFrnG; incap_ses_1082_1876175=F0TsILLrkzVF49+K7goED1I3F2UAAAAAaKPLx1s9m6p0uDxS1yapnw==; nlbi_1876175=f7F5BytsMjvSPvzgJuxx+QAAAACp9AJNLZh+wnJM/V2O4gg1; reese84=3:549C0o9KIUYr5AlqAnJeLQ==:q4Ac0D1O3M1JeYuS3KsA6aunxbOm+Sequ+/KpvzKqBpm7okMWFpuaC9NOCk6xMOkNytQpm+xVom93wRMd3omcbirWe1q6qU/1nl8keNn6uxpksiRmK6InjaiMQuBfOB2EqZ0iRI5Q4doBtumKTWK42AXoS7aWqGX+aEz4+1BMteuuhnzYYtaU8YrjoJVyykMWyHrwmG0KLi9o7LlqDryhmJhjbKgE9E26GlMt16ppgKfwYl/57XIC+xu3aHgq/N2zg7opu634yQhw7fk+8hd8ljJ836mLbPPoBB8cRtOk95FeVB4YqrJ3W6R6Pns30e+ebPLK7q2u6xETTLdW+mPtRItV27Jm5H2cs7+QZFbiGH+pPhA+griTsXv1C0W0DICyR6ChEbaMW4uA0PKwbHZBbwXJTE64ZSGJTVa5S3lbR90wdfZo4TONTdlx+URlKnmMyLZXUNZRokzuNU6KvdGjw==:cuNJArrKa1Ez+1JAT913EL3cR+/RramkMuAv3VnD+8s=; SSLB=1; SSID=CQB9XB04AAAAAABUNxdlKuVAAFQ3F2UBAAAAAACAn9loVDcXZQD0DK0AAAFMGQAAVDcXZQEAyAAAAxgdAABUNxdlAQDCAAAB2hsAAFQ3F2UBAMcAAAFvHAAAVDcXZQEA; SSSC=1.G7284351756216100138.1|173.6476:194.7130:199.7279:200.7448; SSRT=VDcXZQABAA; sid=xESjvOXca0KAvIDL8xDHv8zWJZXfpgQNuF7kGpJy; SecureSessionID-8lcKAygMZZ4AAAFFzHAngfeq=cc7a7c737b72bc99fb7cf8909b2ab5cb3aebbee6d7752733f1983260b688e5c4; pgid-PLUS-website-Site=loZWaZo9dWFSRppQeDpemCWD0000QObqYlXc; CES-Surveys=muted; pageLoads=1; SSOD=AFkeAAAAEgD-HQAAAgAAAFQ3F2VjNxdlAgAAAA; SSPV=07kAAAAAAAIABAAAAAAAAAAAAAMAAAAAAAAAAAAA; nlbi_1876175_2147483392=wT3vFghSNwfLm11BJuxx+QAAAAAk63jDhIE5bvJrItmCP3rz; AWSALB=6jmSqdaXAc5km3VeuZPeXFmHhf+gL8hKtZaO+aHCnaWA6hWRmjlVd/6s5iHT1dGst/hVS+Brlrlo6gPxuQ2aUDguVg9Wj8heYVgeekcNNeRIKKIao+qD5xA1LMlf; AWSALBCORS=6jmSqdaXAc5km3VeuZPeXFmHhf+gL8hKtZaO+aHCnaWA6hWRmjlVd/6s5iHT1dGst/hVS+Brlrlo6gPxuQ2aUDguVg9Wj8heYVgeekcNNeRIKKIao+qD5xA1LMlf',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.plus.nl/aanbiedingen',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://www.plus.nl/aanbiedingen', cookies=cookies, headers=headers)