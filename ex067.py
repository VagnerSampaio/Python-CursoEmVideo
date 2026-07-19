while True:
    n = int(input("Quer ver a tabuada? "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n:2} x {c:2} = {n * c:2}")