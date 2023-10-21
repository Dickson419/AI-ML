import math

"""Hard Threshold"""
def hard_threshold(x):
    return 1 if x > 0 else 0

def evaluate_hypothesis(hypothesis, examples):
    correct_predictions = all(hard_threshold(hypothesis(*example[:-1])) == example[-1] for example in examples)
    return 'y' if correct_predictions else 'n'

"""Logistic Threshold"""
def logistic(x):
    return 1 / (1 + math.exp(-x))

def evaluate_logistic_hypothesis(hypothesis, examples):
    correct_predictions = all(round(logistic(hypothesis(*example[:-1]))) == example[-1] for example in examples)
    return 'y' if correct_predictions else 'n'


"""Rectifier Threshold"""
def rectifier(x):
    return max(0, x)

def evaluate_rectifier_hypothesis(hypothesis, examples):
    correct_predictions = all(round(rectifier(hypothesis(*example[:-1]))) == example[-1] for example in examples)
    return 'y' if correct_predictions else 'n'

# Hypotheses
rectifier_hypotheses = [
    lambda x, y: rectifier(x + y - 4.5),
    lambda x, y: rectifier(x + y - 3.5),
    lambda x, y: rectifier(-x - y + 3.5),
    lambda x, y: rectifier(x + y - 2.5)
]

# Examples with attributes (x, y) and labels
examples = [
    (1, 1, 0),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)
]

# Evaluate each hypothesis
for i, hypothesis in enumerate(rectifier_hypotheses, start=1):
    result = evaluate_rectifier_hypothesis(hypothesis, examples)
    print(f'Rectifier Hypothesis {chr(64 + i)}: {result}')





##### Logistic threshold #####


# Examples with attributes (x, y) and labels
examples = [
    (1, 1, 0),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)
]

# Hypotheses
logistic_hypotheses = [
    lambda x, y: logistic(x + y - 4.5),
    lambda x, y: logistic(x + y - 3.5),
    lambda x, y: logistic(-x - y + 3.5),
    lambda x, y: logistic(x + y - 2.5)
]

# Evaluate each hypothesis
for i, hypothesis in enumerate(logistic_hypotheses, start=1):
    result = evaluate_logistic_hypothesis(hypothesis, examples)
    print(f'Logistic Hypothesis {chr(64 + i)}: {result}')



#### HARD THRESHOLD #####
# Examples with attributes (x, y) and labels
examples = [
    (1, 1, 0),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)
]

# Hypotheses
hypotheses = [
    lambda x, y: x + y - 4.5,
    lambda x, y: x + y - 3.5,
    lambda x, y: -x - y + 3.5,
    lambda x, y: x + y - 2.5
]

# Evaluate each hypothesis
for i, hypothesis in enumerate(hypotheses, start=1):
    result = evaluate_hypothesis(hypothesis, examples)
    print(f'Hypothesis {chr(64 + i)}: {result}')
