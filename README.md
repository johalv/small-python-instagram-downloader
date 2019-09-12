# small-python-instagram-downloader

Simple yet, _hopefully_, powerful
---------------------

This is a very simple, **and work still in progress**, downloader for Instagram photos. It gives a "manual" feeling of downloading the highest resolution picture from a chosen amount of posts.


What and why?
---------------------

This is just me trying what **_BeautifulSoup_** together with **_tkinter_** and **_wget_** can accomplish.

The idea behind it is that the software simulates a keyboard command that takes the user to the next picture, until the downloader is finished.

1. Start off with chosing an Instagram **post**
2. Run the program
3. Chose how many pictures you want to save
4. Go to your active Instagram tab in your browser
5. Stay in the browser not touching your keyboard
6. Done!

### Things that currently __do not__ work and need more thought:

- A "multipost" saves only the last photo
- When browsing a video, the thumbnail will be downloaded
- Sometimes the timing is off, resulting in a duplicates
