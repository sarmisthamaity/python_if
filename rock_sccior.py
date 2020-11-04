u1=input("enter word: ")
u2=input("enter word: ")
if u1==u2:
	print ("it is a tie")
if u1=="scissors":
	if u2=="rock":
		print("rock wins")
	else:
		print ("paper wins")
if u1=="paper":
	if u2=="scissors":
		print("scissors wins")
	else:
		print ("rock wins")
if u1=="rock":
	if u2=="paper":
		print ("paper wins")
	else:
		print ("scissors wins")
else:
	print ("invalid input! you have not entered rock,paper or scissor try again")
