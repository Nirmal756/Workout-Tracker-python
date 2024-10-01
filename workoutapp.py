import streamlit as st
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

# Initialize session state variables to track user progress
if 'workout_data' not in st.session_state:
    st.session_state['workout_data'] = None
if 'started_workout' not in st.session_state:
    st.session_state['started_workout'] = False

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
    st.session_state['workout_data'] = workout_data
    st.write("\n****** Your Workout Plan ******")
    st.write(f"**Workout Type:** {get_workout_name(category)}")
    st.write(f"**Sets:** {workout_data['sets']}")
    st.write(f"**Reps per Set:** {workout_data['reps_per_set']}")
    st.write(f"**Rest between sets:** {workout_data['rest_between_sets']} seconds")
    st.write(f"**Rep time:** {workout_data['rep_time']} seconds")
    st.write(f"**Rest between workouts:** {workout_data['rest_between_workouts']} seconds")
    total_time = ((workout_data['rep_time'] * workout_data['reps_per_set'] + workout_data['rest_between_sets']) * \
                  workout_data['sets']) / 60
    st.write(f"**Total time for workout:** {total_time:.2f} minutes")
    return workout_data
def start_workout():
    workout_data = st.session_state['workout_data']

    st.write("\nStarting workout in 5 seconds, get ready!")
    time.sleep(5)

    for set_num in range(1, workout_data['sets'] + 1):
        st.write(f"\n**Set {set_num} of {workout_data['sets']}:**")

        for rep_num in range(1, workout_data['reps_per_set'] + 1):
            st.write(f"Repetition {rep_num} of {workout_data['reps_per_set']}, start!")
            time.sleep(workout_data['rep_time'])

        if set_num != workout_data['sets']:
            st.write(f"Rest between sets ({workout_data['rest_between_sets']} seconds)")
            time.sleep(workout_data['rest_between_sets'])

    st.write("\nCongratulations, you have completed your workout!")
    st.session_state['started_workout'] = False

def workout_tracker():
    st.title("Workout Trainer")

    if not st.session_state['started_workout']:
        # Show workout plan generation only if workout hasn't started
        name = st.text_input("Enter your name:")
        age = st.text_input("Enter your age:")

        category = st.selectbox("Choose a workout category:", list(workouts.keys()), format_func=get_workout_name)

        level = st.selectbox("Choose workout level:", [1, 2, 3],
                             format_func=lambda x: ["Beginner", "Intermediate", "Advanced"][x - 1])

        if st.button("Generate Workout Plan"):
            generate_workout_plan(category, level)

        # If a workout plan is generated, show the option to start the workout
        if st.session_state['workout_data'] is not None:
            # Display "Do you wish to start the workout?" and Yes/No buttons
            st.write("Do you wish to start the workout?")
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Yes"):
                    st.session_state['started_workout'] = True
                    st.experimental_rerun()  # Re-run the script to clear the interface

            with col2:
                if st.button("No"):
                    st.session_state['workout_data'] = None

    # Once the workout is started, only show the workout in progress, not the inputs
    else:
        start_workout()

if __name__ == "__main__":
    workout_tracker()

