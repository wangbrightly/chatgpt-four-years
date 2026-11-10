from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
import subprocess,concurrent.futures
P=Path(__file__).parent
times=[0,2.5]+[6.25+3.75*i for i in range(13)]
out=P/'research'/'decoded-heroes';out.mkdir(exist_ok=True)
def capture(t):
 f=out/f'{t:g}.png'
 subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-ss',str(t),'-i',str(P/'renders'/'ChatGPT-四周年致敬-1080p.mp4'),'-frames:v','1',str(f)],check=True)
 return f
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: files=list(pool.map(capture,times))
font=ImageFont.truetype(str(P/'assets/fonts/Geist-Regular.ttf'),18)
sheet=Image.new('RGB',(1440,5*300+62),'#F4F3EE');d=ImageDraw.Draw(sheet)
d.text((18,16),'CHATGPT / FOUR-YEAR TRIBUTE     52.5s / 1920 x 1080 / 30fps',font=font,fill='#171B1A')
for i,(f,t) in enumerate(zip(files,times)):
 x=(i%3)*480;y=62+(i//3)*300
 sheet.paste(Image.open(f).convert('RGB').resize((480,270)),(x,y))
 d.text((x+12,y+274),f'{t:05.2f}s',font=font,fill='#171B1A')
sheet.save(P/'renders'/'成片总览.jpg',quality=93)
print('15 actual decoded hero frames -> renders/成片总览.jpg')
