import os
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# Set the path to the folder containing your pictures
pictures_folder = "photoprism/photos"

# Get a list of all the image files in the folder
image_files = [f for f in os.listdir(pictures_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

# Create a Tkinter window
window = tk.Tk()
window.title("PhotoFrame")
window.attributes("-fullscreen", True)

# Create a label to display the images
image_label = tk.Label(window, bg="black")
image_label.pack(fill=tk.BOTH, expand=True)

# Function to update the image
def update_image():
    # Choose a random image from the list
    image_file = random.choice(image_files)

    # Open the image using PIL
    image = Image.open(os.path.join(pictures_folder, image_file))

    # Resize the image to fit the window
    #image = image.resize((window.winfo_width(), window.winfo_height()))
    image = ImageOps.contain(image, (window.winfo_width(), window.winfo_height()))

    # Convert the image to Tkinter format
    tk_image = ImageTk.PhotoImage(image)

    # Update the label with the new image
    image_label.configure(image=tk_image)
    image_label.image = tk_image

    # Schedule the next image update after 5 seconds
    window.after(5000, update_image)

# Start the slideshow
update_image()

# Run the Tkinter event loop
window.mainloop()