# True section

section = 'True Section'
print(section.center(30, '='))

my_age = 18     # 1
print(f"Is my age == 18? I predict True.")
print('\t', my_age == 18)

friend = 'Gabo' # 2
print(f"Is friend == 'Gabo'? I predict True.")
print(f'\t', friend == 'Gabo')

game = 'Minecraft'       #3
print(f"Is game == 'Minecraft'? I predict True.")
print('\t', game == 'Minecraft')

book = 'Python Crash Course'    # 4
print(f"Is book == 'Python Crash Course'? I predict True.")
print('\t', book == 'Python Crash Course')

author = 'Lev Tolstoi'      # 5
print(f"Is author == 'Lev Tolstoi'? I predict True.")
print('\t', author == 'Lev Tolstoi')

print(f"Is book == 'Python Crash Course' or friend == 'Miguel'? I predict True.")   # 6
print('\t', book == 'Python Crash Course' or friend == 'Miguel')

print(f"Is 'lev tolstoi'.title() in author? I predict True.")   # 7
print('\t', 'lev tolstoi'.title() in author)

print(f"Is book != 'Minecraft'? I predict True")    # 8
print('\t', book != 'Minecraft')

print(f"Is 21 < my_age? I predict True.")      # 9
print('\t', 21 > my_age)

print(f"Is 18 >= my_age? I predict True.")          # 10
print('\t', 18 >= my_age)

# False section

print('\n') # new line
section = "False section"
print(section.center(30, '='))

anime = 'Evangelion'    # 1
print(f"Is anime == 'Code Geass'? I predict False.")
print('\t', anime == 'Code Geass')

distro = 'Arch Linux'   # 2
print(f"Is distro == 'Linux Mint'? I predict False.")
print('\t', distro == 'Linux Mint')

name = 'Caleb'          # 3
print(f"Is name == 'Gabo'? I predict False.")
print('\t', name == 'Gabo')

book = 'Candide or Optimism'    # 4
print(f"Is book == 'The Death Of Ivan Ilyich'")
print('\t', book == 'The Death Of Ivan Ilyich')

phone = 'Samsung'       # 5
print(f"Is phone == 'iPhone'? I predict False.")
print('\t', phone == 'iPhone')

print(f"Is 'Overlord' in list(anime)? I predict False.")    # 6
print('\t', 'Overlord' in list(anime))

print(f"Is 'Arch Linux == distro.lower()? I predict False") # 7
print('\t', 'Arch Linux' == distro.lower())

print(f"Is 'war and peace'.upper() == 'war and peace'.title()") # 8
print('\t', 'war and peace'.upper() == 'war and peace'.title())

print(f"Is 'Caleb'.lower() in list(name)? I predict False.")      # 9
print('\t', 'Caleb'.lower() in list(name))

print(f"Is distro == 'Arch Linux' and phone == 'Samsung' and name == 'Gabo'? I predict False.") # 10
print('\t', distro == 'Arch Linux' and phone == 'Samsung' and name == 'Gabo')
