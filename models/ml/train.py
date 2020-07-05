from joblib import dump
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier


iris = datasets.load_iris(return_X_y=True)
y = iris[1]
X = iris[0]


clf_pipeline = [('scaling', MinMaxScaler()), ('clf', RandomForestClassifier(random_state=42))]
pipeline = Pipeline(clf_pipeline)

pipeline.fit(X, y)

dump(pipeline, './ml/iris_rf_v1.joblib')
