from PIL import Image

print("Enter the path to the image you want to use:")
image_path = input().strip().strip('"').strip("'")

inputted_image = Image.open(image_path)
inputted_image = inputted_image.convert("RGB")
# print('Successfully loaded image!')


new_width = 200
new_height = int((inputted_image.height / inputted_image.width) * new_width * 0.55)
inputted_image = inputted_image.resize((new_width, new_height))


# print(f'Image size: {inputted_image.width} x {inputted_image.height}')
# print(f'Iterating through pixel contents: {inputted_image.get_flattened_data()}')


# Gets data of every pixel in image as tuples (R, G, B) 
pixel_data = inputted_image.get_flattened_data()

# Create empty list for all the RGB tuple values converted to brightness values
brightness_values_list = []

# Use for loop to calcualte average brightness of tuples using the formula (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
# Create new variable 'pixel' and assign it to every tuple in pixel_data

for pixel in pixel_data: # For every tuple/pixel in pixel_data
    
    # Gets the R, G and B values of every pixel, adds them and stores the result in added_rgb_values
    # Here, (int(pixel[0]) gets the value of R in every pixel and converts it to an integer value
    
    brightness_values = ((0.2126 * (int(pixel[0]))) + (0.7152 * (int(pixel[1]))) + (0.0722 * (int(pixel[2])))) # formula (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    
    # Appends brightness_values onto the list created earlier 
    brightness_values_list.append(int(brightness_values))
    # For loop repeats for every pixel in image

# Now the list of brightness values is ready and we have the average brightness value of every pixel in the image


# Prepare a list of ASCII characters, from low to high density
ASCII_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 characters 
ASCII_characters = list(ASCII_characters)

characters_printed = 0

for brightness in brightness_values_list: # For every brightness value in the image
    
    # The range of brightness is 0-255
    # We divide brightness by 255 to make it a percentage value and then round it to an integer 
    
    # Since python starts counting from 0 we take the number of ASCII characters and minus 1
    index = int((brightness / 255) * (len(ASCII_characters) - 1))
    
    # Print the ASCII character
    print(ASCII_characters[index], end="")
    characters_printed += 1

    # Once the loop reaches the image's width start a new line
    if characters_printed == inputted_image.width:
        print()
        characters_printed = 0

# input() so when user runs .exe file it doesnt close immendiately
input("Press any key to quit...")