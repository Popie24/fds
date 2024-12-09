def calculate_average(marks): 
    """Returns the average score of the class.""" 
    if len(marks) == 0: 
        return 0 
    return sum(marks) / len(marks) 

def find_highest_and_lowest(marks): 
    """Returns the highest and lowest score in the class.""" 
    if len(marks) == 0: 
        return None, None 
    highest = max(marks) 
    lowest = min(marks) 
    return highest, lowest 

def count_absent_students(attendance): 
    """Returns the count of students who were absent for the test.""" 
    return attendance.count('A') 

def mark_with_highest_frequency(marks): 
    """Returns the mark with the highest frequency.""" 
    if len(marks) == 0: 
        return None 
    frequency = {} 
    for mark in marks: 
        if mark in frequency: 
            frequency[mark] += 1 
        else: 
            frequency[mark] = 1 
    highest_freq_mark = max(frequency, key=frequency.get) 
    return highest_freq_mark 

# Sample data 
marks = [85, 90, 75, 90, 80, 75, 85, 90, 100, 75] 
attendance = ['P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P', 'P']  # 'P' for present, 'A' for absent 

# Function calls 
average_score = calculate_average(marks) 
highest_score, lowest_score = find_highest_and_lowest(marks) 
absent_count = count_absent_students(attendance) 
highest_freq_mark = mark_with_highest_frequency(marks) 

# Output results 
print("Average score of the class:", average_score) 
print("Highest score in the class:", highest_score) 
print("Lowest score in the class:", lowest_score) 
print("Count of students who were absent for the test:", absent_count) 
print("Mark with highest frequency:", highest_freq_mark)
