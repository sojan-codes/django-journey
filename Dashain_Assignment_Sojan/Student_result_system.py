data = [{}, {}, {}]

def stu_topper():
    top = data[0]["Percentage"]
    for val in data:
        if val["Percentage"] > top:
            top = val["Percentage"]
    for i in data:
        if i["Percentage"] == top:
            print("-------------------------------------------")
            print(f'Name of the Topper is {i["Name"]}')
            print("-------------------------------------------")
            break
        

def stu_result():
    print("Student Results:")
    for i in data:
        print("-------------------------------------------")
        print(f'Name : {i["Name"]}')
        print(f'Subject 1: {i["Subject 1"]} | Subject 2: {i["Subject 2"]} | Subject 3: {i["Subject 3"]}')
        print(f'Total : {i["Total"]} | Percentage : {i["Percentage"]} | grade : {i["Grade"]}')
        print("-------------------------------------------")

def stu_grade(val, percentage):
    grade = ""
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"
    val["Grade"] = grade


def stu_per(val, total):
    per = (total / 300) * 100
    val["Percentage"] = round(per, 2)
    stu_grade(val, per)


def stu_total():
    for val in data:
        total = val["Subject 1"] + val["Subject 2"] + val["Subject 3"]
        val["Total"] = total
        stu_per(val, total)


for val in data:
    stu_name = input("Enter your Name: ")
    val["Name"] = stu_name.strip().title()
    while True:
        try:
            marks = float(input("Enter the marks of Subject 1: "))
            if marks >= 0 and marks <= 100:
                val["Subject 1"] = marks
                break
            else:
                print("Marks must be in the range between 0 to 100.")
        except:
            print("Invalid Marks.")
    while True:
        try:
            marks = float(input("Enter the marks of Subject 2: "))
            if marks >= 0 and marks <= 100:
                val["Subject 2"] = marks
                break
            else:
                print("Marks must be in the range between 0 to 100.")
        except:
            print("Invalid Marks.")
    while True:
        try:
            marks = float(input("Enter the marks of Subject 3: "))
            if marks >= 0 and marks <= 100:
                val["Subject 3"] = marks
                break
            else:
                print("Marks must be in the range between 0 to 100.")
        except:
            print("Invalid Marks.")

stu_total()
stu_result()
stu_topper()
