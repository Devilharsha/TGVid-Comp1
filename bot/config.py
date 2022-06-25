#    Copyright (c) 2021 Danish_00
#    Improved By @Shirou

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 5211097098
    OWNER = config("OWNER")
    ffmpegcode = ["-hide_banner -c:v libx265 -vf scale=1280:-2 -x265-params log-level=error:limit-sao:psy-rd=1.5:psy-rdoq=2:aq-mode=3:qcomp=0.75:ref=6:deblock=-1,-1 -pix_fmt yuv420p10 -metadata title="t.me/Somnolin" -preset medium -crf 23 -r 23.976 -map 0:v -c:a libopus -b:a 128k -cutoff 20000 -vbr on -map 0:a -c:s copy -map 0:s?"]
    THUMBNAIL = config("THUMBNAIL")
except Exception as e:
    print("Environment vars Missing! Try again!")
    print(str(e))
    exit(1)
