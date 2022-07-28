import pickle

z = open("strcode","rb")
a = pickle.load(z)
z.close
print(a)