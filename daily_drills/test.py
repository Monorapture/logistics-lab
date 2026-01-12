import time

def start_schicht():
    print("--- WILLKOMMEN IM LAGER ---")
    print("Du stehst vor Tor 1. Ein LKW wartet.")
    print("Was machst du?")
    print("A: LKW abladen")
    print("B: Erstmal Kaffee trinken")
    print("C: Gabelstapler fahren mit Schein")
    print("D: Gabelstapler fahren ohne Schein")
    
    # Hier wartet der Computer auf deine Eingabe
    wahl = input("Tippe A, B, C oder D: ")
    
    # Wir machen die Eingabe klein (.lower()), damit "a" und "A" funktionieren
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
        start_schicht() # Startet von vorne (Rekursion - Vorsicht, aber cool!)

def gabelstapler_fahren_mit_schein():
    print("\nDu fährst den Gabelstapler...")
    time.sleep(2)
    print("Du bringst die Palette zum LKW.")
    time.sleep(2)
    print("Du hast die Palette sicher zum LKW gebracht.")
    time.sleep(2)
    print("Jochen ist glücklich und ihr geht in den Keller saufen.")

def gabelstapler_fahren_ohne_schein():
    print("\nDu fährst den Gabelstapler ohne Schein...")
    time.sleep(2)
    print("Ein Kollege hält dich an und verlangt deinen Schein.")
    time.sleep(2)
    print("Du fährst den Gabelstapler ohne Schein...")
    time.sleep(2)
    print("GAME OVER - Die Berufsgenossenschaft ist sauer.")

def lkw_abladen():
    print("\nDu öffnest den LKW...")
    time.sleep(2)
    print("Oh nein! Die Ladung ist ungesichert!")
    time.sleep(2)
    print("Alles fällt dir entgegen.")
    time.sleep(2)
    print("VERLUST - Die Berufsgenossenschaft ist sauer.")

def chef_gespraech():
    print("\nDer Chef spricht mit dir...")
    time.sleep(2)
    print("Der Chef ist gut drauf.")
    time.sleep(2)
    print("Der Chef sagt scherzhaft: 'Langsam glaube ich du säufst mehr als du verdienst!'")
    
    

def kaffee_trinken():
    print("\nDer Kaffee schmeckt super.")
    time.sleep(2)
    print("Du bist wach und motiviert.")
    time.sleep(2)
    print("Plötzlich ruft der Chef!")
    time.sleep(2)
    chef_gespraech()
    time.sleep(2)
    print("GEWINNEN - Du hast den Tag überlebt.")
    

# Spiel starten
start_schicht()