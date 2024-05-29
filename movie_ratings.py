from flask import Flask, Response
import pandas as pd
import io

app = Flask(__name__)

# Load data from CSV at startup
def load_movie_ratings_data(filename):
    return pd.read_csv(filename)

# Load movie ratings data
movie_ratings_data = load_movie_ratings_data('movie_ratings.csv')

@app.route('/')
def home():
    return """
    Welcome to the Movie Ratings API!
    Use /movie_ratings to view all movie ratings data.
    """

@app.route('/movie_ratings')
def get_movie_ratings():
    # Convert the DataFrame to CSV
    csv_data = movie_ratings_data.to_csv(index=False)
    
    # Create a response object and set the appropriate headers for CSV
    response = Response(
        csv_data,
        mimetype='text/csv',
        headers={"Content-disposition": "attachment; filename=movie_ratings.csv"}
    )
    
    return response

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
