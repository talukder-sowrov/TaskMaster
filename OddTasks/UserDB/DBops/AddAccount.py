from UserDB.models import Person, Client


def add_account(name, age, username, password, tasks, address, city, province, postal):

    test_user = Person(Name=name, Age=age, Username=username, Password=password, Task=tasks, Address=address, City=city
                       , Province=province, Postal=postal)
    test_user.save()



