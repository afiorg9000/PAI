import os
import time
import datetime


def start_focus_mate_session():
    # Prompt for the duration of the focus mate session
    session_duration = int(input("Enter the duration of the focus mate session in minutes: "))

    # Prompt for the task during the session
    task_description = input("What will you be doing during this focus mate session? ")

    # Calculate the end time for the session
    end_time = time.time() + (session_duration * 60)

    # Start the timer
    print("Focus mate session started. Timer set for", session_duration, "minutes.")
    time.sleep(session_duration * 60)

    # Prompt for the final progress update
    final_update = input("Congratulations! Your focus mate session is complete. What progress did you make overall? ")
    print("Final progress update:", final_update)

    # Check integrity and save session information to a data file
    check_integrity(session_duration, task_description, final_update)

    # Ask if the user wants to do another session
    another_session = input("Do you want to do another focus mate session? (yes/no): ")
    if another_session.lower() == "yes":
        start_focus_mate_session()


def save_session_info(duration, task, progress, integrity):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Create a formatted string to save session information
    session_info = f"Session Date: {current_datetime}\nDuration: {duration} minutes\nTask: {task}\nProgress: {progress}\nIntegrity: {integrity}\n"

    # Save session information to a file
    with open("focus_mate_sessions.txt", "a") as file:
        file.write(session_info)
        file.write("\n")


def check_integrity(duration, task, progress):
    # Ask if the user's intention/commitment aligns with the actual session
    intention = input("Did your intention/commitment align with the actual session? (yes/no): ")

    if intention.lower() == "no":
        # If there's a breakdown, prompt for a path forward
        path_forward = input("There was a breakdown. Please input a path forward: ")
        print("Path forward:", path_forward)
        integrity = 0
    else:
        # If the user did what they said, increment the integrity score by 1
        integrity = 1
        increment_integrity_score()

    # Save session information including integrity to a data file
    save_session_info(duration, task, progress, integrity)


def increment_integrity_score():
    # Load the integrity score from a file or initialize it to 0 if the file doesn't exist
    if os.path.exists("integrity_score.txt"):
        with open("integrity_score.txt", "r") as file:
            integrity_score = int(file.read())
    else:
        integrity_score = 0

    # Increment the integrity score by 1
    integrity_score += 1

    # Save the updated integrity score to the file
    with open("integrity_score.txt", "w") as file:
        file.write(str(integrity_score))

