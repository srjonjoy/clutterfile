import os
files=os.listdir("clutter_filr") #creates a list of your png files
i=1
for file in files:
    if file.endswith(".png"): #for only png file i get and i work with
        # print(file)
        os.rename(f"clutter_filr/{file}",f"clutter_filr/{i}.png") #rename method of os value
        i=i+1
        print(file)