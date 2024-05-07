from cProfile import label
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model

#st.write("Hello from Streamlit")
start = '2010-01-01'
end= '2019-12-31'

st.title('Stock trend prediction')

#df=data.DataReader('AAPL','yahoo',start,end)
#df.head()

user_input = st.text_input('enter stock ticker', 'AAPL')
df= data.DataReader('AAPL', 'yahoo', start, end)
#df.head()

#Describing data
st.subheader('Data from 2010-2019')
st.write(df.describe())

#Visualizations
st.subheader('Closing price vs time chart')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time chart with 100MA and 200MA ')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig= plt.figure(figsize=(12,6))
plt.plot(ma100 , 'r' , label='ma100')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'b')
plt.legend()
st.pyplot(fig)

# splitting data into training and testing
data_training = pd .DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd. DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)

# divide data into x-train and y-train
# for 1st 100 days x_train 101th day y_train(predictive)
#after each state it will inc. and forget the 1st value and add an y_train value
x_train = []
y_train = []
for i in range(100, data_training_array.shape[0]):
    x_train.append(data_training_array[i-100: i])
    y_train.append(data_training_array[i, 0])
    
x_train , y_train = np.array(x_train), np.array(y_train)

#Loading my model
model= load_model('keras_model.h5')

#Testing part
past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index =True)
input_data = scaler.fit_transform(final_df)

x_test =[]
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])
    
y_prediction = model.predict(x_test)
scaler = scaler.scale_ 
 
scale_factor = 1/scaler(0)
y_prediction = y_prediction * scale_factor
y_test = y_test * scale_factor

# Final graph
st.subheader('Prediction vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b' ,label =' Original Price')
plt.plot(y_prediction, 'r', label =' Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

