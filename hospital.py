'''
Care hospital wants to know the medical speciality visited by the maximum number of patients. 
Assume that the patient id of the patient along with the medical speciality visited by the 
patient  is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
    "P": "Pediatrics",
    "O": "Orthopedics",
    "E": "ENT
}

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Also write the pytest test cases to test the program.

Note:
Assume that there is always only one medical speciality which is visited by maximum number of patients.
Perform case sensitive string comparison wherever necessary.
'''

# PF-Assgn-32


def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    count1 = 0
    count2 = 0
    count3 = 0
    for keyword in patient_medical_speciality_list:
        if (keyword == 'P'):
            count1 += int(keyword + 1)
        elif (keyword == 'O'):
            count2 += int(keyword + 1)
        else:
            count3 += int(keyword + 1)

    if (count1 > count2 and count1 > count3):
        for key, value in medical_speciality.items():
            if (key == "p"):
                return value
    elif (count2 > count1 and count2 > count3):
        for key, value in medical_speciality.items():
            if (key == "O"):
                return value
    else:
        for key, value in medical_speciality.items():
            if (key == "E"):
                return value

    return speciality


def max_visited_speciality1(patient_medical_speciality_list, medical_speciality):

    result = [0, 0, 0]
    i = 1
    while(i < len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P':
            result[0] = result[0] + 1
        elif patient_medical_speciality_list[i] == 'O':
            result[1] = result[1] + 1
        else:
            result[2] = result[2] + 1
        i = i + 2
    a = max(result)
    a = result.index(a)
    if a == 0:
        speciality = 'Pediatrics'
    elif a == 1:
        speciality = 'Orthopedics'
    else:
        speciality = 'ENT'

    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [
    301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality1(
    patient_medical_speciality_list, medical_speciality)
print(speciality)
