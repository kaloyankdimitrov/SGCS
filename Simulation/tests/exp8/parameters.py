import random
# with 1% failure chance
TRIALS=5
STEPS=20000
WIDTH=801
HEIGHT=801
BOT_COUNT=20
SPEED=2
SENSOR_RANGE=2
DECISION_STEPS=20
CONSIDERED_POSITIONS=5
PHEROMONE_STRENGTH=50
FENCE_STRENGTH=1
PHEROMONE_DROP_STEPS=10
COMM_RANGE=200
def failure(i):
    if random.random() < 0.01:
        return 1
    return 0
