

def solve(data):
  sum_data = [0 for _ in range(10)]
  sum = 0
  for i in xrange(10):
    for d in data:
      if d[0] == str(i):
        sum += int(d)
    sum_data[i] = sum
    sum = 0
  print sum_data
  return str(max(sum_data))

if __name__ == "__main__":
  with open('inputA.txt', 'r') as infile, open('outputA.txt', 'w') as outfile:
    data = []
    for line in infile:
      data.append(line.split())

    num = data.pop(0)

    i = 0
    while i < int(num[0]):
      data.pop(0)
      problem = data.pop(0)
      outfile.write(solve(problem) + '\n')
      i += 1


