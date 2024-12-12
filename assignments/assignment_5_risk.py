import random
import matplotlib.pyplot as plt

# Function to simulate a single battle round
def battle_round():
    # Attacker rolls 3 dice, defender rolls 2 dice
    attacker_rolls = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
    defender_rolls = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)

    # Determine losses based on the rules
    attacker_losses = 0
    defender_losses = 0

    # Compare the highest dice
    if attacker_rolls[0] > defender_rolls[0]:
        defender_losses += 1
    else:
        attacker_losses += 1

    # Compare the second highest dice
    if len(attacker_rolls) > 1 and len(defender_rolls) > 1:
        if attacker_rolls[1] > defender_rolls[1]:
            defender_losses += 1
        else:
            attacker_losses += 1

    return attacker_losses, defender_losses

# Simulate 1000 rounds and track losses
attacker_losses_total = []
defender_losses_total = []

for _ in range(1000):
    attacker_losses, defender_losses = battle_round()
    attacker_losses_total.append(attacker_losses)
    defender_losses_total.append(defender_losses)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(attacker_losses_total, label="Attacker Losses", color='red', alpha=0.7)
plt.plot(defender_losses_total, label="Defender Losses", color='blue', alpha=0.7)
plt.xlabel("Round")
plt.ylabel("Troops Lost")
plt.title("Attacker vs Defender Troop Losses (1000 Rounds)")
plt.legend()
plt.show()
