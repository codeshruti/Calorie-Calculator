import Calorie_calculator
import weightloss_tracker
import calorie_deficit
import streamlit as st
PAGES = {
    "Calorie Calculator": Calorie_calculator,
    "Calorie Deficit Calculator": calorie_deficit,
    "Weight Loss Tracker": weightloss_tracker
}
st.sidebar.title('Calorie cum weight loss tracker')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
