import discord
from discord.ext import commands, tasks
import uuid
from requests import get
import requests
import shutil
import asyncio
import youtube_dl
import re
import os
from urllib.request import urlopen, Request
import youtube_dl   
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote_plus
import datetime
import time
import pickle
from random import choice
import random
import base64
import validators
import ssl
from urllib.parse import quote
import psycopg2
import pixiv_crawler as pc

ssl._create_default_https_context = ssl._create_unverified_context
#from selenium import webdriver
donggu=['https://lh3.googleusercontent.com/yLfpCS130VZkw8yOXHmZklJOKp2weknPMh3tVW6DD1rZBUQx95bNdZKrR6-C6PLLT0thaw9qU4K5o65_4Lm8mYR3RQYeR9iVEgzTmflIokdNfiexYcvOVgxTw3O6SsjOcolfD4nUq8QL3OmISUPVrn0h60yZ_e8YZxDfqAFmehwrime10nxEzXBiq-F-spSttfOXHNy8PTEYNvE0RbOM4lRn-80L3gnidPZ0nAZEeLPcu4Tw1KHd66C243iRRb0HcfLoQzzzNhw7nrBnboz2ij9g5Z4wyervc1fZyoUpxh-lW2RTuv6NtLunsXcN9REdfAecPiujJ3F9sPdURPKtaEtGVCbGaF_jhVsHxxGE4OUhcdeMkX07QVCYEsLa9GmhX2XkWU9CUOjp-rkvfKX1g1WGY81q4Sxm6wuUiIGtNbCELLStmmmpxvfTCLHwhD7Mow3kZFmHwgZWbzz9ghYt7wEJ5Ix9oZiZ1OF7bzNqI7qM437Df-bsLqIJFqorYv0wmaIvOrKXgQ3fGRxFdiUvk9Ptfbn2XfNJhs_oLmnWj67fMck1kptKh1nTE2cKU1wTKkYyY7EqXdWhM4TiDQ-MfVPKtVdfMCnrQE413GcdzE89fFW-ZsZ6B5oPX21pKElamyfnm0QksC_1FIe7pkXlI4OVc3CvDyhD3LtnA8WFedgwUgoYVLiIODaSlYu07yhquimB1v4ZgR-KIz5il2x3aV-Nh-9zBYnJxnhy7qBD4siHMOHVYztE9OXvdU5IeRjyxL9e_IcxFfLM-chQ=w386-h289-no?authuser=0','https://lh3.googleusercontent.com/36LCDTe2xXycGY9Vvz4l114EBD0g-QSZAHlkk6Hbc47UxpmeLlTpXLR7vwDBMOjD18_FFeG-DUxXKsRaIGC5mpLoQhO2cYwyxZo562fSITwKx6JYbEM5CvxQag7TXZvjd28Z6t0kx32hJ_cy9M2Rt2O3VScm0wtEg8xiPEDQSNqY5SuUn2MX_mThIU2ePbahdLSERUpbtdKaDIQ3z82HayY7hzWuOU21PfQQ5JLFRdaCc-6SW6BRzyQhDcWEPS3kfIr3rSBs5m9Q9EbzE_ghUWLWXrVQ5Fs2kKMfIMkX-3Y7xcIwApi6cCDtX8aMoNyRqlnxmVS7_KyeFNbsmn90vxbuPG5LGKc_ux1OjQN52R6FRitdeaoUvcVCL0QrH9C3Q_vAizKyDB3PqMkq0pF7JLU7R4w-Zom55-ZkcRCtKo_69rYUhATP60HXhPEY-mG0c9qt1dTIFKQpsYkarr8rAMWzG8QAOK2nzDnZUa7k-yXEc6mFMxb4jTT7jI-T1Cf-I-nygGC2YFUCbZPnODFURXEH6gAKNjX5PvMM7boVwS_uQV7SjNW2i6ftRdvtSNkuJKbjyRe-_1tkF88iW0xAHICOQDjfNhpzugR7d5fJTIHTAo-r835GTAtXWof1eLV7abHE7ZC1JJMijnsN_OIiW7rcomd25F6rjxByYESFfoGHpMoKPM-GDTfqddbLJrJX6GpsvxVmqOsPgCmQ6yiXKdKTAVYa1hc1HHOYCk48fDTHBCuFAERMm9dqJP_0UZ7xcipxJ_cTRu_s2nu6=w434-h325-no?authuser=0','https://lh3.googleusercontent.com/ysA0uJp626Xv-CFufLjMX25zilDyX7LFkJJkRtKnXyYPuBD3-CCtFKn-8DLQ6nuUgCiEuvCdDiSV748r8ZXPqySHnB-ERvMOXuPO9QnzNV_GdbFteFJajoKEzTqyL-buS_Gfv42pGLejChOeh6ZJc9eCnn4ov9kcsvA6OiQFcYKCOMmk47CvNAAlmX1Xsntbt0idqrd7NEovL5ve0jerUXtVnwAAEltwPSrOmZafA0-bsmk4vpnuLSpN_0M8bfyLWn8WUWVzmcY3ehf5GBu85g9VOggIXh8XkE9tQqbHC6gSufGKffJ8u_pHFb3jJyxrwmYvPB778YTxm8CEvV23-hT1SnEVhwweeJZKxfdst18GYQYgAYnYI4o5Zn2QVI1qGGSrM6EoInu3b9E8E06OjQJY_B_8ZYqX_rcYau4xh0ywJmhUMeT0pbBWhCG771R1S0Qg8avVvAtTfPg-9U52XSjhS0-vu5xR_-Ngn1-oImJvaYEPRUoOgpDdz8k24_Deqn1CfH4DIfQEKF-6XWzRNlJakStx3HUYyfzuL8XNjrOoNcGgf0XL-eb2-H-CWN-z_RMrZqwIUkEA0EVR5y06xQL3zMz06dMlPENZbMHgE9jj9EN0pI3fzEIddzorFBTdo0Ng2ECLMbVZ7lBaLP_K2VWQ_Q4EhEAgg_UZo2ZBRilbez0lrC3V5aQDQ0ePA1NAr2oMrohMBAr1EYX9_wHOewohgY4vPQz2qfD0mte05p3YkKx0r34W6dCdLIx0tcfHhcJpn2JSkojTsB2d=w245-h325-no?authuser=0','https://lh3.googleusercontent.com/amJhq3KsvZvrPeYtXvAcVc2mqLCSk3BUzfJh6vgMwdagYraVr5e22r76N0ddwD1HjbNoTwYVR4Zxogj0nI_E7vinbkdlOCjYW-bIHr-FYbDedStvu8boO4RYENlkQQt_9KFI1wnA5euon5IA5RedPnnbXQVdX7K7tfzFZWWRmbqee9ChAwE0lPW_YkCc1Is8qxJvupWGqhig5ZjqSHGxo1A_bs4yDntKHQpqv9QnBhRUBQg12q95dViv6GWGL8bTwYrLkdmlOL_s31GXQz9JIliAsRG-rxmngSjH_vsCVMOQlVLYFfH5YAfP_M-ejKDlp9OomOeKR4iHRfH3ElNik4EtmlcvbEbO-bWRKwYWiiJfjmIB9F4lbmG_rMNA1lfKjXttCSEcyu004L1-CPFbj-CK5ihFH94_NuxFQbZwgX1rLZ6o6DhvBwQh0PryLx3QEmcm7QABxjzteOqt9kBZf7KYHMh6d_iH8frZIo4R8g4T7PfA4_B7-ksvIyOYGfF1LmG7i1duF6f8eIqVPXptHNwJ8S46xj410gL5AzMhuP3siPCWtgDwmKzQzXXeo97EJXM1rfJP_yKpmGB5r5gmCKhZcam5WCSpJ4bi1AzJiZbbbUXm9HDwYy0IVNjf_dxiS8j8dwz8P9m4c2Sk657weDhlzY1LZm611ZL5o4ZTWVuNGfLjZWBscbP8e72uFDppYu9Dicu0P_8W4nQZrhP9sDtOjt2EvgN6Okk5VzgTy0kXezkOgvClWFGFNpKqzqbhdM8E9hnCojsTzjtn=w244-h325-no?authuser=0']
pagenum=1
nummer=0
dic=[]
bad = ['??????','??????','??????']
status=['??????', '????????????', '????????????', '?????? ???????????????']
from googleapiclient.discovery import build


