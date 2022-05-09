class A:

    def sayName(self, name):
        print(f'my name is {name}')

    def sayNameNoSelf(name):
        print(f'my name is {name} NoSelf')


A().sayName('homayoon')
A.sayNameNoSelf('homayoon')
