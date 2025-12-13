import pickle

model = pickle.load(open("model/model.pkl", "rb"))

price = model.predict([[1600, 3, 2]])
print("Predicted Price:", price[0])
