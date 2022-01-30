sentence = input("Please enter a sentence: ")
my_dict = {}
for i in sentence:
  if i in my_dict.keys():
    my_dict[i] += 1
  else:
    my_dict[i] = 1
print(my_dict)
