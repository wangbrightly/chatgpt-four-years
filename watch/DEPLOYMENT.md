# 私有在线播放页

- URL：https://chatgpt-four-years-tribute-watch.miniatureplum.chatgpt.site/
- Sites project_id：`appgprj_6af32924a8608191a645cc59f3f9af11`
- 可见性：仅站点所有者可访问。GitHub 源仓库也继续保持私有。
- 原始合成文件仍位于项目根的 index.html，本目录的 index.html 只负责成片播放。

本目录保留播放器源码和构建脚本；`node watch/build.mjs` 从现有成片生成 watch/dist，视频以 `video/mp4` 提供，H.264 / yuv420p + AAC，MP4 的 moov 元数据置于媒体数据之前。托管服务应支持 `Range` / `206 Partial Content`，使章节跳转和进度拖动正常工作。

当前托管使用 Sites 独立源仓库。更新时复用此 project_id，通过 Sites 技能读取站点、取得短期凭据、打开对应源工作区，再同步构建输出并发布；不要另建站点。凭据只通过标准输入传给技能 helper，不写入 Git 仓库。

本次验证：浏览器已读取 52.5 秒 / 1920×1080 元数据；实际播放进度超过 0.8 秒；点击 2026 章节跳至 33.75 秒并继续播放；390px 手机视口无横向溢出；页面脚本错误为零。视频的画面及配乐未重新编码。
