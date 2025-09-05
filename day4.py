import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, f1_score, recall_score
import seaborn as sns
import matplotlib.pyplot as plt
#

data = pd.read_csv('spam.csv')
X = data.drop('spam', axis=1)
y = data['spam']

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.25, random_state = 42)
#Train the logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
#
print(X_test)
# Evaualate the model using accuracy,confussion matrix
accuracy = accuracy_score(y_test, y_pred)
pression = precision_score(y_test, y_pred)
recal = recall_score(y_test , y_pred)
f1 = f1_score(y_test, y_pred)

print (f"Accuracy :,{accuracy}")
print (f"Precision: ,{pression}")
print (f"Recall: , {recal}")
print (f"F1-Score: ,{f1}")

#visualize the confussion matrix using Seaborn

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True , fmt = 'd')
plt.title('Confusion Matrix')
plt.show()