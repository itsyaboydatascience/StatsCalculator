import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
#Main menu 
    data = pd.DataFrame()
    menu()
    choice = validate(7)
    while choice != 7:
        if choice == 1:
            data = load()
            menu()
            choice = validate(7)
        elif choice == 2:
            if data.empty:
                error()
                menu()
                choice = validate(7)
            else:
                display_df(data)
                menu()
                choice = validate(7)
        elif choice == 3:
            if data.empty:
                error()
                menu()
                choice = validate(7)
            else:
                clean(data)
                menu()
                choice = validate(7)
        elif choice == 4:
            if data.empty:
                error()
                menu()
                choice = validate(7)
            else:
                names, number, average, standard_deviation, standard_error, maximum, minimum, median, = analyse(data)
                stats(names, number, average, standard_deviation, standard_error, maximum, minimum,median)
                disp_corr(data)
                menu()
                choice = validate(7)
        elif choice == 5:
            if data.empty:
                error()
                menu()
                choice = validate(7)
            else:
                plots(data)
                menu()
                choice = validate(7)
        elif choice == 6:
            if data.empty:
                error()
                menu()
                choice = validate(7)
            else:
                savecsv(data)
                menu()
                choice = validate(7)
        else:
            exit()
#error function
error = lambda: print("Please upload a data set first.")

#displys main menu
def menu():
    print(""" Welcome to DataFrame Statistician!
    Coded by: James Lazzaro
    1 - Load data from a file
    2 - View data
    3 - Clean data
    4 - Analyse data
    5 - Visualise data
    6 - Save data to file
    7 - Quit """)

#validates user input
def validate(n):
    valid = False
    while not valid:
        try:
            choice = int(input("Please choose an option: "))
            if choice not in range(1, n + 1):
                raise Exception
            valid = True
            return choice
        except:
            print(f'Please enter a number from 1 to {n} ')

#loads user data
def load():
    try:
        filename = input("Please enter the filename followed by .csv: ")
        data = pd.read_csv(filename)
        cols = data.columns.tolist()
        print(cols)
        index = input('Please choose one of the following headers as an index: ')
        if index == '':
            data = pd.read_csv(filename)
            data = data.replace(0,np.nan)
        else:
            data = pd.read_csv(filename, index_col=index)
            data = data.replace(0,np.nan)
        return data
    except:
        print('The file you entered does not exist, please enter a valid file.')

#displays data
def display_df(data): 
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(data)

#Creates variables for analysis
def analyse(data):
    input = False
    while not input:
        print('Please choose a variable to analyse: ')
        
        disp_var(data)
        choice = validate(len(data.columns))
        input = True
        index = choice - 1
        var = data.iloc[:, index]
        names = data.columns[index]
        number = len(var)
        maximum = round(var.max(), 2)
        minimum = round(var.min(), 2)
        average = round(var.mean(), 2)
        standard_deviation = round(var.std(), 2)
        standard_error = round(var.sem(), 2)
        median = round(var.median(),2)
        return names, number, average, standard_deviation, standard_error, maximum, minimum, median
#display correlation matric   
def disp_corr(data):
    print(data.corr(method = 'pearson'))
    
#display stats
def stats(names, number, average, standard_deviation, standard_error, maximum, minimum,median):
    print(names)
    print('----------')
    print(f'Number of values (n):\t{number}')
    print(f'\t\tMinimum:\t\t{minimum}')
    print(f'\t\tMaximum:\t\t{maximum}')
    print(f'\t\tMean:\t\t\t{average}')
    print(f'\t\tMedian:\t\t\t{median}')
    print(f'\t\tStandard Deviation:\t{standard_deviation}')
    print(f'\t\tStd.Err of Mean:\t{standard_error}')
       
#prints variables and and index
def disp_var(data):
    variable = data.columns
    for k, var in zip(range(1,len(variable)+1), variable):
        print(f'\t{k} - {var}')

#creates plots from dataframe
def plots(data):
    plot = {1: 'line', 2: 'bar', 3: 'box'}
    subplots = {1: False, 2: True}
    print('Please choose a style of plot: ')
    print('\t1 - Line Chart')
    print('\t2 - Bar Graph')
    print('\t3 - Box Chart')
    choice1 = validate(3)
    print()
    print('Please choose a layout: ')
    print('\t1 - Single plot')
    print('\t2 - Subplots')
    choice2 = validate(2)
    title = str(input('Please choose a title:'))
    xlabel = (str(input('Please choose X label:')))
    ylabel = (str(input('Please choose Y label:')))
    data.plot(kind = plot[choice1], subplots = subplots[choice2])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

#saves data frame to csv
def savecsv(data):
    filename = str(input('Please choose a name for your file followed by .csv: '))
    if filename == '':
        print('Please enter a filename: ')
        savecsv(data)
    else:
        data.to_csv(filename, encoding='utf-8', index=False)

#drops missing data base on user input of threshold
def drop_missing(data):
    print(data)
    data.dropna(thresh = int(input('Please enter threshold: ')), inplace = True)
    print(data)
    
#gets user input
def get_input(prompt):
        value = int(input(prompt))
        return value

#replaces NAN with user input
def fill_missing(data):
    print(data)
    data = data.replace(np.nan, input('Please enter number to replace missing values with: '))
    print(data)
    return(data)

#renames column with user input
def rename(data):
    cols = data.columns.tolist()
    print(cols)
    choice1 = str(input('Please choose a column to rename: '))
    choice2 = str(input('Please enter a new name: '))
    data = data.rename(columns={choice1:choice2})
    print(data)

#drops column based on user input
def drop_col(data):
        cols = data.columns.tolist()
        print(cols)
        delete = str(input('Please choose a coloumn to delete: '))
        data = data.drop(columns=[delete])
        print(data)

#drops rows that contain duplicate data
def drop_dup(data):
    input('Press <Enter> to remove all duplicate rows')
    print("""
    BEFORE
    """)
    print(data)
    data = data.drop_duplicates()
    print("""
    
    AFTER
    """)
    print(data)

#Sub menu for data cleaning
def clean(data):
    print("""please choose from one of the following
    1 - Drop rows with missing values
    2 - Fill missing values
    3 - Drop duplicate rows
    4 - Drop column
    5 - Rename column
    6 - Finish cleaning""")
    choice = validate(6)
    while choice != 7:
        if choice == 1:
            drop_missing(data)
            clean(data)
            choice = validate(7)
        elif choice == 2:
            if data.empty:
                error()
                clean(data)
                choice = validate(7)
            else:
                fill_missing(data)
                clean(data)
                choice = validate(7)
        elif choice == 3:
            if data.empty:
                drop_dup(data)
                clean(data)
                choice = validate(7)
            else:
                drop_dup(data)
                clean(data)
                choice = validate(7)
        elif choice == 4:
            if data.empty:
                error()
                clean(data)
                choice = validate(7)
            else:
                drop_col(data)
                clean(data)
                choice = validate(7)
        elif choice == 5:
            if data.empty:
                error()
                clean(data)
                choice = validate(7)
            else:
                rename(data)
                clean(data)
                choice = validate(7)
        elif choice == 6:
            main()
main()