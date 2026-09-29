import streamlit as st

st.title("Student Exam Analyzer")

students = [
    {
        "id": 1,
        "name": "Aden Daqane",
        "course": "Medicine",
        "math": 85,
        "english": 90,
        "science": 88
    },
    {
        "id": 2,
        "name": "Abdirahim Shueb",
        "course": "Computer Science",
        "math": 88,
        "english": 94,
        "science": 80
    },
    {
        "id": 3,
        "name": "Mohamed Ali",
        "course": "Engineering",
        "math": 92,
        "english": 86,
        "science": 90
    }
]

st.subheader("Students")

for student in students:
    total = student["math"] + student["english"] + student["science"]
    average = total / 3

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student["average"] = average
    student["grade"] = grade

st.dataframe(students)

st.subheader("Search Student")

search = st.text_input("Enter student name or ID")

if search:
    found = False

    for student in students:
        if search.lower() in student["name"].lower() or search == str(student["id"]):
            st.write(student)
            found = True

    if found == False:
        st.warning("Student not found")
    st.subheader("Filter Students")

filter_type = st.selectbox(
    "Choose what you want to filter by",
    ["Course", "Grade"]
)

if filter_type == "Course":
    courses = []

    for student in students:
        if student["course"] not in courses:
            courses.append(student["course"])

    selected_course = st.selectbox("Choose a course", courses)

    filtered_students = []

    for student in students:
        if student["course"] == selected_course:
            filtered_students.append(student)

    st.dataframe(filtered_students)

else:
    grades = ["A", "B", "C", "D", "F"]

    selected_grade = st.selectbox("Choose a grade", grades)

    filtered_students = []

    for student in students:
        if student["grade"] == selected_grade:
            filtered_students.append(student)

    st.dataframe(filtered_students)
st.subheader("Top Performers")

sorted_students = sorted(
    students,
    key=lambda student: student["average"],
    reverse=True
)

top_students = sorted_students[:3]

for student in top_students:
    st.write(
        student["name"],
        " , Average:",
        student["average"],
        " , Grade:",
        student["grade"]
    )
    st.subheader("Overall Summary")

total_students = len(students)

total_average = 0

for student in students:
    total_average += student["average"]

overall_average = total_average / total_students

highest_average = students[0]["average"]

for student in students:
    if student["average"] > highest_average:
        highest_average = student["average"]

lowest_average = students[0]["average"]

for student in students:
    if student["average"] < lowest_average:
        lowest_average = student["average"]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", total_students)
col2.metric("Overall Average", round(overall_average, 2))
col3.metric("Highest Average", highest_average)
col4.metric("Lowest Average", lowest_average)