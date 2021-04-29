# Transfer your liked youtube music playlist to other playlist
Copy your liked youtube music to a playlist

Create your youtube credentials following(use option Desktop)
https://stackoverflow.com/a/52222827/2138792

Also enable youtube data api v3 on https://console.developers.google.com/

keep file in same folder as code

Replace file name in line 25 `client_secrets_file`

Get your destination playlist id 
https://www.youtube.com/playlist?list=[PLAYLIST_ID]

replace it in `destination_play_list`

###### **optional**

###### By default source playlist is Youtube Music Liked music playlist

###### If you need to change that then replace `source_play_list` default value being `LM`

Use Python>=3.6


` pip3 install -r requirements.txt`

Run

`python3 main.py`


## Note
The YouTube-API has a request-limit, so it worked for "only" ~200 Songs
