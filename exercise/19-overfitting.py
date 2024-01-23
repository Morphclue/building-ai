from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

x, y = make_moons(
    n_samples=500,
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
knn = KNeighborsClassifier(n_neighbors=42)
knn.fit(x_train, y_train)

print("training accuracy: %f" % knn.score(x_train, y_train))
print("testing accuracy: %f" % knn.score(x_test, y_test))
