import datetime

print("===Create a Register===")

# Create Empty Dictionary
register_dict = {}

def add_entry(name):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return name, now

# Get user to fill Dictionary with names whilst also storing the current time they were added
def register():
        while True:
            name = input("Enter a name: ")
            entry_name, entry_time = add_entry(name)
            register_dict[entry_name] = entry_time
            again = input("Would you like to add another name? (y/n): ").lower()
            if again == "n":
                print(f"\n===Register===")
                    # Loop through both key and value at the same time using .items()
                for name, time in sorted(register_dict.items()): # Unpack Dictionary entries into two variables (name/time)
                    print(f"{name} - {time}") # time variable has now been assigned the timestamp
                print(f"\n===End of List===")
                break
            elif again == "y":
                print("Please enter another name")

register() # Call on function to repeat loop