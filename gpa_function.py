print("GPA Calculator")
print("______________")


#function to get Grade Point of Score
def gpaScoreGradePoint (score):
    if score >= 90:
        ans = 4.0
        return ans
    elif score >= 80:
        ans = 3.0
        return ans
    elif score >= 70:
        ans = 2.0
        return ans
    elif score >= 60:
        ans = 1.0
        return ans
    else:
        ans = 0.0
        return ans


#function to assign letter to score
def gpaScoreLetter (letter):
    if letter >= 90:
        ans = "A"
        return ans
    elif letter >= 80:
        ans = "B"
        return ans
    elif letter >= 70:
        ans = "C"
        return ans
    elif letter >= 60:
        ans = "D"
        return ans
    else:
        ans = "F"
        return ans

#Take courses and scores and assign GPA and score
course_num = int(input("Enter the number of courses you take\n"))
for course in range(course_num):
    course_name = input("Enter course name\n")
    exam_score = float(input("Enter exam score out of 100\n"))
    ans_out = gpaScoreGradePoint(exam_score)
    gpa_letter = gpaScoreLetter(exam_score)
    print ("Course: ", course_name)
    print ("Exam Score:", exam_score)
    print ("GPA", ans_out)
    print ("Grade: ", gpa_letter)
    print("########################## \n")
print("Good Bye Now")