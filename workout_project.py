import time

# Workout Data
workouts = {
    1: {  # STRENGTH WORKOUT
        1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "rep_time": 40,
            "rest_between_sets": 60, "rest_between_workouts": 120},
        2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "rep_time": 45,
            "rest_between_sets": 90, "rest_between_workouts": 150},
        3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "rep_time": 50,
            "rest_between_sets": 120, "rest_between_workouts": 180}
    },
    2: {  # CARDIO WORKOUT
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 30, "rep_time": 60,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 20, "rep_time": 75,
            "rest_between_sets": 120, "rest_between_workouts": 150},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 15, "rep_time": 90,
            "rest_between_sets": 150, "rest_between_workouts": 180}
    },
    3: {  # FLEXIBILITY WORKOUT
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 10, "rep_time": 30,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 8, "rep_time": 40,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 6, "rep_time": 50,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    },
    4: {  # MOBILITY WORKOUT
        1: {"workout_count": 4, "sets": 3, "reps_per_set": 10, "rep_time": 30,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 5, "sets": 4, "reps_per_set": 8, "rep_time": 40,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 6, "sets": 5, "reps_per_set": 6, "rep_time": 50,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    },
    5: {  # BODYWEIGHT WORKOUT
        1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "rep_time": 35,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "rep_time": 40,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "rep_time": 50,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    },
    6: {  # YOGA WORKOUT
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "rep_time": 60,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "rep_time": 75,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 5, "rep_time": 90,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    },
    7: {  # POWER LIFTING
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "rep_time": 45,
            "rest_between_sets": 120, "rest_between_workouts": 180},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "rep_time": 60,
            "rest_between_sets": 150, "rest_between_workouts": 180},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 3, "rep_time": 75,
            "rest_between_sets": 180, "rest_between_workouts": 240}
    },
    8: {  # HIIT
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 15, "rep_time": 45,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 12, "rep_time": 60,
            "rest_between_sets": 120, "rest_between_workouts": 150},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 10, "rep_time": 75,
            "rest_between_sets": 150, "rest_between_workouts": 180}
    },
    9: {  # CORE WORKOUT
        1: {"workout_count": 4, "sets": 3, "reps_per_set": 15, "rep_time": 40,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 5, "sets": 4, "reps_per_set": 12, "rep_time": 45,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 6, "sets": 5, "reps_per_set": 10, "rep_time": 50,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    },
    10: {  # LOW IMPACT WORKOUT
        1: {"workout_count": 3, "sets": 3, "reps_per_set": 12, "rep_time": 30,
            "rest_between_sets": 60, "rest_between_workouts": 90},
        2: {"workout_count": 4, "sets": 4, "reps_per_set": 10, "rep_time": 35,
            "rest_between_sets": 90, "rest_between_workouts": 120},
        3: {"workout_count": 5, "sets": 5, "reps_per_set": 8, "rep_time": 40,
            "rest_between_sets": 120, "rest_between_workouts": 150}
    }
}


def get_user_input():
    print("\n****** Welcome to the Workout Tracker ******\n")
    print("*"*44)
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print("\nAvailable Workout Categories:")
    for key in workouts.keys():
        print(f"{key}: {get_workout_name(key)}")

    category = int(input("Choose a workout category (number): "))
    print("\nChoose a workout level:")
    print("1: Beginner\n2: Intermediate\n3: Advanced")
    level = int(input("Enter workout level (1, 2, or 3): "))

    return name, age, category, level


def get_workout_name(category_id):
    workout_names = {
        1: "Strength Workout",
        2: "Cardio Workout",
        3: "Flexibility Workout",
        4: "Mobility Workout",
        5: "Bodyweight Workout",
        6: "Yoga Workout",
        7: "Power Lifting",
        8: "HIIT",
        9: "Core Workout",
        10: "Low Impact Workout"
    }
    return workout_names.get(category_id, "Unknown Workout")


def generate_workout_plan(category, level):
    workout_data = workouts[category][level]
    print("\n****** Your Workout Plan ******")
    print(f"Workout Type: {get_workout_name(category)}")
    print(f"Sets: {workout_data['sets']}")
    print(f"Reps per Set: {workout_data['reps_per_set']}")
    print(f"Rest between sets: {workout_data['rest_between_sets']} seconds")
    print(f"Rep time: {workout_data['rep_time']} seconds")
    print(f"Rest between workouts: {workout_data['rest_between_workouts']} seconds")
    total_time = ((workout_data['rep_time'] * workout_data['reps_per_set'] + workout_data['rest_between_sets']) * \
                 workout_data['sets'])/60
    print(f"Total time for workout: {total_time} minutes")

    return workout_data


def start_workout(workout_data):
    print("\nStarting workout in 20 seconds, get ready!")
    time.sleep(20)

    for set_num in range(1, workout_data['sets'] + 1):
        print(f"\nSet {set_num} of {workout_data['sets']}:")

        for rep_num in range(1, workout_data['reps_per_set'] + 1):
            print(f"Repetition {rep_num} of {workout_data['reps_per_set']}, start!")
            time.sleep(workout_data['rep_time'])
            if rep_num != workout_data['reps_per_set']:
                print(f"Rest between repetitions ({workout_data['rest_between_sets']} seconds)")
                time.sleep(workout_data['rest_between_sets'])

        if set_num != workout_data['sets']:
            print(f"Rest between sets ({workout_data['rest_between_workouts']} seconds)")
            time.sleep(workout_data['rest_between_workouts'])

    print("\nCongratulations , you have completed your workout!")


def workout_tracker():
    name, age, category, level = get_user_input()
    workout_data = generate_workout_plan(category, level)

    proceed = input("\nDo you wish to start the workout? (yes/no): ").lower()
    if proceed == 'yes':
        start_workout(workout_data)
    else:
        print("Returning to the main menu...")
        workout_tracker()



if __name__ == "__main__":
    workout_tracker()
