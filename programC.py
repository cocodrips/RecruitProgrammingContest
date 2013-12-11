
def solve(pnum, cards):
  pscore = [0 for _ in xrange(pnum)]
  candi = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  print pscore

  while len(cards) > 0:
    for j in xrange(len(pscore)):
      card = cards.pop(0)
      if card in candi:
        pscore[j] += int(card)
      if card == 'X':
        while len(cards) > 0:
          next_c = cards.pop(0)
          if next_c in candi:
            pscore[j] *= int(next_c)
            break

      if card == 'D':
        while len(cards) > 0:
          next_c = cards.pop(0)
          if next_c in candi:
            pscore[j] /= int(next_c)
            break

      if card == 'S':
        while len(cards) > 0:
          next_c = cards.pop(0)
          if next_c in candi:
            pscore[j] -= int(next_c)
            break

      if len(cards) == 0:
        break

  return str(max(pscore))


if __name__ == "__main__":
  with open('inputC.txt', 'r') as infile, open('outputC.txt', 'w') as outfile:
    data = []
    for line in infile:
      data.append(line.split())

    num = data.pop(0)
    num = int(num[0])
    print num

    for i in xrange(num):
      player_num = data.pop(0)
      player_num = int(player_num[0])
      cards = data.pop(0)
      cards = list(cards[0])
      outfile.write(solve(player_num, cards) + '\n')
