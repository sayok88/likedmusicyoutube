# Transfer your liked youtube music playlist to other playlist
Copy your liked youtube music to a playlist


#
Create your youtube credentials following(use option Desktop)
https://stackoverflow.com/a/52222827/2138792

Also enable youtube data api v3 on https://console.developers.google.com/

keep file in same folder as code



# Get started
1. run `git clone https://github.com/mawoka-myblock/likedmusicyoutube.git`

2. [Create your YouTube credentials (use option Desktop)](https://stackoverflow.com/a/52222827/2138792) (It is a link to Stackoverflow where it gets explained in detail)

3. enable YouTube data api v3 on https://console.developers.google.com/
4. Download the file in the same folder as the code.

5. Open `config.ini` and edit it for your needs. 
    - `CLIENT_SECRET_FILE` is the name of the file you downloaded from step 2
    - `DEST_PLAYLIST` is the playlist the script will put your liked songs

6. run `pip3 install -r requirements.txt`

7. Lastly, run `python3 main.py`


## Note
The YouTube-API has a request-limit, so it workes for "only" ~200 Songs per day.
