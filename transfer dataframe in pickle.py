import pickle

# Save DataFrame to a pickle file
with open('data_with_rsi.pkl', 'wb') as f:
    pickle.dump(data, f)


###################################################################
import pickle

# Load DataFrame from the pickle file
with open('data_with_rsi.pkl', 'rb') as f:
    data_loaded = pickle.load(f)

# Now you can work with data_loaded as a DataFrame
print(data_loaded.head())
