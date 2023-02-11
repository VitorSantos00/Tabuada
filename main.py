cont = mult = 0
while True:
  num = int(input('Quer ver a tabuada de qual valor? '))
  print('-' * 36)
  if num < 0:
    break
  for c in range(1, 11):
    mult = num * c
    print(f'{num} x {c} = {mult}')
    print('-' * 36)
print('Fim')