def likes(name):
    number_of_people = len(name)
    if number_of_people == 0:
        return "no one likes this"
    elif number_of_people == 1:
        return f"{name[0]} likes this"
    elif number_of_people == 2:
        return f"{name[0]} and {name[1]} like this"
    elif number_of_people == 3:
        return f"{name[0]}, {name[1]} and {name[2]} like this"
    elif number_of_people > 3:
        return f"{name[0]}, {name[1]} and {number_of_people - 2} others like this"
