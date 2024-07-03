import numpy as np
import pickle
import streamlit as st
import pickle




#loaded_model = pickle.load(open('diabetic_model.sav', 'wb'))
#pickle.dump(loaded_model,open('diabetic_model.sav', 'wb'))
#filename='diabetic_model.sav'

#joblib.dump(model, filename)
#loaded_model = joblib.load(filename)
loaded_model = pickle.load(open('diabetic_model.sav', 'rb'))

'''
#**Diabetic prediction model**
'''
def diabetic_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if prediction[0]==0:
        st.write("not diabetic")
    else:
        st.write("diabetic")
def main():
    Pregnancies = st.number_input("Pregnancies")
    Glucose = st.number_input("Glucose")
    BloodPressure = st.number_input("BloodPressure")
    Insulin =st.number_input("Insulin")
    BMI	 = st.number_input("BMI")
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction")
    Age = st.number_input("Age")
    cell_name_list_as_int=  [Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]
    if st.button('Predict'):
        prediction = diabetic_prediction(cell_name_list_as_int)
        st.success(prediction)
if __name__ == "__main__":
    main()



