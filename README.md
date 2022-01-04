●“Customer Churn” refers to the state in which the customer or the
subscriber stops involving transactional activities with the bank.
● We are trying to determine whether a customer will close his/her account
with the bank based on given features by posing a binary classification
problem using Machine learning
models .
● In the Business aspect this project may be useful to the marketing team
of the bank where the Organization can take respective action to retain
the customer.
● I have tried various Machine learning algorithms along with feature Engineering to get the best accuracy of it.In this project I have used 
F1-Score as Metric as it uses harmonic mean of Precision and recall.

+-----------------+---------------------+--------------------+
|    Vectorizer   |        Model        |      F1-score      |
+-----------------+---------------------+--------------------+
| one-hotEncoding |         KNN         |       0.841        |
| one-hotEncoding | Logistic-regression |       0.8035       |
| one-hotEncoding |    Decision Trees   |       0.855        |
| one-hotEncoding |    random forest    |       0.8595       |
| one-hotEncoding |  XGboost-classifier |       0.858        |
| response-coding |         KNN         | 0.8404999999999999 |
| response-coding | Logistic-regression |       0.8125       |
| response-coding |    Decision Trees   |       0.855        |
| response-coding |    random forest    |       0.8575       |
| response-coding |  XGboost-classifier |       0.858        |
+-----------------+---------------------+--------------------+


