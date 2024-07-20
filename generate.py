
import random

def main():
    coins_values = ["Cara", "Sello"]
    l = 0;
    while True:
        coin = random.choice(coins_values)
        print(f"Intento {l} salio: {coin}")
        if l > 40:
            break;
        l+=1
    print("Finalizan lanzamientos")


main()