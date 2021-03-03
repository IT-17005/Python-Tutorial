#xxargs(dictionary)
def student(**details):
    print(details)
    print(details["Id"])
    print(details["Name"])

student(Id=17005,Name="Ruhan")