try:
    print( 0 / 0)
    assert 1 != 1, "Uno no es distinto que uno"    
    age = 10
    if age < 18:
        raise Exception("Age must be 18 or superior")   
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)        
        
print("hola")