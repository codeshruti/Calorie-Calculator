import streamlit as st
st.set_page_config(page_title='Calorie Calculator for Korean Food')
st.title("Calorie Calculator for Korean Food")
st.write("Enter the name of a food item with the serving amount")
# Kimbap, Chadolbagi, kimchi
st.markdown("""
<style>
body {
    color: #000;
    background-color: #C8B4C2;
}
</style>
    """, unsafe_allow_html=True)
import pandas as pd
df1 = pd.read_csv('Korean food_calorie.csv',index_col=0)
dish = st.text_input("Enter the name of dish ")
serving_ = st.number_input("Enter number of Servings")
try: 
	index_ = df1.index[df1['Name of the food']==dish].item()	
except ValueError:
	index_ = 1
else:
	recipe_ = df1['Recipe'][index_]
	cal_ = df1['Calories'][index_]
	carb_ = df1['Carb(g)'][index_]
	fat_ = df1['Fat (g)'][index_]
	proteins_ = df1['Proteins(g)'][index_]
	image_ = df1['Image'][index_]
	st.write("**Calorie count** ",cal_*serving_)
	st.write("**Carb value** ",carb_*serving_)
	st.write("**Fat Value** ",fat_*serving_)
	st.write("**Protein intake** ",proteins_*serving_)
	st.write("**Recipe**",recipe_)
	st.image(image_,width=500)
