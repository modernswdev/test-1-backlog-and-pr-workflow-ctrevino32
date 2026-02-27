# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Removed security backend and hardcoded secret code for simplicity.

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  b_hp -= 10 # Added damage to boss HP
  print("You deal 10 damage!")

def heal():
  global p_hp
  p_hp += 20
  if p_hp > 50: # Added Max HP cap
    p_hp = 50
  print(f"Healed! HP is now {p_hp}")
   elif p_hp <= 0:   # Added code to ensure no healing after defeat
    print:(f"Already defeated!")
  else:
    print(f"Already healthy!")


# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
   choice = ''   # Resets 'choice' variable
  while choice != 'a' and choice != 'h':    # Added logic to ensure valid input
    choice = input("Action [a]ttack, [h]eal: ").lower()   # Removed cheat logic from input prompt

  
  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()    # Removed cheat code logic
  
  if b_hp > 0:
    p_hp -= 10

 if b_hp <= 0:   # Added victory condition
    print("You won!")
  
  if p_hp <= 0:   # Added loss condition
    print("You were defeated!")


print("Game Over!")