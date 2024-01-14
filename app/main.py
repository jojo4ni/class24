import streamlit as st
import numpy as np
import pandas as pd

#輸出
st.title("AA22222")
st.write("# 11111")
st.write("## 11111")
st.info("BBBBBB")
a = np.array([1,2,3,4,5])
st.write(a)
st.table(a)

# 核取方塊
st.write("### 核取方塊")
ch = st.checkbox("美食")
if ch:
    st.info("愛美食")
else:
    st.info("不愛美食")

ch2 = st.checkbox("美食",key="a1")
if ch2:
    st.info("愛美食")
else:
    st.info("不愛美食")

chs = st.columns(3)
txt1 = ""
with chs[0]:
    c0 = st.checkbox("飯",key="c0")
    if c0:
        st.write("#### 要加白飯")
        txt1 +="要加白飯 "
with chs[1]:
    c1 = st.checkbox("小菜",key="c1")
    if c1:
        st.write("#### 要加小菜")
        txt1 +="要加小菜 "
with chs[2]:
    c2 = st.checkbox("湯",key="c2")
    if c2:
        st.write("#### 要加湯")
        txt1 +="要加湯 "
st.info(txt1)

# 選項按鈕
st.write("### 選項按鈕")
gender = st.radio("請選擇性別:", ["男","女","不知"])
st.info(gender)

col1, col2 = st.columns(2)
with col1:
    ra1 = st.number_input("請輸入任一整數")
with col2:
    ra2 = st.number_input("請輸入任一整數", key="ra2")

ra3 = st.radio("請選擇符號:",["++","--","**","//"], key='ra3')#
st.write(ra3)
if ra3=='++':
    st.write((ra1+ra2))
elif ra3=='--':
    st.write(ra1-ra2)
elif ra3=='**':
    st.write(ra1*ra2)
elif ra3=='//':
    st.write(ra1/ra2)    

# 滑桿
st.write("### 滑桿")
num = st.slider("請選擇數字:", 1.0, 20.0, step=0.5)
st.info(num)


# 下拉選單
st.write("### 下拉選單")
city = st.selectbox("city:", ("台北","台中","屏東"), index=1)
st.info(city)


# 上傳csv
st.write("### 上傳csv")
file = st.file_uploader("請選擇CSV檔")
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    st.dataframe(df)

# 按鈕
st.write("### 按鈕")
ok = st.button("OK")
if ok:
    st.info("RUNNING...")


