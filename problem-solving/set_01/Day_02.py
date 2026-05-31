"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter a one-liner passion or goal: ").strip()
emoji = input("Enter your favorite emoji (optional): ").strip()
website = input("Enter your website or handle (optional): ").strip()

print("\nChoose a layout style:")
print("1. Classic")
print("2. Modern")
print("3. Minimalist")

layout_choice = input("Enter the number corresponding to your preferred layout: ").strip()

if layout_choice == "1":
    bio = f"{emoji} {name} | {profession}\n💡 {passion}\n🔗 {website}"
elif layout_choice == "2":
    bio = f"{emoji} {name}\n{profession}\n{passion}\n{website}"
else:
    bio = f"{name} - {profession} | {passion} {emoji} {website}"

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")


