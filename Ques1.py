# Professor Utonium requires 3 ingredients to make Powerpuff Girls. 
# The 3 ingredients are present in the laboratory in the given quantity:

# To make a Powerpuff Girl, Professor Utonium requires:
# 1.	3 units of Ingredient A
# 2.	6 units of Ingredient B
# 3.	10 units of Ingredient C

# The maximum number of Powerpuff Girls which can be created are 3 as after 3, 
# Professor will run out of Ingredient C.

# Can you determine the maximum number?
# Input Format
# The first line of input consists of the number of ingredients, N
# The second line of input consists of the N space-separated integers 
# representing the quantity of each ingredient required to create a Powerpuff Girl.
# The third line of input consists of the N space-separated integers representing the 
# quantity of each ingredient present in the laboratory.
# Constraints
# 1<= N <=10000000 (1e7)
# 0<= Quantity_of_ingredient <= LLONG_MAX 

# Output Format
# Print the required output in a separate line.
# Sample TestCase 1

# Input
# 4
# 2 5 6 3 
# 20 40 90 50 
# Output
# 8 



#Solution

n = int(input("Enter the Number of element : "))
#n=4
ingedients = list(map(int,input("Enter unit of measure for each ingredients :").strip().split()))[:n]
#ingedients=[2,5,6,3]
quantity = list(map(int,input("Enter quantity avaiable for each ingredients :").strip().split()))[:n]
#quantity=[20,40,90,50]

result=[]

if ((len(ingedients) !=  4) & (len(quantity) != 4)):
    print("Please check the input")
else:
    for i in range(n):
        result.insert(i,int(quantity[i]/ingedients[i]))
    
print("Maximun number of powerpuff girls Prof can make = ", min(result))