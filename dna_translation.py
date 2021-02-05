# import DNA data into the program
inputfile = "dna.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n","") # replace newline character with nothing
seq = seq.replace("\r","") # replace newline character with nothing
