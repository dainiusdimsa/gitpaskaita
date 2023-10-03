# 1.	Paveldejimas;
# 2.	Input;
# 3.	Dictionary key ir value/mapping;
# 4.	While;


# Sukurti programa, kuri leistu zaisti su duomenu baze:
# ideti, get, filter, delete, create, update (1-6, 0)


class Animal:
    def __init__(self, name):
        self.name = name

    def begti(self):
        print(f'Animal {self.name} bega.')

class Dog(Animal):
    def __init__(self, bread, name):
        super().__init__(name)
        self.bread = bread

    def loti(self):
        print(f'{self.name} yra veisle {self.bread} ir jie ne loja, o kanda.')


def loti():
    print('Lojimas')


def begti():
    print('Begimas')

# dog = Dog(name='Brisius', bread='Dobermanas')
# dog.begti()


funkcijos = {
    1: loti,
    2: begti,
}

funkcijos[1]

# getattr()

funkcijos[2]()

while True:
    value = input('Duok skaiciu: ')
    if int(value) == 5:
        break


