from faceit_data import FaceitData

API_KEY = "136f0f44-1f91-47f6-96b6-76ee3ffb7bfb"

faceit_data = FaceitData(API_KEY)

player_details = faceit_data.player_details(nickname="Zen-Master")

