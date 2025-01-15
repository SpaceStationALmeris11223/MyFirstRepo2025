#this function takes a list of ingredients and simulates making a sandwich
def build_sandwich(ingredients): #defines(creates) a function
    if not ingredients:
        print("You need to choose some ingredients!")
        return


    print("Let's make a sandwich!")
    print("First, we grab some bread...")

    #loop though each ingredient and add it to the sandwich
    for i, ingredient in enumerate(ingredients, 1):
        print(f"Adding {ingredient}....")
    
    print("and top it with bread")
    #join all ingredients and add it to the sandwihc
    print(f"\nCongrats! You made a {' and ' .join(ingredients)} sandwich")

#Main function that handles user input and error catching
def main():
    try:
        print("Welcome to the Sandwich Maker!")

        #Get ingredeints from user as a comma sepreated string
        ingredients_input = input("Enter the ingredients that you plan to make the sandwich with (seperated by commas) ")

        #conver input into a string to a list
        #1. Split string at commas
        #2 Remove extra whitespace from each ingredient
        ingredients = [i.strip() for i in ingredients_input.split(",")]

#call the sandwich building function with our list of ingredients
        build_sandwich(ingredients)

#Error catcher
    except Exception as e:
        print("oops somthing went wrong! Let's try again");
#Standard pthin
if __name__ =="__main__":
    main()