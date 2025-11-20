import random
import webbrowser
import datetime
"""
1 for snake
-1 for water 
0 for gun
"""

computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

# open file to write
with open("game_result.txt", "w") as f:
    print(f"You choose {reverseDict[you]}", file=f)
    print(f"Computer choose {reverseDict[computer]}", file=f)

if(computer == you):
    print("DRAW")
else:
     if(computer == -1 and you == 1):
            print("you win") 

     elif(computer == -1 and you == 0):
          print("You lose")

     elif(computer == 1 and you == -1):
             print("You lose")

     elif(computer == 1 and you == 0):
          print("you win")

     elif(computer == 0 and you == -1):
            print("You win")

     elif(computer == 0 and you == 1):
            print("you lose")

     elif(computer == -1 and you == -1):
            print("DRAW")

     else:
        print("something went wrong")

print("Game result saved in game_result.txt")


# Add new result to HTML
new_entry = f"<li>{datetime.datetime.now().strftime('%H:%M:%S')} - You: {reverseDict[you]}, Computer: {reverseDict[computer]}</li>\n"

html_file = "game_result.html"

# If file doesn't exist, create basic HTML
try:
    with open(html_file, "r") as f:
        content = f.read()
except FileNotFoundError:
    content = """<html>
<head>
<title>Snake Water Gun Game</title>
<meta http-equiv="refresh" content="2">
</head>
<body>
<h2>Game Results</h2>
<ul id="results">
</ul>
</body>
</html>"""

# Insert new result before </ul>
if "<ul id=\"results\">" in content:
    content = content.replace("<ul id=\"results\">", "<ul id=\"results\">\n" + new_entry)
else:
    # fallback if file was empty
    content = content.replace("</body>", f"<ul>{new_entry}</ul>\n</body>")

# Write updated HTML back
with open(html_file, "w") as f:
    f.write(content)

print("Game result added to game_result.html. Open this file in your browser to see results.")
