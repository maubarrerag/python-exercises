# Test Simulation class
from Simulation import Simulation
from Die import Die

die = Die()
sim = Simulation(die.roll, 1000)
print(sim.mean, sim.median, sim.mode)