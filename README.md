# Handwritten_Digit_Recognition

This project demonstrates how to create a simple application for recognizing handwritten digits using a convolutional neural network (CNN) model trained with TensorFlow. The application allows the user to view images of handwritten digits and predicts the digit shown in each image.


## Usage

1. Train the model by running the `train_model.py` script. This will train the model using the MNIST dataset and save the trained model as `handwrittenco.keras`.

2. Run the `predict_digit.py` script to start the application. This will open a Tkinter window showing an image of a handwritten digit. Click the "Next" button to change the image and see the model's prediction for each digit.

## Files

- `train_model.py`: Script for training the CNN model using the MNIST dataset and saving the trained model.
- `predict_digit.py`: Script for running the Tkinter application to predict handwritten digits.
- `digits/`: Directory containing images of handwritten digits used for prediction.

## Acknowledgements

The model architecture and training code are based on the TensorFlow tutorial for handwritten digit recognition.

