X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]

def predict(X, c):
    for i in X:
        price = sum(coef * c_value for coef, c_value in zip(i, c))
        print(price)

predict(X, c)
