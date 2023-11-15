from vanguard.aleo.common import aleo2json

json_obj = aleo2json("C:/Users/Batuh/OneDrive/Masaüstü/leo2/workshop2/hello/build/main.aleo")

print(f"{json_obj}")

insts = json_obj["functions"]["main"]["instructions"]
for inst in insts:
    tokens = inst["str"].strip(";").split()
    match tokens:
        case ["div", r0, r1, "into", r3]:
            result = True
        case _:
            pass
print(f"{result}")