import hello

def main():
  queue = []

  while True:
    entry = input("Please enter a word, phrase or number you'd like to store in queue: ")
    
    if entry == " " or entry == "quit":
      print(queue)
      print()
      print("Thanks for using this queue")
      break
    else:
      queue.append(entry)
      print(str(len(queue)) + " entries in queue")
      print()
    
if __name__ == '__main__':
  main()
