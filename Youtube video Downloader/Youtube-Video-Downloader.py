from pytube import YouTube

lk = input("enter link : ")

yt = YouTube(lk)

ys = yt.streams.get_highest_resolution()

print("downloading ... ")

ys.download()

print("downloades")
