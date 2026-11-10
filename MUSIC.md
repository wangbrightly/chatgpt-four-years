# 原创音乐：A Question, Then a World

作曲、编配、音色合成文件：[compose.py](compose.py)。没有旁白、歌词、采样曲库或复用音乐；全部音频由正弦波、FM 谐波和滤波噪声程序合成。

128 BPM / 4⁄4 / 28 小节 / 52.5 秒，48 kHz 24 bit 立体声母带。F minor / D-flat / A-flat / E-flat 和声流动，收束在 A-flat major seventh。四音终止动机 Ab–C–Eb–G 为本片编写。鼓组包括下滑音高 kick、滤波 clap、hat，主旋律为原创切分 pluck 和延迟回答。

52.5 秒原始母带响度经 ffmpeg loudnorm 测量：约 −14.28 LUFS integrated，true peak −0.93 dBTP，LRA 5.90 LU；成片混音保持 0.9 音量，避免有损编码产生的峰值溢出。

音乐分析保存在 audiomap.json。通用音频 tracker 估计约129 BPM，原作乐谱明确为128 BPM，故精确剪辑拍点由 score.json 确定：每拍0.46875秒，每两小节3.75秒。没有为了迎合估算器而改曲速或伪造分析结果。

assets/original-score.wav 为无损母带；assets/bgm.mp3 为预览兼容的320 kbps版本。用户可在此项目/致敬视频中使用、剪辑并重新编配本次原创程序合成音乐。
