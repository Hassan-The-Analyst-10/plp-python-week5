word = input("Enter a word: ")

print("\nLetters:")

for letter in word:
    print(letter)

print("\nNumbered letters:")

counter = 1

for letter in word:
    print(f"{counter}. {letter}")
    counter = counter + 1

print(f"\nThe word has {len(word)} letters.")
