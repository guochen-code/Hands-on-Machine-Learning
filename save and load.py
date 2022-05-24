# save and load model
import joblib

# save the model to disk
filename = '3Var_finalized_model.sav'
joblib.dump(voting_soft_clf, filename)

# some time later...
 
# load the model from disk
loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, y_test)
print(result)


*******************************************************************************************************************************************************

# save and load scaler
from pickle import dump
from pickle import load

# save the scaler to disk
dump(scaler_range, open('scaler.pkl', 'wb'))

# some time later...
 
# load the scaler from disk
scaler_3Var = load(open('scaler.pkl', 'rb'))

*******************************************************************************************************************************************************
# save and load pipeline
from pickle import dump
from pickle import load

# save the scaler to disk
dump(clf, open('pipeline.pkl', 'wb')) # clf: refer to sklearn pipeline

# some time later...
 
# load the scaler from disk
pipe= load(open('pipeline.pkl', 'rb'))

pipe.fit(X_train, y_train)

pipe.predict(X_test)


