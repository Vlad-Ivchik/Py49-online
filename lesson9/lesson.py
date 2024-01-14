import os

if not os.path.exists("data"):
    os.mkdir("data")

with open("data/info.csv", "w") as file:
    # file.write("Name|City|Age|Ivan|Minsk|45")
    text = ""
    for i in range(10):
        text += "Name|City|Age|Ivan|Minsk|45\n"
    file.write(text)
