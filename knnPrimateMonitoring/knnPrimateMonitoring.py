# Importing related Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# importing libraries
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


# Importando o dataset de treino
df = pd.read_excel('C:/Users/Lucas/OneDrive/Documents/PYTHON PROJECTS/Machine Learning/Knn algorithm/knnPrimateMonitoring/Data/trainData.xlsx')

print(df.head())
print(df.dtypes)
print(df.describe())


print(df['Sexo do animal'].value_counts())
print(df['Algum grupo'].value_counts())
print(df['Hibrído?'].value_counts())

# Substituindos os valores das variaveis categóricas
df["Sexo do animal"].unique()
df["Sexo do animal"].replace(['female', 'male'], [0,1], inplace=True)

df["Algum grupo"].unique()
df["Algum grupo"].replace(['yes', 'no'], [1,0], inplace=True)

df["Hibrído?"].unique()
df["Hibrído?"].replace(['yes', 'no'], [1,0], inplace=True)

df["Area urbana?"].unique()
df["Area urbana?"].replace(['yes', 'no'], [1,0], inplace=True)

print(df.head())


plt.figure(figsize=(12,10))
# Heatmap para auxiliar na escolha das variáveis principais de treino 
p=sns.heatmap(df.corr(), annot=True,cmap ='RdYlGn')  
plt.show()

X = np.array(df.filter(['Sexo do animal', "Hibrído?", "Tamanho do animal(cm)", "Peso do animal(gramas)", "Idade(ano)"
                        'Algum grupo', "Area urbana?"  ], axis=1))
y = np.array(df.filter(['DeadOrAlive'], axis=1))

# Validação cruzada simples
X_1, X_test, y_1, y_test = train_test_split(X,y, test_size=0.3)
X_tr, X_cv, y_tr, y_cv = train_test_split(X_1, y_1, test_size=0.3)

final_scores = []
for i in range(1,30,2):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_tr, y_tr)
    pred = knn.predict(X_cv)
    acc = accuracy_score(y_cv, pred, normalize=True) * float(100)
    final_scores.append(acc)
    print('\n CV accuracy for k=%d is %d'%(i,acc))

optimal_k = final_scores.index(max(final_scores))
print(optimal_k)

print("Média: {:.2f}%".format(np.mean(final_scores)))
print("Desvio padrão: {:.2f}%".format(np.std(final_scores)))

sns.distplot(final_scores)
plt.yticks([])
plt.title("Acurácias do k-NN")
plt.show()

# Obtendo a acurácia se K=5 nos dados de teste
df_test1 = pd.read_excel('C:/Users/Lucas/OneDrive/Documents/PYTHON PROJECTS/Machine Learning/Knn algorithm/knnPrimateMonitoring/Data/testData.xlsx')
print(df_test1)

# Substituindos os valores das variaveis categóricas
df_test1["Sexo do animal"].unique()
df_test1["Sexo do animal"].replace(['female', 'male'], [0,1], inplace=True)

df_test1["Algum grupo"].unique()
df_test1["Algum grupo"].replace(['yes', 'no'], [1,0], inplace=True)

df_test1["Hibrído?"].unique()
df_test1["Hibrído?"].replace(['yes', 'no'], [1,0], inplace=True)

df_test1["Area urbana?"].unique()
df_test1["Area urbana?"].replace(['yes', 'no'], [1,0], inplace=True)

print(df_test1.head())

X_test = np.array(df_test1.filter(['Sexo do animal', "Hibrído?", "Tamanho do animal(cm)", "Peso do animal(gramas)", "Idade(ano)"
                        'Algum grupo', "Area urbana?"  ], axis=1))
knn = KNeighborsClassifier(n_neighbors = optimal_k)
knn.fit(X_tr, y_tr)
pred = knn.predict(X_test)
print(pred)

#Criando um arquivo com o resultado da previsão
df_test1['Survived'] = pd.Series(pred, index=df_test1.index)
df_test1["Survived"].unique()
df_test1["Survived"].replace([1, 0], ['yes', 'no'], inplace=True)

print(df_test1)

final_df = df_test1.filter(['Id_primata','Survived'], axis=1)
print(final_df.shape)

final_df.to_excel("pred_Survived.xlsx", index=False)


# data and target
data, target = df.drop(columns = ['DeadOrAlive']), df['DeadOrAlive']

# KNN classifier model
knn = KNeighborsClassifier()

# K-fold (k=5)
scores = cross_val_score(knn, data, target, cv=5, scoring='accuracy')

print(scores)
# Results
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))








