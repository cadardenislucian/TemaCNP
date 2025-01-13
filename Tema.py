import random

BUCKETS = 997
NUM_PERS = 1000000

# 60 names in each collection
nume_f = ["Adelina", "Adina", "Ana", "Andra", "Aurora", "Bianca", "Camelia", "Carina", "Crina", "Carmen", "Cristina", "Claudia", "Daria", "Diana", "Daniela", "Elena", "Eliza", "Ema", "Emilia", "Gabriela", "Georgiana", "Gina", "Ioana", "Iulia", "Izabela", "Iris", "Laura", "Lavinia", "Larisa", "Lidia", "Luiza", "Madalina", "Mara", "Maria", "Melania", "Mihaela", "Mirela", "Monica", "Mariana", "Marina", "Nadia", "Nicoleta", "Nina", "Oana", "Otilia", "Olivia", "Paula", "Raluca", "Ramona", "Rodica", "Roxana", "Ruxandra", "Sabina", "Silvia", "Stefania", "Teodora", "Valentina", "Violeta", "Tamara", "Zoe"]
nume_m = ["Adelin", "Anton", "Alexandru", "Andrei", "Bogdan", "Adrian", "Catalin", "Cristian", "Cosmin", "Costin", "Daniel", "Claudiu", "David", "Dragos", "Eduard", "Emilian", "Emanuel", "Florin", "Felix", "Gabriel", "George", "Iulian", "Ivan", "Laurentiu", "Liviu", "Lucian", "Madalin", "Marius", "Octavian", "Ovidiu", "Paul", "Pavel", "Raul", "Robert", "Dorin", "Sabin", "Sebastian", "Stefan", "Sorin", "Teodor", "Valentin", "Victor", "Vlad", "Cezar", "Doru", "Flaviu", "Eugen", "Grigore", "Horatiu", "Horia", "Iacob", "Iustin", "Leonard", "Marcel", "Nelu", "Rares", "Serban", "Sergiu", "Tudor"]
nume_fam = ["Abaza", "Adamescu", "Adoc", "Albu", "Baciu", "Badea", "Barbu", "Candea", "Caragiu", "Cernea", "Chitu", "Conea", "Danciu", "Deac", "Diaconu", "Doinas", "Enache", "Ene", "Erbiceanu", "Filimon", "Florea", "Frosin", "Fulga", "Ganea", "Georgescu", "Ghinea", "Goga", "Hasdeu", "Herlea", "Hoban", "Iacobescu", "Ionescu", "Irimia", "Josan", "Kiazim", "Lambru", "Lascu", "Lipa", "Lucan", "Lungu", "Lupu", "Manea", "Manolescu", "Marinescu", "Mugur", "Neagu", "Nechita", "Negrescu", "Nita", "Oancea", "Olaru", "Onciu", "Pascu", "Parvu", "Radulescu", "Nelu", "Rares", "Stan", "Tamas", "Tudoran"]

class DatePersonale:
    def __init__(self, cnp, nume):
        self.cnp = cnp
        self.nume = nume

class HashTable:
    def __init__(self):
        self.size = BUCKETS
        self.table = [[] for _ in range(self.size)]

    def insert_item(self, date):
        index = self.hash_function(date.cnp)
        self.table[index].append(date)

    def hash_function(self, cnp):
        return int(cnp) % self.size

    def search(self, date):
        index = self.hash_function(date.cnp)
        for i, entry in enumerate(self.table[index]):
            if entry.cnp == date.cnp:
                return i + 1
        return -1

def generare_cnp():
    s = random.randint(1, 8)
    aa = random.randint(0, 99)
    ll = random.randint(1, 12)
    zz = random.randint(1, 31)
    jj = random.randint(1, 48)
    nnn = random.randint(1, 999)
    c = random.randint(0, 9)

    return f"{s:01}{aa:02}{ll:02}{zz:02}{jj:02}{nnn:03}{c:01}"

def generare_nume(cnp):
    sex = int(cnp[0])
    if sex in [1, 3, 5, 7]:  # Male
        prenume = random.choice(nume_m) + " " + random.choice(nume_m)
    else:  # Female
        prenume = random.choice(nume_f) + " " + random.choice(nume_f)
    return prenume + " " + random.choice(nume_fam)

def creare_persoana():
    cnp = generare_cnp()
    nume = generare_nume(cnp)
    return DatePersonale(cnp, nume)

def main():
    num_pers = NUM_PERS
    rand_size = 1000
    total_iter = 0
    og_iter = 0

    persoane = [creare_persoana() for _ in range(num_pers)]

    htable = HashTable()
    for persoana in persoane:
        htable.insert_item(persoana)

    random_pers = random.sample(range(num_pers), rand_size)
    og_iter = sum(random_pers)

    with open("result.txt", "w") as fout, open("statistici.txt", "w") as fout_stats:
        for ind in random_pers:
            pers = persoane[ind]
            iter = htable.search(pers)
            total_iter += iter
            fout.write(f"{pers.cnp}, {pers.nume}\t - pozitie originala: {ind} / hash table: {iter} iteratii.\n")

        fout_stats.write(f"Pentru cautarea a 1000 de persoane:\n")
        fout_stats.write(f"Total iteratii in tabela hash: {total_iter}\n")
        fout_stats.write(f"Total iteratii in structura originala: {og_iter}\n")
        fout_stats.write(f"Medie iteratii in tabela hash: {total_iter / rand_size}\n")
        fout_stats.write(f"Medie iteratii in structura originala: {og_iter / rand_size}\n")
        y = (100 * (og_iter - total_iter)) / og_iter
        fout_stats.write(f"Rezultat: cu {y:.2f}% mai putine iteratii.\n")

if __name__ == "__main__":
    main()
