import time 
import pandas as pd
from selenium import webdriver

def readExcel():
    df=pd.read_csv('Anand11.csv')
    name=df['name']
    team=df['team']
    beat_amount=df["beat"]
    winning_amount=df['winning Amount']
    return name,team,beat_amount,winning_amount

# def downloadUrl(url):
#     driver=webdriver.chrome()
name,team,beat_amount,winning_amount=readExcel()
print(name,team,beat_amount,winning_amount)