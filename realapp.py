import streamlit as st
import pickle
from math import exp
import pandas as pd
#import SessionState

with open('time_losse.pkl','rb') as tl:
    time_losse = pickle.load(tl)

with open('estimator_problems_logaritm.pkl','rb') as est_problem:
    estimator_problems = pickle.load(est_problem) 

with open('pricing.pkl','rb') as prices_estimator:
    pricing = pickle.load(prices_estimator)

with open('preprocessor.pkl','rb') as pre:
    preprocessor = pickle.load(pre)           

### Config
st.set_page_config(
    page_title="Web-detection",
    layout="wide"
)

### HEADER
st.title('Web Application to Project 6')
st.header("A  machine learning application to predict ")
st.markdown(""" This application allow to classify  
""")
st.title("How to use it")
st.markdown("*First chose the start and the end of rent")

st.markdown("*After chose the model,...")  


st.subheader('Prediction of...')


st.sidebar.header("")


model_key = st.sidebar.selectbox("Model of the car",['Citroën', 'Peugeot', 'PGO', 'Renault', 'Audi', 'BMW', 'Ford',
       'Mercedes', 'Opel', 'Porsche', 'Volkswagen', 'KIA Motors',
       'Alfa Romeo', 'Ferrari', 'Fiat', 'Lamborghini', 'Maserati',
       'Lexus', 'Honda', 'Mazda', 'Mini', 'Mitsubishi', 'Nissan', 'SEAT',
       'Subaru', 'Suzuki', 'Toyota', 'Yamaha'])

mileage = st.sidebar.slider("mileage",0,500000) 

engine_power = st.sidebar.slider("engine_power",100,300)

fuel = st.sidebar.selectbox("Fuel",['diesel', 'petrol', 'hybrid_petrol', 'electro'])

paint_color = st.sidebar.selectbox("Paint color",\
    ['black', 'grey', 'white', 'red', 'silver', 'blue', 'orange',
       'beige', 'brown', 'green'])

car_type = st.sidebar.selectbox("Car type",\
    ['convertible', 'coupe', 'estate', 'hatchback', 'sedan',
       'subcompact', 'suv', 'van'])


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


time_of_rent = st.number_input("Time of rent in days",1)

total_price = round(float(price_estimated*time_of_rent))

st.write("The price estimated of the rent is ",total_price,"$.")

threshold = st.slider("Threshold between two rents in minutes",0,700)

mean_time_losse = round(max([0,float(time_losse.predict([[threshold,threshold**2]]))]),0)

money_loss = float(price_estimated)*mean_time_losse/(24*60)

money_loss_relative = money_loss/total_price

st.write("With a threshold equal to ",threshold,'minutes, the owner will suffer an\
    average loss of ',round(money_loss,2),'which reprensents in average', 
    round(100*money_loss_relative,2),'% of the total income')

mean_problem = exp(float(estimator_problems.predict([[threshold]])))

st.write("We estimate that in ",round(100*mean_problem,2)," % of the rent the delay\
    of the checkout will be greater that time delta with following rate")






