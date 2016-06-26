# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    numViruses=100; maxPop=1000; maxBirthProb=0.1; clearProb = 0.05;
    resistances = {'guttagonol': False};
    mutProb = 0.005;
    
    rViruses = []
    rResist = []
    
    delay = 75
    
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    
    #initialize the results holder
    finalPops = []  
    
    
    for trial in range(numTrials):
        #initialize a num_holder
        numViruses = 0
        
        # create a new patient
        p = TreatedPatient(viruses[:], maxPop)
        #run the delayed trials before adding prescription
        for j in range(delay):
            numViruses= p.update()
            
        #add the prescription
        p.addPrescription('guttagonol')
        
        #run the next 150 trials
        for j in range(delay, delay + 150):
            numViruses = p.update()
        
        finalPops.append(numViruses)
        
    pylab.hist(finalPops, bins = 10)
    pylab.xlabel('Final Virus Population for Delay = ' + str(delay))
    pylab.ylabel('Frequency')
    pylab.show()
        
    

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials, d = 0):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    maxPop = 1000
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
    
    delay = d
    
    virusPops = []
    
    for trial in range(numTrials):
        p = TreatedPatient(viruses[:], maxPop)
        
        #create a local holder for the number of viruses
        numViruses = 0
        
        #run the first 150 trials...
        for j in range(150):
            numViruses = p.update()
            
        p.addPrescription('guttagonol')
        
        
        #run the delayed updates...
        for j in range(delay):
            numViruses = p.update()
            
        p.addPrescription('grimpex')
        
        #run another 150 steps...
        for j in range(150):
            numViruses = p.update()
            
        #update the pops holder...
        virusPops.append(numViruses)
        
    #make the plots
    pylab.title('Plot for delay = ' + str(delay))
    pylab.xlabel('Final Virus Population')
    pylab.ylabel('Frequency of Occurence')
    pylab.hist(virusPops, bins = 10)
    pylab.show()
            
    print 'Variance for delay = ' + str(delay) + ': ' + str(getVariance(virusPops))
    
def getVariance(li):
        
        mean = sum(li)/float(len(li))
        
        Ex2f = 0
        for elem in li:
            Ex2f += (elem - mean)**2
            
        return float(Ex2f)/len(li)
        
        


