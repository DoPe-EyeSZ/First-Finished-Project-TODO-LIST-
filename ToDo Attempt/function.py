import pickle
import os


class Function():
    def __init__(self):
        self.num_task = 0
        self.active = True
        if not os.path.exists('task.pickle'):
            with open('task.pickle', 'wb') as file:
                pickle.dump([], file)


    def add(self, task):
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)
        self.num_task+=1

        list.append(task)
        with open('task.pickle', 'wb') as file:
            pickle.dump(list, file)


        self.display()

    def validate(self, i, output):
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)

        while not i.isdigit() or int(i)>len(list) or int(i)<=0:
            print(" \n ERROR TRY AGAIN \n ")
            self.display()
            i = input(output)
        return int(i)

    def remove(self):
        self.display()
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)

        if len(list)==0:
            print("\n There are no tasks to remove \n")
            return
        else:
            x = input(" \n Which task number would you like to remove? \n ")
            c = self.validate(x, " \n Which task number would you like to remove? \n ")

            
            list.pop(int(c)-1)
            with open('task.pickle', 'wb') as file:
                pickle.dump(list, file)

            self.display()

    def edit(self):
        self.display()
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)
        x = input("\n Which task would you like to edit \n")
        c = self.validate(x, "\n Which task would you like to edit \n")
        y = input("\n Make your edit here: ")

        list[int(c)-1] = y
        with open('task.pickle', 'wb') as file:
            pickle.dump(list, file)

        self.display()

    def display(self):
        print("\n Here are your tasks \n")
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)
        
        num = 1
        if len(list)==0:
            print("\n There are zero tasks \n")
        else:
            for x in list:
                print(f"{num}) {x}")
                num+=1

    def clear(self):
        with open('task.pickle', 'wb') as file:
            pickle.dump([], file)
        self.display()

        

    def reorder(self):
        self.display()
        with open('task.pickle', 'rb') as file:
            list = pickle.load(file)
        x=input("\n Which task number would you like to reorder? \n")
        c1 = self.validate(x, "\n Which task number would you like to reorder? \n")
        y=input("\n Which task number would you like to replace it with? \n")
        c2 = self.validate(y, "\n Which task number would you like to replace it with? \n")

        

        temp = list[int(c1)-1]
        list[int(c1)-1] = list[int(c2)-1]
        list[int(c2)-1] = temp

        with open('task.pickle', 'wb') as file:
            pickle.dump(list, file)
        self.display()


    def run(self):
        while self.active:
            x = input("\n What would you like to do? \n (1) Add Tasks \n (2) Remove Task \n (3) Edit Task \n (4) Reorder Task \n (5) Clear List \n (6) Close App \n")

            if x == "1":
                i = input("\n What tasks would you like to add? \n")
                self.add(i)

            elif x == "2":
                self.remove()

            elif x == "3":
                self.edit()
            
            elif x == "4":
                self.reorder()

            elif x == "5":
                self.clear()
            
            elif x == "6":
                self.active=False

            else:
                print("\n Error \n")
            
        print("TODO is closed")



            