def print_line():
    print(25 * '-')


print_line()

somebody_name = "Bob"
print(f"Hello, {somebody_name}, would you like to learn some python today?")

print_line()

strange_title = "Apocalypsis is near"
print(strange_title.lower())
print(strange_title.capitalize())
print(strange_title.upper())

print_line()

famous_quote = ('''Taylor Swift:
               "Do not compare yourself to others.
                If you do so, you are insulting yourself"''')

print(famous_quote)

print_line()

celebrity_name = "Taylor Swift"
famous_quote = (f'''{celebrity_name}:
               "Do not compare yourself to others.
                If you do so, you are insulting yourself"''')
print(famous_quote)

print_line()

famous_person_name = "\tErvin Van Rommel \n "
print(f"Ordinary output: {famous_person_name}")
print(f"left strip output: {famous_person_name.lstrip()}")
print(f"right strip output: {famous_person_name.rstrip()}")
print(f"full strip output: {famous_person_name.strip()}")


