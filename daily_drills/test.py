from time import sleep as sleep

def start_schicht():
    print("--- WILLKOMMEN IM LAGER ---")
    print("Du stehst vor Tor 1. Ein LKW wartet.")
    print("Was machst du?")
    print("A: LKW abladen")
    print("B: Erstmal Kaffee trinken")
    print("C: Gabelstapler fahren mit Schein")
    print("D: Gabelstapler fahren ohne Schein")
    
    
    wahl = input("Tippe A, B, C oder D: ")
    
    
    if wahl.lower() == "a":
        lkw_abladen()
    elif wahl.lower() == "b":
        kaffee_trinken()
    elif wahl.lower() == "c":
        gabelstapler_fahren_mit_schein()
    elif wahl.lower() == "d":
        gabelstapler_fahren_ohne_schein()
    else:
        print("Das habe ich nicht verstanden. Du stolperst über eine Palette.")
        start_schicht() 

def gabelstapler_fahren_mit_schein():
    print("\nDu fährst den Gabelstapler...")
    sleep(2)
    print("Du bringst die Palette zum LKW.")
    sleep(2)
    print("Du hast die Palette sicher zum LKW gebracht.")
    sleep(2)
    print("Jochen ist glücklich und ihr geht in den Keller saufen.")

def gabelstapler_fahren_ohne_schein():
    print("\nDu fährst den Gabelstapler ohne Schein...")
    sleep(2)
    print("Ein Kollege hält dich an und verlangt deinen Schein.")
    sleep(2)
    print("Du fährst den Gabelstapler ohne Schein...")
    sleep(2)
    print("GAME OVER - Die Berufsgenossenschaft ist sauer.")

def lkw_abladen():
    print("\nDu öffnest den LKW...")
    sleep(2)
    print("Oh nein! Die Ladung ist ungesichert!")
    sleep(2)
    print("Alles fällt dir entgegen.")
    sleep(2)
    print("VERLUST - Die Berufsgenossenschaft ist sauer.")

def chef_gespraech():
    print("\nDer Chef spricht mit dir...")
    sleep(2)
    print("Der Chef ist gut drauf.")
    sleep(2)
    print("Der Chef sagt scherzhaft: 'Langsam glaube ich du säufst mehr als du verdienst!'")
    
    

def kaffee_trinken():
    print("\nDer Kaffee schmeckt super.")
    sleep(2)
    print("Du bist wach und motiviert.")
    sleep(2)
    print("Plötzlich ruft der Chef!")
    sleep(2)
    chef_gespraech()
    sleep(2)
    print("GEWINNEN - Du hast den Tag überlebt.")
    

# Spiel starten
start_schicht()