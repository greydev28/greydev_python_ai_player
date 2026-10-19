with open(r"ai_engineer_playbook-main/Part 05 — 📁 Files & Python Ecosystem/file/notes.txt","r",encoding="utf-8") as file:
    for line in file:
       print(line.strip())
with open(r"ai_engineer_playbook-main/Part 05 — 📁 Files & Python Ecosystem/file/journal.txt","a",encoding="utf-8") as file:
    file.write("fred\n")
    file.write("lizzy\n")
    file.write("ben\n")

with open(r"ai_engineer_playbook-main/Part 05 — 📁 Files & Python Ecosystem/file/journal.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())