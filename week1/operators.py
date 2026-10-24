live =int(input("please enter the number of lives"))
print(live)

energy = int(input("please enter amount of energy"))
print(energy)

shield = int(input("please enter amount of shield"))
print(shield)

print("health has been set")

# live, energy and shield as emojis
print("Lives: " + "❤️" * live)
print("Energy: " + "⚡️" * energy)
print("Shield: " + "🛡️" * shield)