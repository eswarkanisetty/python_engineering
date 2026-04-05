student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# can use sum for lists
total_score = sum(student_scores)
print (total_score)
totl_score=0

for score in student_scores:
    totl_score += score
print(totl_score)

#using max() with lists
max_score = max(student_scores)
print(max_score)
max_score1 = 0

for score in student_scores:
    if score > max_score1 :
        max_score1 = score
print(max_score1)



