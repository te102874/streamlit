from re import L
from regex import R
import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title('Streamlit 超入門')
st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味をおしえてください。')
# condition = st.slider('あなたの今の調子は？',0,100, 50)
# 'あなたの趣味：',text,'です。'
# 'コンディション：',condition

# if st.checkbox('Show Image'):
#     img = Image.open('2022-04-16 13.21.35.jpg')
#     st.image(img, caption='Rama', use_column_width=True)

