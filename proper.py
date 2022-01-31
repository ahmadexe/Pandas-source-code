import pandas as pd
 
nm = ['Ahmad', 'Haider', 'Sufi', 'Zoha', 'Saad']
ct = ['Islamabad', 'Sahiwal', 'Bahwalpur', 'Karachi', 'Karachi']
mk = [100,90,80,70,60]
while True:
    print('''
    1. Add new student.
    2. View Student.
    3. Exit
    4. View Database

    ''')

    c = int(input("Enter your choice: "))
    if c == 1:
        try:
            addnm = str(input("Enter name of new student: "))
            addct = str(input(f"Enter the city of {addnm}: "))
            addmk = int(input(f"Enter the marks of {addnm}: "))

            nm.append(addnm)
            ct.append(addct)
            mk.append(addmk)
        except ValueError as error:
            print('No value added or wrong value added.')

    



    maindict = {
    'Name' : nm,
    'City' : ct,
    'Marks' : mk 
    }

    maindataframe = pd.DataFrame(maindict)
    maindataframe.to_csv('proper.csv')
    

    if c == 2:
        check = str(input("Enter the name of student: ")).title()
        mainread = pd.read_csv('proper.py')
        
        print(maindataframe.loc[(maindataframe['Name'] == check)])
       
    
    if c == 3:
        exit()

    if c == 4:
        print(maindataframe)

