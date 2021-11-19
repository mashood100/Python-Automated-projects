"""
Algorithm

Step-1- Create an array rem_bt[] to keep track of remaining
   burst time of processes. This array is initially a 
   copy of bt[] (burst times array)
Step -2 Create another array wt[] to store waiting times
   of processes. Initialize this array as 0.
Step -3- Initialize time : t = 0
Step -4- Keep traversing the all processes while all processes
   are not done. Do following for i'th process if it is
   not done yet.
    a- If rem_bt[i] > quantum
       (i)  t = t + quantum
       (ii) rem_bt[i] -= quantum;
    c- Else // Last cycle for this process
       (i)  t = t + rem_bt[i];
       (ii) wt[i] = t - bt[i]
       (ii) rem_bt[i] = 0; // This process is over

"""









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


#  Waiting time

def findWaitingTime( n, bt, wt, quantum):
    
#  genrating the length for Remaining Brust Time   List   
	rem_bt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 # Current time

# Applying above Algorithm of Round Robin 
 #intilize done variable not done.
	while(1):
      # initlized this true so when interpreter move out from the If else condition The value set to True and loop break out  
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
def findTurnAroundTime( n, bt, wt, tat):
	
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
	findWaitingTime( n, bt,
						wt, quantum)

	# Fun to find turn around time
	# for all processes
	findTurnAroundTime( n, bt,
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