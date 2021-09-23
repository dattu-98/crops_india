import streamlit as st
import pandas as pd
from num2words import num2words
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (14,10)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def get_data():
    path='https://raw.githubusercontent.com/dattu-98/Crop-Production-Analysis/main/datasource.csv'
    return pd.read_csv(path)
st.title("Crop Production Analysis")
df=get_data()
st.sidebar.title('Select the State and Year from dropdown')
#State Input
option_state=st.sidebar.selectbox("Select the State",df['State_Name'].unique())
#Year Input
option_year=st.sidebar.selectbox("Select the Year",df['Crop_Year'].unique())
#Crop Input
option_crop=st.sidebar.selectbox("Select the Crop",df['Crop'].unique())

#Description
crop_year=df.loc[(df.State_Name==option_state) & (df.Crop_Year==option_year)].Production.sum()
area_year=df.loc[(df.State_Name==option_state) & (df.Crop_Year==option_year)].Area.sum()
st.write(str(option_state)+' has produced '+str(crop_year) + str(num2words(round(crop_year)))+' Tonnes/Hectare in '+str(option_year))
st.write(str(option_state)+' has an areable land of '+str(area_year)+ str(num2words(round(area_year)))+' Hectares in '+str(option_year))

#Plot 1
st.subheader("Year vs Total Crop Production(in Tonnes/Hectare)")
df_2=df[(df.State_Name==option_state) & (df.Crop==option_crop)]
x_years=df_2.Crop_Year.unique()
plt.bar(df_2.Crop_Year,df_2.Production);
plt.xticks(x_years);
plt.xlabel("Year")
plt.ylabel("Production in Tonnes/Hectare")
st.pyplot()

#Plot 2
st.subheader("Year vs Areable Land(in Hectares)")
df_3=df[(df.State_Name==option_state) & (df.Crop==option_crop)]
x_years=df_3.Crop_Year.unique()
plt.bar(df_3.Crop_Year,df_3.Area);
plt.xticks(x_years);
plt.xlabel("Year")
plt.ylabel("Areable Land in Hectares")

st.pyplot()
