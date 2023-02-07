●“Customer Churn” refers to the state in which the customer or the
subscriber stops involving transactional activities with the bank.
● We are trying to determine whether a customer will close his/her account
with the bank based on given features by posing a binary classification
problem using Machine learning
models .
● In the Business aspect this project may be useful to the marketing team
of the bank where the Organization can take respective action to retain
the customer.
● I have tried various Machine learning algorithms along with feature Engineering to get the best accuracy of it.In this project I have used F1-Score as Metric as it uses harmonic mean of Precision and recall.

![image](https://user-images.githubusercontent.com/64630755/148063781-3fda4407-e0ae-42e9-8f2c-a7731ba298a8.png) 

## Files Description ## 

* Transform.py - Do all features transformation for test/Real time data
* Application.py - This contains Flask APIs that receives customer details through GUI or API calls, computes the precited value based on our model and returns it.
* template - This folder contains the HTML template (index.html) to allow user to enter customer detail and displays the predicted Customer Status.
* Cutomer_churn_prediction.ipynb - This file contains all EDA,feature Engineering ,model evaluvations for the given Problem Statement.

## Running the project ##

* Run app.py using below command to start Flask API 

`python application.py`

By default, flask will run on port 5000. 

* Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

Enter valid numerical values in all input boxes and hit Predict.

If everything goes well, you should be able to see the predcited vaule on the HTML page! check the output here: http://127.0.0.1:5000/predict
