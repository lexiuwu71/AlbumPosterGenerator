from PIL import Image, ImageDraw, ImageFont

def make_image(info, fontmed, fontbold, fontnorm, fontthin):
    pad = 120
    text_pad = 10
    img = Image.new(mode="RGB", size=(1440,1920), color=(255,255,255))
    img_w, img_h = img.size

    cover = Image.open(f"{info["albumpath"]}/{info["coverart"]}", 'r')
    cover = cover.resize((img_w-pad-pad, img_w-pad-pad), Image.Resampling.LANCZOS)
    cover_w, cover_h = cover.size
    offset = ((img_w - cover_w) // 2, pad)
    img.paste(cover, offset)

    fnt = ImageFont.truetype(fontbold, 100)
    d = ImageDraw.Draw(img)
    d.text((pad+text_pad, cover_w+pad+pad), info["album"], font=fnt, fill=(0, 0, 0, 255), anchor="ls")

    fnt = ImageFont.truetype(fontmed, 50)
    _text = d.text((cover_w+pad-text_pad, cover_w+pad+pad), info["artist"], font=fnt, fill=(0, 0, 0, 255), anchor="rs")

    ascent, descent = fnt.getmetrics()
    (width, baseline), (offset_x, offset_y) = fnt.font.getsize(info["artist"])

    fnt = ImageFont.truetype(fontnorm, 50)
    d.text((cover_w+pad-text_pad, cover_w+pad+pad-ascent), info["date"], font=fnt, fill=(0, 0, 0, 255), anchor="rs")

    height = cover_w+pad+pad+(pad//4)
    shape = [(pad, height), (pad+cover_w, height)]

    line = ImageDraw.Draw(img)
    line.line(shape, fill=(0,0,0), width=11)

    if len(info["songs"]) % 2 != 0:
        mid = len(info["songs"]) // 2 + 1  # Give one more to the left column
    else:
        mid = len(info["songs"]) // 2  # Regular split

    left = info["songs"][:mid]
    right = info["songs"][mid:]

    song_layout = [left,right]
    leftcolumnlenght = len(song_layout[0])

    left_title_width = 0
    fnt = ImageFont.truetype(fontnorm, 32)
    for column, i in enumerate(song_layout):
        title_width = 0
        for idx, song in enumerate(i):
            ascent, descent = fnt.getmetrics()
            (width, baseline), (offset_x, offset_y) = fnt.font.getsize(info["songs"][(column*leftcolumnlenght)+idx][0])
            d.text((pad+((pad+left_title_width+text_pad)*column), height+(pad//4)+((ascent+10)*idx)), info["songs"][(column*leftcolumnlenght)+idx][0], font=fnt, fill=(0, 0, 0, 255), anchor="lt")
            (width, baseline), (offset_x, offset_y) = fnt.font.getsize(info["songs"][(column*leftcolumnlenght)+idx][0])
            title_width = max(title_width,width)
        for idx, song in enumerate(i):
            print(title_width)
            d.text((pad+title_width+text_pad+((pad+left_title_width+text_pad)*column), height+(pad//4)+((ascent+10)*idx)), info["songs"][(column*leftcolumnlenght)+idx][1], font=fnt, fill=(0, 0, 0, 255), anchor="lt")
        left_title_width = title_width

    img.show()
    img.save("poster.png")

    return