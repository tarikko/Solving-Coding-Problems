'''
- Solution #1 (doesn't work properly for more than 3 characters) :
    - Solving Steps :
        1 - Getting the length of the string and displaying it
        2 - Generating an array of chracters from the input string
        3 - Appending each character to the solved array and the temporary array
        4 - (see the image below)
        5 - Adding all the characters stored in the temporary array to the temporary string and then appending it to the solved array
        6 - Done
    - This solving method can be improved further more so feel free to contribute to this repo and adding your own improved solution.
'''
#### 1 - Getting the length of the string and displaying it ####

length = 0

def getLength(String):
    global length
    length = len(String)
    print(f"The length of the string \"{String}\" is {length}.\n")

#### 2 - Generating an array of chracters from the input string ####

arr = []

def new_array(String):
    global arr
    for x in range(length):
        arr.append(String[x]) ### 3 - Appending each character to the solved array and the temporary array ###

#### 4 - (see the image below) ####

solved_arr = []
temp_arr = []
temp_string = ""

def sort(arr):

    global temp_arr
    global temp_string
    global sloved_arr

    for x in range(len(arr)):
        solved_arr.append(arr[x])
        temp_arr.append(arr[x])

    for x in range(len(arr)):
        for y in range(x, len(arr)):
            if y > x and y != x:
                solved_arr.append(arr[x] + arr[y])

    for x in range(len(temp_arr)):
        temp_string = temp_string + solved_arr[x] #### 5 - Adding all the characters stored in the temporary array to the temporary string and then appending it to the solved array ####
        
    solved_arr.append(temp_string)

    print(solved_arr)

#### 6 - Done ####

def Generate_strings(String):
    
    getLength(String)
    new_array(String)

    global arr

    sort(arr)

#### This file was coded **entierly** by Tarik Abdelkader (tarikko) ####