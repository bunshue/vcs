"""
WhatsApp

pip install emoji==1.7.0

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import re
import regex
import emoji
import plotly.express as px
from collections import Counter
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def startsWithDateAndTime(s):
    pattern = "^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -"
    result = re.match(pattern, s)
    if result:
        return True
    return False


startsWithDateAndTime("7/26/18, 22:51 - Bobby: This message was deleted")


def FindAuthor(s):
    s = s.split(":")
    if len(s) == 2:
        return True
    else:
        return False


def getDataPoint(line):
    splitLine = line.split(" - ")
    dateTime = splitLine[0]
    date, time = dateTime.split(", ")
    message = " ".join(splitLine[1:])
    if FindAuthor(message):
        splitMessage = message.split(": ")
        author = splitMessage[0]
        message = " ".join(splitMessage[1:])
    else:
        author = None
    return date, time, author, message


data = []  # List to keep track of data so it can be used by a Pandas dataframe
parsedData = []
conversation = "data/whatsapp-chat-data.txt"

with open(conversation, encoding="utf-8") as fp:
    fp.readline()  # Skipping first line of the file because contains information related to something about end-to-end encryption
    messageBuffer = []
    date, time, author = None, None, None
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if startsWithDateAndTime(line):
            if len(messageBuffer) > 0:
                parsedData.append([date, time, author, " ".join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message = getDataPoint(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

# Upload widget is only available when the cell has been executed in the current browser session. Please rerun this cell to enable.

df = pd.DataFrame(
    parsedData, columns=["Date", "Time", "Author", "Message"]
)  # Initialising a pandas Dataframe.
df["Date"] = pd.to_datetime(df["Date"])
cc = df.tail(20)
print(cc)

cc = df.info()
print(cc)

cc = df.Author.unique()
print(cc)

df = df.dropna()
cc = df.info()
print(cc)

total_messages = df.shape[0]
print(total_messages)

media_messages = df[df["Message"] == ""].shape[0]
print(media_messages)


def split_count(text):
    emoji_list = []
    data = regex.findall(r"\X", text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    return emoji_list


df["emoji"] = df["Message"].apply(split_count)


emojis = sum(df["emoji"].str.len())
print(emojis)


URLPATTERN = r"(https?://\S+)"
df["urlcount"] = df.Message.apply(lambda x: re.findall(URLPATTERN, x)).str.len()


links = np.sum(df.urlcount)


print("Data science Community")
print("Messages:", total_messages)
print("Media:", media_messages)
print("Emojis:", emojis)
print("Links:", links)


media_messages_df = df[df["Message"] == ""]


messages_df = df.drop(media_messages_df.index)


cc = messages_df.info()
print(cc)


messages_df["Letter_Count"] = messages_df["Message"].apply(lambda s: len(s))
messages_df["Word_Count"] = messages_df["Message"].apply(lambda s: len(s.split(" ")))
messages_df["MessageCount"] = 1

cc = messages_df.tail(20)
print(cc)

l = ["Aman Kharwal", "Sahil Pansare", "Sumehar"]
for i in range(len(l)):
    # Filtering out messages of particular user
    req_df = messages_df[messages_df["Author"] == l[i]]
    # req_df will contain messages of only one particular user
    print(f"Stats of {l[i]} -")
    # shape will print number of rows which indirectly means the number of messages
    print("Messages Sent", req_df.shape[0])
    # Word_Count contains of total words in one message. Sum of all words/ Total Messages will yield words per message
    words_per_message = (np.sum(req_df["Word_Count"])) / req_df.shape[0]
    print("Words per message", words_per_message)
    # media conists of media messages
    media = media_messages_df[media_messages_df["Author"] == l[i]].shape[0]
    print("Media Messages Sent", media)
    # emojis conists of total emojis
    emojis = sum(req_df["emoji"].str.len())
    print("Emojis Sent", emojis)
    # links consist of total links
    links = sum(req_df["urlcount"])
    print("Links Sent", links)
    print()


total_emojis_list = list(set([a for b in messages_df.emoji for a in b]))
total_emojis = len(total_emojis_list)
print(total_emojis)


total_emojis_list = list([a for b in messages_df.emoji for a in b])
emoji_dict = dict(Counter(total_emojis_list))
emoji_dict = sorted(emoji_dict.items(), key=lambda x: x[1], reverse=True)
for i in emoji_dict:
    print(i)

emoji_df = pd.DataFrame(emoji_dict, columns=["emoji", "count"])
print(emoji_df)

import plotly.express as px

fig = px.pie(emoji_df, values="count", names="emoji")
fig.update_traces(textposition="inside", textinfo="percent+label")
fig.show()


text = " ".join(review for review in messages_df.Message)
print("There are {} words in all the messages.".format(len(text)))
stopwords = set(STOPWORDS)
# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
# Display the generated image:
# the matplotlib way:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# There are 160610 words in all the messages.

"""
l = ["Aman Kharwal", "Sahil Pansare", "Sumehar"]
for i in range(len(l)):
    dummy_df = messages_df[messages_df['Author'] == l[i]]
    text = " ".join(review for review in dummy_df.Message)
    stopwords = set(STOPWORDS)
    #Generate a word cloud image
    print('Author name',l[i])
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    #Display the generated image
    plt.figure( figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
