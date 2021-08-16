# Test Simulation class:

from Die import Die
from Simulation import Simulation

die = Die()
sim = Simulation(die.roll, 1000)
print(sim.mean, sim.median, sim.mode)