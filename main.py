def find_prob(a, b):

    if a==1:
            prob_a = 0.2
            if b==1:
                    prob_bga = 0.85
            elif b==2:
                    prob_bga = 0.15
            else:
                   
                    print("Invalid Choice")
            prob_a_and_b = prob_a * prob_bga
            print("probability of b given a:", prob_bga)
            print("Probability of both the events accuring", prob_a_and_b)

    elif a==2:
            prob_a = 0.8
            if b==1:
                    prob_bga = 0.2
            elif b==2:
                    prob_bga = 0.98
            else:
                    print("Invalid Choice")
            prob_a_and_b = prob_bga
            print("Probability of b given a:", prob_bga)
            print("Probability of both the events occuring:", prob_a_and_b)

    else:
            print("invalid Choice")

print("Let's calculate probability. Please enter choices for the events...")

print("Person has step throat \n 1.yes \n 2.no ")
a = int(input("Enter your choice"))

print("Person has tested positive \n 1.yes \n 2.no ")
b = int(input("Enter your choice"))

print("Probability for a and b")
find_prob(a, b)