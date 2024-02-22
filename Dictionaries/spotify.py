playlist = {
    "Title":"Calms",
    "Author":"Supeetha",
    "songs":[
        {"title":"flowers","artist":["miley"],"duration":3.5},
        {"title":"lover","artist":["taylor","justin"],"duration":5.5}
        
        ]
    }

#entire playtime:
duration = 0
for song in playlist["songs"]:
    #print(song["title"])
    duration = duration + song["duration"]
    
print(duration)

print(playlist.get("Title"))