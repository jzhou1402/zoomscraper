# file1 = open('input.csv', 'r')
# out = open("input.txt", "w")

# lines = file1.readlines()  

# prev = ""
# for i in lines:
#     i = i.strip()
#     if i != prev:
#         out.write(i + '\n')
#     prev = i
        
file2 = open('input.txt', 'r')
out2 = open("demo.txt", "w")
out3 = open("excluded.txt", "w")

lines = file2.readlines()

for i in lines:
    if not(" " in i) and not("." in i):
        print(i)
        out2.write(i.lower())
    else:
        out3.write(i)
