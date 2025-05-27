# Contents of main.py
import eda
import prediction
import streamlit as st

# Define pages
PAGES = {
    # Format -> 'Menu title': module_name
    "EDA": eda,
    "Inference": prediction
}

# Set sidebar title
st.sidebar.title('Navigation')

# Set sidebar selection
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run app function in selected page
page = PAGES[selection]
page.app()