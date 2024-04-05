import sys
import re
    
# 1
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"(cat.*){2}", line):
        print(line)

# 2
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\bcat\b", line):
#         print(line)

#3
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"z.{3}z", line):
#         print(line)

#4
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\\", line):
#         print(line)

#5
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"(\w+)\1", line):
#         print(line)

#6    
# pattern = r"human"
# for line in sys.stdin:
#     line = line.rstrip()
#     new_line = re.sub(pattern, r"computer", line)
#     print(new_line)

#7    
# pattern = r"\ba+\b"
# for line in sys.stdin:
#     line = line.rstrip()
#     new_line = re.sub(pattern, r"argh", line, 1, re.IGNORECASE)
#     print(new_line)

#8    
# pattern = r"\b(\w)(\w)(\w*)"
# for line in sys.stdin:
#     line = line.rstrip()
#     new_line = re.sub(pattern, r"\2\1\3", line)
#     print(new_line)

#9  
# pattern = r"(\w)(\1+)"
# for line in sys.stdin:
#     line = line.rstrip()
#     new_line = re.sub(pattern, r"\1", line)
#     print(new_line)

# 10 - дополнительная      
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.match(r"^0*(1(01*0)*1|0)+$", line):
#         print(line)