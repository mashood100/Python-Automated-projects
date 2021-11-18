################# proccess input
proclst = []
n = int(input("Enter number of Proccess : "))
 
for i in range(0, n):
    ele = i
 
    proclst.append(ele) # adding the element
print("Process Number List: ", proclst )
################################ proccess input end


######################## brust time



brustlst = []
 
for i in range(0, n):
    element_B = int(input("One By one enter Brust Time of each Process  "))
 
    brustlst.append(element_B) # adding the element
     
print("Brust times List: ",brustlst )



##########################

proc = proclst
n = len(proclst)

burst_time = brustlst

#  Quantum Time
quantum = int(input(("enter Quantum time : ")))


# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, bt,
						wt, quantum):
	rem_bt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 # Current time

	# Keep traversing processes in round
	# robin manner until all of them are
	# not done.
	while(1):
		done = True

		# Traverse all processes one by
		# one repeatedly
		for i in range(n):
			
			# If burst time of a process is greater
			# than 0 then only need to process further
			if (rem_bt[i] > 0) :
				done = False # There is a pending process
				
				if (rem_bt[i] > quantum) :
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t += quantum

					# Decrease the burst_time of current
					# process by quantum
					
					rem_bt[i] -= quantum
					
				    
				# If burst time is smaller than or equal
				# to quantum. Last cycle for this process
				else:
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t = t + rem_bt[i]

					# Waiting time is current time minus
					# time used by this process
					wt[i] = t - bt[i]

					# As the process gets fully executed
					# make its remaining burst time = 0
					rem_bt[i] = 0
			print("Remaining Brust Time",rem_bt[i],"sec of Process",proc[i])		
				
		# If all processes are done break the Loop
		if (done == True):
			break
			
# Fun calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = bt[i] + wt[i]


# Fun to calculate average waiting
# and turn-around times.
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	# Fun to find waiting time
	# of all processes
	findWaitingTime(processes, n, bt,
						wt, quantum)

	# Fun to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, bt,
								wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	

findavgTime(proc, n, burst_time, quantum)
