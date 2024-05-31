# Access Method

## Methodology

### Data Gathering
- **IMDb, TMDb & Metacritic**: Collected the ratings through their public APIs and web crawling.

### Data Integration
- Standardized the collected movie rating data across different sources.
- Normalized the ratings to a standard 0-10 scale.

### Security
- Require user ID to access to the API dataset.

### Update
- The database should have monthly updates as new ratings/movies come in from the resources to ensure data accuracy.
- Clarify the information resources and details to maintain transparency.

## Access

### View the webpage visual
- User do not need to create any account to have an overview on the homepage with movie images and ratings information.

### User Registration
- However, users will need to create an account through their own email to gain access to API access for more detail data.

### Navigation
- After login, the user can download the movie rating dataset.

### Data Retrieval
- Users can download the database for movie_ratings.csv by accesing the API

## New Data Structure

- **movie_id (integer)**: Unique identifier for each movie.
- **Title (string)**: Movie name.
- **Release_year (integer)**: Year of movie release.
- **Director (string)**: Name of the movie director.
- **Genres (string)**: List of movie genres.
- **IMDb_score (integer)**: Movie rating from IMDb.
- **TMDb_score (integer)**: Movie rating from TMDb.
- **Metacritic (integer)**: Movie rating from MetaCritic.
- **Average_score (float)**: Combined rating from IMDb, TMDb, and Metacritic (automatically calculated).
  

## Example

### Request <api>/moviews_rating
Response: download the dataset in csv format

(The response might not work as the flask is not running)

## Instruction to function API
1. download movie_rating.py
2. install Flask server
3. launch Flask server (export FLASK_APP=movie_ratings.py)
4. access the link provided
