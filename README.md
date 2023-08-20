# Movie-Recommender-System


https://github.com/Findcoding/Movie-Recommender-System/assets/69085143/74b89f1d-fc61-491e-8078-41c25478bc4f


<!-- ![Home](https://github.com/Findcoding/Movie-Recommender-System/assets/69085143/402066ea-d069-4aed-98a6-ad72069b9f37) -->

## Create Virtual Environment
- Download virtual Environment Module
```
pip install virtualenv
```
- Locate base directory and use this command to create virtual environment
```
virtualenv <environment_name>
```
## Download Kaggle Dataset
- Download [dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), and then put all .csv files inside **Dataset** folder
## Run Command to install required Python Module
```sh
pip install -r requirements.txt
```
## To run App use this command
```sh
python manage.py runserver
```

## Implementation 
- **Simple Recommender:** The Simple Recommender offers generalized recommnendations to every user based on movie popularity and (sometimes) genre. The basic idea behind this recommender is that movies that are more popular and more critically acclaimed will have a higher probability of being liked by the average audience. This model does not give personalized recommendations based on the user. The implementation of this model is extremely trivial. All you have to do is sort our movies based on ratings and popularity and display the top movies of our list. As an added step, we can pass in a genre argument to get the top movies of a particular genre.
![Simple Recommender]![image](https://github.com/niranjanchauhan/movie-recommend/assets/56686095/501a8db2-7b39-4ccc-ae52-35ba7a43e5a8)


- **Content Based Recommender:** The recommender we built in the previous section suffers some severe limitations. For one, it gives the same recommendation to everyone, regardless of the user's personal taste. If a person who loves romantic movies (and hates action) were to look at our Top 15 Chart, s/he wouldn't probably like most of the movies. If s/he were to go one step further and look at our charts by genre, s/he wouldn't still be getting the best recommendations.

For instance, consider a person who loves Dilwale Dulhania Le Jayenge, My Name is Khan and Kabhi Khushi Kabhi Gham. One inference we can obtain is that the person loves the actor Shahrukh Khan and the director Karan Johar. Even if s/he were to access the romance chart, s/he wouldn't find these as the top recommendations.

To personalise our recommendations more, we build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine.
![Content Based Recommender]![image](https://github.com/niranjanchauhan/movie-recommend/assets/56686095/6a01f007-36a0-4277-9efb-5762b8e8cb9b)


- **Hybrid Recommender:** In this section, We build a simple hybrid recommender that brings together techniques we have implemented in the content based and collaborative filter based engines. 

This is how it will work:
 _Input:_ User ID and the Title of a Movie
 _Output:_ Similar movies sorted on the basis of expected ratings by that particular user.
 ![Hybrid Recommender]![image](https://github.com/niranjanchauhan/movie-recommend/assets/56686095/1359f1ff-5a92-44be-9e9d-5030efe56908)



