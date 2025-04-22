import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

random_state=1
output_file='model/final_model.bin'
DATA_PATH='SaYoPillow.csv'

#load the dataset
print("Loading the dataset...")
df=pd.read_csv(DATA_PATH)
df.columns=[
    'snoring_rate',
    'respiration_rate',
    'body_temperature',
    'limb_movement',
    'blood_oxygen',
    'eye_movement',
    'sleeping_hours',
    'heart_rate',
    'stress_level'
]
#train validation split
most_important_features = [
    'limb_movement',
    'sleeping_hours',
    'snoring_rate',
    'body_temperature',
    'eye_movement'
]
df_train, df_val = train_test_split(df, test_size=0.4, random_state=random_state, stratify=df.stress_level)


#training function
def train(df_train, y_train, random_state=1):
    dicts=df_train[most_important_features].to_dict(orient='records')
    dv=DictVectorizer(sparse=False)
    X_train=dv.fit_transform(dicts)
    model=XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    return dv, model
def predict(df, dv, model):
    dicts=df[most_important_features].to_dict(orient='records')
    X=dv.transform(dicts)
    y_pred=model.predict(X)
    return y_pred

print("Training the model...")
dv, model = train(df_train, df_train.stress_level.values, random_state)

#Run prediction and evaluate
print("Evaluating model...")
y_pred=predict(df_val, dv, model)
y_test=df_val.stress_level.values
acc=accuracy_score(y_test,y_pred)
print("Accuracy for Validation=%.3f"%acc)

#save the model and vectorizer
print(f"Saving the model to {output_file}...")
with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)
print('☑️ Model training is completed and saved.')