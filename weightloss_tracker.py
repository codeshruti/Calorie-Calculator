import streamlit as st
import pandas as pd
import datetime
from datetime import date
def shortcut():
	scval = st.beta_expander("Information about Calories Burnt",False)
	scval.markdown("**Walking**")
	scval.markdown("1 Hour--> 350 Cal")
	scval.markdown("1,000 Steps-->60 Cal")
	scval.markdown("10,000 Steps-->600 Cal")
	scval.markdown("**Running at an average speed**")
	scval.markdown("1 Mile--> 100 Cal")
	scval.markdown("1 KM-->60 Cal")
	scval.markdown("5 Miles-->500 Cal")	
	scval.markdown("5 KM-->300 Cal")
	scval.markdown("**Swimming at a slow pace**")
	scval.markdown("1 Hour--> 500 Cal")
	scval.markdown("1 Lap of 50m Pool-->25 Cal")
	scval.markdown("**Swimming at a fast pace**")
	scval.markdown("1 Hour--> 750 Cal")
	scval.markdown("1 Lap of 50m Pool-->50 Cal")
	scval.markdown("**Gym Workout for 1 Hour**")
	scval.markdown("Light workout--> 200 Cal")
	scval.markdown("Medium workout--> 350 Cal")
	scval.markdown("Heavy workout--> 500 Cal")
	scval.markdown("**Bike Ride for 1 Hour**")
	scval.markdown("At 20 Km/hr or 13 Miles/hr--> 600 Cal")
	scval.markdown("At 25 Km/hr or 16 Miles/hr--> 740 Cal")	
	scval1 = st.beta_expander("Information about Calorie Intake",False)
	scval1.markdown("**Average general Calorie intake--> 2000-2500 Cal**")
	scval1.markdown("**No. of Calorie Deficit required to lose 1 kg--> 7800 Cal**")
	scval1.markdown("**Deficit of 1,100 cals per day --> 1 kg loss per week**")
	scval1.markdown("**Daily loss for 2 kg per week is 0.3 kg per day**")
	scval1.markdown("**1 kg of fat--> 7,500 calories**")
	scval1.markdown("Calories for 2 small meals--> 1000 Cal")
	scval1.markdown("Calories for 3 small meals--> 1800 Cal")
	scval1.markdown("Apple, orange or banana--> 100 Cal")
	scval1.markdown("Muesli with 1 cup of milk--> 500 Cal")
	scval1.markdown("Fish 400 g with salad--> 600 Cal")
	scval1.markdown("Steak 300 g with salad--> 800 Cal")
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
	st.markdown("____")
	shortcut()
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







