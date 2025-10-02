"""
XXX pip install gradio==3.1.0

pip install gradio==3.50.2

"""

import sys

print('------------------------------------------------------------')	#60個

"""
import gradio as gr

def replace1(text):
  return text.replace('morning', 'evening')

grobj = gr.Interface(fn=replace1, inputs=gr.inputs.Textbox(), outputs=gr.outputs.Textbox())
grobj.launch()

print('------------------------------------------------------------')	#60個

"""

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

#手寫數字
import tensorflow as tf
from urllib.request import urlretrieve
import gradio as gr

# Loading the MNIST model and data
# 可下載最新之 .h5 檔案
# urlretrieve("https://gr-models.s3-us-west-2.amazonaws.com/mnist-model.h5", "mnist-model.h5")
# mnist-model.h5 路徑不能含中文
mnist_model_filename = "D:/_git/vcs/_big_files/mnist-model.h5"
model = tf.keras.models.load_model(mnist_model_filename)

def mnist(image):
    image = image.reshape(1, -1)  #(28,28)轉為(1,784)
    prediction = model.predict(image).tolist()[0]
    return {str(i): prediction[i] for i in range(10)}

out = gr.outputs.Label(num_top_classes=3, label='預測結果')
grobj = gr.Interface(fn=mnist, inputs="sketchpad", outputs=out, title="手寫數字")
#grobj = gr.Interface(fn=mnist, inputs="sketchpad", outputs=out, title="手寫數字", live=True)
grobj.launch()

print('aaaa')

sys.exit()


print('------------------------------------------------------------')	#60個

# Inception圖片物件偵測

import tensorflow as tf
import numpy as np
import requests
import gradio as gr

model = tf.keras.applications.InceptionV3()
#讀取標籤
response = requests.get('https://git.io/JJkYN')
labels = response.text.split('\n')
#print(labels)

def classify(img):
  img = np.expand_dims(img, 0)
  img = tf.keras.applications.inception_v3.preprocess_input(img)
  prediction = model.predict(img).flatten()
  return {labels[i]: float(prediction[i]) for i in range(len(prediction))}

image = gr.inputs.Image(shape=(299, 299))
label = gr.outputs.Label(num_top_classes=3, label='預測結果')
grobj = gr.Interface(fn=classify, inputs=image, outputs=label, title='Inception物件偵測')
#grobj = gr.Interface(fn=classify, inputs=image, outputs=label, title='Inception物件偵測', examples=[['lion1.jpg'], ['tiger1.jpg']])
grobj.launch()


print('------------------------------------------------------------')	#60個

"""
#英文對話(GPT-2)
# pip install git+https://github.com/huggingface/transformers.git

import gradio as gr
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

def generate_text(inp):
    input_ids = tokenizer.encode(inp, return_tensors='tf')
    beam_output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    output = tokenizer.decode(beam_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return output[:-1]

out = gr.outputs.Textbox(label='GPT-2回應')
grobj = gr.Interface(generate_text,inputs="textbox", outputs=out, title="GPT-2")
grobj.launch()
"""

print('------------------------------------------------------------')	#60個

#自動歌詞產生器

import gradio as gr

grobj = gr.Interface.load("huggingface/uer/gpt2-chinese-lyric", inputs="text", outputs="text")
grobj.launch()

#pip install opencc

import gradio as gr
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline
from opencc import OpenCC

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-lyric")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-lyric")
cc = OpenCC('s2twp')

def generate_text(inp):
    text_generator = TextGenerationPipeline(model, tokenizer)
    ret = text_generator(inp, max_length=100, do_sample=True)
    return cc.convert(ret[0]['generated_text'])

output_text = gr.outputs.Textbox()
grobj = gr.Interface(generate_text,inputs="textbox", outputs=output_text, title="自動產生歌詞")
grobj.launch()

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

#鐵達尼號生存預測

import gradio as gr
import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def encode_ages(df): 
    df.Age = df.Age.fillna(-0.5)
    bins = (-1, 0, 5, 12, 18, 25, 35, 50, 80)
    categories = pd.cut(df.Age, bins, labels=False)
    df.Age = categories
    return df

def encode_fares(df):
    df.Fare = df.Fare.fillna(-0.5)
    bins = (-1, 0, 8, 15, 31, 50, 80, 100, 550)
    categories = pd.cut(df.Fare, bins, labels=False)
    df.Fare = categories
    return df

def encode_sex(df):
    mapping = {"male": 0, "female": 1}
    return df.replace({'Sex': mapping})

data = pd.read_csv('https://raw.githubusercontent.com/gradio-app/titanic/master/train.csv')

def transform_features(df):
    df = encode_ages(df)
    df = encode_fares(df)
    df = encode_sex(df)
    return df

data1 = data[['Fare', 'Age', 'Sex', 'Survived']]
data1 = transform_features(data1)
X_all = data1.drop(['Survived'], axis=1)
y_all = data1['Survived']
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

def predict_survival(sex, age, fare):
    df = pd.DataFrame.from_dict({'Sex': [sex], 'Age': [age], 'Fare': [fare]})
    df = encode_sex(df)
    df = encode_fares(df)
    df = encode_ages(df)
    pred = clf.predict_proba(df)[0]
    return {'死亡': pred[0], '生還': pred[1]}

sex = gr.inputs.Radio(['female', 'male'], label="性別")
age = gr.inputs.Slider(minimum=0, maximum=80, step=1, default=22, label="年齡")
fare = gr.inputs.Slider(minimum=0, maximum=550, step=1, default=20, label="船費")
out = gr.outputs.Label(label='預測結果')
grobj = gr.Interface(fn=predict_survival, inputs=[sex, age, fare], outputs=out, title='鐵達尼號生存預測', live=True)
grobj.launch()

print('------------------------------------------------------------')	#60個

#使用自行訓練的模型

import tensorflow.keras
import numpy as np
import gradio as gr

# left_right.h5 路徑不能含中文
mnist_model_filename = "D:/_git/vcs/_big_files/left_right.h5"
model = tensorflow.keras.models.load_model(mnist_model_filename)
labels = ['normal','left','right']

def classify(img):
  img = (img.astype(np.float32) / 127.0) - 1
  img = np.expand_dims(img, 0)
  prediction = model.predict(img)
  return {labels[i]: float(prediction[0][i]) for i in range(len(prediction[0]))}

image = gr.inputs.Image(shape=(224, 224), label='輸入圖片')
label = gr.outputs.Label(num_top_classes=3, label='預測結果')
grobj = gr.Interface(fn=classify, inputs=image, outputs=label, examples=[['left1.jpg'], ['right1.jpg'], ['normal1.jpg']], title='使用自行訓練的模型')
grobj.launch()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



