# program se zepta na prijmeni a podle jeho tvaru odhadne, zda je to zena ci muz

prijmeni = input("Zadej sve prijmeni: ")
if prijmeni[-3:] == "ová" or prijmeni[-1:] == "á":
    print("Pravdepodobne jsi zena")
else:
    print("Pravdepodobne jsi muz")