import speedtest

class InternetSpeed:

    def DownloadUpload(self):
        sp = speedtest.Speedtest()
        sp.get_servers()
      
        down = str(round(sp.download()/(10**6),3))+" Mbps"
        print("Download Internet Speed : ",down)

        upload = str(round(sp.upload()/(10**6),3))+" Mbps"
        print("Upload Internet Speed : ",upload)

      
speed =  InternetSpeed()
print()
speed.DownloadUpload()  # Get download / uplaod  speed 