# Diamond Hernandez
# 03-28-2026
# P4HW1
# Loop score program


print("\033[95m", end="")  

# Get initial input
num_scores = int(input("🌸 How many scores would you like to enter? "))

# Start list
score_list = []

# Get scores
count = 0
while count < num_scores:
    score = int(input(f"Enter score #{count + 1}: "))
    
    # Set invalid scores
    while score < 0 or score > 100:
        score = int(input("Oops! Please enter a score between 0 and 100: "))
    
    # Add to list
    score_list.append(score)
    count += 1

# Display results
print("\n----------Results----------")
lowest_score = min(score_list)
print(f"🌸 Lowest score: {lowest_score}")

# Remove lowest score
score_list.remove(lowest_score)
print(f"🌸 Modified list: {score_list}")

# Get average
average = sum(score_list) / len(score_list)
print(f"🌸 Scores average: {average:.2f}")

# Calculate letter grades
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"🌸 Grade: {grade} ")
print("---------------------------")
