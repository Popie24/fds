def get_students_playing_both(cricket_players, badminton_players): 
    """Returns a list of students who play both cricket and badminton.""" 
    return list(set(cricket_players) & set(badminton_players)) 

def get_students_playing_either(cricket_players, badminton_players): 
    """Returns a list of students who play either cricket or badminton but not both.""" 
    return list(set(cricket_players) ^ set(badminton_players)) 

def count_students_playing_neither(cricket_players, badminton_players, all_students): 
    """Returns the number of students who play neither cricket nor badminton.""" 
    cricket_set = set(cricket_players) 
    badminton_set = set(badminton_players) 
    neither_count = 0 
    for student in all_students: 
        if student not in cricket_set and student not in badminton_set: 
            neither_count += 1 
    return neither_count 

def get_students_playing_cricket_and_football_not_badminton(cricket_players, 
                                                           football_players, 
                                                           badminton_players): 
    """Returns the list of students who play cricket and football but not badminton.""" 
    cricket_set = set(cricket_players) 
    football_set = set(football_players) 
    badminton_set = set(badminton_players) 
    return list(cricket_set & football_set - badminton_set) 

# Sample data 
cricket_players = ['Alice', 'Bob', 'Charlie', 'David'] 
badminton_players = ['Bob', 'Eve', 'Frank'] 
football_players = ['Charlie', 'David', 'George'] 
all_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Hannah'] 

# Function calls 
both_sports = get_students_playing_both(cricket_players, badminton_players) 
either_sport = get_students_playing_either(cricket_players, badminton_players) 
neither_count = count_students_playing_neither(cricket_players, badminton_players, all_students) 
cricket_football_not_badminton = get_students_playing_cricket_and_football_not_badminton(cricket_players, football_players, badminton_players) 

# Output results 
print("Students who play both cricket and badminton:", both_sports) 
print("Students who play either cricket or badminton but not both:", either_sport) 
print("Number of students who play neither cricket nor badminton:", neither_count) 
print("Students who play cricket and football but not badminton:", cricket_football_not_badminton)
