import json
import os
from datetime import datetime

HISTORY_FILE = "bill_history.json"
PEOPLE_FILE = "people_spending.json"


def load_data(file_name):
    if not os.path.exists(file_name):
        return {}
    with open(file_name, "r") as f:
        return json.load(f)


def save_data(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


def split_bill(total, people, tip_percent=0):
    tip_amount = total * (tip_percent / 100)
    grand_total = total + tip_amount
    per_person = grand_total / len(people)
    return per_person, tip_amount, grand_total


def save_bill_history(total, per_person, people, tip, grand_total):
    history = load_data(HISTORY_FILE)

    entry = {
        "date": str(datetime.now()),
        "total": total,
        "tip_percent": tip,
        "grand_total": grand_total,
        "per_person": per_person,
        "people": people
    }

    history[str(datetime.now())] = entry
    save_data(HISTORY_FILE, history)


def update_people_spending(people, per_person):
    data = load_data(PEOPLE_FILE)

    for person in people:
        if person not in data:
            data[person] = 0
        data[person] += per_person

    save_data(PEOPLE_FILE, data)


def main():
    print("\n💸 Welcome to the Bill-Splitting App 💸\n")

    total = float(input("Enter total bill amount: $"))
    tip_percent = float(input("Tip percentage (0 if none): "))
    num_people = int(input("How many people? "))

    people = []
    for i in range(num_people):
        name = input(f"Enter name of person {i+1}: ")
        people.append(name)

    per_person, tip_amount, grand_total = split_bill(total, people, tip_percent)

    print("\n------- RESULT -------")
    print(f"Tip added: ${tip_amount:.2f}")
    print(f"Grand total: ${grand_total:.2f}")
    print(f"Each person owes: ${per_person:.2f}")
    print("----------------------\n")

    save_bill_history(total, per_person, people, tip_percent, grand_total)
    update_people_spending(people, per_person)

    print("History saved! ✔")
    print("People's spending updated! ✔")

    print("\n📚 Saved to bill_history.json")
    print("📊 Spending tracked in people_spending.json\n")


if __name__ == "__main__":
    main()
