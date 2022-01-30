#1. Downloading, Installing and Starting Python SciPy
#1.1 Install SciPy Libraries
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#https://www.scipy.org/install.html
#1.2 Start Python and Check Versions
python

# Check the versions of libraries
 
# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
#2. Load The Data
#2.1 Import libraries
# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
...
#2.2 Load Dataset
...
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
#3.1 Dimensions of Dataset
...
# shape
print(dataset.shape)
#You should see 150 instances and 5 attributes:(150, 5)
#3.2 Peek at the Data
...
# head
print(dataset.head(20))
#You should see the first 20 rows of the data
#3.3 Statistical Summary
...
# descriptions
print(dataset.describe())
#3.4 Class Distribution
...
# class distribution
print(dataset.groupby('class').size())
#4. Data Visualization
#4.1 Univariate Plots
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()


