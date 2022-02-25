import Calorie_calculator
import weightloss_tracker
import calorie_deficit
import rec_system
import streamlit as st
st.set_page_config(page_title='Calorie Calculator')
PAGES = {
    "Calorie Calculator": Calorie_calculator,
    "Calorie Deficit Calculator": calorie_deficit,
    "Weight Loss Tracker": weightloss_tracker,
    "Recommendation System": rec_system
}
st.sidebar.title('Calorie cum weight loss tracker')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
