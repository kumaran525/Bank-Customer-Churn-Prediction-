#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pickle
import numpy as np
from scipy.sparse import hstack
class Transform:
    def __init__(self):
        pass
    def transform(self,l):
        #self.l=['France','Female',1,1,619,2,0,1,40,10100]
        Scaler1=pickle.load(open('Pickles/scaler1.pkl', 'rb'))
        Scaler2=pickle.load(open('Pickles/scaler2.pkl', 'rb'))
        Scaler3=pickle.load(open('Pickles/scaler3.pkl', 'rb'))
        Scaler4=pickle.load(open('Pickles/scaler4.pkl', 'rb'))
        Scaler5=pickle.load(open('Pickles/scaler5.pkl', 'rb'))
        Scaler6=pickle.load(open('Pickles/scaler6.pkl', 'rb'))
        vectorizer1=pickle.load(open('Pickles/vectorizer1.pkl', 'rb'))
        vectorizer2=pickle.load(open('Pickles/vectorizer2.pkl', 'rb'))
        model=pickle.load(open('Pickles/model.pkl', 'rb'))
        X_te_cr=Scaler1.transform(np.array(l[4]).reshape(-1,1)).reshape(1,-1)
        X_te_age=Scaler2.transform(np.array(l[8]).reshape(-1,1)).reshape(1,-1)
        X_te_ten=Scaler3.transform(np.array(l[5]).reshape(-1,1)).reshape(1,-1)
        X_te_bal=Scaler4.transform(np.array(l[6]).reshape(-1,1)).reshape(1,-1)
        X_te_pr=Scaler5.transform(np.array(l[7]).reshape(-1,1)).reshape(1,-1)
        X_te_sal=Scaler6.transform(np.array(l[9]).reshape(-1,1)).reshape(1,-1)
        X_te_geo=vectorizer1.transform([l[0]])
        X_te_gen=vectorizer2.transform([l[1]])
        X_te_hr=np.array([l[2]])
        X_te_ac=np.array([l[3]])
        #print(type(X_te))
        X_te=hstack((X_te_gen.astype(float),X_te_geo.astype(float),np.reshape(X_te_hr,(len(X_te_hr),1)).astype(float),np.reshape(X_te_ac,(len(X_te_ac),1)).astype(float),np.transpose(X_te_cr),np.transpose(X_te_ten),np.transpose(X_te_bal),np.transpose(X_te_pr),np.transpose(X_te_age),np.transpose(X_te_sal)))
        return model.predict(X_te)[0]


# # In[134]:


# T=Transform()
# T.transform(['france','male',1,1,600,2,0,1,40,1011])


# # In[ ]:




