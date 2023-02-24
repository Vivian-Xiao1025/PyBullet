import pybullet as p

# Load the saved state of the simulation
p.connect(p.GUI)
p.restoreState(fileName="turtleState.bullet")
print("State restored")
