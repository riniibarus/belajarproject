print (" xxxx Program Logiika / Boolean xxxx ")
nilai_A = True
nilai_B = False
nilai_C = True
nilai_D = False
print  ("A : ",nilai_A)
print  ("B : ",nilai_B)
print  ("C : ",nilai_C)
print  ("D : ",nilai_D)
print (" xxxx Hasil Pengetesan xxxx ")
#operator not
hasil = not nilai_A
print  ("Not A (True) : ",hasil)
hasil = not nilai_B
print  ("Not B (False) : ",hasil)

print (" xxxx Operator OR xxxx ")
hasil = nilai_A or nilai_B
print ("A (True) or B (False) = ",hasil)
hasil = nilai_A or nilai_C
print ("A (True) or C (True) = ",hasil)
hasil = nilai_B or nilai_D
print ("B (False) or D (False) = ",hasil)

print (" xxxx Operator AND xxxx ")
hasil = nilai_A and nilai_B
print ("A (True) and B (False) = ",hasil)
hasil = nilai_A and nilai_C
print ("A (True) and C (True) = ",hasil)
hasil = nilai_B and nilai_D
print ("B (False) and D (False) = ",hasil)

print (" xxxx Operator XOR xxxx ")
hasil = nilai_A ^ nilai_B
print ("A (True) xor B (False) = ",hasil)
hasil = nilai_A ^ nilai_C
print ("A (True) xor C (True) = ",hasil)
hasil = nilai_B ^ nilai_D
print ("B (False) xor D (False) = ",hasil)
print (" xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ")
