question_list = [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]
options_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]                                                                                   
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
help_option=[[3,4],[1,4],[1,2]]
helpline=0
i=0
while i<len(question_list):
    print ("this is your question")
    print (i+1,question_list[i])
    j=0
    print ("this is your option")
    while j<len(options_list[i]):
        print (j+1,options_list[i][j])
        j=j+1
    user_input=input("choose your option/do u want to helpline yes or no: ")
    if user_input=="yes" or "y":
        if helpline==0:
            print (help_option[i])
            give_option=int(input("enter your option: "))
            if give_option==solution_list[i]:
                print ("your answer is right")
                helpline=helpline+1
            else:
                print ("your answer is wrong")
                break
        else:
            print ("you can't use helpline")
            user=int(input("choose your option: "))
            if user==solution_list[i]:
                print ("your answer is right")
            else:
                print ("your answer is wrong")
                break
    elif user_input==solution_list[i]:
        print ("congrates your answer is right")
    else:
        print ("sadly your answer is wrong")
        break
    i=i+1



