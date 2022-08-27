# -*- coding: utf-8 -*-

import re
import time
import os
import requests
import platform
import socket as sock
import hashlib
from base64 import b64encode, b64decode, encode
import codecs
import binascii
from sys import stdout, exit
import multiprocessing
import sys
from json import dumps
from faker import fork

try:
    import pip
except(NameError,KeyError,IOError):
    os.system("python -m pip install -U --force-reinstall pip")

try:
    packages = ["bs4","requests","ipaddress","ipinfo","faker"]
    pip.main(['install'] + packages + ['--upgrade'])
except(NameError,IOError,OSError):
    exit(f" Modules not installed, Please try again")

from datetime import datetime
now = datetime.now()

b = requests.get('https://api.ipify.org').text.strip()
ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}).json()['country_name'].lower()
hostname = sock.gethostname()
faker = fork()
ip_u = fork.ipv4()

AUTHOR = "Technical Abm"
GITHUB = "https://github.com/Technical-Abm"
FACEBOOK = "https://www.facebook.com/techabm"

def thumbnail():
    t01 =          "\t8888888888 888b    888  .d8888b."
    t02 =          "\t888        8888b   888 d88P  Y88b"
    t03 =          "\t888        88888b  888 888    888"
    t04 =          "\t8888888    888Y88b 888 888       "
    t05 =          "\t888        888 Y88b888 888       "
    t06 =          "\t888        888  Y88888 888    888"
    t07 =          "\t888        888   Y8888 Y88b  d88P"
    t07 =          '\t8888888888 888    Y888  "Y8888P" '
    t08 = "---------------------------------------------------"
    t09 = f" (~) Author : {AUTHOR}"
    t10 = f" (~) Github : {GITHUB}"
    t11 = f" (~) Page   : {FACEBOOK}"
    t12 = "---------------------------------------------------"
    t13 = f" Arch : {platform.uname()[4]}                    Tme : {now.strftime('%H:%M:%S')}    "
    t14 = f" Date : {now.strftime('%Y/%m/%d')}                 Rel : {ips}"
    t15 = f" Host : {hostname} \t           Ips : {ip_u}"
    t16 = "---------------------------------------------------"
    print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s"%(t01,t02,t03,t04,t05,t06,t07,t08,t09,t10,t11,t12,t13,t14,t15,t16))

class base64encode_decoode(object):
    def __init__(self) -> None:
        os.system("clear")
        thumbnail()
        print()
        print(" [1] Encode MD5 Text")
        print(" [2] Encode SHA1 Text")
        print(" [3] Encode SHA224 Text")
        print(" [4] Encode HEXADECIMAL Text")
        print(" [5] Exit")
        print("---------------------------------------------------")
        print()
        self.user = input(" Choose an option :- ")
        if "1" in self.user:
            os.system("clear")
            thumbnail()
            print()
            self.text = input(" Enter your text or file :- ")
            self.hax = hashlib.md5(self.text.encode())
            print()
            print(self.hax.hexdigest())
            print()
            input(" Press enter to save file ")
            time.sleep(3)
            ask_user()
        elif "2" in self.user:
            os.system("clear")
            thumbnail()
            print()
            self.ua = input(" Enter text or file name :- ")
            self.object = hashlib.sha1(self.ua.encode())
            print()
            print(self.object.hexdigest())
            print()
            input(" Press enter to save file ")
            time.sleep(3)
            ask_user()
        elif "3" in self.user:
            __hexcode__()
        elif "4" in self.user:
            os.system("clear")
            thumbnail()
            print()
            self.user = input(" Enter file name or text :- ")
            self.encode = binascii.hexlify(bytes(self.user, "utf-8"))
            self.encode = str(self.encode).strip("b")
            self.encode = self.encode.strip("'")
            self.encode = re.sub(r'(..)', r'\1 ', self.encode).strip()
            print(self.encode)
            input(" Press enter to save file ")
            time.sleep(3)
            ask_user()
        elif "6" in self.user:
            exit()

class __hexcode__(object):
    def __init__(self) -> None:
        os.system("clear")
        thumbnail()
        print()
        self.str = input(" Enter file name or any text :- ")
        self.has = hashlib.sha224(self.str.encode())
        print()
        print(self.has.hexdigest())
        input(" Press enter to save file ")
        time.sleep(3)
        ask_user()

if __name__ == '__main__':
    class ask_user(object):
        def __init__(self) -> None:
            os.system("clear")
            thumbnail()
            print()
            try:
                self.ask = input(" DO you want to save encode file :- ")
                if "yes" or "Yes" in self.ask:
                    os.system("clear")
                    thumbnail()
                    print()
                    self.encodes = input(" Enter your encode here :- ")
                    self.saves = input(" enter any file name to save encode :- ")
                    print()
                    self.jsonstringdata = dumps(self.encodes)
                    with open(self.saves,"w") as load:
                        load.write(self.jsonstringdata)
                        pass
                    time.sleep(2)
                    print(" Your file saved as :- "+self.saves)
                    pass
                elif "no" or "No" in self.ask:
                    print()
                    base64encode_decoode()
                    pass
                pass
            except(FileNotFoundError,FileExistsError):
                print()
                time.sleep(1)
                print(f" Your file is {self.saves} not found")
                time.sleep(1)
                base64encode_decoode()
    base64encode_decoode()
    #feel me more :)
