# 一个问题，然后是世界

ChatGPT 四周年第三方致敬片，52.5 秒，1920×1080 / 30 fps，原创电子配乐，无旁白。

纪念区间 2022.11.30–2026.11.30。资料截止 2026.11.10，周年预制片。非 OpenAI 官方出品，未获官方背书。

- **[在线播放成片（私有观看页）](https://chatgpt-four-years-tribute-watch.miniatureplum.chatgpt.site/)** — 打开后点击播放器播放，支持进度拖动、全屏和章节跳转；需使用创建页面的 ChatGPT 账号访问。
- [下载 MP4 文件](renders/ChatGPT-四周年致敬-1080p.mp4)
- [事实表与官方链接](FACTS.md)
- [原创配乐说明](MUSIC.md)、[合成代码](compose.py)、[无损母带](assets/original-score.wav)
- [视觉调研及限制](research/VISUAL-RESEARCH.md)
- [分镜](STORYBOARD.md) · [验证记录](VERIFICATION.md)
- 可编辑源工程：[主合成](index.html)、[分段合成](compositions/frames/)

![成片总览](renders/成片总览.jpg)

音乐的精确拍点由 score.json 保存；音频分析结果另存 audiomap.json。所有字体、GSAP 与音乐为本地资源，渲染无需外链。

使用已安装 HyperFrames 0.8.181 打开本目录，或 npm run dev；本工程的 package.json 保留固定版本。重新组装使用该技能 assemble-index.mjs 后执行 node finish-master.mjs，以恢复独立致敬标识及本地资源。

本地预览与渲染需要 Node.js 22+、FFmpeg / FFprobe，以及 HyperFrames 可用的 Chromium。首次运行 npm 脚本会获取固定版本 CLI：

```sh
npm run dev
npm run check
npm run render -- --quality delivery --fps 30 --output renders/ChatGPT-四周年致敬-1080p.mp4
```

重新合成音乐或生成成片总览时，另需 Python 3.9+：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python compose.py
python make-contact.py
```

已提交的配乐和字体可直接用于现有合成，预览现有工程无需先运行 Python。运行 compose.py 会重新生成 WAV 母带；如要更新预览用 MP3，再执行 `ffmpeg -y -i assets/original-score.wav -codec:a libmp3lame -b:a 320k assets/bgm.mp3`。

在线播放器的源码位于 [watch/](watch/)。运行 `node watch/build.mjs` 生成 `watch/dist/`，包含原生 HTML5 播放器、封面和启用 fast start 的 MP4；该页面可以部署到支持视频字节范围请求的静态托管服务。GitHub 中的 MP4 文件链接保留为下载入口。
