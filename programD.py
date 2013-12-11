
def solve(vectors):

  for vi in xrange(len(vectors)):
    dob = [[False for _ in xrange(200)] for __ in xrange(200)]
    # umeru
    for vii in xrange(len(vectors)):
      if vi == vii:
        continue

      v = vectors[vii]
      for x in xrange(v[0], v[0] + v[2] + 1):
        for y in xrange(v[1], v[1] + v[3] + 1):
          dob[x][y] = True

    #check
    target = vectors[vi]
    flag = True
    for x in xrange(target[0], target[0] + target[2] + 1):
      for y in xrange(target[1], target[1] + target[3] + 1):
        if dob[x][y] == False:
          flag = False
          break
      if not flag:
        break
    else:
      return "TRUE"

  return "FALSE"


if __name__ == "__main__":
  with open('inputD.txt', 'r') as infile, open('outputD.txt', 'w') as outfile:
    data = []
    for line in infile:
      data.append(line.split())

    num = data.pop(0)
    num = int(num[0])

    for i in xrange(num):
      player_num = data.pop(0)
      player_num = int(player_num[0])
      vectors = []
      for p in xrange(player_num):
        vector = data.pop(0)
        for v in xrange(len(vector)):
          vector[v] = int(vector[v])
        vectors.append(vector)
      outfile.write(solve(vectors) + '\n')
