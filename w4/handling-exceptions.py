# learnTogether Week 4

# Handling exceptions: To use multiple except clauses.
# Slice the pizza!
pizza_mass = 350.0 #(grams)
while True:
    try:
        num_slices = int(input("\nServe the pizza as how many slices? "))
        slice_mass = pizza_mass / num_slices
    # Input can not be interpreted as an int.
    except ValueError:
        print("Please enter an integer.")
        continue
    # Input was zero.
    except ZeroDivisionError:
        print("Can not serve it as zero slices.")
        continue
    # Input was negative.
    else:
        if num_slices < 0: 
            print("Can not serve a negative number of slices.")
            continue
    break

print("The mass of each pizza slice is {:0.2f} grams.".format(slice_mass))