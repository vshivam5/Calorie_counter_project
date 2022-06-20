import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyqrcode
import png

from dataclasses import dataclass
from pyqrcode import QRCode


calorie_limit = 3000
protein_limit = 180
fat_limit = 80
carbs_limit = 300


today =[]


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fats: int
    carbs: int

done = False

while not done:
    print("""
    (1) Add new Food
    (2) Visualize your Progress and To Export Data in Excel Sheet
    (3) Quite
    """)
    
    choice = input("Enter Your Choice: ")

#for data Entring
    if choice == '1':
        print("Adding a new food!")
        print()
        name = input('Name: ')
        calories = int(input('Calories: '))
        protein = int(input('protein: '))
        fats = int(input('Fats: '))
        carbs = int(input('Carbs: '))
        food = Food(name, calories, protein, fats, carbs)
        today.append(food)
        print("Sucessfully Added !")

#for visualization 
    elif choice == '2':
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fats for food in today)
        carbs_sum = sum(food.carbs for food in today)
        
        
        fig, axs = plt.subplots(2,2,figsize=(10,10))
        
        axs[0,0].pie([protein_sum,fats_sum,carbs_sum], labels = ['Protein', 'Fats','Carbs'], autopct="%1.1f%%")
        axs[0,0].set_title("Macronutrients Distribution")

        axs[0,1].bar([0,1,2], [protein_sum,fats_sum,carbs_sum] , width = 0.4)
        axs[0,1].bar([0.5,1.5,2.5],[protein_limit, fat_limit, carbs_limit], width =0.4)
        axs[0,1].set_title("Macronutrients Progress")

        axs[1,0].pie([calorie_sum, calorie_limit - calorie_sum], labels=['Calories', 'Remaining'], autopct="%1.1f%%")
        axs[1,0].set_title("Calories Goal Progress")
        
        axs[1,1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label ="Calories Eaten")
        axs[1,1].plot(list(range(len(today))), [calorie_limit]*len(today), label = 'Calorie Goal')
        axs[1,1].legend()
        axs[1,1].set_title('Calories Goal over Time')
       
        fig.tight_layout()
        fig.savefig('Calories_visualtions.png')
        plt.show()

        data = pd.DataFrame(today)
        datatoexcel = pd.ExcelWriter('Calories_counter.xlsx')
        data.to_excel(datatoexcel)
        datatoexcel.save()
        print("Data Successfully Exported as Excel File")

    
        url = pyqrcode.create()
        url.svg('myQR.svg', scale = 8)
        url.png('myQR.png', scale = 6)
        

#for exit
    elif choice == 'q' or '3':
      done = True
    else:
      print("Invalid Choice")
