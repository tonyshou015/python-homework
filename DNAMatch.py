DNA1= "AATCGATCTCGAATTCAC"
similar= ""
DNA2= "ATTCGTACTCGGATCCTC"

for i in range(0, len(DNA1)):
    if DNA1[i] == DNA2[i]:
        similar += "|"
    else:
        similar += " "

print(DNA1)
print(similar)
print(DNA2)

similarity=similar.count("|")/len(similar)
print("相似度:{:.2%}".format(similarity))
