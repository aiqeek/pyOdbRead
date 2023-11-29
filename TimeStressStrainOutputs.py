from odbAccess import *
from sys import argv
import numpy
#
aaa=argv[-1]
if aaa[0:2]!='C:':
	name=argv[-1]
if aaa[0:2]=='C:':
	print 'no file!'
	print argv[-1]
	name='dcb_k4444.44.odb'
if name[-3:]!='odb':
	name=name+'.odb'
#
#read in odb name from command line
odb=openOdb(path=name,readOnly=True)
#
#Select the assembly instance and Select element of interest for output
#NB python starts countin at 0, THEREFORE ELEMENT 1 IN MESH = INDEX 0
#TWO MATERIAL MODEL ELEMENT 1, INDEX 0 = WELD METAL
#TWO MATERIAL MODEL ELEMENT 2, INDEX 1 = PARENT METAL
#HERE PM-WM-1 IS THE INSTANCE PART NAME IN ASSEMBLY MODULE OF ABAQUS
el_ref=odb.rootAssembly.instances['PM_WM-1'].elements[1]         
#
#initialise empty arrays where data will be written to
fielddata=[]
STRANDAT=[]
STRESSDAT=[]
#
#Set stpnm equal to the number of steps 
stpnm = odb.steps.keys()
#
#For loop over number of steps
for stepId in range(len(stpnm)):
        #
        #Conditional statement selecting name of step,
        #step names must match input file exactly here
        #this model had an initial elastic step and a second creep steep 
        if stepId == 0:
                stepname='Elastic'
        else:
                stepname='UM_CREEP'
        #
        #next need to set up output from each frame in a step
        for frm in odb.steps[stepname].frames: 
                timerp=frm.frameValue           #writes frame number to frm
                try:
                        #STRAIN DATA EXTRACTION EVERY FRAME
                        edata=frm.fieldOutputs['E'].getSubset(region=el_ref,position=INTEGRATION_POINT)
                        #STRESS DATA EXTRACTION EVERY FRAME
                        sdata=frm.fieldOutputs['S'].getSubset(region=el_ref,position=INTEGRATION_POINT)
                        #APPEND DATA TO FIELDDATA VARIABLE FOR WRITING TO FILE
                        fielddata.append([timerp])
                        STRANDAT.append([edata.values[0].data[1]]) 
                        STRESSDAT.append([sdata.values[0].data[1]])
                except:
                        #print 'skipping partial frame'
                        bbbb=1
#
numpy.savetxt(name[0:-4]+'_TIME_V4.txt',fielddata, delimiter='\t')
numpy.savetxt(name[0:-4]+'_STRAIN_V4.txt',STRANDAT, delimiter='\t')
numpy.savetxt(name[0:-4]+'_STRESS_V4.txt',STRESSDAT, delimiter='\t')
#
