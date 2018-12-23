data = "Hello, I am Meng haochemg"
data = data.lower()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
print("There are %d total characters and %d unique caracters in your data." % (data_size, vocab_size))
print(chars)