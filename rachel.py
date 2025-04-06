import streamlit as st
import random
st.set_page_config(
    page_title="It's ok sweetheart",
    layout="wide",
    page_icon="content/BubbleTea.ico",
    initial_sidebar_state="expanded"
    
)

a,b=st.tabs(["Need love ? ","Need wisdom ? "])


def recup(path):
      fichier=open(path,encoding="UTF-8")
      dat=fichier.read()
      fichier.close()
      dat=dat.split("\n")
      return dat
love=recup("love.txt")
wisdom=recup("wisdom.txt")
#                 A   -   Love
l_text=""
love_b=a.button("Click here for some love")

if love_b:
      l_text=love[random.randint(0,len(love)-1)]
a.text(l_text)

#                 B   -   Wisdom
w_text=""
wisdom_b=b.button("Click here for some wisdom")

if wisdom_b:
      w_text=wisdom[random.randint(0,len(wisdom)-1)]
      
b.text(w_text)

