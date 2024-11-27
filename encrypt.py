alphabet = list(" абвгдежзийклмнопрстуфхцчшщъыьэюя")
text = "что пользы напрасно и вечно желать"


def text_to_num(text):
    letters = list(text)
    numbers = []

    for letter in letters:
        index = alphabet.index(letter)

        if index < 10:
            numbers.append(f"0{index}")
        else:
            numbers.append(f"{index}")

    return int("".join(numbers))


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

x = text_to_num(text)

print(f"text = {num_to_text(x)}")

c = pow(x, E_B, M_B)
s = pow(c, D_A, M_A)

with open("encrypt.txt", "w", encoding="utf8") as file:
    file.write(f"E_A = {E_A} ({len(str(E_A))})\n")
    file.write(f"M_A = {M_A} ({len(str(M_A))})\n")
    file.write(f"text = {s} ({len(str(s))})\n")
