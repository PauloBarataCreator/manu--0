import yaml
import numpy as np


data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

inputs, outputs = [],[]

for command in data['commands']:
   inputs.append(command['input'].lower())
   outputs.append('{}\{}'.format(command['entity'],command['action']))

# print(inputs)
# print(outputs)

print(command)

# print(data)




#Processar textos por meio de: palavras, caracteres, bytes, sub-palavras

chars = set()

for input in inputs + outputs:
  for ch in input:
    if ch not in chars:
      chars.add(ch)

print("Número de caracteres:", len(chars))


#Criar dataset