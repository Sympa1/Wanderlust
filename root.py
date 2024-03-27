def fruehling():
    '''Wenn der Frühling ausgewählt wurde, wird diese Funktion gestartet'''
    print()

def sommer():
    '''Wenn der Sommer ausgewählt wurde, wird diese Funktion gestartet'''
    print()

def herbst():
    '''Wenn der Herbst ausgewählt wurde, wird diese Funktion gestartet'''
    print()

def winter():
    '''Wenn der Winter ausgewählt wurde, wird diese Funktion gestartet'''
    print()

input_reisezeit = input("Wähle zwischen Frühling, Sommer, Herbst oder Winter!\nWas ist deine lieblings Reisezeit?: ")
print(f"Deine lieblings Reisezeit ist also der {input_reisezeit}. Eine ausgezeichnete Wahl!")

if input_reisezeit == "Frühling":
    fruehling()
elif input_reisezeit == "Sommer":
    sommer()
elif input_reisezeit == "Herbst":
    herbst()
elif input_reisezeit == "Winter":
    winter()
else:
    print(f"{input_reisezeit} ist keine gültige Eingabe!")