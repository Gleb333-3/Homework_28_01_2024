listt = [
["Stefan", "Raj", "Marie"],
["Alexa", "Amy", "Edward"],
["Liz", "Claire", "Juan"],
["Dee", "Luke", "Katie"]
]

new_order = listt[0][::1] + listt[1][::-1] + listt[2][::1] + listt[3][::-1]

print(new_order)