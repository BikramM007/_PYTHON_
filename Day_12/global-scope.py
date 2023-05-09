enemies = 2

def incease_enemies():
    enemies = "Zombies"
    print(f"enemies inside function: {enemies}")

incease_enemies()
print(f"enemies outside function: {enemies}")

#another example
def incease_enemie():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

incease_enemie()
print(f"enemies outside function: {enemies}")
