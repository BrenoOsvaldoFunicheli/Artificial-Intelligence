import pandas as pd
import numpy as np
import pandas as pd
from sklearn import tree  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
from SI.DecisionTree.label import MultiColumnLabelEncoder

hemo = pd.read_csv('/home/breno/PycharmProjects/untitled2/Data/Dados HMG 04-04-2008 a 29-06-2018 - Raw.csv',
                   low_memory=False)

attrs = ['Municipio', 'Bairro', 'Profissao', 'Data do obito']
cls_attr = 'Data do obito'


def train_model(X_train, y_train):
    # Create Decision Tree classifer object
    clf = tree.DecisionTreeClassifier()

    # Train Decision Tree Classifer
    return clf.fit(X_train, y_train)


def slice_data(x, y):
    return train_test_split(x, y, test_size=0.3,
                            random_state=1)  # 70% training and 30% test


def test_model(clf, X_test, y_test):
    # Predict the response for test dataset
    y_pred = clf.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


# LIMPEZA DOS DADOS
def clean_null(df, attrs):
    for att in attrs[:-1]:
        df = df.dropna(subset=[att])
    return df


def filter_columns(df, attrs):
    return df[attrs]


def prepare_cls_attr(df, cls_atr):
    y = df[cls_attr].map({np.nan: 0.}).to_frame()
    y = y[cls_attr].map({np.nan: 1., 0.: 0.}).to_frame()  # atributo de classe
    y.columns = ('cls_a',)
    return y


hm = filter_columns(hemo, attrs)
hm = clean_null(hm, attrs)
y = prepare_cls_attr(hm, cls_attr)
hm = hm.drop(columns=[cls_attr])

le = MultiColumnLabelEncoder()
xt = le.fit_transform(hm)

