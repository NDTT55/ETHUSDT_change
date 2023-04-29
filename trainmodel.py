from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
def go(X_train,y_train,X_test,y_test):
    #тренируем линейную регрессию
    model=LinearRegression()
    model.fit(X=X_train,y=y_train)
    print('MSE:',mean_squared_error(y_true=y_test, y_pred=model.predict(X_test)))
    print("MAE:", mean_absolute_error(y_true=y_test, y_pred=model.predict(X_test)))
    plt.scatter(X_test, y_test,label='real')
    plt.scatter(X_test, model.predict(X_test),label='predict')
    plt.legend()
    plt.title('difference between real and predict')
    plt.show()
    return model







