s1=int(input("s1 girin:"))
s2=int(input("s2 girin:"))
s3=int(input("s3 girin:"))
if s1<s2:
    s1, s2=s2, s1
if s1<s3:
    s1, s3=s3, s1
if s2<s3:
    s2, s3=s3, s2
print(f"{s1}>{s2}>{s3}")
