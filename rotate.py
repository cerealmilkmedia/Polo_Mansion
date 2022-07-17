import requests

proxy = '216.137.184.253:80'

r = requests.get('http://www.google.com', proxies={'http': proxy, 'https': proxy})
print(r.status_code)


# <Proxy US 0.11s [HTTPS] 64.189.24.250:3129>
# <Proxy US 0.13s [HTTP: High, HTTPS] 198.41.67.18:8080>
# <Proxy US 0.13s [HTTPS] 162.214.193.59:3128>
# <Proxy US 0.34s [HTTPS] 20.81.62.32:3128>
# <Proxy US 0.70s [HTTPS] 209.182.235.252:3128>
# <Proxy US 1.51s [HTTPS] 20.203.160.74:3128>
# <Proxy US 0.06s [HTTP: High] 20.47.108.204:8888>
# <Proxy US 0.06s [HTTP: High] 20.110.214.83:80>
# <Proxy US 0.07s [HTTP: High] 198.199.86.11:3128>
# <Proxy US 0.10s [HTTP: High] 34.75.123.131:80>
