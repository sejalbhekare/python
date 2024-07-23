#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle
import streamlit as st


# In[2]:


loaded_model = pickle.load(open(r'trained_model.sav','rb'))


# In[3]:


def Rainfall_pred_function(input_data):
    
# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        print('It will not rain tomorrow')
    else:
        print('it may rain tomorrow')


# In[4]:


def main():
    st.title("Rainfall Prediction Web App")
    
    
    MinTemp= st.text_input("The minimum temperature: ")
    MaxTemp= st.text_input("The Maximum temperature: ")
    Rainfall= st.text_input("The amount of rainfall recorded for the day: ")
    Sunshine= st.text_input("The number of hours of bright sunshine in the day: ")
    WindGustSpeed= st.text_input("The direction of the strongest windgust: ")
    Humidity9am = st.text_input("Humidity at 9am: ")
    Humidity3pm = st.text_input("Humidity at 3pm: ")
    Pressure9am = st.text_input("Atmospheric pressure reduced to mean sea level at 9am: ")
    Pressure3pm = st.text_input("Atmospheric pressure reduced to mean sea level at 3pm: ")
    Cloud9am = st.text_input(" sky obscured by cloud at 9am: ")
    Cloud3pm = st.text_input(" sky obscured by cloud at 3pm: ")
    Date = st.text_input("The date of observation: ")
    Location = st.text_input("location of the weather station: ")
    WindGustDir = st.text_input("The direction of the strongest wind gust: ")
    RainToday = st.text_input("Whether it rained today or not: ")
    
    Rainfall_predication=""
    if st.button("rainfall predication Test Result: "):
        Rainfall_predication= Rainfall_pred_function([MinTemp,MaxTemp,Rainfall,Sunshine,WindGustSpeed,Humidity9am,Humidity3pm,
                                        Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Date,Location,WindGustDir,RainToday])
    st.success(Rainfall_predication)
    
    
if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




