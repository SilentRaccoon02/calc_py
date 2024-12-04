alphabet = list(" абвгдежзийклмнопрстуфхцчшщъыьэюя")
c = 85353448248576281261631154925974519516651484546418928501296587277181671018917156255149930113486797715080647789221020892120576018027859439885257237372783941654407820450983701397538199026


def num_to_text(num):
    string = str(num)

    if len(string) % 2 != 0:
        string = f"0{string}"

    letters = []

    for i in range(0, len(string), 2):
        letter = int(string[i : i + 2])
        letters.append(alphabet[letter])

    return "".join(letters)


with open("key_A.txt") as file:
    E_A = int(file.readline().strip())
    file.readline()  # skip p1
    file.readline()  # skip p2
    M_A = int(file.readline().strip())
    D_A = int(file.readline().strip())

print(f"E_A = {E_A}")
print(f"M_A = {str(M_A)[:2]}...{str(M_A)[-2:]}")
print(f"D_A = {str(D_A)[:2]}...{str(D_A)[-2:]}\n")


with open("key_B.txt", encoding="utf8") as file:
    E_B = int(file.readline().strip())
    M_B = int(file.readline().strip())

print(f"E_B = {E_B}")
print(f"M_B = {str(M_B)[:2]}...{str(M_B)[-2:]}\n")


s = pow(c, D_A, M_A)
x = pow(s, E_B, M_B)

print(f"text = {num_to_text(x)}")
