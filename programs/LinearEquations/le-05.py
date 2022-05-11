# Collect equation
prompt1 = "Enter equation : "
equation = input(prompt1)

# split equation into LHS and RHS
parts = equation.split( ' ' )

for part in parts:
    part = part.strip()
    if "+" in part:
        if "x" not in part:
            posCon = part
    if "+" in part:
        if "x" in part:
            posVar = part
    if "-" in part:
        if "x" not in part:
            negCon = part
    if "-" in part:        
        if "x" in part:
            negVar = part

print( "Positive Constants :", posCon )
print( "Positive Variables : ", posVar )
print( "Negative Constants :", negCon )
print( "Negative Variables : ", negVar )
