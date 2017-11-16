with open("Binary", 'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
# bin_file.write(range(17))
with open("Binary", 'br') as binFile:
    for b in binFile:
        print(b)
