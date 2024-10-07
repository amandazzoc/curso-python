count = 1
while count < 10:
  print(count)
  if count == 5:
    break
  count += 1

for i in range(1, 10):
  if i == 5:
    continue
  print(i)