#DATABASE_URL = os.environ['postgres://zzysgozigaqerq:55d69d43eba241b68f7bf1f03ef7b28c689e278d4bfb688e3283ce5b69f8944b@ec2-54-155-254-112.eu-west-1.compute.amazonaws.com:5432/d33us2htjq962o']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')


app = commands.Bot(command_prefix = "!")
 
@app.event
async def on_ready():
    change_status.start()
    print('???????????? ??????????????????: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

'''@app.event
async def on_message(message): ##### remove bad words
    message_contant=message.content 
    for i in bad:
        if i in message_contant:

            await message.channel.send(message.author.mention+'?????? ?????? ?????? ??? ????????????.')
        await app.process_commands(message)'''
           



@tasks.loop(seconds=50)
async def change_status():
    await app.change_presence(activity=discord.Game(choice(status)))




@app.command()
async def ??????(ctx):
    await ctx.send(random.choice(donggu))

@app.command()
async def ???(ctx):
    await ctx.send(ctx.message.author.mention+f'????????????: {round(app.latency* 1000)}ms')

@app.command()
async def ?????????(ctx):
    api_key = 'AIzaSyDzIOd6FSfBnf_1dkKUe-NJfcGLF18-d9A'

    #service build
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='statistics',
        id='UCD6rjjj15pZeWkJnTUdb5OA'
    )

    response = request.execute()
    subs=response["items"][0].get("statistics")["subscriberCount"]
    #print(type(response)) #dict
    print(subs)
    await ctx.send(f'Kumori ?????? ?????? ????????? ?????? {subs} ??? ?????????!')




