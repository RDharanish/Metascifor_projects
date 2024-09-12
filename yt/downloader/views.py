# downloader/views.py
from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp
import os

def download_video(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if link:
            try:
                ydl_opts = {
                    'format': 'best', 
                    'outtmpl': 'downloads/%(title)s.%(ext)s',  
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                
                return HttpResponse("Video downloaded successfully!")
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        else:
            return HttpResponse("Please provide a valid YouTube link.")
    return render(request, 'downloader/index.html')
