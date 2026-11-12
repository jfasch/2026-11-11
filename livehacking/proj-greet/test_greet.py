import greet

def test_greet():
    output =  greet.greet('Hrvoje')
    assert output == 'Hi Hrvoje, my name is Joerg'
