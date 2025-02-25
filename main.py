#!/usr/bin/python

import sys, os
from mutagen.mp3 import MP3
from mutagen.flac import FLAC

from tkinter import filedialog
from tkinter import *

from image_maker import *

album_path = "/home/lexi/Music/Music/Bandcamp/[FLAC] (2018) Car Seat Headrest - Twin Fantasy"
use_tkinter = True

font_path_bold = "BlinkMacSystemFont/otf/BlinkMacSystemFont-Bold.otf"
font_path_med = "BlinkMacSystemFont/otf/BlinkMacSystemFont-Medium.otf"
font_path_norm = "BlinkMacSystemFont/otf/BlinkMacSystemFont-Regular.otf"
font_path_thin = "BlinkMacSystemFont/otf/BlinkMacSystemFont-Thin.otf"

def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
     
    return "%2d:%02d" % (minutes, seconds)

def most_common(lst):
    return max(set(lst), key=lst.count)

def get_album_info(album_path, use_tkinter):
    info = {}

    if use_tkinter:
        root = Tk()
        root.withdraw()
        album_path = filedialog.askdirectory()
        print(f"\n{album_path}\n")

    info["albumpath"] = album_path

    coverart = ""
    songs = []
    if os.path.exists(album_path):
        for i in sorted(os.listdir(album_path)):
            if i.upper().endswith(".JPG") or i.upper().endswith(".PNG"):
                coverart = i
            elif i.upper().endswith(".FLAC") or i.upper().endswith(".MP3"):
                songs.append(i)
            else:
                continue
    print(f"\nCover Art: {coverart}\n")
    info["coverart"] = coverart
    print(f"Songs:")
    artist = []
    date = []
    album = []
    info["songs"] = []
    for i in songs:
        try:
            if i.upper().endswith(".FLAC"):
                audio = FLAC(f"{album_path}/{i}")
            else:
                audio = MP3(f"{album_path}/{i}")

            album_artist = audio["albumartist"][0]
            if album_artist != "":
                artist.append(album_artist)
            artist.append(audio["artist"][0])

            release_date = str(audio["date"][0])
            if release_date != "":
                date.append(release_date)

            album_title = str(audio["album"][0])
            if album_title != "":
                album.append(album_title)

            print(f"{audio["title"][0]} - {convert_time(audio.info.length)}")
            info["songs"].append((audio["title"][0],convert_time(audio.info.length)))
        except Exception as e:
            print(f"[ERROR] Unrecognized File Format or smth idrk: {str(e)}")
    
    info["artist"] = most_common(artist)
    info["album"] = most_common(album)
    info["date"] = most_common(date)
    print(f"\nArtist: {info["artist"]}\nAlbum: {info["album"]}\nRelease Date: {info["date"]}\n")

    question = input("Is this correct? (Y/n): ")
    if str(question.upper()) == "N":
        print("Okay, Exiting...")
        exit()

    return info

def main():
    info = get_album_info(album_path=album_path, use_tkinter=use_tkinter)
    make_image(info, font_path_med, font_path_bold, font_path_norm, font_path_thin)

if __name__ == "__main__":
    main()