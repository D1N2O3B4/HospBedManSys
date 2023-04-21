


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

