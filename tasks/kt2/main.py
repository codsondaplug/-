from random import choice

# | {chr(0x2764)}x{lives}
symbol = chr(9632)
answer = 'да'
quantity_of_lives = 5
hints = []
words = []
count=-1

def game(answer: str) -> bool:
  return answer=='да'

def get_word(used_words: list[str]=[]) -> str:
  with open('words.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    words = []
    for line in lines:
      word = line.strip().split(':')
      words.append(word[0])
    rand_word = choice(words)
    while True:
      if rand_word in used_words:
        rand_word = choice(words)
      else:
        break
  return rand_word

def get_hint(word: str, past_hints: list[str]) -> str:
  with open('words.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
      hints = line.strip().split(':')
      if hints[0]==word:
        hint = hints[1].strip().split(';')
        break
    rand_hint = choice(hint)
    while True:
      if rand_hint in past_hints:
        rand_hint = choice(hint)
      else:
        break
    return rand_hint

def get_table(word: str, symbol: chr) -> str:
  table = ''
  for i in range(len(word)*2-1):
    if i%2==0:
      table += symbol
    else:
      table += ' '
  return table

def get_lives(quantity_of_lives: int) -> int:
  return quantity_of_lives

def get_counter(counter: int) -> int:
  return counter

def alive(lives: int) -> bool:
  return lives>0

def print_question(table: str, lives: int, hint: str, counter_files: int) -> str:
  if lives<5:
    with open(f'{counter_files}_picture.txt', 'r', encoding='utf-8') as p:
      picture = p.read()
      print(picture)
  print(f"{table}")
  print(f"Подсказка: {hint}")
  guess = input('Назовите букву или всё слово целиком: ')

  return guess.upper()

def word_correct(word: str, guess: str) -> bool:
  return word==guess

def print_victory(word: str, table: str) -> str:
  table = ''
  for i in range(len(word)*2-1):
    if i%2==0:
      table += word[i//2]
    else:
      table += ' '
  print(table)
  words.append(word)
  if len(words)<6:
    answer = input('Вы выиграли! Хотите ещё сыграть? (да/нет): ')
    return answer
  else:
    print('Вы выиграли! У нас закончились слова, спасибо за игру')
    return 'no'

def contains(word: str, guess: str) -> bool:
  return guess in word

def open_letter(word: str, guess: str, table: str) -> str:
  table1 = ''
  for i in range(len(word)*2-1):
    if guess==word[i//2] and i%2==0:
      table1 += word[i//2]
    else:
      table1 += table[i]
  return table1

def minus_live(lives: int) -> int:
  return lives-1

def plus_count(count: int) -> int:
  return count+1

def print_wrong(hint: str):
  hints.append(hint)
  print('Неправильно. Вы теряете 1 жизнь!')

def table_word(word: str, table: str) -> bool:
  return table.replace(' ', '')==word

def you_lose(word: str) -> str:
  words.append(word)
  hints=[]
  with open(f'4_picture.txt', 'r', encoding='utf-8') as p:
      picture = p.read()
      print(picture)
  if len(words)<6:
    answer = input('Вы проиграли... Хотите ещё сыграть? (да/нет): ')
    return answer
  else:
    print('Вы проиграли... У нас закончились слова, спасибо за игру')
    return 'no'

while game(answer):
  word = get_word(words)
  hint = get_hint(word, hints)
  table = get_table(word, symbol)
  lives = get_lives(quantity_of_lives)
  counter_files = get_counter(count)

  while alive(lives):
    guess = print_question(table, lives, hint, counter_files)
    if word_correct(word, guess):
      answer = print_victory(word, table)
      break
    elif contains(word, guess):
      table = open_letter(word, guess, table)
    else:
      print_wrong(hint)
      lives = minus_live(lives)
      hint = get_hint(word, hints)
      counter_files = plus_count(counter_files)
    if table_word(word, table):
      answer = print_victory(word, table)
      break

  if not alive(lives):
    answer = you_lose(word)