@app.command() 
async def hello(ctx):
    await ctx.send('??????????????? ???????????? ????????? ???????????? ????????? ?????????.')
     

@app.command()
async def ??????(ctx):
    embed = discord.Embed(title='????????? ?????? ?????? ???????????????',description='????????? ??????', color = 0x00ff00)
    embed.set_thumbnail(url='https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F150D130F4A1B6D7FAB')
    await ctx.send(embed=embed)

@app.command()
async def ?????????(ctx):
        res = requests.get("https://capi.msub.kr/").json()
        embed = discord.Embed(title="????????? API", description=res["status"], color = 0xe74c3c)
        embed.add_field(name="?????????", value=res['today']["confirmation"], inline=True)
        embed.add_field(name="?????? ??????", value=res['today']["cured"], inline=True)
        embed.add_field(name="?????????", value=res['today']["dead"], inline=True)
        embed.add_field(name="??????", value=res['today']["isolation"], inline=False)
        embed.set_footer(text=res['today']["update"])
        await ctx.channel.send(embed=embed)


@app.command()
async def ??????(ctx):
    url = "https://api.hangang.msub.kr/"
    fp = requests.get(url).json()

    
    #time.sleep(10)
    #soup=BeautifulSoup(source, 'lxml')
  
    print(fp["temp"])
    await ctx.send(f'?????? ?????? ????????? {fp["temp"]} ??C ?????????.')
#??????
@app.command()
async def ??????(ctx, word, url):
    global dic
    with open('DIC.txt', 'rb') as f:
        dic=pickle.load(f)


    if word not in dic:
        dic.append(word)
        dic.append(url)
        await ctx.send(word +" (???)??? ????????? ?????? ???????????????")
        with open('DIC.txt', 'wb') as e:
            pickle.dump(dic, e, protocol=pickle.HIGHEST_PROTOCOL)
        print (dic)
        
    else:    
        await ctx.send(word + " (???)??? ?????? ???????????? ?????? ?????????.")

