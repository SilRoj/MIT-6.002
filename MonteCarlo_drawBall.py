#Monte Carlo sim for buckets
import random
from pylab import plot, axis, title, ylabel, xlabel, show, grid

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

    sum = 0.0
    for i in range(numTrials):
    	Bucket = [1,2,3,4,5,6]
    	redBall = 0
    	greenBall = 0
    	for j in range(3):
    		DrawnBall = random.choice(Bucket)
    		#print DrawnBall
    		if DrawnBall < 4:
    			redBall += 1.0
    		else:
    			greenBall += 1.0
    		Bucket.remove(DrawnBall)
    		#print Bucket
    	if redBall == 3 or greenBall == 3:
    		sum += 1.0
    		#print sum
    return sum/numTrials


def showPlot1(numTrials):
	x = []
	y = []
	for i in range(1,numTrials):
		x.append(i)
		y.append(noReplacementSimulation(i))
	
	plot(x, y)
	grid(linestyle='--',lw=2,marker='o',)
	title('Bucket Simulation')
	ylabel("over %s trials" % numTrials)
	xlabel("Room area")    
	show()

showPlot1(1000)




