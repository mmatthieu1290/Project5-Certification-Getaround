import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel 

import json
import pickle
import pandas as pd

with open('pricing.pkl','rb') as prices_estimator:
    pricing = pickle.load(prices_estimator)

with open('preprocessor.pkl','rb') as pre:
    preprocessor = pickle.load(pre) 

description = """
The API gives an estimation of a daily rent price. The structure of input data is the following:
 {'input':[car_1,car_2,....,car_k]}.\n\n
 
  For each i=1,...,k; car_i= [model_key , 
  mileage,
 engine_power,
 fuel, 
 paint_color,
 car_type,
 private_parking_available,
 has_gps,
 has_air_conditioning,
 automatic_car,
 has_getaround_connect,
 has_speed_regulator,
 winter_tires]\n 
\n

For model_key, chose between: 'Citroën', 'Peugeot', 'PGO', 'Renault', 'Audi', 'BMW', 'Ford',
       'Mercedes', 'Opel', 'Porsche', 'Volkswagen', 'KIA Motors',
       'Alfa Romeo', 'Ferrari', 'Fiat', 'Lamborghini', 'Maserati',
       'Lexus', 'Honda', 'Mazda', 'Mini', 'Mitsubishi', 'Nissan', 'SEAT',
       'Subaru', 'Suzuki', 'Toyota', 'Yamaha'.\n 

For mileage, gives a float whose unit is miles.\n

For engine_power, gives a float whose unit is horsepower.\n

For fuel, chose between: 'diesel', 'petrol', 'hybrid_petrol' or 'electro'.\n

For paint_color, chose between: 'black', 'grey', 'white', 'red', 'silver', 'blue', 'orange',
 'beige', 'brown' or 'green'.\n

For car_type, chose between: 'convertible', 'coupe', 'estate', 'hatchback', 
'sedan', 'subcompact', 'suv' or 'van'.\n

For the characteristics private_parking_available, has_gps,
 has_air_conditioning,
 automatic_car,
 has_getaround_connect,
 has_speed_regulator and winter_tires: 1 if it has, else 0.
"""

tags_metadata = [
    '''{
        "name": "Rental_price",
        "description": "The API return the daily price of each car.",
        "parameters" : "ploo"
    },'''
]


app = FastAPI(title="Rental price estimation",
    description=description,
    version="0.1",
    contact={
        "name": "Matthieu Maréchal"
    })#,
   # openapi_tags=tags_metadata)

@app.get("/", tags=["Rental_price"]) # here we categorized this endpoint as part of "Name_1" tag
async def index():
    message = "This API gives an estimation of the car rental price. If you want to learn more, check out documentation of the api at `/docs`"
    return message    

features = ['model_key',
 'mileage',
 'engine_power',
 'fuel',
 'paint_color',
 'car_type',
 'private_parking_available',
 'has_gps',
 'has_air_conditioning',
 'automatic_car',
 'has_getaround_connect',
 'has_speed_regulator',
 'winter_tires']

numerical_features = ['mileage',
 'engine_power',
 'private_parking_available',
 'has_gps',
 'has_air_conditioning',
 'automatic_car',
 'has_getaround_connect',
 'has_speed_regulator',
 'winter_tires']

class Caracteristics(BaseModel):
    input : List[list]

@app.post("/predict")
async def get_pricing(data:Caracteristics):
    if len(data.input)>0:
      nb = len(data.input)
      if nb>1:
        dict_prices = dict()
      for k in range(nb):
       if len(data.input[k])<len(features):
        return 'Missing some features',400
       car_caract = pd.DataFrame([{key:data1 for key,data1 in zip(features,data.input[k])}])  
       for numerical_feature in numerical_features:
        car_caract[numerical_feature] = car_caract[numerical_feature].astype(float)
       X = preprocessor.transform(car_caract)
       price_estimated = round(float(pricing.predict(X)),2)
       if nb ==1:
        return json.dumps({'Daily rent price':price_estimated})  
       else:
        dict_prices.update({f'Daily rent price, car {k+1}':price_estimated}) 
      return json.dumps(dict_prices)  
    else:
       return 'bad request', 400  



if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)

