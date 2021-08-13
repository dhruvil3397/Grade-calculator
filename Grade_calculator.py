# Program to create grade calculator in Python
Dhruvil = {"name" : "Dhruvil Soni","assignment" : [80,50,40,20],"test" :[75,75],"lab":[78.20,77.20]}
Raj = {"name":"Raj Patel","assignment":[82,56,44,30],"test":[80,80],"lab":[67.90,78.72]}

# calculate average scores
def aveg_scores(marks):
    total_sum=sum(marks)
    total_sum=float(total_sum)
    avg = total_sum/len(marks)
    return avg
# function calculate the total average
def total_avg(students):
    assignment = aveg_scores(students["assignment"])
    test = aveg_scores(students["test"])
    lab = aveg_scores(students["lab"])
    return (0.1*assignment + 0.7*test + 0.2*lab)

# calculate the grades
def grade(score):
    if score >= 90 :return "A"
    if score >=80 : return "B"
    if score >=70 : return "C"
    if score >= 60 :return "D"
    else :
        return "E"

# calculate the total average marks of the whole class
students = [Dhruvil,Raj]
def class_avg(student_list):
    result_list = []
    for student in student_list:
        stud_avg =total_avg(student)
        result_list.append(stud_avg)
        return aveg_scores(result_list)

for i in students:
    print(i["name"])
    print("=+=+=+=+=+=+=+==+=+=++==+")
    print("Average marks of",i["name"],"is :",total_avg(i))
    print("Letter grade of ",i["name"],"is :",grade(total_avg(i)))

# calculate the average of whole class
class_av =class_avg(students)
print("class average is :",class_av)
print("Letter Grade of the class is :",grade(class_av))
