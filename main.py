from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузка набора данных Iris
iris = load_iris()

# Разделение набора данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.9, random_state=42)

# Создание и обучение модели логистической регрессии
model = LogisticRegression()
model.fit(X_train, y_train)

# Прогнозирование классов на тестовой выборке
y_pred_test = model.predict(X_test)
y_train_pred = model.predict(X_train)

# Оценка производительности модели ok
accuracy = accuracy_score(y_test, y_pred_test)
accuracy_train = accuracy_score(y_train,y_train_pred)
print("Accuracy:", accuracy)
print("Accuracy:", accuracy_train)

