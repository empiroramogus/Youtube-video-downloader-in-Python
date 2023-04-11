import pytube

link = input("link the video: ")
yt = pytube.YouTube(link)
choice = input("choice "
               "[1]high quality "
               "[2]low quality "
               "[3]sound only: ")
if choice=="1" :
    yt.streams.get_highest_resolution().download()
elif choice=="2" :
    yt.streams.get_lowest_resolution().download()
elif choice=="3" :
    yt.streams.get_audio_only().download()
else:
    print("error")
print("the video downloaded")
a = input("click anything to close")