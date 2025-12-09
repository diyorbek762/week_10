raw_scores = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 75),
    ("Alice", "Physics", 90),
    ("Charlie", "History", 88),
    ("Bob", "Physics", 82),
    ("Alice", "History", 92)
]

gradebook={}
for score in raw_scores:
    name, subject, student_score = score
    if not name in gradebook:
        gradebook[name]= {subject: student_score}
    else:
        gradebook[name][subject]= student_score
print(gradebook)
