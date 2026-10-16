def save_player(player):
    with open(r"ai_engineer_playbook-main/Part 05 — 📁 Files & Python Ecosystem/file/player.txt","a",encoding="utf-8")as file:
        file.write(f'{player.name},{player.age},{player.position}')