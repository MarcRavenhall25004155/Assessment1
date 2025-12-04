# Print Menu Message

print("===Create a Register===")

# Create empty list

name_list = []

# Get user to fill list
def register():
        while True:
            name = input("Enter a name: ")

            name_list.append(name)

            again = input("Would you like to add another name? (y/n): ")
            if again == "n":

                ordered_list = sorted(name_list)
                print(f"\n===Register===")
                for i in ordered_list:
                    print(f"\n{i}")
                break
            elif again == "y":
                print("Please enter another name")

register()