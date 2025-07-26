#Ask users for their name and title
name = input("What's your name? ")
title = input("What's your title? ")

#remove whitespaces from str and capitalize user's name and title
name = name.strip().title()
title = title.strip().title()

#Say hello to user
print(f"hello, {name} {title}")