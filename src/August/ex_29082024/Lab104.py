# # Dict
# # Key and Value
# # name -> "Pramod"
#
# student_infor = {
#
#     "name" : "Amith",
#     "age"  : 22,
#     "age"  : 25,
#     "address" : "KA"
# }
#
# print(student_infor)
# print(student_infor["name"])
# print(student_infor["age"])
# print(student_infor["address"])
# student_infor["age"] = 55
# print(student_infor)
#
# student_infor4 = dict(name = "Kamal", age=12, adress="New_Delhi")
# print(student_infor4)

student_infor1 = {

    "name" : "Amith",
    "age"  : 22,
    "age"  : 25,
    "address" : {
        "home_address" : "KA",
         "office_address": "Goa"
    }
}

# print(student_infor1)

student_infor2 = {

    "name" : "Nijit",
    "age"  : 25,
    "age"  : 29,
    "address" : {
        "home_address" : "MP",
         "office_address": "MH"
    }
}

# print(student_infor2)

Mix = [student_infor1,student_infor2]
print(Mix)