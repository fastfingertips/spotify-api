from spotifyClient import *

client_id = '?CLIENT_ID?'
client_secret = '?CLIENT_SECRET?'

spotify = SpotifyAPI(client_id, client_secret)
spotify.search({"track": "Feel Real Pretty"}, search_type="track")

