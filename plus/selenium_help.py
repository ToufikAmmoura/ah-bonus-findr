# simple function to change cURL cookies to the format that Selenium needs

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

cookies_list = [{"name": key, "value": value} for key, value in cookies.items()]

# Print the result for visualization
for item in cookies_list:
    print('driver.add_cookie(',item,')', sep='')