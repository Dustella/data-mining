def greetings(name):
    print(f"Greetings, {name}")
    
def sum(a,b):
    result = a + b
    return result

def main():
    greetings("John")
    greetings("Mary")
    greetings("Bob")
    
    print(sum(1,2))
    print(sum(3,4))
    print(sum(5,6)) 

main()