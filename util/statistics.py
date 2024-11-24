import os

from util.download import CACHE_DIR, DOWNLOAD_DIR, ZIP_DIR


async def totalCaches():
    song_count = len(os.listdir(DOWNLOAD_DIR)) if os.path.exists(DOWNLOAD_DIR) else 0
    playlist_count = len(os.listdir(ZIP_DIR)) if os.path.exists(ZIP_DIR) else 0
    cache_count = len(os.listdir(CACHE_DIR)) if os.path.exists(CACHE_DIR) else 0
    return song_count + playlist_count + cache_count


async def totalSongs():
    return len(os.listdir(DOWNLOAD_DIR)) if os.path.exists(DOWNLOAD_DIR) else 0


async def totalPlaylists():
    return len(os.listdir(ZIP_DIR)) if os.path.exists(ZIP_DIR) else 0


async def totalSongData():
    return len(os.listdir(CACHE_DIR)) if os.path.exists(CACHE_DIR) else 0


async def totalStorage():
    song_size = (
        sum(os.path.getsize(f"{DOWNLOAD_DIR}/{f}") for f in os.listdir(DOWNLOAD_DIR))
        if os.path.exists(DOWNLOAD_DIR)
        else 0
    )
    playlist_size = (
        sum(os.path.getsize(f"{ZIP_DIR}/{f}") for f in os.listdir(ZIP_DIR))
        if os.path.exists(ZIP_DIR)
        else 0
    )
    cache_size = (
        sum(os.path.getsize(f"{CACHE_DIR}/{f}") for f in os.listdir(CACHE_DIR))
        if os.path.exists(CACHE_DIR)
        else 0
    )
    return song_size + playlist_size + cache_size


async def songStorage():
    song_size = (
        sum(os.path.getsize(f"{DOWNLOAD_DIR}/{f}") for f in os.listdir(DOWNLOAD_DIR))
        if os.path.exists(DOWNLOAD_DIR)
        else 0
    )
    return song_size


async def playlistStorage():
    playlist_size = (
        sum(os.path.getsize(f"{ZIP_DIR}/{f}") for f in os.listdir(ZIP_DIR))
        if os.path.exists(ZIP_DIR)
        else 0
    )
    return playlist_size


async def cacheStorage():
    cache_size = (
        sum(os.path.getsize(f"{CACHE_DIR}/{f}") for f in os.listdir(CACHE_DIR))
        if os.path.exists(CACHE_DIR)
        else 0
    )
    return cache_size
