from ps3b_precompiled_27 import *

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        
    rViruses = []
    rResist = []
    
    #initialize the results holder
    for i in range(300):
        rViruses.append(0.0)
        rResist.append(0.0)
        
    #run the trials
    for trial in range(numTrials):
        #create a new patient:
        p = TreatedPatient(viruses[:], maxPop)
        
        #run the first 150 trials:
        for j in range(0, 150):
            rViruses[j] += p.update()
            rResist[j] += p.getResistPop(['guttagonol'])
            
        #add the prescriptions
        p.addPrescription('guttagonol')
        
        #run the next 150 trials:
        for j in range(150, 300):
            rViruses[j] += p.update()
            rResist[j] += p.getResistPop(['guttagonol'])
            
    #take the averages
    for i in range(300):
        rViruses[i] /= float(numTrials)
        rResist[i] /= float(numTrials)
        
    #make the total plot
    pylab.figure()

    pylab.plot(rViruses, label = 'Total Population')
    #make the resistant plot
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.plot(rResist, label='Resistant Population')
    pylab.legend()
    pylab.show()