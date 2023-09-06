# import streamlit to make user interface

import streamlit as st

st.set_page_config(page_title="Stock Market", page_icon=":bank:", layout="wide") #layout pode ser centered

# show images to the user in app
st.image("images/1.png", width=1500)
st.write("---")
st.image("images/2.png", width=1500)
st.write("---")
st.image("images/3.png", width=1500)
st.write("---")
st.image("images/4.png", width=1500)
st.write("---")
st.image("images/5.png", width=1500)
st.write("---")
st.image("images/6.png", width=1500)                  
                    
                    
#st.sidebar.success("TEste") # paginação

# pages = {
#     "Home": 0,
#     "Add Product": 1,
#     "Pantry": 2,
# }

# # Create a sidebar navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", list(pages.keys()))