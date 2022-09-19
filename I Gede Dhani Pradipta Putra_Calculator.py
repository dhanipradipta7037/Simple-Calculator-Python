#!/usr/bin/env python
# coding: utf-8

# In[2]:


cont = "y"
while cont.lower() == "y":
    the_operation = str(input('Pilih operator(+,-,/,*): '))
    a=0
    while True:
        try:
            a = int(input('Input angka pertama: '))
        except ValueError:
            print('Tolong input angka yang benar')
            continue
        else:
            break

    b=0
    while True:
        try:
            b = int(input('Input angka kedua: '))
        except ValueError:
            print("Tolong input angka yang benar")
            continue
        else:
            break

    if the_operation == '*':
        hasil=a*b
        print(f'jawaban: {hasil}')
    elif the_operation == '+':
        hasil=a+b
        print(f'jawaban: {hasil}')
    elif the_operation == '-':
        hasil=a-b
        print(f'jawaban: {hasil}')
    elif the_operation == '/':
        hasil=a/b
        print(f'jawaban: {hasil}')
    
    cont = input("Continue?y/n:")
    if cont == "n":
        break


# In[ ]:





# In[ ]:




