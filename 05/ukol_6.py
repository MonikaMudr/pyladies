song_lyrics = '''Just a young gun with a quick fuse
I was uptight, wanna let loose
I was dreaming of bigger things
And wanna leave my own life behind
Not a yes sir, not a follower
Fit the box, fit the mold
Have a seat in the foyer, take a number
I was lightning before the thunder
Thunder, thunder
Thunder, thun', thunder
Thun-thun-thunder, thunder, thunder
Thunder, thun', thunder
Thun-thun-thunder, thunder
Thunder, feel the thunder
Lightning and the thunder
Thunder, feel the thunder
Lightning and the thunder
Thunder, thunder
Thunder
Kids were laughing in my classes
While I was scheming for the masses
Who do you think you are?
Dreaming 'bout being a big star
They say you're basic, they say you're easy
You're always riding in the back seat
Now I'm smiling from the stage while
You were clapping in the nose bleeds'''

def count_letter(song_lyrics, letter):
    count = 0
    for i in song_lyrics:
        if i.lower() == letter:
         count += 1
    print(count)

count_letter(song_lyrics, "k")