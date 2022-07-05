#    Copyright (c) 2021 Danish_00
#    Improved By @Shirou

from decouple import config

try:
    APP_ID = "7405235"
    API_HASH = "5c9541eefe8452186e9649e2effc1f3f"
    BOT_TOKEN = "5534205730:AAGqKRKCrvmG_T37Q-jNUMDHZqmxQc0QYeg"
    DEV = 1615607413
    OWNER = "1164918935"
    ffmpegcode = ["-preset veryfast -c:v libx265 -s 1280:-2 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By DaddyCooL' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 128k -vbr on -c:s copy -map 0 threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/4583a984bc40a98fa9154.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
