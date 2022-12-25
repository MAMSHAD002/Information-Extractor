import wikipedia


def Information(Name):
    result = wikipedia.summary(Name,3)
    print(result)

Name = input("Say your name: ")

Information(Name)