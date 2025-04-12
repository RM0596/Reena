class A:
     varA = "Welcome Class A"

class B:
     varB="Welcome Class B"

class C(A,B):
     varC="Welcome Class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)