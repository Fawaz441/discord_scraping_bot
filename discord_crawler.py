import time
import discord
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

client = discord.Client()
options = Options()
options.headless = True             #set to true if you want to see the browser
options.add_argument("--window-size=1920,1200")
driver_path = "C:/Users/user/Desktop/bot/chromedriver"    #your chromedriver.exe path
browser = webdriver.Chrome(executable_path=driver_path, options=options)

def write_to_file(stock_name):
    url = 'the url you want to crawl '
    open('final.txt', 'w').close()      #clearing the file to store the crawled data
    browser.get(url)
    time.sleep(5)
    stuff_list = []
    h1 = browser.find_element_by_class_name(' element class name ')
    other_info = browser.find_element_by_class_name(' element class name ')
    news = browser.find_element_by_class_name(' element class name ')
    stuff_list.append(h1)
    stuff_list.append(other_info)
    stuff_list.append(news)
    g = open("final.txt","w+")
    for stuff in stuff_list:
        g.write(stuff.text)
    g.close()



@client.event
async def on_message(message):
    if message.content.startswith('.sh'):    #the command you want to use e.g if you want to use .ff DRSP set to .ff
        stock_name = str(message.content)
        stock_name = stock_name.split()
        stock_name = stock_name[1].upper()
        write_to_file(stock_name) 
        reader = open("final.txt","r")
        Lines = reader.readlines()
        for line in Lines:
            await message.channel.send(line.strip())
    elif message.content.startswith('hello'):
        await message.channel.send('hi,i am a bot')
    else:
        return 



client.run(' your discord client token ')