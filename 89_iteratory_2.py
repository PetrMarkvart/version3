
class NaVelkeZnaky:
    def __init__(self, n):
        self.u_jakeho_jsme_jmena = 0
        self.jmena = ["alice", "bety", "cecilie", "dan", "evzen"]
        self.kolik_mame_jmen = 5

    def __iter__(self):
        return self

    def __next__(self):





for velke in NaVelkeZnaky(["alice", "bety", "cecilie", "dan", "evzen"]):
    print(velke) #Alice, Bety, Cecilie,...

jmena = ["alice", "bety", "cecilie", "dan", "evzen"]
print(jmena[0][0])