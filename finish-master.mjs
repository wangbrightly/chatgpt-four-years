import {readFileSync,writeFileSync} from 'node:fs';
let html=readFileSync(new URL('./index.html',import.meta.url),'utf8');
html=html.replace('<html lang="en">','<html lang="zh-CN">').replace(/<script src="https:\/\/cdn\.jsdelivr[^<]*<\/script>/,'<script src="assets/gsap.min.js"></script>');
html=html.replace(/class="frame"/g,'class="frame clip"');
html=html.replace(/data-track-index="1"/g,'data-track-index="1" data-width="1920" data-height="1080"');
html=html.replace('data-volume="0.9"','data-volume="0.9"');
html=html.replace('position: relative; width: 1920px; height: 1080px;','position: relative; width: 100%; height: 100%;');
html=html.replace('</style>',`
@font-face{font-family:Geist;src:url('assets/fonts/Geist-Regular.ttf');font-weight:400}
@font-face{font-family:Geist;src:url('assets/fonts/Geist-Bold.ttf');font-weight:700}
@font-face{font-family:NotoSansSC;src:url('assets/fonts/NotoSansSC.ttf');font-weight:100 900}
#master-chrome{position:absolute;inset:0;pointer-events:none;z-index:100;font-family:Geist,NotoSansSC,sans-serif}
#master-brand{position:absolute;left:88px;top:56px;height:42px;display:flex;align-items:center;gap:14px;background:#F4F3EE;color:#171B1A;border:1px solid #171B1A;border-radius:32px;padding:0 20px;font-size:21px;letter-spacing:.08em}
#master-dot{width:10px;height:10px;display:block;border-radius:50%;background:#146451}
#master-independent{position:absolute;right:88px;top:56px;height:42px;display:flex;align-items:center;background:#F4F3EE;color:#171B1A;border:1px solid #171B1A;border-radius:32px;padding:0 20px;font-size:21px;letter-spacing:.025em}
#master-track{position:absolute;bottom:0;left:0;right:0;height:7px;background:#F4F3EE}
#master-progress{width:100%;height:100%;background:#146451;transform-origin:left center}
</style>`);
html=html.replace('    </div>\n\n    <script>',`      <div id="master-chrome"><div id="master-brand"><i id="master-dot"></i>A QUESTION, THEN A WORLD</div><div id="master-independent">第三方致敬 / INDEPENDENT TRIBUTE</div><div id="master-track"><div id="master-progress"></div></div></div>
    </div>

    <script>`);
html=html.replace('window.__timelines["main"] = gsap.timeline({ paused: true });',`const main=gsap.timeline({paused:true});
main.fromTo('#master-progress',{scaleX:0},{scaleX:1,duration:52.5,ease:'none'},0);
window.__timelines['main']=main;
main.seek(0);`);
writeFileSync(new URL('./index.html',import.meta.url),html);
console.log('Master finished: local GSAP + all-time third-party labels + linear beat-spanning progress.');
