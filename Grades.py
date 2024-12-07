def calculate_grade(assignments, projects, achievements, final_exam):
    """Calculate the final grade based on course weights."""
    # Weights for each component
    WEIGHTS = {
        'assignments': 0.20,
        'projects': 0.70,
        'achievements': 0.05,
        'final_exam': 0.05
    }

    # Calculate weighted scores
    weighted_score = (
        assignments * WEIGHTS['assignments'] +
        projects * WEIGHTS['projects'] +
        achievements * WEIGHTS['achievements'] +
        final_exam * WEIGHTS['final_exam']
    )
    return weighted_score

def determine_letter_grade(score):
    """Determine the letter grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    print("Enter the learner's scores out of 100:")
    assignments = float(input("Assignments: "))
    projects = float(input("Projects: "))
    achievements = float(input("Achievements: "))
    final_exam = float(input("Final Exam: "))

    final_score = calculate_grade(assignments, projects, achievements, final_exam)
    letter_grade = determine_letter_grade(final_score)

    print(f"Final Score: {final_score:.2f}%")
    print(f"Final Grade: {letter_grade}")

