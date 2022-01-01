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
df1 = pd.read_csv('Korean food_calorie__.csv',index_col=0)
dish = st.selectbox("Select the name of dish ",('Kimbap/김밥','Tteokbokki/떡볶이','Kalguksu/칼국수','Gopchang-jeongol/곱창전골','Chadolbagi/차돌바기','Samgyeopsal/삼겹살','Panjeon/판전','Korean Tofu Kimchi Soup/두부 김치찌개','Samgetang/삼계탕','Pork Ribs/돼지 갈비','Dumplings/만두','Carrots In Korean/당근 한국어','Galbi Jjim/갈비찜','Bibimbap/비빔밥','Yeongyang dolsatbap/영양 돌솥밥','Carrot Salad/당근 샐러드','Korean Food Lunch/한식 점심','Ddukbaegi Bulgogi/뚝배기 불고기','Jjamppong/짬뽕','Octopus bibimbap/문어비빔밥','Sujebi/수제비','Dumpling Soup/만두 수프','Yukgaejang/육개장','Beef bulgogi/소불고기','Vegetable Dumbling/야채 덤블링','Bulgogi/불고기','Korean cold noodles/한국 냉면','Korean Eel soup/장어탕','Sundubu/순두부','Korean Homemade food/한국 집에서 만든 음식','Bibimnangmein/비빔낭마인','Bi Bim Bap/비빔밥','Noodle/국수','Galbi-tang /갈비탕','Bibimbap With Beef/소고기 비빔밥','Ginseng Chicken Soup/인삼 치킨 수프','Dwen Jang Jigae/드웬 장지개','Korean Beef Noodles/한우국수','Tofu Kimchi/두부','Makchang/막창','Steamed Monkfish/아귀찜','Sundaegukbab/순대국밥','Doganitang/도가니탕','Bulgogi /불고기','Eomukguk/어묵국','Soon Dae/순대','Sirloin Steak/등심 스테이크','Oi Kimchi/오이 김치','Tempah/템파','Seaweed Salad/미역 샐러드','Hobbang/호뱅','Broiled Eels/구운 장어','Korean bbq/한국식 바베큐','Nori/Seaweed/김','Upjinsal roast/웁진살 구이','Samgyupsal Pork Belly/삼겹살 삼겹살','JwiPo/주이포','Kim Bugak/미역 스낵','Sogogi Youkgajang/소고기육가장','Korean bbq marinade/한국식 바베큐 마리네이드','Self heating food/자체 가열 식품','Korean Chicken Stir-Fry/한국 치킨 볶음','Beef Intestine /쇠고기 창자','Pork Bone Soup – Gamjatang/감자탕','Ojingeo Deopbap/오징어덮밥','Ddukbokkie/떡볶이','Dwenjanggigae/웬장기개','Ja Jang Myeon/자장면','Doenjang Soup With Spinach/시금치 된장국','Korean Biscuit/한국 과자','Seasoned Tofu /양념 두부','Korean Short Rib Soup/한식 갈비탕','Roasted Pork Belly /구운 삼겹살','Tteokguk/축하 수프','Korean beef/한우','Dak kkochi/떡볶이','Rice Cake Soup/떡국','Stuffed Cucumber Kimchi/오이 박제 김치','Yeot/쯧쯧','Gim/김','Triangular kimbap/삼각김밥','Baked Chub Mackerel/구운 고등어','Bebimbap/비빔밥','Bread Ttoah/빵또아','Korean seaweed/한국 해초','Saeukkang/새강','Bread Ttoah/빵또아','Korean seaweed/한국 해초','Udon boeuf/우동부프','Korean Kimchi/한국 김치','Korean Bbq/한국식 바베큐','Dashida/다시다','Galbitang/갈비탕','Kimchi/김치','Bibimbap vegetables/비빔밥 야채','Korean Chicken/한국 치킨','Sikhye/식혜','Saeng Maekju/생맥주','Patbingsu/팥빙수','Tangpyeongchae/탕평채'))
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
	kd = df1['Korean Description'][index_]
	st.write("**Calorie count** ",cal_*serving_)
	st.write("**Carb value** ",carb_*serving_)
	st.write("**Fat Value** ",fat_*serving_)
	st.write("**Protein intake** ",proteins_*serving_)
	st.write("**Recipe**",recipe_)
	st.write("**Description in Korean**",kd)	
	st.image(image_,width=500)
