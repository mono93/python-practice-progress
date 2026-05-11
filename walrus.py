value = 13
# remainder = value % 5

if (remainder := value % 5):
    print(f"{value} is not a multiple of 5. Remainder: {remainder}")


available_sizes = ["S", "M", "L", "XL"]
if (size := input("Enter a size (S, M, L, XL): ").upper()) in available_sizes:
    print(f"Size {size} is available.")
else:    
    print(f"Size {size} is not available.")
