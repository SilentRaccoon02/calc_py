import sympy
from sympy.core.intfunc import mod_inverse
from sympy.ntheory.generate import randprime

alphabet = list(" абвгдежзийклмнопрстуфхцчшщъыьэюя")


def gen_prime(e, a, b):
    while True:
        p = randprime(a, b)

        if sympy.gcd(e, p) == 1:
            return p


def gen_primes(e, a, b, n):
    while True:
        p1 = gen_prime(e, a, b)
        p2 = gen_prime(e, a, b)
        M = p1 * p2

        if len(str(M)) == n:
            return p1, p2


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


E_A = 65537
# p1_A, p2_A = gen_primes(E_A, 10**91, 10**93, 186)
p1_A = 984920300865875204214321150641705469666955029930352215988533094060429447316915953536010552891
p2_A = 588203927462499963382880606232712623966898235476616277115707143048940511236717902338572924647
# print(f"p1_A = {p1_A}")
# print(f"p2_A = {p2_A}")

# E_B = 65537
# p1_B, p2_B = gen_primes(E_B, 10**91, 10**93, 185)
# p1_B = 47746945406154217675890739140745836873751161769286138366765437951339399008722171731621781759
# p2_B = 797275763860295596383959712637470328542053423896216196086911734693404579335365698646741066537
# print(f"p1_B = {p1_B}")
# print(f"p2_B = {p2_B}")

M_A = p1_A * p2_A
phi_M_A = (p1_A - 1) * (p2_A - 1)
D_A = mod_inverse(E_A, phi_M_A)

print("--- RSA ---")
print(f"M_A = {M_A}")
print(f"D_A = {D_A}\n")

# M_B = p1_B * p2_B
# phi_M_B = (p1_B - 1) * (p2_B - 1)
# D_B = mod_inverse(E_B, phi_M_B)

# print(f"M_B = {M_B}")
# print(f"D_B = {D_B}\n")

print("--- testing ---")
print(f"p1_A isprime {sympy.isprime(p1_A)}")
print(f"p2_A isprime {sympy.isprime(p2_A)}")
print(f"M_A len = {len(str(M_A))} (must be 186)")
print(f"gcd(D_A, phi_M_A) = {sympy.gcd(D_A, phi_M_A)}\n")

# print(f"p1_B isprime {sympy.isprime(p1_B)}")
# print(f"p2_B isprime {sympy.isprime(p2_B)}")
# print(f"M_B len = {len(str(M_B))} (must be 185)")
# print(f"gcd(D_B, phi_M_B) = {sympy.gcd(D_B, phi_M_B)}\n")

text = "что пользы напрасно и вечно желать"
x = text_to_num(text)

# ключи получателя
M_B = 11123124002019062506030100011206111806320031172906030924010815745794759347585743707034598975904130141516993834908682683650731156906426563008706197799949609202996304843670166275359339203
E_B = 25092119

# кодирование A -> B
c = pow(x, E_B, M_B)
s = pow(c, D_A, M_A)

# сообщение получателя
s_line = 2024
a_line = pow(s_line, D_A, M_A)
x_line = pow(a_line, E_B, M_B)

# # декодирование A -> B
# a = pow(s, E_A, M_A)
# x_line = pow(a, D_B, M_B)

# # кодирование B -> A
# s = pow(x, D_B, M_B)
# c = pow(s, E_A, M_A)

# # декодирование B -> A
# s_line = pow(c, D_A, M_A)
# x_line = pow(s_line, E_B, M_B)

print(f"--- encoding ---")
print(f"x = {x}")
print(f"s = {s}\n")

# print(f"--- decoding ---")
# print(f"x_line = {num_to_text(x_line)}")
