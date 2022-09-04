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