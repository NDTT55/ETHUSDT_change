import trainmodel
from sklearn.model_selection import train_test_split
import gettingdata
import numpy
import currentdata

if __name__=='__main__':
   btc_data,eth_data=gettingdata.go()
   X = numpy.array([[i] for i in btc_data['Change %']])
   y = numpy.array(eth_data['Change %'])
   X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8)
   model=trainmodel.go(X_train,y_train,X_test,y_test)
   currentdata.go(model)