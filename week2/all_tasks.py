def find_and_print(messages): 
    # write down your judgment rules in comments 

    # if any keywords in their sentence, it would be considered as that the user is older than 17 years old
    # create a list of these keywords!

    # 'college student': general case is that all above 18 years old, but corner case would be genius student!

    # to be accurate, we should use the following keywords, but it is complicated for coding.
    # keywords = ['18 years old', 'legal age in Taiwan', 'vote']

    # to simplify the situation, we just use a single word for keywords
    keywords = ['18', 'legal', 'vote']
    
    # your code here, based on your own rules 

    for item in messages:

        
        words = messages[item].split()
        for word in words:
            if word in keywords:
                print(item)
                break
      
find_and_print({ 
"Bob":"My name is Bob. I'm 18 years old.", 
"Mary":"Hello, glad to meet you.", 
"Copper":"I'm a college student. Nice to meet you.", 
"Leslie":"I am of legal age in Taiwan.", 
"Vivian":"I will vote for Donald Trump next week", 
"Jenny":"Good morning." 
}) 


def calculate_sum_of_bonus(data): 
    # write down your bonus rules in comments 
    # Bonus is based on 3 things, salary, performance, and role fields.

    # Salary: base. just the numbers
    # performance. 3 levels. above/average/below.  the weighing factor: 30%/10%/20%
    # role fields: 3 levels. Individual contributors/managers/C-level. weighing factor: 10%/20%/30% 
    
    # your code here, based on your own rules 
    sum_bonus = 0

    dict_performance = {"above average": 0.03,
                        "average": 0.02,
                        "below average": 0.01,
                        }
    
    dict_role = {"CEO": "c_level",
                #  "Manager": "mid_level", # for future reference
                 "Engineer": "individual_contributor",
                 "Sales": "individual_contributor",
                 }
    
    dict_role_to_number = {"c_level": 0.03,
                           "mid_level": 0.02,
                           "individual_contributor": 0.01,
    }

    for item in data:
        for index in range(len(data[item])):
            if not isinstance(data[item][index]['salary'], int):
                data_salary = data[item][index]['salary']
                base = convert_to_integer(data_salary)

            else:
                base = data[item][index]['salary']

            bonus =  base * dict_performance[data[item][index]['performance']] + \
                        base * dict_role_to_number[dict_role[data[item][index]['role']]]

            sum_bonus += bonus
    
    print(sum_bonus)


def convert_to_integer(string_value):
    # Remove non-numeric characters and convert to integer
    numeric_value = int(''.join(filter(str.isdigit, string_value)))

    # Apply currency conversion if "USD" is present in the string
    if "USD" in string_value:
        numeric_value *= 30

    return numeric_value




calculate_sum_of_bonus({ 
"employees":[ 
    { 
    "name":"John", 
    "salary":"1000USD", 
    "performance":"above average", 
    "role":"Engineer" 
    }, 
    { 
    "name":"Bob", 
    "salary":60000, 
    "performance":"average", 
    "role":"CEO" 
    }, 
    { 
    "name":"Jenny", 
    "salary":"50,000", 
    "performance":"below average", 
    "role":"Sales" 
    } 
] 
})  # call calculate_sum_of_bonus function 


def func(*data): 
    # your code here
    # dictionary to document the frequency of names
    dict_middle_name = {}
    answer = []

    # Part 1: to create a lookup dictionary
    for name in data:
        if len(name) == 3 or len(name) == 2:
            dict_middle_name[name[1]] = dict_middle_name.get(name[1], 0) + 1
        else:
            print("Name is not right!")
            
    # Part 2: to print out the name whose frequency is only once
    # Part 2 is to be optimized. No need to go through all items again... Not sure how to simplify this part
    target_frequency = 1
    
    for name in data:
        if dict_middle_name[name[1]] == target_frequency:
            answer.append(name)
    
    if len(answer) == 0:
        print("沒有")
    else:
        for name in answer:
            print(name)



func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆 
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花  花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有

def get_number(index):
    # your code here

    # this method is not that good. Brute force.
    # Optimized solution is recursion. But, I cannot make it for recursion...
    answer_array = []
    for item in range(index + 1):
        answer = 0
        if item % 2 == 0: # even number!
            answer = 3 * (item // 2)
        elif item == 1:
            answer = 4
        else:
            combo_1st_index = item // 2
            combo_2nd_index = combo_1st_index + 1
            answer = answer_array[combo_1st_index] + answer_array[combo_2nd_index]
        answer_array.append(answer)
    print(answer_array[index])

  
get_number(1)  # print 4 
get_number(5)  # print 10 
get_number(10)  # print 15 


