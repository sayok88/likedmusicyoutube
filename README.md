# Transfer your liked YouTube Music playlist to other playlist
Copy your liked YouTube Music to a playlist

Tested with Python>=3.8 and >=3.9

# Get started
1. Run `git clone https://github.com/mathe8/likedmusicyoutube.git`

2. Google Cloud Configuration

	- [Create a project on Google Cloud](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project)

	- After created the project, on the project dashboard create your YouTube credentials
	
	   - [Create your YouTube credentials (use option Desktop)](https://stackoverflow.com/a/52222827/2138792) (It is a link to Stack Overflow where it gets explained in detail)
	   
	- Download the JSON file (`client_secret.json` or similiar) in the same folder as the code

	- Enable YouTube Data API v3 on your Google Cloud project : https://console.developers.google.com/

3. Open `config.ini` and edit it for your needs 
    - `CLIENT_SECRET_FILE` is the name of the JSON file you downloaded from step 2
    - `DEST_PLAYLIST` is the playlist the script will put your liked songs

4. Run `pip3 install -r requirements.txt`

5. 	
	Lastly, run `python3 main.py` to make the transfer process (with ~200 songs limit)

	Or run `python3 export-txt.py` to just export a txt file with links of your liked YouTube Music, then check `playlist.txt` with the results


## Note
The YouTube-API has a request-limit, so it workes for "only" ~200 Songs per day

The export process of the txt file is not impacted by the YouTube API request limit

###### Optional

Use venv or not

By default source playlist is Youtube Music Liked playlist  
If you need to change that then replace source_play_list default value being `LM`
