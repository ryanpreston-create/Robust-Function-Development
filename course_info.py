"""
Course Information System

Stores course data in three dictionaries keyed by course number and lets
the user look up a course's room number, instructor, and meeting time.
"""

# Dictionary 1: Course Number -> Room Number
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

# Dictionary 2: Course Number -> Instructor
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# Dictionary 3: Course Number -> Meeting Time
# (Standard textbook values; replace if your assignment specifies others.)
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m.",
}


def display_course_info(course_number: str) -> None:
    """Print the room, instructor, and meeting time for a course."""
    if course_number in room_numbers:
        print(f"\nCourse:       {course_number}")
        print(f"Room Number:  {room_numbers[course_number]}")
        print(f"Instructor:   {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}\n")
    else:
        print(f"\n'{course_number}' is not a valid course number.")
        print(f"Valid courses: {', '.join(room_numbers)}\n")


def main() -> None:
    print("=== Course Information System ===")
    while True:
        course = input("Enter a course number (or 'Q' to quit): ").strip().upper()
        if course == "Q":
            print("Goodbye!")
            break
        if not course:
            continue
        display_course_info(course)


if __name__ == "__main__":
    main()
