'''
This program calculates grade weight average of homework, labs, midterm exam, and the final exam.
'''


def main():
    print("Hello,Welcome")

    print("Please enter your grades out of 100 for each category.")

    homework = eval(input("Homework: "))
    labs = eval(input("Labs: "))
    midterm = eval(input("Midterm: "))
    final = eval(input("Final: "))
    average = homework * 0.25 + labs * 0.20 + midterm * 0.25 + final * 0.30

    print("Your grade weight average is",average, "out of 100.")
    

main()
    
