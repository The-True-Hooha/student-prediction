import pandas as pd

# Load user data
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols, encoding='latin1')

# Load movie data
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols)

m_cols = ['movie_id', 'title', 'release_date']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(3), encoding='latin1')

# Perform the merges
data = pd.merge(pd.merge(ratings, users, on='user_id'), movies, on='movie_id')
data = data[['user_id', 'title', 'movie_id', 'rating']]

print("The BD has " + str(data.shape[0]) + " ratings ")
print("The BD has ", data.user_id.nunique(), " users ")
print("The BD has ", data.movie_id.nunique(), " items ")
print(data.head())

print(pd. __version__)