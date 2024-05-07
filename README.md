# stock market prediction and analysis web app using python

# Abstract:

Predicting how the stock market will perform is one of the most difficult things to do. There are so many factors involved in the prediction – physical factors vs. physiological, rational and irrational behaviour, etc. All these aspects combine to make share prices volatile and very difficult to predict with a high degree of accuracy. In this project, we have worked with historical data about the stock prices of a publicly listed company. We present a recurrent neural network (RNN) and Long Short-Term Memory (LSTM) approach to predict stock market indices. 

Keywords:

![](https://img.shields.io/static/v1?label=LSTM&message=long-short-term-memory&color=orange) ![](https://img.shields.io/static/v1?label=RNN&message=recurrent-neural-network&color=orange) ![](https://img.shields.io/static/v1?label=RMSE&message=root-mean-square-error&color=orange) ![](https://img.shields.io/static/v1?label=Lib&message=Streamlit&color=orange) ![](https://img.shields.io/static/v1?label=Py&message=prediction_stock-prices_dataset&color=orange)

Long short-term memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feed forward neural networks, LSTM has feedback connections. It can not only process single data points (such as images), but also entire sequences of data (such as speech or video).

# Dataset
![table](https://user-images.githubusercontent.com/80147820/174331662-63fbec90-b2e5-48bd-bb66-02b10ed097b2.jpg)


Why we used LSTM?

LSTMs are widely used for sequence prediction problems and have proven to be extremely effective. The reason they work so well is because LSTM is able to store past information that is important, and forget the information that is not. -Stackabuse.com

Common Architecture of LSTM:

•	Forget Gate
•	Input Gate
•	Output Gate

How to build LSTM?

In order to build the LSTM, we need to import a couple of modules from Keras:

•	Sequential for initializing the neural network
•	Dense for adding a densely connected neural network layer
•	LSTM for adding the Long Short-Term Memory layer
•	Dropout for adding dropout layers that prevent overfitting

What is Streamlit used for?

Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.

# Closing time vs Time chart with 100MA and 200MA

![image](https://user-images.githubusercontent.com/80147820/174331886-0fe84f04-aafd-4efe-9639-f3618f6474ef.png)

# Prediction vs Original graph

![image](https://user-images.githubusercontent.com/80147820/174332006-1c2040bd-9ba0-4cca-8e1e-d17a9295cae7.png)

