# print('Hello django')
#  -----------------
# if 3 > 2:
#     print('it good')
#  ----------------
# if 5 > 8:
#     print('true')
# else:
#     print('false')

#-----------FUNCTION----
def maya():
    print('My name is rayyan')
maya()

#-----------FUNCTION WITH PARAMETER----
def maya(name):
    if name == 'Rayyan':
        print('Hi Rayyan!')
    elif name == 'Adam':
        print('Hi Adam!')
    else:
        print('Hi anonymous!')
maya("Rayyan")

# ---------------------
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")

# ---------LOOPS--------
girls = ['Naima', 'Asha', 'Shuwekha', 'Maryam', 'Azza']
for name in girls:
    hi(name)
    print('******')
# -------------------
for i in range(1, 6):
    print(i)


