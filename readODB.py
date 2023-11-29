import sys
print(sys.version)
sys.path.append("C:\\Program Files\\folderFromAbaqusLearningVersion_\\code_\\win_b64\\code\\bin")
#sys.path.append('C:\Program Files\folderFromAbaqusLearningVersion_\code_\win_b64\code\python2.7\lib')
from odbAccess import openOdb

# Path to your ODB file
odb_path = "Job-1.odb"

# Open the ODB file
odb = openOdb(odb_path)

# Access the first step in the ODB
step_name = odb.steps.keys()[0]  # Assumes there is at least one step
step = odb.steps[step_name]

# Access the first frame in the step
frame = step.frames[0]

# Print some information from the ODB
print("ODB Information:")
print(f"ODB Name: {odb.name}")
print(f"Step Name: {step.name}")
print(f"Frame Number: {frame.frameId}")

# Access nodal displacements from the first node
node_label = 1  # Change this to the label of the node you are interested in
node = odb.rootAssembly.nodeSets["ALL_NODES"].nodes[node_label - 1]
disp = frame.fieldOutputs["U"].getSubset(region=node)

# Print nodal displacements
print("\nNodal Displacements:")
for value in disp.values:
    print(f"Node {node_label} - U1: {value.data[0]}, U2: {value.data[1]}, U3: {value.data[2]}")

# Close the ODB file
odb.close()