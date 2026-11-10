"""Original score: 'A Question, Then a World'. 128 BPM / 28 bars / 52.5 s.
No sampled sounds, external melodies, vocals or copyrighted recordings.
"""
import numpy as np, soundfile as sf, json
from scipy.signal import butter,sosfilt
from pathlib import Path
P=Path(__file__).parent; (P/'assets').mkdir(exist_ok=True)
sr=48000; bpm=128; beat=60/bpm; duration=52.5
rng=np.random.default_rng(11302022); mix=np.zeros((int(sr*duration),2),dtype=np.float64)
def put(sig,start,vol=1,pan=0):
    i=int(start*sr); n=min(len(sig),len(mix)-i)
    if n<=0:return
    gains=np.array([np.cos((pan+1)*np.pi/4),np.sin((pan+1)*np.pi/4)])
    mix[i:i+n]+=sig[:n,None]*vol*gains
def note(midi,dur,kind='pluck'):
    t=np.arange(int(sr*dur))/sr; f=440*2**((midi-69)/12)
    if kind=='bass':
      x=np.sin(2*np.pi*f*t)+.28*np.sin(4*np.pi*f*t)+.1*np.sin(6*np.pi*f*t)
      env=(1-np.exp(-t*180))*np.exp(-t*5)
    elif kind=='pad':
      x=sum(np.sin(2*np.pi*f*(1+det)*t+ph) for det,ph in [(-.002,.3),(0,0),(.002,.8)])/3
      x+=.15*np.sin(4*np.pi*f*t)
      env=np.minimum(t/.18,1)*np.minimum((dur-t)/.6,1)*.7
    else:
      x=np.sin(2*np.pi*f*t+2*np.exp(-t*13)*np.sin(2*np.pi*f*2*t))+.18*np.sin(4*np.pi*f*t)
      env=(1-np.exp(-t*350))*np.exp(-t*7)*np.minimum((dur-t)/.02,1)
    return np.tanh(x)*env
def kick():
    t=np.arange(int(sr*.42))/sr; f=47+112*np.exp(-t*38)
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*10)+rng.normal(0,.08,len(t))*np.exp(-t*180)
def hat(open=False):
    t=np.arange(int(sr*(.22 if open else .08)))/sr
    noise=rng.normal(0,1,len(t)); noise=sosfilt(butter(2,6500,fs=sr,btype='highpass',output='sos'),noise)
    return noise*np.exp(-t*(22 if open else 65))
def clap():
    t=np.arange(int(sr*.22))/sr; x=sosfilt(butter(2,[1000,8500],fs=sr,btype='bandpass',output='sos'),rng.normal(0,1,len(t)))
    e=sum(np.exp(-np.maximum(t-d,0)*55)*(t>=d) for d in [0,.013,.027])
    return x*e*.45 + .15*np.sin(2*np.pi*185*t)*np.exp(-t*24)
chords=[[53,56,60,63],[49,53,56,60],[56,60,63,67],[51,55,58,63]]
motif=[0,7,10,14,12,7,3,10,0,3,7,12,10,7,14,15]
events=[]
for bar in range(28):
    t0=bar*4*beat; chord=chords[(bar//2)%4]; root=chord[0]-24
    energy=.65 if bar<4 else (.85 if bar<8 else (1 if bar<18 else (1.12 if bar<24 else .8)))
    if bar>=26:chord=[56,60,63,67]; root=32
    for n in chord:put(note(n,4*beat+.5,'pad'),t0,.09*energy,(-.5 if n%2 else .5))
    for k in range(4):
      ts=t0+k*beat
      if bar<26 or k==0:put(kick(),ts,.65*energy)
      if k in [1,3] and bar<26:put(clap(),ts,.22*energy,.06)
      if bar>=2 and bar<26:
       put(note(root+(12 if k==3 else 0),beat*.8,'bass'),ts+beat*.5,.35*energy)
      events.append({'t':round(ts,6),'kind':'score_beat','bar':bar+1,'beat':k+1})
    for k in range(8):
      if bar<26:put(hat(k%4==3),t0+k*beat*.5,.065*energy,(-.35 if k%2 else .35))
      if bar>=4 and bar<26:
       idx=(bar*8+k)%16; pitch=chord[0]+12+motif[idx]
       put(note(pitch,.55),t0+k*beat*.5,.115*energy,np.sin(k)*.55)
       put(note(pitch,.55),t0+(k*.5+.75)*beat,.032*energy,-np.sin(k)*.55)
    if bar in [3,7,11,15,17,23,25]:
      for k in range(8):put(clap(),t0+3*beat+k*beat/8,.025+.012*k,0)
    if bar in [0,4,8,12,16,18,20,24,26]:
      t=np.arange(int(sr*.85))/sr
      sig=sosfilt(butter(2,7000,fs=sr,btype='highpass',output='sos'),rng.normal(0,1,len(t)))*np.exp(-t*7)
      put(sig,t0,.09,0)
# Original four-note closing answer: Ab, C, Eb, G (maj7).
for j,n in enumerate([68,72,75,79]):put(note(n,2.4),48.75+j*beat*.5,.17,(-.35+j*.23))
# gentle stereo crossfeed / soft mastering; transparent fade to exact endpoint
mix=np.tanh(mix*1.5); mix*=.89/max(np.abs(mix).max(),1e-6)
fade=np.minimum(np.arange(len(mix))/(sr*.008),1)*np.minimum((len(mix)-1-np.arange(len(mix)))/(sr*.8),1)
mix*=fade[:,None]
sf.write(P/'assets/original-score.wav',mix,sr,subtype='PCM_24')
(P/'score.json').write_text(json.dumps({'title':'A Question, Then a World','bpm':bpm,'duration':duration,'beats':events,'composition':'All notes and timbres authored procedurally; no samples or vocals.'},indent=2))
print('Wrote original-score.wav: 52.5 s, 128 BPM, stereo 48 kHz')
