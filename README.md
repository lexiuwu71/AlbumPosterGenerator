# AlbumPosterGenerator
A few Python script using Pillow that generates an album poster using local files! (Heavily inspired by @elliotjarnit's project of the same name)

ill update the readme later :P

run the script and select the folder for your album

the first png or jpg in the folder will be the cover art
then in alphabetical order it will select music so for example this works

```
'Car Seat Headrest - Twin Fantasy - 01 My Boy (Twin Fantasy).flac'
'Car Seat Headrest - Twin Fantasy - 02 Beach Life-In-Death.flac'
'Car Seat Headrest - Twin Fantasy - 03 Stop Smoking (We Love You).flac'
'Car Seat Headrest - Twin Fantasy - 04 Sober to Death.flac'
'Car Seat Headrest - Twin Fantasy - 05 Nervous Young Inhumans.flac'
'Car Seat Headrest - Twin Fantasy - 06 Bodys.flac'
'Car Seat Headrest - Twin Fantasy - 07 Cute Thing.flac'
'Car Seat Headrest - Twin Fantasy - 08 High to Death.flac'
'Car Seat Headrest - Twin Fantasy - 09 Famous Prophets (Stars).flac'
'Car Seat Headrest - Twin Fantasy - 10 Twin Fantasy (Those Boys).flac'
'Car Seat Headrest - Twin Fantasy.jpg'
 cover.bmp
```

or

```
01 My Boy (Twin Fantasy).flac'
02 Beach Life-In-Death.flac'
03 Stop Smoking (We Love You).flac'
04 Sober to Death.flac'
05 Nervous Young Inhumans.flac'
06 Bodys.flac'
07 Cute Thing.flac'
08 High to Death.flac'
09 Famous Prophets (Stars).flac'
10 Twin Fantasy (Those Boys).flac'
Car Seat Headrest - Twin Fantasy.jpg'
cover.bmp
```

or

```
01.flac
02.flac
03.flac
04.flac
05.flac
05.flac
06.flac
07.flac
08.flac
09.flac
10.flac
idk.jpg
```

as long as they appear in order in your file manager/ls, you'll be good

then make sure they have metadata

release year (it will choose the most common)
artist and album artist (you dont have to have album artist, it will just chose the most common artist)
album name (it will choose the most common)

again it searches for the first jpg or png in the folder, it will NOT use embeded art