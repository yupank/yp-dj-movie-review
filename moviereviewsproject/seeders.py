from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry 
from movie.models import Movie

@SeederRegistry.register
class MovieSeeder(seeders.CSVFileModelSeeder):
    model = Movie
    csv_file_path = './seeders_data/movies_sd_1.csv'
    