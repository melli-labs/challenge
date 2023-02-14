import sys

def interpret(program):
  program = [line.strip().split() for line in program]
  machine = dict()
  pc = 0
  text_segment = range(0, len(program))
  stdout = ''

  def unwrap(token):
    try:
      return int(token)
    except:
      return int(machine[token])

  while pc in text_segment:
    tokens = program[pc]
    try:
      match tokens[0]:
        case 'add':
          x, y = tokens[1], unwrap(tokens[2])
          machine[x] += y
          pc += 1
        case 'mov':
          x, y = tokens[1], unwrap(tokens[2])
          machine[x] = y
          pc += 1
        case 'print':
          x = tokens[1]
          stdout += chr(machine[x])
          pc += 1
        case 'jnz':
          x, y = unwrap(tokens[1]), unwrap(tokens[2])
          pc += y if x != 0 else 1
    except:
      print(f'Invalid instruction \'{tokens}\'')
      return
  return stdout

def read_program(filename):
  with open(filename) as program:
    return program.readlines()

def run_tests():
  test1 = [
    'mov a 9999',
    'mov b -10',
    'add a b',
    'print a',
    'mov a 10',
    'print a',
  ]

  test2 = [
    'jnz 0 8',
    'mov a 9992',
    'mov b 3',
    'mov c -1',
    'add a c',
    'add b c',
    'jnz b -2',
    'jnz 1 2',
    'mov a 10060',
    'print a',
    'mov a 10',
    'print a',
  ]

  test3 = [
    'mov one 1',
    'mov minus -1',
    'mov a 13',
    'mov b 0',
    'jnz 1 2',
    'add b one',
    'add a minus',
    'jnz a -2',
    'mov c 97',
    'add c b',
    'print c',
  ]

  test_cases = (
    (test1, '✅\n'),
    (test2, '✅\n'),
    (test3, 'm'),
  )

  for program, expected in test_cases:
    result = interpret(program)
    if result != expected:
      print(f'[TEST FAILED] {expected = }, but {result = }')

if __name__ == '__main__':
  run_tests()
  part1 = './input-1.asm'
  part2 = './input-2.asm'
  program = part2 if len(sys.argv) > 1 and sys.argv[1] == '2' else part1
  print(interpret(read_program(program)))
