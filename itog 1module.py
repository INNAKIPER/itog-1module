grades=[5,3,3,5,4],[2,2,2,3],[4,5,5,3],[4,4,3],[5,5,5,4,5]
students={'Jonny','Bilbo','Steve','Khendrik','Aaron'}
sorted_students=sorted(students)
print(sorted_students)
grades_dict={}
for student,grade in zip(sorted_students,grades):grades_dict[student]=sum(grade)/len(grade)
print(grades_dict)
