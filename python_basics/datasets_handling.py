# -*- coding: utf-8 -*-
"""Datasets_handling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F2Ca5Fk__rT2goz4E2IG6AUWQg_m8ySq

importing datasets through kaggle api
"""

!pip install kaggle

"""upload your kaggle.json file"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""importing the earthquake dataset"""

!kaggle competitions download -c LANL-Earthquake-Prediction

from zipfile import ZipFile

dataset='/content/LANL-Earthquake-Prediction.zip'
with ZipFile(dataset,'r') as zip:
  zip.extractall()
print('dataset is extracted')

"""methods to handle missing values:-
1.imputation
2.dropping
"""

!pip install standardScalar

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

dataset=pd.read_csv('/content/Placement_Dataset.csv')

dataset.head()

dataset.isnull().sum()

"""**Central Tendencies:**

1.   mean
2.   median
3.   mode






"""

#analyse the distribution of data in salary column
fig,ax=plt.subplots(figsize=(8,8))
sns.distplot(dataset.salary)

"""Replace the missing values with median value"""

dataset['salary'].fillna(dataset['salary'].median,inplace=True)

dataset.isnull().sum()

"""**Data Standardization**
The process of standardizing the data to a common format and common range
"""

dataset=sklearn.datasets.load_breast_cancer()

print(dataset)

breast_cancer_df=pd.DataFrame(dataset.data,columns=dataset.feature_names)

breast_cancer_df.head()

x=breast_cancer_df
y=dataset.target

print(x)

print(y)

"""splitting the data into training data and test data"""

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=3)

print(X_test)

"""Srandardize the data"""

print(dataset.data.std())

scaler=StandardScaler()

scaler.fit(X_train)

X_train_standardized=scaler.transform(X_train)

print(X_train)

X_test_standardized=scaler.transform(X_test)

print(X_train_standardized.std())

"""**Laber Encoding**

*   converting the labels into numeric form


"""

from sklearn.preprocessing import LabelEncoder

"""Label Encoding of Breast Cancer Dataset"""

cancer_data=pd.read_csv('/content/breast_cancer_data.csv')

cancer_data.head()

cancer_data['diagnosis'].value_counts()

label_encode=LabelEncoder()

labels=label_encode.fit_transform(cancer_data.diagnosis)

cancer_data['target']=labels

cancer_data.head()

"""0-->Benign

1-->Malignant
"""

cancer_data['target'].value_counts()

"""**Imbalanced Dataset:**
A dataset with an unequal class distribution


"""

credit_card_data=pd.read_csv('/content/credit_data.csv')

credit_card_data.head()

credit_card_data['Class'].value_counts()

credit_card_data.shape

"""This is highly imbalanced dataset

0--->legit transactions

1--->fradulant transations
"""

credit_card_data.tail()

credit_card_data.isnull().sum()

credit_card_data.iloc[-1]

#seperating the legit and fradulent transactions
legit=credit_card_data[credit_card_data.Class==0]
fraud=credit_card_data[credit_card_data.Class==1]

legit.value_counts('Class')

fraud.value_counts('Class')

"""Under-Sampling

Building a sample dataset containing of Legit & Fradulent Transactions
"""

legit_sample=legit.sample(n=492)

legit_sample.shape

"""Concatenate two DataFrames"""

new_dataset=pd.concat([legit_sample,fraud],axis=0)

new_dataset.shape

"""**Tf-idf Vectorizer**



Term Frequency(TF)=(Number of times term t appears in a document)/(Number of terms in the document)


Inverse document frequency(IDF)=log(N/n),where,N is the number of documents and n  is the number of documents a term t has appeared in.

The IDF value of a rare word is high,whereas the IDF of a frequent word is low.

**TF-IDF** value of a term=TF*IDF




"""

news_dataset=pd.read_csv('/content/fake_news_dataset.csv')

news_dataset.head()

nltk.download('stopwords')

print(stopwords.words('english'))

#convert the textual data to feature vector
vectorizer=TfidfVectorizer()

vectorizer.fit()

news_dataset.isnull().sum()

