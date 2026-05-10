first_name = "Monojit"
last_name = "Saha"

full_name = first_name + " " + last_name

print(f"Full name: {full_name}")
print(f"Full name length: {len(full_name)}")
print(f"Full name in uppercase: {full_name.upper()}")
print(f"Full name in lowercase: {full_name.lower()}")
print(f"Full name in title case: {full_name.title()}")
print(f"Full name in reverse: {full_name[::-1]}")
print(f"Full name in slice: {full_name[0:7]}")
print(f"Every other character from start to index 7: {full_name[:7:2]}")
print(f"From index 8 to the end: {full_name[8:]}")
print(f"Last character: {full_name[-1]}")

label_text = "Héllo, Worlð!"
encoded_text = label_text.encode("utf-8")
print(f"Encoded text: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")