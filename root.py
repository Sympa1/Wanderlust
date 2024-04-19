def fruehling():
    """Wenn der Frühling als String übergeben wird, wird diese Funktion gestartet"""
    while True:
        input_reise_art = input(
            "Würdest du gerne fliegen, mit dem Zug- oder dem Schiff fahren? (Flugzeug/Zug/Schiff)\nAntwort: ")
        if input_reise_art in ["Flugzeug", "Zug", "Schiff"]:
            if input_reise_art == "Flugzeug":
                print(
                    f"Du möchtest als mit dem {input_reise_art} verreisen. Spannend, dann wäre Japan mit den Traumhaften Kirschblüten das perfekte Reiseziel!")
                break
            elif input_reise_art == "Zug":
                print(
                    f"Du möchtest also mit dem {input_reise_art} verreisen. Spannend, dann wäre ein wunderschöner Frühling in den Alpen genau das richtige!")
                break
            elif input_reise_art == "Schiff":
                print(
                    f"Du möchtest als mit dem {input_reise_art} verreisen. Spannend, Dan unternehme doch eine malerische Ober-Rhein-Tour?")
                break
        else:
            print(f"{input_reise_art} ist keine gültige Eingabe!")


def sommer():
    """Wenn der Sommer als String übergeben wird, wird diese Funktion gestartet"""
    while True:
        input_reise_art = input(
            "Würdest du gerne fliegen, mit dem Zug- oder dem Schiff fahren? (Flugzeug/Zug/Schiff)\nAntwort: ")
        if input_reise_art in ["Flugzeug", "Zug", "Schiff"]:
            if input_reise_art == "Flugzeug":
                print(
                    f"Du möchtest als mit dem {input_reise_art} verreisen. Cool, du solltest in Canada eine Rafting "
                    f"Tour machen!. Vielleicht siehst du ja einen Bären?")
                break
            elif input_reise_art == "Zug":
                print(
                    f"Paris kann man super per {input_reise_art} erreichen. Du solltest dich mal in ein kleines Cafe setzen!")
                break
            elif input_reise_art == "Schiff":
                print(
                    f"Da du mit dem {input_reise_art} verreisen möchtest, bietet sich eine entspannte Kreuzfahrt im "
                    f"Mittelmeer an.")
                break
        else:
            print(f"{input_reise_art} ist keine gültige Eingabe!")


def herbst():
    """Wenn der Herbst als String übergeben wird, wird diese Funktion gestartet"""
    while True:
        input_reise_art = input(
            "Würdest du gerne fliegen, mit dem Zug- oder dem Schiff fahren? (Flugzeug/Zug/Schiff)\nAntwort: ")
        if input_reise_art in ["Flugzeug", "Zug", "Schiff"]:
            if input_reise_art == "Flugzeug":
                print(
                    f"Du möchtest als mit dem {input_reise_art} verreisen. Der Indian Summer in Nordamerika soll "
                    f"bezaubernd sein!")
                break
            elif input_reise_art == "Zug":
                print(
                    f"Du möchtest also mit dem {input_reise_art} verreisen. Wie wäre es mit Rumänien? Draculas Burg "
                    f"bei Halloween soll besonders gruselig sein!")
                break
            elif input_reise_art == "Schiff":
                print(
                    f"Eine NCL kreuzfahrt, z.B. von New York nach Halifax, ist genau das richtig wenn du mit dem {input_reise_art} verreisen möchtest!")
                break
        else:
            print(f"{input_reise_art} ist keine gültige Eingabe!")


def winter():
    """Wenn der Winter als String übergeben wird, wird diese Funktion gestartet"""
    while True:
        input_reise_art = input(
            "Würdest du gerne fliegen, mit dem Zug- oder dem Schiff fahren? (Flugzeug/Zug/Schiff)\nAntwort: ")
        if input_reise_art in ["Flugzeug", "Zug", "Schiff"]:
            if input_reise_art == "Flugzeug":
                print(f"Du möchtest als mit dem {input_reise_art} verreise. Madeira ist genau das richtige im Winter!")
                break
            elif input_reise_art == "Zug":
                print(f"Mach doch einen Ski Urlaub in den Alpen, wenn du mit dem {input_reise_art} verreisen möchtest!")
                break
            elif input_reise_art == "Schiff":
                print(
                    f"Wie wäre es mit Polarlichter in Skandinavien? Mit dem {input_reise_art} kannst du von Kiel nach "
                    f"Stockholm fahren!")
                break
        else:
            print(f"{input_reise_art} ist keine gültige Eingabe!")


while True:
    input_reisezeit = input(
        "Möchtest du gerne im Frühling, Sommer, Herbst oder Winter verreisen? ("
        "Frühling/Sommer/Herbst/Winter)\nAntwort: ")
    if input_reisezeit in ["Frühling", "Sommer", "Herbst", "Winter"]:
        if input_reisezeit == "Frühling":
            print(f"Deine lieblings Reisezeit ist also der {input_reisezeit}. Eine ausgezeichnete Wahl!")
            fruehling()
            break
        elif input_reisezeit == "Sommer":
            print(f"Deine lieblings Reisezeit ist also der {input_reisezeit}. Eine ausgezeichnete Wahl!")
            sommer()
            break
        elif input_reisezeit == "Herbst":
            print(f"Deine lieblings Reisezeit ist also der {input_reisezeit}. Eine ausgezeichnete Wahl!")
            herbst()
            break
        elif input_reisezeit == "Winter":
            print(f"Deine lieblings Reisezeit ist also der {input_reisezeit}. Eine ausgezeichnete Wahl!")
            winter()
            break
    else:
        print(f"{input_reisezeit} ist keine gültige Eingabe!")
