options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Discontinued", "Option 9", "Option 10", "Out of Stock"]

for option in options:
    if option == "Out of Stock":
        print(f"{option} - Skipping this option.")
        continue
    if option == "Discontinued":
        print(f"{option} - Stopping the loop.")
        break
    print(f"Processing: {option}")