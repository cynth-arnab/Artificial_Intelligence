import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import HillClimbSearch, BicScore, MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


data = pd.DataFrame(data={
    'A': [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    'B': [0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    'C': [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})


hc = HillClimbSearch(data)
best_model = hc.estimate(scoring_method=BicScore(data))

print("Learned structure: ", best_model.edges())


model = BayesianNetwork(best_model.edges())
model.fit(data, estimator=MaximumLikelihoodEstimator)


for cpd in model.get_cpds():
    print("CPD of {variable}:".format(variable=cpd.variable))
    print(cpd)


inference = VariableElimination(model)


result = inference.query(variables=['C'], evidence={'A': 1})
print("\nProbability of C given A=1:")
print(result)

result = inference.query(variables=['C'], evidence={'A': 1, 'B': 0})
print("\nProbability of C given A=1 and B=0:")
print(result)

