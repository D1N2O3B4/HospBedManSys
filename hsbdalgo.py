def get_priority(patient):
    if patient["SELDOM_SICK"] == False:
        if patient["CATEGORY"] == 'A':
            if patient["AGE"] > 50 or patient["AGE"] < 18:
                return 2000 + patient["AGE"]
            return 1800 + patient["AGE"]
        if patient["CATEGORY"] == 'B':
            if patient["AGE"] > 50 or patient["AGE"] < 18:
                return 1500 + patient["AGE"]
            return 1300 + patient["AGE"]  
        if patient["CATEGORY"] == 'C':
            if patient["AGE"] > 50 or patient["AGE"] < 18:
                return 1000 + patient["AGE"]
            return 800 + patient["AGE"]
            
    else:
        if patient["CATEGORY"] == "A":
            if patient["AGE"] < 18:
                return 1700 + patient["AGE"]
            else:
                return 1600 + patient["AGE"]
        elif patient["CATEGORY"] == "B":
            if patient["AGE"] < 18:
                return 1200 + patient["AGE"]
            else:
                return 1100 + patient["AGE"]
        else:
            if patient["AGE"] < 18:
                return 600 + patient["AGE"]
            else:
                return 400 + patient["AGE"]


patient_list = [
    {"ID":1,"CATEGORY":"A","AGE":35,"SELDOM_SICK":True},
    {"ID":2,"CATEGORY":"B","AGE":67,"SELDOM_SICK":False},
    {"ID":3,"CATEGORY":"A","AGE":67,"SELDOM_SICK":False},
    {"ID":4,"CATEGORY":"C","AGE":18,"SELDOM_SICK":False},
    {"ID":5,"CATEGORY":"C","AGE":9,"SELDOM_SICK":False},
    {"ID":5,"CATEGORY":"A","AGE":12,"SELDOM_SICK":True},
    {"ID":6,"CATEGORY":"A","AGE":45,"SELDOM_SICK":True}   
]


sorted_patient_list = sorted(patient_list, key=get_priority,reverse=True)

print(sorted_patient_list)

