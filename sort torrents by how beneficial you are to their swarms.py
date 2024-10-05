from os import popen
import qbittorrentapi
import time
torrents = {}

# qbittorrent path is hardcoded, it's fine for my use
popen("C:\\Program Files\\qBittorrent\\qbittorrent.exe")
conn_info = dict(
    host="localhost",
    port=8080)
qb = qbittorrentapi.Client(**conn_info)
time.sleep(5)

for torrent in qb.torrents_info():
    try:
        impact = (torrent.uploaded / (time.time() - torrent.completion_on)) / torrent.num_complete
    except ZeroDivisionError: 
        if torrent.uploaded:
            impact = float('inf')
        else:
            impact = 0
    torrents[torrent.name] = impact
for impacts in sorted(torrents, key=torrents.get):
    print(impacts, round(torrents[impacts], 2))

qb.app_shutdown()