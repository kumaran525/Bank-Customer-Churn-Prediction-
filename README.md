●“Customer Churn” refers to the state in which the customer or the subscriber stops involving transactional activities with the bank.
● We are trying to determine whether a customer will close his/her account with the bank based on given features by posing a binary classification problem using Machine learning
models.
● In the Business aspect this project may be useful to the marketing team of the bank where the Organization can take respective action to retain the customer.
● I have tried various Machine learning algorithms along with feature Engineering to get the best accuracy of it. In this project, I have used F1-Score as a Metric as it uses the harmonic mean of Precision and recall.

<img width="531" alt="image" src="https://user-images.githubusercontent.com/64630755/232133850-a89a632b-56a6-434a-ad3b-16d97e40a160.png"> 

## Files Description ## 

* Transform.py - Do all features transformation for test/Real time data
* Application.py - This contains Flask APIs that receives customer details through GUI or API calls, computes the precited value based on our model and returns it.
* template - This folder contains the HTML template (index.html) to allow user to enter customer detail and displays the predicted Customer Status.
* Cutomer_churn_prediction.ipynb - This file contains all EDA,feature Engineering ,model evaluvations for the given Problem Statement.

## Running the project ##

* To install necessary libraries to run the Project 

 `pip install -r /path/to/requirements.txt`
 
* Run app.py using below command to start Flask API 

`python application.py`

By default, flask will run on port 5000. 

* Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

Enter valid values in all input boxes and hit Predict.

If everything goes well, you should be able to see the predcited vaule on the HTML page! check the output here: http://127.0.0.1:5000/predict
