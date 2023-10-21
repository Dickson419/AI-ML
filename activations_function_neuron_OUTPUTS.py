import numpy as np

"""Program to give the three outputs of a neuron's activation: Hard threshold, logistic and rectifier"""

# Input value --> CHANGE THIS
x = 6

# Hard Threshold
hard_threshold_output = 1 if x >= 0 else 0

# Logistic Function
logistic_output = 1 / (1 + np.exp(-x))

# Rectifier Function
rectifier_output = max(0, x)

# Round to the nearest integer
hard_threshold_output = round(hard_threshold_output)
logistic_output = round(logistic_output)
rectifier_output = round(rectifier_output)

# Print the results
print("Hard Threshold Output:", hard_threshold_output)
print("Logistic Output:", logistic_output)
print("Rectifier Output:", rectifier_output)
