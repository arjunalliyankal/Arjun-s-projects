import tkinter as tk
import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
def show_entry_fields():
    entries_list = [e.get() for e in entries]
    input_string = [float(s) for s in entries_list]
    return input_string

def show_output():
    input_string = show_entry_fields()
               
    output_text= machine_learning(input_string)
    
    
    
    
    
   # label = tk.Label(root, text=output_text, font=("Helvetica", 24))
    #label.pack()


    label = tk.Label(frame, text=output_text, font=("Helvetica", 24), fg="blue", bg="yellow", anchor="nw")
    label.pack()
    #print(f"Label text: {label.cget('text')}")
    #label.pack()
    
    #label.config(text=output_text)

def machine_learning(input_string):
    # Perform machine learning on input_string
    diabetes_data = pd.read_csv(r'diabetes prediction\diabetes.csv')
    diabetes_data.head(5)
    diabetes_data.shape
    diabetes_data.describe()
    diabetes_data['Outcome'].value_counts()
    diabetes_data.groupby('Outcome').mean()
    #o means the person with diabetes 1 means the person's with out diabetes

    x=diabetes_data.drop(columns='Outcome')
    y=diabetes_data['Outcome']
    diabetes_data.head(5)

    Scaler = StandardScaler()
    Scaler.fit(x)
    standardized_data = Scaler.transform(x)
    standardized_data

    x = standardized_data
    y = diabetes_data['Outcome']

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, stratify=y , random_state=2)
    classifier = svm.SVC(kernel= 'linear')
    classifier.fit(x_train, y_train)
    x_train_prediction = classifier.predict(x_train)
    training_data_accurcy = accuracy_score(x_train_prediction, y_train )
    training_data_accurcy
    x_test_prediction = classifier.predict(x_test)
    test_data_accuracy = accuracy_score(x_test_prediction, y_test)
    test_data_accuracy

    #input_data = [9,110,92,0,0,37.6,0.191,30]
    input_data = input_string
    #input_data = show_entry_fields()
    #print(input_data)
    input_data_array_as_numpy = np.asarray(input_data)
    input_data_reshaped = input_data_array_as_numpy.reshape(1, -1)
    std_data = Scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    #print(prediction)
    if prediction[0] == 0:
        return    "The person is not diabetic"
    else:
      return "The person is diabetic"  
    


     
master = tk.Tk()
tk.Label(master, text="Pregnancies:").grid(row=0)
tk.Label(master, text="Glucose:").grid(row=1)
tk.Label(master, text="Blood pressure:").grid(row=2)
tk.Label(master, text="Skin thickness:").grid(row=3)
tk.Label(master, text="Insulin:").grid(row=4)
tk.Label(master, text="BMI:").grid(row=5)
tk.Label(master, text="Diabetespedigreefunction:").grid(row=6)
tk.Label(master, text="Age:").grid(row=7)

entries = []
for i in range(8):
    e = tk.Entry(master)
    e.grid(row=i, column=1)
    entries.append(e)

tk.Button(master, text='Quit', command=master.quit).grid(row=9, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(master, text='CHECK', command=show_output).grid(row=9, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

frame = tk.Frame(master)
frame.grid(row=10, column=4, columnspan=10)



master.mainloop()
    