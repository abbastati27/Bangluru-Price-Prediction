# Bangalore Home Price Prediction
This is a web application that predicts the price of a home in Bangalore based on various input features such as location, size, number of bedrooms, and bathrooms. The application uses a machine learning model to provide the predicted price in INR (Indian Rupees).

# Features
1. Location Selection: Choose the location of the property from a dropdown.
2. Size (in sqft): Enter the size of the property in square feet.
3. Number of Bedrooms: Enter the number of bedrooms in the property.
4. Number of Bathrooms: Enter the number of bathrooms in the property.
5. Price Prediction: Get the predicted price for the given input details.

# Machine Learning Model
The application utilizes a Linear Regression model to predict home prices based on various features of the property. The model is trained using historical property data from Bangalore, which includes details such as location, size, number of bedrooms, and bathrooms. Here’s a summary of how the model was created:

# Data Preprocessing:
1. Removed unnecessary columns such as area_type, availability, and society.
2. Converted the size column to extract the number of bedrooms (bhk).
3. Cleaned up the total_sqft column to handle non-numeric values and incorrect data ranges.
4. Handled missing values and outliers in the dataset to ensure the accuracy of the model.

# Feature Engineering:
1. Created new features like price per sqft to better understand the pricing dynamics.
2. Encoded categorical features (e.g., location) using one-hot encoding to convert them into numerical format.

# Model Training:
1. The dataset was split into training and testing sets using an 80-20 split ratio.
2. A Linear Regression model was trained on the features to predict the home price.

# Model Evaluation:
The model’s accuracy was evaluated using the R-squared score, which measures how well the model fits the data.

# Model Serialization:
The trained model is saved using pickle for easy loading and inference.

# Technologies Used
1. Backend: Python, Flask
2. Machine Learning: Scikit-learn (Linear Regression), Pickle
3. Frontend: HTML, CSS, Bootstrap
4. Deployment: Local server for testing, can be hosted on any cloud platform for production.

# Installation Instructions
1. Clone the repository: git clone https://github.com/abbastati27/Bangluru-Price-Prediction.git
2. Navigate to the project directory: cd Bangluru-Price-Prediction
3. Install the required dependencies: pip install -r requirements.txt
4. Run the Flask server: python app.py
5. Open the index.html file in the browser.

# How It Works
1. The model is pre-trained on historical property price data, with features like location, size, number of bedrooms, and bathrooms.
2. When the user enters the property details, the input is processed, and the model predicts the price.
3. The predicted price is then displayed in INR format.

# Model File
1. The trained machine learning model is stored in a pickle file called project.pickle.
2. A JSON file columns.json contains the list of columns used in the model for reference.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

