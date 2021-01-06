dict1={}

dict1["name"]='Tyson', "touss"
dict1["address"]='1313 Mockingbird Lane', "main street"
dict1["favorite food"]='cherry pie', "fudge"
dict1["drink"]='water', 'beer'

print(dict1.items())#tuple

for key, value in dict1.items() :
    print(f"the {key} is {value[0]}; {value[1]}")


def decorator(func):
    def wrapper():
        name = input("give me an authentication name: ")
        if name == "gertrude":
            func()
        else: print("try a different input")
        print("it was nice working with you")

    return wrapper

@decorator
def mult():
    num1= input("give me an integer: ")
    num2=input("give me another integer: ")
    print(int(num1)* int(num2))

mult()