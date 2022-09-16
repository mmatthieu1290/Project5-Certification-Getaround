import streamlit as st
import pickle
from math import exp
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
#import SessionState

with open('time_losse.pkl','rb') as tl:
    time_losse = pickle.load(tl)

with open('estimator_problems_inverse.pkl','rb') as est_problem:
    estimator_problems = pickle.load(est_problem) 

with open('pricing.pkl','rb') as prices_estimator:
    pricing = pickle.load(prices_estimator)

with open('preprocessor.pkl','rb') as pre:
    preprocessor = pickle.load(pre)           

### Config
st.set_page_config(
    page_title="App-car-rental",
    layout="wide"
)

### HEADER
st.title('')
st.header("Influence of threhold")

st.sidebar.header("")


model_key = st.sidebar.selectbox("Model of the car",['Citroën',
 'Peugeot',
 'Renault',
 'Audi',
 'BMW',
 'Mercedes',
 'Volkswagen',
 'Mitsubishi',
 'Nissan',
 'Toyota'])

mileage = st.sidebar.slider("mileage",0,500000) 

engine_power = st.sidebar.slider("engine_power",100,300)

fuel = st.sidebar.selectbox("Fuel",['diesel', 'petrol', 'hybrid_petrol', 'electro'])

paint_color = st.sidebar.selectbox("Paint color",\
    ['black', 'grey', 'white', 'red', 'silver', 'blue', 'orange',
       'beige', 'brown', 'green'])

car_type = st.sidebar.selectbox("Car type",\
    ['convertible', 'coupe', 'estate', 'hatchback', 'sedan',
       'subcompact', 'suv', 'van'])




threshold = st.slider("Threshold between two rents in minutes",0,700)

mean_time_losse = round(max([0,float(time_losse.predict([[threshold,threshold**2]]))]),0)

connexion = sqlite3.connect('db_deployment.db')

connexion.commit()

df_loss = pd.read_sql_query('select * from loss_time',con = connexion)

df_problems = pd.read_sql_query('select * from check_out_problems',con = connexion)

df_slope = pd.read_sql_query('select * from slope_check_out_problems',con = connexion)

x = df_loss.iloc[:,0]

y1 = df_loss.iloc[:,1]

y2 = df_problems.iloc[:,1]

mean_problem = 1/(float(estimator_problems.predict([[threshold]])))

if threshold < df_slope.iloc[0,0]:
    mean_problem = df_problems.iloc[0,1] + df_slope.iloc[0,1]*threshold
else:
    mean_problem = 1/(float(estimator_problems.predict([[threshold]]))) 

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, np.max([np.array(y1).reshape((-1,1)),np.zeros((len(y1),1))],axis = 0), 'g-')
ax1.plot(threshold*np.ones(400),np.linspace(-10,430,400),c = 'r')
ax2.plot(x, 100*y2, 'b-')
ax1.scatter(threshold,mean_time_losse,c='g')
ax1.text(x=threshold-70,y=mean_time_losse+10,s=f'{mean_time_losse}')
ax2.scatter(threshold,100*mean_problem,c = 'b')
ax2.text(x=threshold+10,y=100*mean_problem+0.1,s=f'{round(100*mean_problem,2)}%')

ax1.set_xlabel('threshold')
ax1.set_ylabel('time loss', color='g')
ax2.set_ylabel('Percentage of check out with delay', color='b')

st.pyplot(fig)

time_of_rent = st.number_input("Time of rent in days",1)

mean_relative_time_losse = mean_time_losse/(24*60*time_of_rent)

st.write("On average",mean_time_losse," rental minutes will be lost per rental.\
     This represents",\
    round(100*mean_relative_time_losse,2),'% of the total rental time.')

   


st.write("We estimate that in ",round(100*mean_problem,2)," % of rentals, \
    the car will be returned after the scheduled time of the next rental.")

st.header("Estimation of the price of rent.")    

private_parking_available = st.checkbox('Private parking available')
has_gps = st.checkbox('Has gps')
has_air_conditioning = st.checkbox('Has air conditioning')
automatic_car = st.checkbox('Automatic car')
has_getaround_connect = st.checkbox('Has getaround connect')
has_speed_regulator = st.checkbox('Has speed regulator')
winter_tires = st.checkbox('Winter tires')

features = {'model_key':[model_key],
 'mileage':[mileage],
 'engine_power':[engine_power],
 'fuel':[fuel],
 'paint_color':[paint_color],
 'car_type':[car_type],
 'private_parking_available':[int(private_parking_available)],
 'has_gps':[int(has_gps)],
 'has_air_conditioning':[int(has_air_conditioning)],
 'automatic_car':[int(automatic_car)],
 'has_getaround_connect':[int(has_getaround_connect)],
 'has_speed_regulator':[int(has_speed_regulator)],
 'winter_tires':[int(winter_tires)]}

df_features = pd.DataFrame(features)

X = preprocessor.transform(df_features)

price_estimated = pricing.predict(X)

total_price = round(float(price_estimated*time_of_rent))

st.write("The price estimated of the rent is ",total_price,"$.")

money_loss = float(price_estimated)*mean_time_losse/(24*60)

money_loss = round(money_loss,2)

st.write("The loss with this threshold is estimated to:",money_loss,"$.")