# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:20:48 2024

@author: sindh
"""

import json
import requests

url='https://48db-34-133-223-43.ngrok-free.app/diabetes_prediction'

input_data_for_model={
    'Pregnancies':1,
    'Glucose':85,
    'BloodPressure':66,
    'SkinThickness':29,
    'Insulin':0,
    'BMI':26.6,
    'DiabetesPedigreeFunction':0.351,
    'Age':31
    }
input_json=json.dumps(input_data_for_model)
response=requests.post(url,data=input_json)
print(response.text)