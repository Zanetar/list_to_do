import fileinput
import sys
import datetime


class List_to_do:
    def __init__(self):
        self.tasks=[]

    def add(self):
        try:
            a=make_task()
            self.tasks.append(a + '\n')
        except ValueError: print('Wybrano zły znak')

    def write(self):
        t=self.tasks
        f=open('zadania.txt', 'a')
        f.writelines(t)
        f.write()
        f.close()

    def show_all(self):
        print('Twoja lista')
        f = open('zadania.txt')
        print(f.read())
        f.close()

    def edit(self):
        print('Twoja lista:')
        f = open('zadania.txt')
        print(f.read())
        f.close()

        file='zadania.txt'
        searchtext=input('Wpisz nazwę zadania, które ma być zmienione. Następnie na nowo przejdź przez proces uzupełniania zadania z nowymi danymi!')
        change= make_task()
        with fileinput.FileInput(file,inplace = True, backup ='.bak') as f:
            for line in f:
                if searchtext in line:
                    print(change,end ='\n')
                else:
                    print(line, end ='')
        print('Zadanie zostało zmienione!')



def menu():
    try:
        list=List_to_do()
        while True:
            print ('Witaj w programie List to do')
            print ('Zarządzaj swoimi zadaniami')
            print('Co chcesz zrobić?')
            print('1. Utwórz nowe zadanie')
            print('2. Edytować istniejącą listę')
            print('3. Wyświetlić istnejącą listę')
            print('0- aby wyjść')
            choose=int(input())
            if choose==0:
                print('Do widzenia')
                break
            else:
                choose= int(choose)
                if choose==1:
                    list.add()
                    print('Twoje zadanie zostało utworzone.')
                    list.write()
                elif choose==2:
                    list.edit()

                elif choose==3:
                    list.show_all()
                else:
                    print('Wybrałeś zły znak')
                    break
    except: print('Wybrałeś zły znak!')





class Task:
    def __init__(self, name: object, description: object, priority: object, start: object, finish: object) -> object:

        self.name=name
        self.description=description
        self.priority=priority
        if priority>5:
            self.priority=5
            print('Najwyższy priotytet to 5.')
        elif priority<1:
            self.priority=1
            print('Najniższy priorytet to 1.')
        try:
            self.start= datetime.datetime.strptime(start, '%m/%d/%Y').date()
            self.finish=datetime.datetime.strptime(finish, '%m/%d/%Y').date()
        except: print('Zadanie nie zostało utworzone. Niepoprawna forma daty!')

    def __repr__(self):
        return(f'Nazwa zadania : {self.name}. Opis zadania: {self.description}. '
               f'Priorytet zadania {self.priority}. Start zadania {self.start}. '
               f'Koniec zadania {self.finish}')

    def __str__(self):
        return (f'Nazwa zadania : {self.name}. Opis zadania: {self.description}. '
                f'Priorytet zadania {self.priority}. Start zadania {self.start}. '
                f'Koniec zadania {self.finish}')
def make_task():
    task=Task(input('Wpisz nazwę zadania'),
              input('Wpisz treść zadania'),
              int(input('Wpisz priorytet zadania gdzie 1=niski a 5 najwyższy')),
              input('Wpisz dane rozpoczęcia w formacie:mm/dd/yyyy'),
              input('Wpisz planowaną datę zakończenia w formacie:mm/dd/yyyy'))
    return task.__str__()

menu() #wywołanie programu
