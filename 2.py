import time

class Pupil:
    def __init__(self,Surname,Name,Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name,'-', pupil.Mark)
        print('\n')

def print_five(pupils):
    print('Отличники:')
    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname)
    print('\n')

def print_average(pupils):
    average = 0
    for pupil in pupils:
        average += pupil.Mark
    average /=len(pupils)
    print('Средняя оценка класса:',average)

start_time = time.time()
with open('pupils_large.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0],data[1], int(data[2]))
        pupils.append(pupil)

print_five(pupils)
print_average(pupils)
print('Время выполнения:', (time.time()-start_time),'секунд')



