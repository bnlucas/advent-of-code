from typing import Iterator


def load_input() -> Iterator[Iterator[int]]:
  input = open("input.txt").read()
  groups = input.split("\n\n")

  return map(lambda group: map(int, group.split("\n")), groups)


def run():
  calorie_groups = load_input()
  
  elves_calories = list(map(sum, calorie_groups))
  elves_calories.sort()

  print(sum(elves_calories[-3:]))


if __name__ == '__main__':
  run()
