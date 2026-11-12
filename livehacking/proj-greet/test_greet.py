def greet(name):
    return f'Hi {name}, my name is Joerg'

def test_greet():
    output = greet('Hrvoje')
    assert output == 'Hi Hrvoje, my name is Joerg'
