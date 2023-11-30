from Rectangle_class import Rectangle, Parallelepipede
import copy
R0 = Rectangle()
R1 = Rectangle(8, 4)
RC = copy.copy(R1)

print(R0.Equals(R1))
print("Permitre est :", R0.Perimetre())
print("Permitre est :", R1.Perimetre())
print("Permitre est :", RC.Perimetre())
print("Surface est :", R0.Surface())
print("Surface est :", RC.Surface())
print("Surface est :", RC.Surface())
print(R0.ToString())
print(R1.ToString())
print(RC.ToString())

P0 = Parallelepipede()
P1 = Parallelepipede(8, 4, 6)
PC = copy.copy(P1)

print(R0.Equals(R1))
print("Volume est :", P0.Volume())
print("Volume est :", P1.Volume())
print("Volume est :", PC.Volume())
print("Surface est :", P0.Surface())
print("Surface est :", P1.Surface())
print("Surface est :", PC.Surface())
print(P0.ToString())
print(P1.ToString())
print(PC.ToString())

