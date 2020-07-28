from threading import main_thread
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import joblib

def train():
  dataset = datasets.load_digits()
  X = dataset.images
  y = dataset.target
  X = X.reshape((-1, 64))
  clf = LinearSVC()
  clf.fit(X, y)
  joblib.dump(clf, 'digits.pkl')

if __name__ == "__main__":
    train()
