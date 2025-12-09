import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis de entrada
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Variável de saída
power = ctrl.Consequent(np.arange(0, 101, 1), 'power')

# Conjuntos fuzzy
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['medium'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['high'] = fuzz.trimf(temperature.universe, [30, 40, 40])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['high'] = fuzz.trimf(humidity.universe, [40, 100, 100])

power['low'] = fuzz.trimf(power.universe, [0, 0, 50])
power['medium'] = fuzz.trimf(power.universe, [30, 50, 70])
power['high'] = fuzz.trimf(power.universe, [60, 100, 100])

# Regras fuzzy
rule1 = ctrl.Rule(temperature['low'] & humidity['low'], power['low'])
rule2 = ctrl.Rule(temperature['medium'] & humidity['low'], power['medium'])
rule3 = ctrl.Rule(temperature['high'] & humidity['low'], power['high'])
rule4 = ctrl.Rule(temperature['low'] & humidity['high'], power['medium'])
rule5 = ctrl.Rule(temperature['medium'] & humidity['high'], power['high'])
rule6 = ctrl.Rule(temperature['high'] & humidity['high'], power['high'])

power_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])

# Função usada pelo Streamlit
def compute_power(temp, umid):
    sim = ctrl.ControlSystemSimulation(power_ctrl)
    sim.input['temperature'] = temp
    sim.input['humidity'] = umid
    sim.compute()
    return sim.output['power']
