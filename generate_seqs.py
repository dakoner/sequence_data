from random import choices
import pickle

bases = ["A", "C", "G", "T"]
n = 10000000
k = 4

x = choices(bases, k=n * k)
chunk_size = k
sequences = [
    "".join(x[i : i + chunk_size]) for i in range(0, len(x), chunk_size)
]

pickle.dump(sequences, open("seqs.pkl", "wb"))

