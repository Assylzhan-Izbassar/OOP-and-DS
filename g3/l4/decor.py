def handshake(say_hello):
    def rule():
        print('Рукопожатье')
        say_hello()
    return rule


@handshake
def say_hello():
    print('Привет!')

# say_hello()



# пример 2
def nut(ice_cream):
    def make(nachinka):
        print()
        return ice_cream(nachinka)
    return make

@nut
def ice_cream(nachinka):
    return 'мороженное с' + nachinka

print(ice_cream('начинка'))