print('Welcome to Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Who is our protagonist, Elliot? ')
    if answer.lower()=='From the onset, we learn that Elliot sees a therapist, avoids physical contact, and is an introvert. As a hobby, he enjoys hacking his friends to find out their secrets, obsessions, and other pecadilloes. For example, when he learns his therapist, Krista, is dating a married man, Elliot interferes and makes the man stop stringing her along. When he has finished hacking a person, he stores all the information on CDs kept in a booklet and titles them with popular dad-rock album names.':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: And also, why does everyone on the show call E Corp Evil Corp?')
    if answer.lower()=='Because we are watching from Elliot’s point of view, and that’s how he hears people say it in his head.':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
