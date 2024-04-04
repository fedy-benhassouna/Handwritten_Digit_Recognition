import cv2
import numpy as np
import tensorflow as tf
import tkinter as tk
from PIL import ImageTk, Image

# Load the model
model = tf.keras.models.load_model('handwrittenco.keras')

img_num = 1

# Create a new Tkinter window
window = tk.Tk()

# Function to change the image and make a prediction
def change_image():
    global img_num
    try:
        # Read the image
        img = cv2.imread(f"digits/digit{img_num}.png")[:, :, 0]

        # Invert the image
        img = np.invert(np.array([img]))

        # Make a prediction
        predictions = model.predict(img)

        # Get the predicted digit
        predicted_digit = np.argmax(predictions)

        # Print the predicted digit
        print(f"It's probably a {predicted_digit}")

        # Load an image using PIL (Python Imaging Library)
        pil_img = Image.open(f"digits/digit{img_num}.png")
        pil_img = pil_img.resize((250, 250), Image.BILINEAR) # or Image.BICUBIC, or Image.LANCZOS
        tk_img = ImageTk.PhotoImage(pil_img)

        # Update the label with the new image
        label.config(image=tk_img)
        label.image = tk_img

        # Update the title with the prediction
        window.title(f"Predicted digit ")
    except:
        print("error")
    finally:
        img_num += 1

# Load the first image
img = Image.open(f"digits/digit{img_num}.png")
img = img.resize((250, 250), Image.BILINEAR) # or Image.BICUBIC, or Image.LANCZOS
img = ImageTk.PhotoImage(img)

# Create a label and add the image to it
label = tk.Label(window, image=img)
label.image = img
label.pack()

# Create a button that changes the image when clicked
button = tk.Button(window, text="Next", command=change_image)
button.pack()

# Start the Tkinter event loop (this will keep the window open)
window.mainloop()
