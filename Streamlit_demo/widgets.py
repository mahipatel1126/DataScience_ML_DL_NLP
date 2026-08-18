import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected {choice}.")

data = {
    "Name" : ["John", "Jane", "Jake", "Jill"],
    "Age" : [28, 34, 29, 31],
    "City" : ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write("Here is the dataframe:")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Here is the uploaded dataframe:")
    st.write(df_uploaded)


# import streamlit as st

# st.title("THIS IS WIDGETS.PY")
# st.success("You are running widgets.py")

# st.stop()