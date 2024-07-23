#Bayesian-Network
pip install pgmpy

import numpy as np
import csv
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

heartDisease = pd.read_csv('/content/heart.csv')
heartDisease = heartDisease.replace('?', np.nan)

heartDisease['age'] = pd.cut(heartDisease['age'], bins=[0, 30, 40, 50, 60, 70, 80, 90, 100],
                             labels=['0-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'])

print('Few examples from the dataset are given below')
print(heartDisease.head())

model = BayesianNetwork([('age', 'trtbps'), ('age', 'fbs'),
                         ('sex', 'trtbps'), ('exng', 'trtbps'),
                         ('trtbps', 'output'), ('fbs', 'output'),
                         ('output', 'restecg'), ('output', 'thalachh'),
                         ('output', 'chol')])

print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

print('\n1. Probability of Heart Disease given Age=30-40')
q = HeartDisease_infer.query(variables=['output'], evidence={'age': '30-40'})
print(q.values[0])

print("\nUnique values of 'chol':")
print(heartDisease['chol'].unique())

print('\n2. Probability of Heart Disease given cholesterol=233')
q = HeartDisease_infer.query(variables=['output'], evidence={'chol': 233})
print(q.values[0])

edges = [('age', 'trtbps'), ('age', 'fbs'), ('sex', 'trtbps'), ('exng', 'trtbps'),
         ('trtbps', 'output'), ('fbs', 'output'), ('output', 'restecg'),
         ('output', 'thalachh'), ('output', 'chol')]

G = nx.DiGraph()


G.add_edges_from(edges)

edges = [('age', 'trtbps'), ('age', 'fbs'), ('sex', 'trtbps'), ('exng', 'trtbps'),
         ('trtbps', 'output'), ('fbs', 'output'), ('output', 'restecg'),
         ('output', 'thalachh'), ('output', 'chol')]


G = nx.DiGraph()

G.add_edges_from(edges)

colors = {'age': 'red', 'trtbps': 'blue', 'fbs': 'green', 'sex': 'yellow',
          'exng': 'purple', 'output': 'orange', 'restecg': 'pink',
          'thalachh': 'gray', 'chol': 'cyan'}

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=[colors[node] for node in G.nodes])

for label, color in colors.items():
    plt.plot([0], [0], color=color, label=label)
plt.legend()

plt.show()

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
