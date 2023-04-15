import streamlit as st

# Add a title to the web page
st.title("To my beautiful girlfriend")

# Add a header to the web page
st.header("I just wanted to tell you how much I love you.")

# Add a text box to the web page
st.write("You are the most amazing person I have ever met, and I am so lucky to have you in my life.")

# Add an image to the web page
from PIL import Image
image = Image.open('val1.jpg')
st.image(image, caption='You and Me', use_column_width=True)

# Add a footer to the web page
st.write("Love always, Chehan")