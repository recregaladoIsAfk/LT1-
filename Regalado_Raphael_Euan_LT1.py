notebook_count = int(input(print("What is the total number of notebooks? ")))
box_count = int(input(print("How many notebooks can each box hold? ")))

#First, we ask the user for the values, in this case, the number of notebooks and boxes.

if box_count < notebook_count:
    box_total = print("The total number of boxes that can be filled is ", notebook_count // box_count)
    leftover = print("And there will be ", notebook_count % box_count, "left over.")
    
#If the total number of notebooks is greater than the amoyunt of boxes, it wll display the 
#total number of boxes that can hold the amount of notebooks, if there is extra, it will go to the loose pack.

elif box_count > notebook_count:
    print("It cannot fill a full box, so", notebook_count, "will go to the loose pack.")
    
#If not, then it wll say so and the notebooks will go the the lose pack as well.