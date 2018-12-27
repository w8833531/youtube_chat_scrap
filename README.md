## youtube_chat_scrap
### Usage
This project use to scrap youtube video comments or live chat and get user's channel localizations,give a country statistics
### python requirement 
python > 2.7
pip pipenv installed
### install
```
git clone https://github.com/w8833531/youtube_chat_scrap
cd youtube_chat_scrap
pipenv install
pipenv shell
```

### video comments channel country statistics
```
add: youtube video url that you want to static in video_id.txt file
run:  bash result.sh 
result in: result.txt file
```
### live chat country statistics
```
add: headers/params/data in live_chat_channel.
run:  bash result_live.sh
result in: result.txt file
```
### python files 
```
comments.py -- use to get multi video comments channel id to channel_id.txt file.
channel.py -- read channel_id.txt file and get channel country to country.txt file.
live_chat_channel.py -- use to get live chat channel id. see more in live_chat_channel.py file how to setting.
```