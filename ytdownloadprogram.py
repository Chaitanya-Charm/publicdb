import os
from pytube import YouTube
import moviepy.editor as mve
url=input('Please Enter the Link of YouTube Video:')
allres={1:'144p',2:'240p',3:'360p',4:'480p',5:'720p',6:'1080p',7:'1440p',8:'2160p',9:'4320p'}
yt=YouTube(url)
print('Title of the Video is=',yt.title)
if yt.streams==[]:
    print("Sorry,This Video can't be downloadable using pytube module")
else:
    print('What do you want to download')
    choice=int(input('1.Video\n2.Audio\nEnter yor choice:'))
    if choice==1:
        hres=yt.streams.filter(adaptive=True).first().resolution
        print('Available Qualities for this video are')
        for i in allres:
            if allres[i]!=hres:
                print(i,':',allres[i])
            else:
                print(i,':',allres[i])
                break
        print('Choose From the above Qualities')
        res=int(input("Enter your choice:"))
        print(allres[res])
        if len(yt.streams.filter(resolution=allres[res],progressive=True))==0:
            fname=yt.title
            
            #Finding and downloading only video file
            print('Started downloading only video file...')
            print('Video File Size[approximate]= ',yt.streams.filter(resolution=allres[res]).first().filesize)
            videopath=yt.streams.filter(resolution=allres[res],subtype='webm').first().download(filename=fname+'video')
            print('Video File downloaded succssfully')
            
            #Finding and downloading only audio file
            print('Started downloding only audio file...')
            print('Audio File Size[approximate]= ',yt.streams.filter(type='audio').last().filesize)
            audiopath=yt.streams.filter(type='audio').last().download(filename=fname+'audio')
            print('Audio File downloaded Successfully')
            
            #Merging video and audio files
            print('Merging only video and only audio files')
            video=mve.VideoFileClip(videopath)
            audio=mve.AudioFileClip(audiopath)
            final_clip=video.set_audio(audio)
            
            #Final Video(video+Audio) is stored in our machine 
            final_clip.write_videofile(videopath.split('.')[0]+'.mp4')
            
            #Removing temporary video and audio
            os.remove(videopath)
            os.remove(audiopath)
        else:
            print('Started downloading video file(video+audio)...')
            print('Video File Size[approximate]= ',yt.streams.filter(resolution=allres[res],progressive=True).first().filesize)
            videopath=yt.streams.filter(resolution=allres[res],progressive=True).first().download()
            os.replace(videopath,videopath.split('.')[0]+'.mp4')
    elif choice==2:
        print('Started downloading audio file...')
        print('Audio File Size[approximate]= ',yt.streams.filter(type='audio').last().filesize)
        videopath=yt.streams.filter(type='audio').last().download()
        os.replace(videopath,videopath.split('.')[0]+'.mp3')
        print('Audio file downloaded successfully')
    else:
        print('Invalid Choice')