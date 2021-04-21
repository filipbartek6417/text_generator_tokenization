# Write your code here
from random import choices
from re import match, split
from nltk.tokenize import regexp_tokenize

file = 'corpus.txt'
tokens = []
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        tokens.extend(regexp_tokenize(line, '[^ \t\n]+'))
length = len(tokens)
c = {}
for index, item in enumerate(tokens):
    if index < length - 2:
        new_item = str(item + " " + tokens[index + 1])
        tokens[index] = [new_item, tokens[index + 2]]
        c.setdefault(new_item, {})
        c[new_item].setdefault(tokens[index + 2], 0)
        c[new_item][tokens[index + 2]] += 1
tokens.pop()
tokens.pop()
current_token = ''
for _ in range(1000):
    while not match('^[A-Z][^.?!]*[^.?!]$', current_token):
        current_token = choices(tokens)[0][0]
    sentence = [current_token]
    length = 2
    while not match('.*[.?!]$', current_token) or length < 5:
        current_token = split(" ", current_token)[1] + " " + max(c[current_token], key=c[current_token].get)
        sentence.append(split(" ", current_token)[1])
        length += 1
    print(" ".join(sentence))
# inp = input()
# while inp != 'exit':
#     try:
#         print('Head:', inp)
#         for i in c[inp].items():
#             print('Tail:', i[0], 'Count:', i[1])
#     except IndexError:
#         print('Index Error. Please input a value that is not greater than the number of all bigrams.')
#     except ValueError:
#         print('Typerror. Please input an integer.')
#     except Exception as e:
#         print(e)
#     finally:
#         inp = input()
