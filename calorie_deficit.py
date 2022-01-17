import streamlit as st
import pandas as pd
import datetime
from datetime import date

def app():
	st.title("Calorie Deficit Tracker")
	st.markdown("""
<style>
body {
    color: #000;
    background-color: #CF9FFF;
}
</style>
    """, unsafe_allow_html=True)
	sweight = st.number_input("Enter the current weight in kilograms")
	height = st.number_input("Enter the height in centimetres")
	gender = st.selectbox("Enter the Gender",("Male","Female"))
	age = st.number_input("Enter the age in years")
	calfood = st.number_input("Enter the food calorie intake")
	act = st.selectbox("Enter the type of lifestyle ",("Sedentary : Sitting most of the day with no structured exercise","Moderately active : Sedentary and low active job with 1 hr exercise daily or Active job (moderate movement 8+ hrs per day) but no structured exercise","Vigorously active : Active job (moderate movement 8+ hours per day) and 1 hr exercise per day or Sedentary or low active job but 2 hours of exercise daily","Extremely active : Training more than 2 hrs per day or Moderately active job (walking all day) plus at least 1 hr of exercise daily"))
	if act=="Sedentary : Sitting most of the day with no structured exercise":
		act = 1.55
	elif act == "Moderately active : Sedentary and low active job with 1 hr exercise daily or Active job (moderate movement 8+ hrs per day) but no structured exercise":
		act = 1.85
	elif act == "Vigorously active : Active job (moderate movement 8+ hours per day) and 1 hr exercise per day or Sedentary or low active job but 2 hours of exercise daily":
		act = 2.2
	else:
		act = 2.4
	rmr_male = 88.362 + (13.397 * sweight) + (4.799 * height) - (5.677 * age)
	rmr_female = 447.593 + (9.247 * sweight) + (3.098 * height) - (4.330 * age)
	if gender == "Male":
		bmr = 10 * sweight + 6.25 * height - 5 * age  + 5
		st.write("**Resting Metabolic Rate: **",round(rmr_male,2))
	else:
		bmr = 10 * sweight + 6.25 * height - 5 * age  - 161
		st.write("**Resting Metabolic Rate: **",round(rmr_female,2))
	mcal = bmr * act
	mcalw = mcal * 7
	st.write("**Calorie Deficit for the week: **",round(mcal,2))
app()
