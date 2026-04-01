
# =====================================================
import subprocess
import ffmpeg
import time
print("\033[7;33m""PLEASE FOLLOW THE STEPS CAREFULLY:"+"\033[0m""\n1:DOWNLOAD THE ffmpeg release built version--https://www.gyan.dev/ffmpeg/builds/--\n2:COPY THE PATH AND PASTE BELOW\n3:LAST FOLDER OF PATH MUST BE *bin*\n")
time=time.sleep(1)
path_ffmpeg=input("TYPE PATH OF ffmpeg EXAMPLE[C:/ffmpeg/bin]:\n")
while True:
    try:
        url = input("ENTER URL:\n")
        result = subprocess.run(
            ["yt-dlp", "-F", url],
            capture_output=True,
            text=True
        )
        check=(result.stdout)
        print(check)
        # print("PLEASE SELECT THE TYPE")
        check=input("1:GET BEST QUALITY AUDIO/VIDEO\n2:CUSTOM SETTINGS\n")
        if check =="1":
                try:
                  subprocess.run(["yt-dlp","-f","bv*+ba/b",
                                  "--remux-video" ,"mp4",
                                 "--ffmpeg-location",rf"{path_ffmpeg}",
                                 "--js-runtimes",
                                 "--remote-components", "ejs:github",url])
                except:
                  print("PLEASE TRY AGAIN")
        if check =="2":
            pick=input("TYPE THE FORMAT-ID:")
            details1=input("\033[7;31m"+"PLEASE SELECT THE FILE TYPE:"+"\033[0m""\n1:NEED AUDIO IN mp3\n2:NEED VIDEO IN mp4\n3:NO CHANGE ORIGINAL\n")



            if details1 =="1":
                try:
                    subprocess.run([    
                        "yt-dlp",
                        "-f", pick,
                        "-x",
                        "--audio-format" , "mp3",
                        "--ffmpeg-location",rf"{path_ffmpeg}",
                        "--js-runtimes","node",
                        # "--remote-components", "ejs:github",
                        url])
                    print("\033[7;32m"+"DOWNLOAD COMPLETE"+"\033[0m")
                    
                except:
                    print("INVALID FORMAT ID [only audio]")
            elif details1 =="2":
                try:
                    subprocess.run([    
                        "yt-dlp",
                        "-f", pick,
                        # "-x",
                        # "--audio-format" , "mp3"
                        "--remux-video" ,"mp4",
                        "--ffmpeg-location",rf"{path_ffmpeg}",
                        "--js-runtimes",
                        "--remote-components", "ejs:github",
                        url])
                    print("DOWNLOAD COMPLETE")
                except:
                    print("INVALID FORMAT ID [only video]")
            elif details1 =="3":
                try:
                        subprocess.run([ 
                        "yt-dlp",
                        "-f", pick,
                        "--ffmpeg-location",rf"{path_ffmpeg}",
                        "--js-runtimes",
                        "--remote-components", "ejs:github",
                        url])
                        print("DOWNLOAD COMPLETE")
                except:
                    print("FORMAT NOT AVAILABLE")
    except:
             print("SYSTEM ERROR PLEASE TRY AGAIN")
# =======================================================
# https://music.youtube.com/watch?v=Heo-7o5LRJ8&si=-dG77i4FcNEjsFg6
# C:/ffmpeg/bin/ffmpeg-8.1 release/bin
# https://www.facebook.com/share/v/181qtGH937/
# https://www.tiktok.com/@funnyvideo.s41/video/7599551306751069470?is_from_webapp=1&sender_device=pc