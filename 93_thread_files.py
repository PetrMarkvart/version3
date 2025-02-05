import threading, time

def write_into_file(filename):

    #jak zapsat číslo do cisla.txt ?
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(500000):
            f.write(f"Číslo {i}")

start = time.time()

#nahraďte vlákny.
# varianta 1 - vytvořte 4 vlákna ručně
# varianta 2 - vytvořte 4 vlákna ve for cyklu
vlakno1 = threading.Thread(target=write_into_file("cislo1.txt"), args=(1,))
vlakno2 = threading.Thread(target=write_into_file("cislo2.txt"), args=(2,))
vlakno3 = threading.Thread(target=write_into_file("cislo3.txt"), args=(3,))
vlakno4 = threading.Thread(target=write_into_file("cislo4.txt"), args=(4,))
vlakno1.start()
vlakno2.start()
vlakno3.start()
vlakno4.start()
vlakno1.join() #počkám na dokončení
vlakno2.join()
vlakno3.join() #počkám na dokončení
vlakno4.join()

write_into_file("cislo1.txt")
write_into_file("cislo2.txt")
write_into_file("cislo3.txt")
write_into_file("cislo4.txt")

#porovnejte dobu zápisu
end = time.time()
print(f"Zápis čtyř souborů trval {end-start:.2f} sekund")