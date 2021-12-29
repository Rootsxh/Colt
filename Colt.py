from time import monotonic
from urllib import request
from os import system, makedirs 

proxies_creator = """




                        ______     ______     __         ______  
                       /\  ___\   /\  __ \   /\ \       /\__  _\ 
                       \ \ \____  \ \ \/\ \  \ \ \____  \/_/\ \/ 
                        \ \_____\  \ \_____\  \ \_____\    \ \_\ 
                         \/_____/   \/_____/   \/_____/     \/_/ 
                                         

			        by https://github.com/SAIHTAMcfg



"""

http_links = [
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
]

https_links = [
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
]

socks4_links = [
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
]

socks5_links = [
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
]

def getchecked(proxies_unchecked:list, timeout:int, limit:int, url:str, _type:str):
	i = 0
	number = len(proxies_unchecked)
	makedirs("checked_proxies/", exist_ok=True)
	
	for proxy in proxies_unchecked:
		proxy_handler = request.ProxyHandler({
		"http": "http://" + proxy,
		"https": f"{_type}://" + proxy,
		})

		opener = request.build_opener(proxy_handler)
		opener.addheaders = [('User-Agent', 'Mozilla/5.0  (Windows NT 6.1; Win64; x64)')]
		request.install_opener(opener)

		try:
			before = monotonic()
			response = request.urlopen(url, timeout=timeout)

			i += 1
			print(f"\033[32m[+] {i}/{number} | {proxy} | timeout = {int(monotonic() - before)}\033[0m")

			with open(f"checked_proxies/{_type}_checked_proxies.txt", "a+") as file:
				file.write(proxy + "\n")

		except:
			print(f"\033[31m[-] {i}/{number} | {proxy} | timout = {int(monotonic() - before)}\033[0m")

		if limit:
			if limit == i:
				break

	print(f"\033[34m\n{i} Proxies Checked!\033[0m")
	input()

def getunchecked(_list:list, timeout:int, limit:int, url:str, _type:str):
	j = 0
	proxies_unchecked = []
	makedirs("unchecked_proxies/", exist_ok=True)

	for url in _list:
		try:
			req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})  
			response = request.urlopen(req).read().decode("utf-8")

		except:
			pass

		else:
			for proxy in response.splitlines():
				proxies_unchecked.append(proxy)

	with open(f"unchecked_proxies/{_type}_unchecked_proxies.txt", "w") as file:
		file.write(str(proxies_unchecked))

	system("cls")
	print(proxies_creator)
	getchecked(proxies_unchecked=proxies_unchecked, timeout=timeout, limit=limit, url=url, _type=_type)

def main():
	system("")

	while True:
		system("cls")
		system("color d")
		print(proxies_creator)

		choice = input("Que voulais vous ? [all, http, https, socks4, socks5] >>> ")
		timeout = int(input("temps >>> "))
		limit = input("limite de Proxy >>> ")

		if limit.lower() in ["n", "no", "none"]:
			limit = None

		if choice == "all":
			getunchecked(_list=http_links, timeout=timeout, limit=limit, url="http://info.cern.ch/", _type="http")
			getunchecked(_list=https_links, timeout=timeout, limit=limit, url="https://google.com", _type="https")
			getunchecked(_list=socks4_links, timeout=timeout, limit=limit, url="https://google.com", _type="socks4")
			getunchecked(_list=socks5_links, timeout=timeout, limit=limit, url="https://google.com", _type="socks5")

		elif choice == "http":
			getunchecked(_list=http_links, timeout=timeout, limit=limit, url="http://info.cern.ch/", _type="http")

		elif choice == "https":
			getunchecked(_list=https_links, timeout=timeout, limit=limit, url="https://google.com", _type="https")

		elif choice == "socks4":
			getunchecked(_list=socks4_links, timeout=timeout, limit=limit, url="https://google.com", _type="socks4")

		elif choice == "socks5":
			getunchecked(_list=socks5_links, timeout=timeout, limit=limit, url="https://google.com", _type="socks5")

		else:
			continue

		restart = input("Voulais vous recommencer ? [y/n]")
		if restart.lower() not in ["y", "yes"]:
			break

	exit("Good Bye")

main()
