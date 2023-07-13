function findAndPrint(messages){ 
    // write down your judgment rules in comments 
    const arr_keywords = ['18', 'legal', 'vote'];
    // your code here, based on your own rules
    
    const keys = Object.keys(messages);
    // const Object.entries(messages)



 


    for (let i = 0; i < keys.length; i++) {
        let arr_words = messages[keys[i]];

        for (let j = 0; j < arr_keywords.length; j++) {
            if (arr_words.includes(arr_keywords[j])) {
                console.log(keys[i])
            }
            if (arr_words.includes(arr_keywords[j])) { break; }
        }
    }
    } 

findAndPrint({ 
"Bob":"My name is Bob. I'm 18 years old.", 
"Mary":"Hello, glad to meet you.", 
"Copper":"I'm a college student. Nice to meet you.", 
"Leslie":"I am of legal age in Taiwan.", 
"Vivian":"I will vote for Donald Trump next week", 
"Jenny":"Good morning." 
}); 


function convert_to_integer(string) {
    let numeric_value = string.replace(/[^0-9]/g, '');
    numeric_value = parseInt(numeric_value, 10);
    if (string.includes("USD")) {
        numeric_value *= 30;
    };
    return numeric_value;
}


function calculateSumOfBonus(data){

    // write down your bonus rule in comments 
    const dict_performance = {"above average": 0.03,
    "average": 0.02,
    "below average": 0.01,
    }

    const dict_role = {"CEO": "c_level",
    //   "Manager": "mid_level",  for future reference
    "Engineer": "individual_contributor",
    "Sales": "individual_contributor",
    }

    const dict_role_to_number = {"c_level": 0.03,
        "mid_level": 0.02,
        "individual_contributor": 0.01,
    }
        
    // your code here, based on your own rules

    let sum_bonus = 0;
    
    const keys_1st_level = Object.keys(data);
    const keys_2nd_level = Object.keys(data[keys_1st_level[0]]);
    // console.log(keys_1st_level);
    // console.log(keys_2nd_level);

    for (let i = 0; i < keys_1st_level.length; i++) {
        for(let j = 0; j < keys_2nd_level.length; j++) {
            // console.log(data[keys_1st_level[0]][j]['salary']);
            
            let temp_salary = data[keys_1st_level[0]][j]['salary'];
            if (temp_salary.constructor === Number) {
                base = data[keys_1st_level[i]][j]['salary'];
            } else { 
                base = convert_to_integer(temp_salary);

            }

            let bonus = base * dict_performance[data[keys_1st_level[i]][j]['performance']] + base * dict_role_to_number[dict_role[data[keys_1st_level[i]][j]['role']]];
            
            sum_bonus += bonus;


        }
    }
    console.log(sum_bonus);

    
    } 




calculateSumOfBonus({ 
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
});  // call calculateSumOfBonus function 


function func(...data){ 
    // your code here 
    let dict_middle_name = {};
    let answer = [];


    // Part 1: to create a lookup dictionary
    for ([index, value] of data.entries()) {
        if (value.length === 3 || value.length === 2) {
            dict_middle_name[value[1]] = (dict_middle_name[value[1]] || 0) + 1; 
        } else {
            console.log("Name part has an issue!")
        }
    }

    // # Part 2: to print out the name whose frequency is only once
    // # Part 2 is to be optimized. No need to go through all items again... Not sure how to simplify this part
    target_frequency = 1;

    for ([index, value] of data.entries()) {
        if (dict_middle_name[value[1]] === target_frequency) {
            answer.push(value)
        }
    }

    if (answer.length === 0) {
        console.log("沒有");
    } else {
        for ([index, value] of answer.entries()) {
            console.log(value);
        }
    }

    } 




func("彭⼤牆", "王明雅", "吳明");  // print 彭⼤牆 
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花");  // print  林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花");  // print 沒有 

function getNumber(index) { 
    // your code here 
    let answer_array = [];
    
    for (let item = 0; item <= index; item++) {
        let answer = 0
        if (item % 2 === 0) {
            answer = 3 * (Math.floor(item / 2))
        } else if (item == 1){
            answer = 4

        } else {
            let combo_1st_index = Math.floor(item / 2);
            let combo_2nd_index = combo_1st_index + 1;
            answer = answer_array[combo_1st_index] + answer_array[combo_2nd_index];
        }
        answer_array.push(answer);
        
    } 
    // console.log(answer_array);
    console.log(answer_array[index]);
    } 


getNumber(1);  // print 4 
getNumber(5);  // print 10 
getNumber(10);  // print 15 