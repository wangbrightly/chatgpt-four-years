---
name: A Question, Then a World
colors:
  paper: '#F4F3EE'
  ink: '#171B1A'
  green: '#BCE5CF'
  teal: '#146451'
  coral: '#EE896C'
  blue: '#A8C8EF'
typography:
  display: { fontFamily: Geist, weight: 700 }
  body: { fontFamily: NotoSansSC, weight: 500 }
  data: { fontFamily: Geist, weight: 400 }
---

用户指定以官方视觉观察为基调，故本次使用定制设计系统，优先于工作流默认预设。字体文件全部位于 assets/fonts：Geist-Bold.ttf / Geist-Regular.ttf / NotoSansSC.ttf。

从已查看的官方 GPT‑5.5 视频提取：偏白浅底、干净几何无衬线、圆角输入区域、提示→结果、近景推到全局。官方品牌指南强调圆形几何与人文温度。网页浏览受加载验证页影响，不能声称已观察完整首页；依靠官网可读取的品牌说明与官方发布短片实帧建立基调。

第三方差异：以「一个问题，然后是世界」为独立片名，薄边框年表、珊瑚橙 / 草绿 / 浅蓝分色，超大版本数字，四瓣对话方块（不得制作 OpenAI 标志或近似结形）。每帧常驻小号 THIRD-PARTY TRIBUTE 由主工程覆盖；片尾明确中文「第三方致敬 · 非 OpenAI 官方出品」。不使用官方 logo、官方配乐或官方片段。

画面：1920×1080。安全边距 88px；主标题 110–220px，模型版本数字可到 350px；注释 24–28px；正文 40–54px。顶栏 y=62，底注 y=974；活动内容主要在 y=160–900。图形可以满版，文字保持安全区。暗底时注释使用 paper 色，浅底使用 ink 色。单帧可以用底色切换，但不闪烁频闪。每 3.75s 一个事实段，段内每 0.46875s 或半拍发生层级有别的入场、平移、图形展开、追随波形或数字锁定，主信息稳定保留约 2 秒。

避免：静态 PPT、重复同一布局、所有内容都套卡片、堆砌通用渐变球、伪造聊天记录、未标示演示的产品界面。视觉原理示意必须是抽象几何，不呈现伪造产品截图。

开发：主工程加载 GSAP；子工程只有 template 内 style/root/script。路径以项目根为基准 assets/fonts/...。各 composition CSS 必须作用于自己的 id，不写全局 body/html/* 样式。只有一条 paused GSAP timeline。完整可 seek。抽象持续运动的对象可用有限 repeat/yoyo。所有组开始/结束用 opacity 0ms 切换，普通内部 div 不是 .clip。禁止 JS 动态修改文字，所有文字节点静态写好，数字动画用静态数字层或字符列滚动，避免回放不确定。不要使用 font measuring 回调。
