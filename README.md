# 6002x
A collection of problem sets solved for MIT's Introduction to Computational Thinking and Data Science course on edX.
This was the fall 2015 course. Over the course of six weeks, I learned the foundations of graphs, modelling, 
and conducting simulations using Python's Pylab package. Below, you can find descriptions of some of the more interesting problem sets.

### Problem Set 2
This was perhaps the most fun assignment of the entire course. As an introduction to models and simulations, I compared the performance
of two different kinds of vacuum cleaning robots using the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
(which involves using randomness to solve problems that may be deterministic in principle). 
The model was extended to analyze the impacts of room dimensions and the presence of multiple robots running concurrently. 

### Problem Set 3
This problem set required me to build a simplified model used to analyze the lifecycle and evolution of viruses in patient's body. Using 
this model, I understood how quickly different viruses spread around the body, and how they may evolve to develop resistances to certain
drugs. I additionally plotted graphs to understand the various distributions further. 

### Problem Set 4
Essentially an extension of problem set 3. I built upon the existing virus, drug, and patient models to run new simulations and 
and understand more about what was happening. In particular, I used these simulations to determine the best time during the virus
lifecycle to diagnose the patient with drugs. Inside the plots folder, you can see the final results after running the several trials 
of the growth. The delay indicates the number of time steps between infection and diagnosis. As you might expect, the final virus population is least when the patient is diagnosed earlier. 

### Problem Set 5
This focused on graph algorithms and optimization. `mit_map.txt` contains data about the paths between buildings on the MIT campus.
`map_representation.gif` is the visual representation of `mit_map.txt` The first two numbers one each line are codes for buildings. 
The third number indicates the total distance between the two buildings, and the fourth indicates the outdoor distance. 
The goal was to implement a graph data structure, and then use breadth-first and depth-first search to find the shortest distance 
given some constraints (the total outdoor distance should be less than 550m, example).
