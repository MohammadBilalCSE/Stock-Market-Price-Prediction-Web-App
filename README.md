# SMPRADE 📊📈

## Project Overview
**SMPRADE - Final Year Project** is a final year project that combines finance, machine learning, and real-time data analysis. It provides a platform to track stock prices, perform financial analysis, predict stock trends, and visualize data through interactive charts. It also includes features like user authentication, profile management, and social interaction through posts and news fetching.



## 🚀 Technologies Used
- **Django** 🐍: Backend framework for handling server-side logic and user authentication.
- **Python** 🐍: Core programming language used for backend and machine learning models.
- **HTML5** 🌐: Structure and layout of web pages.
- **CSS3** 🎨: Styling the web pages to create a clean and modern user interface.
- **JavaScript** 📜: Enhancing user experience and handling client-side interactivity.
- **Firebase Authentication** 🔒: Secure user authentication.
- **Firebase Database** 💾: Storing user data and posts.
- **Plotly** 📉: Data visualization library used for generating interactive stock charts.
- **yfinance** 📈: Fetching stock market data from Yahoo Finance.
- **Scikit-learn** 🤖: Implementing machine learning models for stock prediction.
- **NewsAPI** 📰: Fetching real-time news articles.



## Features 🎉

### 🔑 Authentication
- **Login/Signup**: Secure login and signup system with Firebase Authentication.
- **Profile Management**: Upload and update profile pictures.

### 📈 Stock Data Visualization
- Real-time stock price charts and financial data using **Plotly**.
- **Candlestick charts** for stock price visualization.
- Prediction of stock trends using machine learning with **scikit-learn**.

### 📰 News Fetching
- Fetch and display the latest business news using **NewsAPI**.
- Ability to search news articles based on user input.

### 📚 Data Science Features
- **Stock Prediction**: Use of machine learning models to predict future stock prices based on historical data.
- **Data Analysis**: Fetch real-time and historical stock data, analyze it, and visualize the results.

### 💬 Social Features
- **Post Creation**: Users can create and share posts.
- **Delete Post**: Option to delete posts.


###  Screenshots
 - ![Homepage] : (smpproject/media/Homepage-img.png)
 - ![Price Prediction Page] : (smpproject/media/Prediction-img.png)




## Installation

To run the SMPRADE project locally, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher
- Firebase account for authentication setup
- Plotly
- Scikit-learn
- yfinance
- Requests library

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohammadBilalCSE/Stock-Market-Price-Prediction-Web-App.git
   cd Stock-Market-Price-Prediction-Web-App
   ```

2. **Create a virtual environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Firebase Authentication**:

   - Go to the Firebase Console and create a new project.
   - Enable Firebase Authentication and create an API key.
   - Add Firebase settings in your `settings.py`.

5. **Run the migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to see the project in action.



## Future Enhancements

- Adding more machine learning models for better stock prediction accuracy.
- Supporting additional financial APIs for more in-depth market analysis.
- Implementing user notifications for stock price alerts.

Happy Coding !!!
