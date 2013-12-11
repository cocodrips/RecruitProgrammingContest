
class E:
  win_prob = 5 / 12.0
  lose_prob = 7 / 12.0
  expects = 0

  def solve(self, a, e):
    dp = [[1 for _ in xrange(e + 1)] for __ in xrange(a + 1)]
    for ai in xrange(0, a):
      for ei in xrange(0, e):
        dp[ai + 1][ei] = dp[ai][ei] * self.lose_prob
        dp[ai][ei + 1] = dp[ai][ei] * self.win_prob

    expects = 0
    for ai in xrange(a):
      expects += dp[ai][e] * (a - ai)

    return str(expects)

def main():
  with open('inputE.txt', 'r') as infile, open('outputE.txt', 'w') as outfile:
    data = []
    for line in infile:
      data.append(line.split())

    num = data.pop(0)
    num = int(num[0])

    for _ in xrange(num):
      [a, n] = map(int, data.pop(0))
      enemy_num = 0
      for _ in xrange(n):
        enemy_num += map(int, data.pop(0))[0]
      outfile.write(E().solve(a, enemy_num) + '\n')

if __name__ == "__main__":
  main()
