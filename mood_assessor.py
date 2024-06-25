import datetime
import os


def get_mood():
    while True:
        mood = input("Please enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood == 'happy':
            return 2
        elif mood == 'relaxed':
            return 1
        elif mood == 'apathetic':
            return 0
        elif mood == 'sad':
            return -1
        elif mood == 'angry':
            return -2
        print("Invalid mood entered. Please try again.")


def store_mood(mood_value):
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, 'mood_diary.txt')
    with open(file_path, 'a') as file:
        today = datetime.date.today().isoformat()
        file.write(f"{today},{mood_value}\n")


def has_entered_today():
    file_path = os.path.join('data', 'mood_diary.txt')
    if not os.path.exists(file_path):
        return False
    today = datetime.date.today().isoformat()
    with open(file_path, 'r') as file:
        for line in reversed(file.readlines()):
            if line.startswith(today):
                return True
    return False


def get_last_seven_entries():
    file_path = os.path.join('data', 'mood_diary.txt')
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        entries = [int(line.strip().split(',')[1]) for line in file.readlines()][-7:]
    return entries if len(entries) == 7 else []


def diagnose_mood(entries):
    counts = [0, 0, 0, 0, 0]  # [happy, relaxed, apathetic, sad, angry]
    for entry in entries:
        if entry == 2:
            counts[0] += 1
        elif entry == 1:
            counts[1] += 1
        elif entry == 0:
            counts[2] += 1
        elif entry == -1:
            counts[3] += 1
        elif entry == -2:
            counts[4] += 1

    average = sum(entries) // len(entries)
    diagnosis = "average"
    if average == 2:
        diagnosis = 'happy'
    elif average == 1:
        diagnosis = 'relaxed'
    elif average == 0:
        diagnosis = 'apathetic'
    elif average == -1:
        diagnosis = 'sad'
    elif average == -2:
        diagnosis = 'angry'

    if counts[0] >= 5:
        diagnosis = 'manic'
    elif counts[3] >= 4:
        diagnosis = 'depressive'
    elif counts[2] >= 6:
        diagnosis = 'schizoid'

    return f"Your diagnosis: {diagnosis}!"


def assess_mood():
    if has_entered_today():
        print("Sorry, you have already entered your mood today.")
        return
    mood_value = get_mood()
    store_mood(mood_value)
    entries = get_last_seven_entries()
    if entries:
        diagnosis = diagnose_mood(entries)
        print(diagnosis)


