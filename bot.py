import telebot
import requests,random

import os
os.system('pip3 install -r requirements.txt')
os.system('pip install -r requirements.txt')

auth='6813197862:AAGrypDMrwc_rA697332St3TFfua7ATOIbQ'

bot = telebot.TeleBot(auth) # creating a instance
def tc(x,y):
  num=y

  r=requests.request('POST','https://calltracer.in/',data={'country':x,'q':num})
  a=r.content

  g=str(str(a).split('<td>')[2]).split('<')[0]

  i=str(a).split('<td>')[5].strip("</td>")

  j=str(str(a).split('<td>')[6]).strip('</small></td></tr><tr>')

  k=str(a).split('<td>')[7].split('<')[0]
  l=str(a).split('<td>')[8].split('>')[1].split('<')[0]

  m=str(a).split('<td>')[9].strip("</td>")

  n=str(a).split('<td>')[10].split('>')[1].split("<")[0]

  o=str(a).split('<td>')[11].split("<")[0]

  p=str(a).split('<td>')[12].split("<")[0]

  q=str(a).split('<td>')[13].split("<")[0]

  r=str(a).split('<td>')[14].split("<")[0]

  s=str(a).split('<td>')[15].split("<")[0]

  t=str(a).split('<td>')[16].split("<")[0]

  u=str(a).split('<td>')[17].split("<")[0]

  v=str(a).split('<td>')[18].split("<")[0]
  w=str(a).split('<td>')[19].split("<")[0]

  x=str(a).split('<td>')[20].split("<")[0]

  y=str(a).split('<td>')[25].split("<")[0]
  z=str(a).split('<td>')[26].split("<")[0]
  msg=f'''NUM :{g}
  {i} : {j}
  {k}  : {l}
  {m} : {n}
  {o}  : {p}
  {q} : {r}
  {s} : {t}
  {u} : {v}
  {w} : {x}
  {y} : {z}
  
  '''
  return msg

@bot.message_handler(commands=["start"])
def runner(message):

  bot.reply_to(message," call tracer tool made by hacker X ~ Deleted Account /help for more info ")


@bot.message_handler(commands=["help"])
def nner(message):
  bot.reply_to(message,"""/run country_name number_without_+
  /run IN 73870#####
  AU,US,UK,BR,MX,DE,CH  only
  its mainly for these """)

@bot.message_handler(commands=["run",'run_tool','rn'])
def xrn(message):
  ex=message.text.split()
  kx=tc(ex[1],ex[2])

  bot.reply_to(message,kx)

  

bot.infinity_polling() # looking for message
