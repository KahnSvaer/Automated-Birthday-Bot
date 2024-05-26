@echo off

taskkill /F /IM chromedriver.exe
taskkill /F /IM chrome.exe

python D:\Projects\Self\BirthdayBot\main.py

taskkill /F /IM chromedriver.exe