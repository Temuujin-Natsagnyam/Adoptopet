# Imports START
from flask import Flask, render_template, request
import csv
import re
from operator import itemgetter
# END

# Logical functions START
def matcher(row, colour, gender, name, animal):
    result = False
    if colour == row[5] or colour == '':
        if name == row[1] or name == '':
            if animal == row[2] or animal == "all":
                if gender == row[3] or gender == "all":
                    result = True
    return result

def search(colour, gender, name, animal, flag):
    data = []
    with open("static/test_out.csv") as f:
        pet_data = csv.reader(f)
        next(pet_data, None) # discard the header
        for row in pet_data:
            if  matcher(row, colour, gender, name, animal):
                data.append(row)
    
    if flag == "pop":  #curate the pets by popularity
        data.sort(key=itemgetter(8), reverse=True)
    elif flag == "alph": #curate the pets alphabetically
        data.sort(key=itemgetter(1))

    return data

def get_auto_sugg(substring_name, substring_colour):
    substring_name = '^'+substring_name
    substring_colour = '^'+substring_colour
    names = []
    colours = []
    with open("static/test_out.csv") as f:
        pet_data = csv.reader(f)
        next(pet_data, None) # discard the header
        for pet in pet_data:
            if re.search(substring_name, pet[1]):
                if pet[1] not in names:
                    names.append(pet[1])
            if re.search(substring_colour, pet[5]):
                if pet[5] not in colours:
                    colours.append(pet[5])
    return names, colours

def add_updoot(specific_pet):
    read = open('static/test_out.csv')
    all_pets = csv.reader(read) 
    all_pets = list(all_pets)
    read.close()

    ctr = 0
    for pet in all_pets:
        if pet[0] == specific_pet:
            all_pets[ctr][8] = str(int(pet[8]) + 1)
        ctr += 1
    
    write = open('static/test_out.csv', 'w', newline='')
    writer = csv.writer(write)
    writer.writerows(all_pets)
    write.close()
#END


# Web-application routing START
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template(
        "index.html"
    )

@app.route("/result", methods=["GET"])
def result():

    if request.args.get("updoot") == '1':   # route if updoot is clicked
        pet = request.args.get("pet")
        add_updoot(pet)
        global data                         # show the user the same page once upvotes clicked
        return render_template(             # so use data variable from previous load   
            "result.html", data=data)

    gender = request.args.get("gender")    # Store all get requests in variables
    animal = request.args.get("animal")
    colour = request.args.get("colour")    # the current input the user has
    name = request.args.get("name")         
    sort_flag = request.args.get("sort")

    if  request.args.get("auto") == '1':   # route if autocomplete is requested
        names, colours = get_auto_sugg(name, colour)  # get arrays of suggestions from current user input
        
        if colour == '' and name == '':    # avoid autosuggesting whole dataset when searching for ""
            return render_template( 
                "index.html", names=[], colours=[]) #TODO resolve blank inputs inside get_auto_sugg function instead of here
        
        elif colour == '':
            return render_template(
                "index.html", names=names, colours=[])
        
        elif name == '':
            return render_template(
                "index.html", names=[], colours=colours)
        
        return render_template(
            "index.html", names=names, colours=colours
        )

    data = search(colour, gender, name, animal, sort_flag)     # route for normal requests
    return render_template(
        "result.html",
        data=data)

if __name__ == "__main__":
    app.run(debug=True)
#END
