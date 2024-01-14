import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("資料分析視覺化")

csv = st.sidebar.selectbox("請選擇資料集:", ["IRIS", "糖尿病"])
num = st.sidebar.slider("請選擇顯示資料數量:", 5 ,30)

if csv == "IRIS":
    df = pd.read_csv("app\Iris.csv")
    X = df.iloc[:, [3,4]]
    
    m = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
    y = df.Species.map(m)
    x1 = df.PetalLengthCm
    x2 = df.PetalWidthCm

else:
    df = pd.read_csv("app\diabetes.csv")
    X = df.iloc[:, [5,6]]
    y = df.Outcome
    x1 = df.BloodPressure#DiabetesPedigreeFunction#SkinThickness
    x2 = df.Glucose#BMI#BloodPressure

st.write("### 資料的前{}筆".format(num))
st.dataframe(df.head(num))

#繪圖
fig, ax = plt.subplots()
plt.scatter(x1, x2, c=y)
st.pyplot(fig)

