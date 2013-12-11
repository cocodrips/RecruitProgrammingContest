def solve(message, hint_messages):
  correct = av(message)

  answer = []
  ans = []
  for h in hint_messages:
    arr = h.split(':')
    answer.append(arr[0])
    ans.append(av(arr[1]))

  for a in xrange(len(ans)):
    ans[a] = abs(correct - ans[a])

  n = ans.index(min(ans))
  return answer[n]


def av(message):
  sum = 0.0
  m_len = 0

  for word in message.split():
    for _ in word:
      sum += 1
    m_len += 1
  return sum / m_len


if __name__ == "__main__":
  with open('inputB.txt', 'r') as infile, open('outputtestB.txt', 'w') as outfile:
    data = []
    for line in infile:
      data.append(line.split())

    num = data.pop(0)
    num = int(num[0])

    for i in xrange(num):
      message = data.pop(0)
      message = ' '.join(message)
      lenn = data.pop(0)
      hint_message = []
      for i in xrange(int(lenn[0])):
        hint = data.pop(0)
        hint = ' '.join(hint)
        hint_message.append(hint)

      outfile.write(solve(message, hint_message) + '\n')
