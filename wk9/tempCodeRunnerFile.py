songs = input("Enter song titles separated by comma: ").split(",")

for i in range(len(songs)):
    songs[i] = songs[i].strip()

songs.sort()

print("Sorted playlist:", songs)