#This is the intro to tell the user about the test.
print("Welcome to the MBTI personality analysis program. Here, you will explore your,MBTI type in 20 questions.")
#Here we tell the user to answer with "Agree" or "Disagree".
print("Answer the following question with 'agree' or 'disagree'.")
#final_result is the bag of the letters which store the suitable letter depending on the answers. 
final_result = ""
#Group 1 questions: Determine if the first letter is I or E.
agree_group1 = 0 
Q_ans1 = input("Q1: You regularly make new friends?")
if Q_ans1 == "agree":
    agree_group1 += 1
Q_ans2 = input("Q2: You find the idea of networking or promoting yourself to strangers easy?")
if Q_ans2 == "agree": 
    agree_group1 += 1
Q_ans3 = input("Q3: You enjoy participating in team-based activities?")
if Q_ans3 == "agree":
    agree_group1 += 1
Q_ans4 = input("Q4: You usually begin with introducing yourself first at social gatherings?")
if Q_ans4 == "agree": 
    agree_group1 += 1
Q_ans5 = input ("Q5: You feel more drawn to busy, bustling atmospheres than to quiet, intimate places?")
if Q_ans5 == "agree": 
    agree_group1 += 1
if agree_group1 >= 3:
    final_result = final_result + "E"
else:
    final_result = final_result + "I"
# Group 2 questions: Determine if the second letter is S or N.
agree_group2 = 0 
Q_ans6 = input ("Q6: You usually don't worry about turning a thing for the worse?")
if Q_ans6 == "agree":
    agree_group2 += 1
Q_ans7 = input("Q7: You can't imagine yourself writing fictional stories for living?")
if Q_ans7 == "agree": 
    agree_group2 += 1
Q_ans8 = input ("Q8: You usually base your choises on objective facts rather than emotional impressions?")
if Q_ans8 == "agree":
    agree_group2 += 1
Q_ans9 = input ("Q9: You don't enjoy unfamiliar ideas and view points?")
if Q_ans9 == "agree": 
    agree_group2 += 1
Q_ans10 = input ("Q10: You believe that pondering abstract philosophical questions is a waste of time?")
if Q_ans10 == "agree": 
    agree_group2 += 1
if agree_group2 >= 3:
    final_result = final_result + "S"
else:
    final_result = final_result + "N"
# Group 3 questions: Determine if the third letter is T or F.
Q_ans11 = input("Q11: You usually feel persuaded by what resonates emotionally with you than by factual arguments?")
if Q_ans11 == "agree":
    agree_group3 += 1
Q_ans12 = input("Q12: You can't prioritize facts over people's feeling when determining a course of action?")
if Q_ans12 == "agree":
    agree_group3 += 1
Q_ans13 = input("Q13: You prioritize being sensitive over being completely honest?")
if Q_ans13 == "agree":
    agree_group3 += 1
Q_ans14 = input("Q14: When facts and feelings conflict, you usually find yourself follow your heart?")
if Q_ans14 == "agree":
    agree_group3 += 1
Q_ans15 = input("Q15: You more likely to rely on emotional intuition than logical reasoning when making a choice?")
if agree_group3 >= 3: 
    final_result = final_result + "F"
else: 
    final_result = final_result + "T"
# Group 4 questions: Determine if the fourth letter is J or P.
Q_ans16 = input("Q16: Your living and working spaces are clean and organized?")
if Q_ans16 == "agree":
    agree_group4 += 1
Q_ans17 = input("Q17: You prioritize and plan tasks effectively, completing them well before the deadline?")
if Q_ans17 == "agree":
    agree_group4 += 1
Q_ans18 = input("Q18: You like to use organizing tools like schedules and lists?")
if Q_ans18 == "agree":
    agree_group4 += 1
Q_ans19 = input("Q19: You like to have a to do list for each day?")
if Q_ans19 == "agree":
    agree_group4 += 1
Q_ans20 = input("Q20: If your plans are interrupted, your top priority is to get back on track as soon as possible?") 
if Q_ans20 == "agree": 
    agree_group4 += 1
if agree_group4 >= 3:
    final_result = final_result + "J"
else:
    final_result = final_result + "P"
    # The end of the test.
print("your final MBTI type:" + final_result)
    
    
    
    
    
    
    
    
