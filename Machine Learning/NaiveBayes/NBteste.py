import pandas as pd
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Designa as variáveis previsor e alvo
x = np.array([[-3, 7], [1, 5], [1, 2], [-2, 0], [2, 3], [-4, 0], [-1, 1], [1, 1], [-2, 2], [2, 7], [-4, 1], [-2, 7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])

model = GaussianNB()

# Treina o modelo usando os dados de treino
model.fit(x, y)

# Resultado de previsão
predicted = model.predict([[1, 2]])
print(predicted)
