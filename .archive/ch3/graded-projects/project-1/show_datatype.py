import pandas as pd

df = pd.read_csv('./data/spotify_albums.csv', nrows=2)
for dtype in df.dtypes.iteritems():
    print(dtype)