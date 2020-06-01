# A player can win only when his/her beyblade power is strictly greater than the opponents 
# beyblade power.

# Example:
# Consider the team size is 3, N = 3

# The 3 players of both the teams are shown with their beyblade powers.

# Team G-Revolution is presented in the order: Tyson, Max, Ray
# Team All Starz is presented in the order: Michael, Eddy, Steve

# With the given arrangement, Team G-Revolution would be able to win only 1 fight. 
# Team G-Revolution should be shuffled in an optimal manner as below:

# The maximum number of fights Team G-Revolution can win is 2 when they are arranged optimally or 
# fight in an optimal order.

# Team G-Revolution needs help with the device. Tyson has heard about your skills and called 
# you up to help them shuffle their positions in an order such that they would be able to win 
# the maximum number of fights. Can you help Tyson and Team G-Revolution?

# Input Format
# The first line of input consists of the number of test cases, T
# The first line of each test case consists of the number of members each team can have, N.
# The second line of each test case consists of N space-separated integers representing the power of beyblades of Team G-Revolution members.
# The third line of each test case consists of N space-separated integers representing the power of beyblades of opponent team members.

# Constraints
# 1<= T <=100000
# 1<= N <=100000
# 0<= Power of Beyblade <= LLONG_MAX 

# Output Format
# For each test case, print the maximum number of fights Team G-Revolution can win if they go to fight in an optimal manner.

# Sample TestCase 1
# Input
# 1
# 10
# 3 6 7 5 3 5 6 2 9 1 
# 2 7 0 9 3 6 0 6 2 6 
# Output
# 7
############################################################################################################
#SOlution

#Enter the number of League#
case = int(input("Enter the number of Cases: "))
#case = 1

#Enter the number of players in each team
member = int(input("Enter the number of players in each team: "))
#member = 10
#member = 3

#Enter the Power Level of each player in List format
teamg = list(map(int,input("\nEnter the power level of each player in team G: ").strip().split()))[:member]
#teamg=[3,6,7,5,3,5,6,2,9,1]
#teamg=[20,50,30]

#list(input("Enter the power level of each player in team G"))
teamas = list(map(int,input("\nEnter the power level of each player in team All Starz: ").strip().split()))[:member]
#teamas=[2,7,0,9,3,6,0,6,2,6]
#teamas=[60,40,25]

teamg.sort(reverse=False)
teamas.sort(reverse=False)
win=0

for i in range(member):
    teamaslen=len(teamas)
    for j in range(teamaslen):
        if teamg[i]>teamas[j]:
            win= win + 1
            print("\nPlay ", teamg[i], " with ", teamas[j])
            teamas.pop(j)
            break
print("\nTotal Win after tournament : ", win)

