from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="c6e9c56c25874351b4815f1c6a4e79a8",
        client_secret="6da5fcdfe4df4ee586b1309975fd7d83",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

print(f"user_id: {user_id}")

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"add ok: {uri}")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")