@app.command()
async def ??????(ctx, word):
    global dic
    with open('DIC.txt', 'rb') as f:
        dic=pickle.load(f)
    
    if word in dic:
        await ctx.send(dic[dic.index(word)+1])
    
    else:
        await ctx.send(word + "(???)??? ?????? ??? ????????????.")
    
@app.command()
async def ??????(ctx, word):
    global dic
    with open('DIC.txt', 'rb') as f:
        dic=pickle.load(f)
    if word in dic:
        del dic[dic.index(word)+1]
        dic.remove(word)
        
        await ctx.send(word + " (???)??? ?????? ????????????.")
        with open('DIC.txt', 'wb') as e:
            pickle.dump(dic, e, protocol=pickle.HIGHEST_PROTOCOL)
    
@app.command()
async def ??????(ctx):
    with open('DIC.txt', 'rb') as f:
        dic=pickle.load(f)
    for i in dic:
        
        print (i)
        await ctx.send(i)   

#?????????
@app.command()
async def ?????????(ctx):
    global nummer
    global pagenum
    #headers={'User-Agent': 'Mozilla/5.0'}
    #??????????????? ????????? ????????????.
    url = "https://nhentai.to/?page=" + str(pagenum)
    fp = Request(url, headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AookeWebKit/537.36 (KHTML, like Gecko) Chrome/ 84.0.4147.105 Safari/537.36'})
    source = urlopen(fp, timeout=8).read()

    #???????????? img_area ????????? ????????? ????????? ????????????.
    soup = BeautifulSoup(source, 'lxml').find("div", class_= "container index-container")
    soup = soup.find("a", class_ = "cover")

    #????????? ????????? ?????? ????????? ????????????.
    imgURL = soup.find("img")["data-src"]
    #print (imgURL)
    #urllib.request.urlretrieve(imgURL,'00001.jpg')
    if nummer >=10:
        await ctx.send("????????? ?????? ??? ?????????")
        pagenum +=1
        print(pagenum)
        print(url)

    else:    
        await ctx.send(imgURL)
        nummer+=1
        pagenum +=1
        print(pagenum)
        print(url)


@app.command()
async def ??????(ctx, tag):
            tag = tag
            ret = random.choice(requests.get("https://gelbooru.com//index.php?page=dapi&s=post&q=index&json=1&tag=" + tag).json())
            embed = discord.Embed(title="Gelbooru API").set_image(url=ret["file_url"])
            embed.set_footer(text=ret["created_at"])
            await ctx.channel.send(embed=embed)



@app.command()
async def hitomi(ctx):
    pagen=0
    key = 'language%3Akorean%24'
    await ctx.send("????????? ?????? 6??? ????????? ???????????????.")
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    titles=[key]
    
    for b in titles:
        m=0
        
        
        url = ("https://e-hentai.org/?f_cats=1017&f_search="+b)
        print(url)

        fp = Request(url, headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AookeWebKit/537.36 (KHTML, like Gecko) Chrome/ 84.0.4147.105 Safari/537.36'})
        #dd = webdriver.Chrome(executable_path='chromedriver', options=options)
        #dd.get(url)
        source = urlopen(fp, timeout=8).read()
        #print(source)
        #???????????? img_area ????????? ????????? ????????? ????????????.
        soup = BeautifulSoup(source, 'lxml')
        time.sleep(1)
        #print(soup.prettify())
        soup1 = soup.findAll("td", class_= "gl3c glname")
        soup = soup.findAll("div", class_= "glthumb")
        #print(soup1)
        #soup = soup.find("a")
        #print (soup)
        #????????? ????????? ?????? ????????? ????????????.
        if m<=6:
            for x in soup1:
                link=x.find("a")['href']
                print (link)
                
                
            for i in soup:
            
                title = i.find("img")["alt"]
                img= i.find("img")['src']
                key=quote(title.replace(" ", ""))
                titles.append(key)
                
                
            for r in soup:
                
                img= r.find("img")['src']
                
               
                embed = discord.Embed(title=title, color=0xF361A6)
                embed.set_image(url=img)
                embed.add_field(name="??????", value=link, inline=False)
                await ctx.send(embed=embed)  
                m+=1
                break
        
        pagen+=1
        if pagen >=7:
            break
                    
        '''  '''

                
                
                    
                    
                        
            
    


            

        





#memes
@app.command()
async def ??????(ctx):
    await ctx.send('https://media.discordapp.net/attachments/389802029456949250/734793035811913798/image0.gif')


for filename in os.listdir("Cogs"): #2
    if filename.endswith(".py"): #3
        app.load_extension(f"Cogs.{filename[:-3]}") #4


@app.command()
async def ????????????(ctx):
    sampics = random.choice(["https://www.the-sun.com/wp-content/uploads/sites/6/2021/06/KB_COMP_Samsung-samantha-1.jpg", 'https://img.mbn.co.kr/filewww/news/2021/06/07/162305127060bdcc06d7d22.jpg', 'https://i2.ruliweb.com/img/21/06/02/179cc3e1d4350ce91.jpeg'])
    embed = discord.Embed(title='SAM',description='Serviceable Artificial feMale',timestamp=datetime.datetime.now(), color = 0x00aaaa)
    embed.add_field(name="!??????", value="?????? ????????? ???????????????.", inline=False)
    embed.add_field(name="!play", value="????????? ?????? ?????????.", inline=False)
    embed.add_field(name="!??????", value="????????? ????????? ???????????????.", inline=False)
    embed.add_field(name="!??????", value="????????? ???????????????.", inline=False)
    embed.add_field(name="!??????", value="?????? ???????????? ????????????.", inline=False)
    embed.add_field(name="!?????????", value="??????", inline=False)
    embed.add_field(name="!??????", value="????????? ???????????????.", inline=False)
    embed.set_author(name="????????????",icon_url='http://www.businesspost.co.kr/news/photo/201804/20180417205023_15744.jpg')
    embed.set_thumbnail(url='https://img.hankyung.com/photo/202106/01.26562695.1.jpg')
    embed.set_image(url=sampics)
    embed.set_footer(text="Ver. 0.0a   Devloped by Pix")
    await ctx.send(embed=embed)
''''''
#music player
'''@app.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if app.voice_clients == []:
    	await channel.connect()
    	await ctx.send("?????? ????????? ?????? ???, " + str(app.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio', 'default_search': 'auto'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(info)
        URL = info['formats'][0]['url']
        print(url)
    await ctx.send(f"?????????: {info['title']}")
    voice = app.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))'''
''''''
    
@app.command(name="??????")
async def load_commands(ctx, extension):
    app.load_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark: {extension}???(???) ??????????????????!")



"""@app.command(pass_context=True)
    async def play2(ctx, url):
    server = ctx.author.voice.channel
    await app.say ('Music now playing...')
    voice_client = app.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, ytdl_options={'default_search': 'auto'} after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()"""

@app.command()
async def ??????(ctx):
	await app.voice_clients[0].disconnect()
@app.command()
async def ??????(ctx):
    if not app.voice_clients[0].is_paused():
        app.voice_clients[0].pause()
    else:
        await ctx.send("already paused")

@app.command()
async def ??????(ctx):
    if app.voice_clients[0].is_paused():
        app.voice_clients[0].resume()
    else:
        await ctx.send("?????? ?????? ??? ?????????.")

@app.command()
async def stop(ctx):
    if app.voice_clients[0].is_playing():
        app.voice_clients[0].stop()
    else:
        await ctx.send("??????.")

@app.command()
async def ??????(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("?????? ????????? ???????????????.")
        




app.run('')

