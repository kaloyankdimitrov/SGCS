import random
# with 1% failures
TRIALS=3
STEPS=2000
WIDTH=801
HEIGHT=801
BOT_COUNT=100
SPEED=2
SENSOR_RANGE=2
DECISION_STEPS=10
CONSIDERED_POSITIONS=5
PHEROMONE_STRENGTH=100
FENCE_STRENGTH=1
EVAPORATION_RATE=0.12
PHEROMONE_DROP_STEPS=20
COMM_RANGE=50

def failure(i):
    if random.random() < 0.01:
        return 1
    return 0
