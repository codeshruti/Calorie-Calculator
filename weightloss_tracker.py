import streamlit as st
import pandas as pd
import datetime
from datetime import date
def func(val,sweight,height,gender,age,lr,cw,calfood,calburn):
	st.write("**Days from the Start: **",val)
	target_t = sweight - (val*lr)/7 
	st.write("**Start Weight: **",sweight)
	st.write("**Target Today: **",round(target_t,2))
	prg = target_t - cw
	if prg>0:
		st.write("**Progress: Ahead of target by **",round(prg,2)," **kg**")
	else:
		st.write("**Progress: Behind target by **",round(prg,2)," **kg**")
	rmr_male = 88.362 + (13.397 * cw) + (4.799 * height) - (5.677 * age)
	rmr_female = 447.593 + (9.247 * cw) + (3.098 * height) - (4.330 * age)
	if gender =="Male":
		cd = rmr_male + calburn - calfood
		st.write("**Resting Metabolic Rate: **",round(rmr_male,2))
	else:
		cd = rmr_female + calburn - calfood
		st.write("**Resting Metabolic Rate: **",round(rmr_female,2))
	st.write("**Calorie Deficit: **",round(cd,2))
	loss_exp = cd/7500
	st.write("**Loss Expected: **",round(loss_exp,2))
def app():
	st.title("Weight Loss Tracker")
	st.markdown("""
<style>
body {
    color: #000;
    background-color: #CF9FFF;
}
</style>
    """, unsafe_allow_html=True)
	date = st.date_input("Enter the start date",datetime.date(2022, 1, 1))
	sweight = st.number_input("Enter the start weight in kilograms")
	height = st.number_input("Enter the height in centimetres")
	gender = st.selectbox("Enter the Gender",("Male","Female"))
	age = st.number_input("Enter the age in years")
	lr = st.number_input("Enter the loss rate(in kgs) per week")
	cw = st.number_input("Enter the weight now")
	calfood = st.number_input("Enter the food calorie intake")
	calburn = st.number_input("Enter the calories burnt")
	cdate = datetime.date.today()
	if cdate == date:
		val = 1
		func(val,sweight,height,gender,age,lr,cw,calfood,calburn)
	elif cdate>date:
		delta = cdate - date
		val = delta.days
		func(val,sweight,height,gender,age,lr,cw,calfood,calburn)
	else:
		st.write("** Please select a Start date before current date**")







