'''
# importing the necessary packages 
import time 
import sys 
import os 
https://ap-southeast-1.console.aws.amazon.com/cloud9/ide/15a23549b9cd4d93965c2cc6f15995f4

# Function for implementing the loading animation 
def load_animation(): 

	# String to be displayed when the application is loading 
	load_str = "starting your console application..."
	ls_len = len(load_str) 


	# String for creating the rotating line 
	animation = "|/-\\"
	anicount = 0
	
	# used to keep the track of 
	# the duration of animation 
	counttime = 0		
	
	# pointer for travelling the loading string 
	i = 0					

	while (counttime != 100): 
		
		# used to change the animation speed 
		# smaller the value, faster will be the animation 
		time.sleep(0.075) 
							
		# converting the string to list 
		# as string is immutable 
		load_str_list = list(load_str) 
		
		# x->obtaining the ASCII code 
		x = ord(load_str_list[i]) 
		
		# y->for storing altered ASCII code 
		y = 0							

		# if the character is "." or " ", keep it unaltered 
		# switch uppercase to lowercase and vice-versa 
		if x != 32 and x != 46:			 
			if x>90: 
				y = x-32
			else: 
				y = x + 32
			load_str_list[i]= chr(y) 
		
		# for storing the resultant string 
		res =''			 
		for j in range(ls_len): 
			res = res + load_str_list[j] 
			
		# displaying the resultant string 
		sys.stdout.write("\r"+res + animation[anicount]) 
		sys.stdout.flush() 

		# Assigning loading string 
		# to the resultant string 
		load_str = res 

		
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len 
		counttime = counttime + 1
	
	# for windows OS 
	if os.name =="nt": 
		os.system("cls") 
		
	# for linux / Mac OS 
	else: 
		os.system("clear") 

# Driver program 
if __name__ == '__main__': 
	load_animation() 

	# Your desired code continues from here
	# s = input("Enter your name: ") 
	s ="****ROOM RP****"
	sys.stdout.write("Hello "+str(s)+"\n") 

'''

#Rocket Animation - www.101computing.net/text-based-animations/
import os
import time

def animate_Rocket():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)
    print("          /\        ")
    print("         /RP\       ")
    print("         |HO|       ")
    print("         |NY|       ")
    print("         /||\       ")
    time.sleep(0.2)
    os.system('clear')  
    distanceFromTop -= 1
    if distanceFromTop <0:
      distanceFromTop = 20
  
  
#Main Program Starts Here....
animate_Rocket()
'''


while True:
    print("\n" * distanceFromTop)
    print("          /\        ")
    print("          ||        ")
    print("          ||        ")
    print("         /||\        ")
    time.sleep(0.2)
    os.system('clear')  
    distanceFromTop -= 1
    if distanceFromTop <0:
      distanceFromTop = 20
  
'''































