import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

def attack(attacker, defender):
    damage = random.randint(1, attacker.attack)
    damage -= defender.defense  # Subtract defender's defense from the damage
    damage = max(0, damage)  # Ensure damage is not negative
    defender.health -= damage
    return damage

def heal(character):
    healing_amount = random.randint(10, 20)
    character.health += healing_amount
    return healing_amount

def choose_path():
    paths = ["Forest", "Cave"]
    print("Choose your path:")
    for i, path in enumerate(paths, 1):
        print(f"{i}. {path}")
    
    choice = int(input("Enter the number of your chosen path: "))
    return paths[choice - 1]

def encounter_enemy():
    enemies = {
        "Slime": Character("Slime", 30, 10, 5),
        "Spider": Character("Spider", 40, 15, 8)
    }

    enemy_name, enemy = random.choice(list(enemies.items()))
    print(f"\nYou encounter a {enemy_name}!")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: Health = {player.health}")
        print(f"{enemy_name}: Health = {enemy.health}")

        action = input("Do you want to attack, heal, or defend? (attack/heal/defend): ").lower()

        if action == "attack":
            damage_to_enemy = attack(player, enemy)
            print(f"You attacked {enemy_name} and dealt {damage_to_enemy} damage.")
            if not enemy.is_alive():
                print(f"You defeated the {enemy_name}!")
                break

            damage_to_player = attack(enemy, player)
            print(f"{enemy_name} counterattacked and dealt {damage_to_player} damage.")
            if not player.is_alive():
                print("You have been defeated!")
                break
        elif action == "heal":
            healing_amount = heal(player)
            print(f"You healed yourself and gained {healing_amount} health.")
            damage_to_player = attack(enemy, player)  # Enemy still attacks after healing
            print(f"{enemy_name} attacked you and dealt {damage_to_player} damage.")
            if not player.is_alive():
                print("You have been defeated!")
                break
        elif action == "defend":
            player.defense += 3  # Increase player's defense for the next turn
            print("You chose to defend. Your defense is increased for the next turn.")
            damage_to_player = attack(enemy, player)
            print(f"{enemy_name} attacked you, but your defense reduced the damage to {damage_to_player}.")
            if not player.is_alive():
                print("You have been defeated!")
                break
        else:
            print("Invalid choice. Please enter 'attack', 'heal', or 'defend'.")

if __name__ == "__main__":
    print("Welcome to the RPG Game!")

    player = Character("Player", 100, 20, 5)

    while player.is_alive():
        chosen_path = choose_path()

        if chosen_path == "Forest":
            print("You enter the forest.")
            encounter_enemy()
        elif chosen_path == "Cave":
            print("You enter the cave.")
            encounter_enemy()
        else:
            print("Invalid path.")

    print("Game Over.")
