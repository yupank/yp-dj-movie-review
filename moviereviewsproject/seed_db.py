import psycopg2 
import csv
import json

# preparing and writing seeding data - the django_seeding does not work as expected - seeders appear in admin but data were not updated
# seed_data = [
#     ['title', 'description', 'image', 'url']
# ]
# for idx in range(11,16):
#       seed_data.append([idx, f'Movie_{idx}', f'Description_{idx}', 'movie/images/movie.png', ' '])

# with open('./seeders_data/movies_sd_1.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(seed_data)

conn = psycopg2.connect(database ="yp_movies_app", user = "lssgav", 
                        host = "localhost", port = "5432") 

cur = conn.cursor() 

# external database seeding 
movies = [f"{idx}, 'Movie_{idx}', 'Bad_movie_description_{idx}', 'movie/images/movie.png', ''" for idx in range(21,23) ]
mov_query = f"INSERT into movie_movie (id, title, description, image, url) VALUES"
for mov in movies:
    mov_query += f" ({mov}),"
cur.execute(mov_query[0:-1]) 

# reading an external postgress db
query = "SELECT id, title, description, image, url from movie_movie;"
cur.execute(query) 
rows = cur.fetchall() 
# for row in rows: 
# 	print(row[0], row[1], row[2], row[3]) 

# preparing the dict with model's data for fixture

# Data to be written
fixture_data = [
	{
	    "model": "movie.Movie",
        "pk": row[0],
        "fields": {
        "title": row[1],
        "description": row[2],
		"image": row[3],
		"url": row[4]
        }
    } for row in rows
]
print(fixture_data)
with open("./seeders_data/movies_sd_2.json", "w") as outfile:
	json.dump(fixture_data, outfile)
     
conn.close()

