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

print('\n') # new line
# False section

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
