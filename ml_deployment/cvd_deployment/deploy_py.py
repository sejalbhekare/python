#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle
import streamlit as st


# In[2]:


loaded_model = pickle.load(open(r'cvd_model.sav','rb'))


# In[3]:


def cvd_predication_function(input_data):
    
# changing the input_data to numpy array
    input_data_as_nparray = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_nparray.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        print('Risk of cardiovascular disease')
    else:
        print('No risk of cardiovascular disease')


# In[4]:


def main():
    st.title("cardiovascular disease Prediction Web App")
    
    
    Height_(cm) == st.text_input("Height of the individual in cm: ")
    Weight_(kg) == st.text_input("Weight of the individual in kg: ")
    General_Health == st.text_input("individual current health condition: ")
    Checkup == st.text_input("About how long has it been since you last visited a doctor for a routine checkup?")
    Exercise == st.text_input("Do you exercise every day?")
    Cancer == st.text_input("Do you have any type of cancer?")
    Depression == st.text_input("Do you have a depressive disorder?")
    Diabetes == st.text_input("Are you having Diabetes?")
    Sex == st.text_input("Gender: ")
    Age_Category == st.text_input("Age Category")
    Smoking_History == st.text_input("Do you smoke?")
    Alcohol_Consumption == st.text_input("Do you drink alcohol?")
    
    
    cvd_predication=""
    if st.button("cardiovascular disease predication Test Result: "):
        cvd_predication = cvd_predication_function([Height_(cm),Weight_(kg),General_Health,Checkup,Exercise,Cancer,Depression,Diabetes,
                                         Sex,Age_Category,Smoking_History,Alcohol_Consumption])
    st.success(cvd_predication)
    
if __name__ == '_main_':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




