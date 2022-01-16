'''
Decoradores (decorators)


o que é?
    - Função que envolve outra função
    - Sintaxe propia com '@'
    
Decorador sem compressão

def grettings(func):
    def wrapper():
        print('Olá, seja bem vindo!')
        func()
        print('Tenha um bom dia!')
    return wrapper

def hello_world():
    print('Hello World!')


value = grettings(hello_world)
value()
,

def grettings(func):
    def wrapper(*args, **kwargs):
        print('Olá, seja bem vindo!')
        func(*args, **kwargs)
        print('Tenha um bom dia!')
    return wrapper

@grettings
def hello_world(value, value2):
    print(f'Hello World! {value}: {value2}')

hello_world('a', 'b')


def grettings(label):
    def intern(func):
        def wrapper(*args, **kwargs):
            print(label)
            print('Olá, seja bem vindo!')
            func(*args, **kwargs)
            print('Tenha um bom dia!')
        return wrapper
    return intern

@grettings("teste")
def hello_world(value, value2):
    print(f'Hello World! {value}: {value2}')

hello_world('a', 'b')

def timer(func_name):
    from datetime import datetime
    def intern(func):
        def wrapper(*args, **kwargs):
            print(f"Function Name:{getattr(func, '__name__')}")
            start = datetime.now()
            func(*args, **kwargs)
            end = datetime.now()
            time_to_run = end - start
            print(f'Time to run: {time_to_run}')
        return wrapper
    return intern
    
'''


def timer(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        print(f"Function Name:{getattr(func, '__name__')}")
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time_to_run = end - start
        print(f'Time to run: {time_to_run}')
    return wrapper

@timer
def esperar_5_segundos():
    from time import sleep
    sleep(5)

esperar_5_segundos()
