# Agent UI Atlas

[English](README.md) · **简体中文**

面向 AI Agent 的 UI 设计语言与风格参考索引。它把分散在不同仓库中的设计资源，整理成可以直接理解和选择的风格，例如**苹果风格**、**Linear 风格**、**动森风格**或**星露谷式像素风格**。

> 最后核对：**2026-07-16**
> 首版来源于 [starvingarc](https://github.com/starvingarc) 公开的 GitHub Star 与 Fork。
> 当前快照：**104 种 UI / 参考风格**、**16 种图像素材风格**、**3 种动效风格**。

## 使用方法

1. 从下方表格选择一种基础 UI 风格。
2. 将对应的 **Agent 调用短语**复制给编程或设计 Agent。
3. Agent 需要完整规范、Skill、Prompt 或参考实现时，再打开上游来源。
4. 如有必要，在一种基础 UI 风格上最多叠加一种图像素材层和一种动效层。

示例：

> 采用苹果风格：大量留白、SF 系字体、电影感产品图。叠加苹果流体动效，但保持交互克制。

## 可用形式

表格只使用以下固定值：

- **DESIGN.md**：Agent 可以直接读取的设计系统文档。
- **Agent Skill**：可安装或复制给 Agent 的设计指令。
- **Prompt/Component Library**：可复用的提示词、组件集或视觉提示词集合。
- **Reference Implementation**：可供研究或复刻的、有辨识度的实际界面。
- **Background Theme**：场景或背景方向，不代表完整 UI 系统。

## 目录

- [品牌与产品风格](#品牌与产品风格)
- [通用 UI 设计语言](#通用-ui-设计语言)
- [游戏、IP 与场景主题](#游戏ip-与场景主题)
- [参考型界面](#参考型界面)
- [图像素材层](#图像素材层)
- [动效层](#动效层)
- [收录原则](#收录原则)
- [许可与声明](#许可与声明)

## 品牌与产品风格

这些条目覆盖 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 收录的 73 个品牌型设计预设。当 Huashu 提供明显等价的实现时，两个上游来源会保留在同一行。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| Airbnb 风格 | 暖色旅行平台 | 暖珊瑚色、圆润控件、摄影主导 | 旅行、预订和消费平台 | `采用Airbnb 风格：暖珊瑚色、圆润控件、摄影主导。` | DESIGN.md | [Airbnb DESIGN.md](https://getdesign.md/airbnb/design-md) |
| Airtable 风格 | 彩色结构化数据界面 | 彩色强调、友好网格、结构化数据 | 数据库、运营工具和协作表格 | `采用Airtable 风格：彩色强调、友好网格、结构化数据。` | DESIGN.md | [Airtable DESIGN.md](https://getdesign.md/airtable/design-md) |
| 苹果风格 | 高端产品极简主义 | 大量留白、SF 系字体、电影感产品图 | 消费产品、移动应用和高端落地页 | `采用苹果风格：大量留白、SF 系字体、电影感产品图。` | DESIGN.md | [Apple DESIGN.md](https://getdesign.md/apple/design-md) |
| Binance 风格 | 高紧迫感交易界面 | 黄黑高对比、密集市场信息 | 加密交易所和交易看板 | `采用Binance 风格：黄黑高对比、密集市场信息。` | DESIGN.md | [Binance DESIGN.md](https://getdesign.md/binance/design-md) |
| BMW 风格 | 德式高端汽车 | 高端暗色表面、精密模块构图 | 汽车、工业和高端产品网站 | `采用BMW 风格：高端暗色表面、精密模块构图。` | DESIGN.md | [BMW DESIGN.md](https://getdesign.md/bmw/design-md) |
| BMW M 风格 | 赛车性能风格 | 赛车高对比、M 色条、技术精度 | 性能产品和运动科技 | `采用BMW M 风格：赛车高对比、M 色条、技术精度。` | DESIGN.md | [BMW M DESIGN.md](https://getdesign.md/bmw-m/design-md) |
| Bugatti 风格 | 电影黑超奢华 | 电影黑、单色克制、纪念碑式大字 | 奢侈品发布和高端产品展示 | `采用Bugatti 风格：电影黑、单色克制、纪念碑式大字。` | DESIGN.md | [Bugatti DESIGN.md](https://getdesign.md/bugatti/design-md) |
| Cal.com 风格 | 中性日程极简 | 干净中性色、简单结构、开发者友好控件 | 日程和效率 SaaS | `采用Cal.com 风格：干净中性色、简单结构、开发者友好控件。` | DESIGN.md | [Cal.com DESIGN.md](https://getdesign.md/cal/design-md) |
| Claude 风格 | 暖色出版型 AI | 奶油纸色、赤陶橙、出版物排版 | AI 产品、思考型工具和长内容 | `采用Claude 风格：奶油纸色、赤陶橙、出版物排版。` | DESIGN.md | [Claude DESIGN.md](https://getdesign.md/claude/design-md) · [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Clay 风格 | 艺术指导型有机渐变 | 有机形状、柔和渐变、不对称艺术指导 | 创意机构和表达型产品网站 | `采用Clay 风格：有机形状、柔和渐变、不对称艺术指导。` | DESIGN.md | [Clay DESIGN.md](https://getdesign.md/clay/design-md) |
| ClickHouse 风格 | 黄色技术文档 | 黄色强调、技术布局、文档优先层级 | 数据库、分析和技术文档 | `采用ClickHouse 风格：黄色强调、技术布局、文档优先层级。` | DESIGN.md | [ClickHouse DESIGN.md](https://getdesign.md/clickhouse/design-md) |
| Cohere 风格 | 鲜艳企业 AI | 鲜艳渐变、几何形态、数据密集看板 | 企业 AI 平台和分析产品 | `采用Cohere 风格：鲜艳渐变、几何形态、数据密集看板。` | DESIGN.md | [Cohere DESIGN.md](https://getdesign.md/cohere/design-md) |
| Coinbase 风格 | 机构化加密金融 | 干净蓝色、宽松布局、信任导向层级 | 金融科技、钱包和机构产品 | `采用Coinbase 风格：干净蓝色、宽松布局、信任导向层级。` | DESIGN.md | [Coinbase DESIGN.md](https://getdesign.md/coinbase/design-md) |
| Composio 风格 | 彩色集成暗色界面 | 现代暗色表面和彩色集成图标 | 集成目录和 Agent 工具平台 | `采用Composio 风格：现代暗色表面和彩色集成图标。` | DESIGN.md | [Composio DESIGN.md](https://getdesign.md/composio/design-md) |
| Cursor 风格 | 顺滑 AI 开发者暗色 | 暗色表面、克制渐变、代码产品构图 | AI 编程工具和开发者产品 | `采用Cursor 风格：暗色表面、克制渐变、代码产品构图。` | DESIGN.md | [Cursor DESIGN.md](https://getdesign.md/cursor/design-md) |
| Dell 1996 风格 | 目录时代企业网页 | 黑色页面框、彩带卡片、Times 正文、GIF 贴纸 | 年代复刻网页和怀旧目录 | `采用Dell 1996 风格：黑色页面框、彩带卡片、Times 正文、GIF 贴纸。` | DESIGN.md | [Dell 1996 DESIGN.md](https://getdesign.md/dell-1996/design-md) |
| ElevenLabs 风格 | 电影感音频界面 | 电影黑表面、声波母题、蓝紫信号色 | 语音 AI、音乐、播客和音频产品 | `采用ElevenLabs 风格：电影黑表面、声波母题、蓝紫信号色。` | DESIGN.md | [ElevenLabs DESIGN.md](https://getdesign.md/elevenlabs/design-md) · [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Expo 风格 | 代码导向移动开发界面 | 暗色主题、紧凑字体、代码主导区块 | 移动开发平台和 SDK 文档 | `采用Expo 风格：暗色主题、紧凑字体、代码主导区块。` | DESIGN.md | [Expo DESIGN.md](https://getdesign.md/expo/design-md) |
| Ferrari 风格 | 稀疏红色汽车编辑风 | 明暗黑白和极少量法拉利红 | 豪华汽车和性能叙事 | `采用Ferrari 风格：明暗黑白和极少量法拉利红。` | DESIGN.md | [Ferrari DESIGN.md](https://getdesign.md/ferrari/design-md) |
| Figma 风格 | 多彩专业俏皮 | 鲜艳多色、模块化工具、专业俏皮感 | 设计工具和创意协作软件 | `采用Figma 风格：鲜艳多色、模块化工具、专业俏皮感。` | DESIGN.md | [Figma DESIGN.md](https://getdesign.md/figma/design-md) |
| Framer 风格 | 动效优先黑蓝风 | 黑蓝配色、大字、动效驱动产品叙事 | 建站工具和交互作品集 | `采用Framer 风格：黑蓝配色、大字、动效驱动产品叙事。` | DESIGN.md | [Framer DESIGN.md](https://getdesign.md/framer/design-md) |
| HashiCorp 风格 | 企业基础设施黑白风 | 干净黑白、模块化基础设施图 | DevOps、基础设施和企业平台 | `采用HashiCorp 风格：干净黑白、模块化基础设施图。` | DESIGN.md | [HashiCorp DESIGN.md](https://getdesign.md/hashicorp/design-md) |
| HP 风格 | 电光蓝几何科技 | 纯白画布、电光蓝 CTA、几何装饰 | 硬件、企业科技和产品电商 | `采用HP 风格：纯白画布、电光蓝 CTA、几何装饰。` | DESIGN.md | [HP DESIGN.md](https://getdesign.md/hp/design-md) |
| IBM 风格 | Carbon 企业系统 | 结构化蓝色、严格网格、实用组件 | 企业软件、数据和复杂工作流 | `采用IBM 风格：结构化蓝色、严格网格、实用组件。` | DESIGN.md | [IBM DESIGN.md](https://getdesign.md/ibm/design-md) |
| Intercom 风格 | 友好对话式 SaaS | 友好蓝色、圆润对话模式 | 消息、客服和对话产品 | `采用Intercom 风格：友好蓝色、圆润对话模式。` | DESIGN.md | [Intercom DESIGN.md](https://getdesign.md/intercom/design-md) |
| Kraken 风格 | 紫色密集交易看板 | 紫色强调暗色界面和密集市场数据 | 交易、金融和实时看板 | `采用Kraken 风格：紫色强调暗色界面和密集市场数据。` | DESIGN.md | [Kraken DESIGN.md](https://getdesign.md/kraken/design-md) |
| Lamborghini 风格 | 黑金殿堂式奢华 | 纯黑、金色强调、锐利宏大字体 | 奢侈品、汽车和戏剧化产品发布 | `采用Lamborghini 风格：纯黑、金色强调、锐利宏大字体。` | DESIGN.md | [Lamborghini DESIGN.md](https://getdesign.md/lamborghini/design-md) |
| Linear 风格 | 精密紫色产品极简 | 超极简暗色、细分割线、克制紫色 | 任务管理、Agent 控制台和效率 SaaS | `采用Linear 风格：超极简暗色、细分割线、克制紫色。` | DESIGN.md | [Linear DESIGN.md](https://getdesign.md/linear.app/design-md) |
| Lovable 风格 | 友好渐变构建器 | 俏皮渐变、亲和文案、友好开发者质感 | AI 构建器和入门型开发工具 | `采用Lovable 风格：俏皮渐变、亲和文案、友好开发者质感。` | DESIGN.md | [Lovable DESIGN.md](https://getdesign.md/lovable/design-md) |
| Mastercard 风格 | 暖色轨道金融编辑风 | 奶油画布、轨道胶囊形、暖色编辑感 | 支付、金融和企业叙事 | `采用Mastercard 风格：奶油画布、轨道胶囊形、暖色编辑感。` | DESIGN.md | [Mastercard DESIGN.md](https://getdesign.md/mastercard/design-md) |
| Meta 风格 | 摄影优先蓝色零售 | 摄影主导、明暗分区、蓝色 CTA | 硬件商店和消费产品生态 | `采用Meta 风格：摄影主导、明暗分区、蓝色 CTA。` | DESIGN.md | [Meta DESIGN.md](https://getdesign.md/meta/design-md) |
| MiniMax 风格 | 大胆霓虹 AI 暗色 | 大胆暗色界面和鲜明霓虹强调 | AI 模型平台和未来感产品发布 | `采用MiniMax 风格：大胆暗色界面和鲜明霓虹强调。` | DESIGN.md | [MiniMax DESIGN.md](https://getdesign.md/minimax/design-md) |
| Mintlify 风格 | 绿色阅读型文档 | 干净文档表面、绿色强调、清晰导航 | 文档、API 参考和知识库 | `采用Mintlify 风格：干净文档表面、绿色强调、清晰导航。` | DESIGN.md | [Mintlify DESIGN.md](https://getdesign.md/mintlify/design-md) |
| Miro 风格 | 亮黄无限画布 | 亮黄强调、空间工具、协作画布模式 | 白板、视觉规划和协作 | `采用Miro 风格：亮黄强调、空间工具、协作画布模式。` | DESIGN.md | [Miro DESIGN.md](https://getdesign.md/miro/design-md) |
| Mistral AI 风格 | 法式紫色极简 | 工程化极简、紫色调、清晰字体 | AI 基础设施和技术品牌网站 | `采用Mistral AI 风格：工程化极简、紫色调、清晰字体。` | DESIGN.md | [Mistral AI DESIGN.md](https://getdesign.md/mistral.ai/design-md) |
| MongoDB 风格 | 绿色开发者文档 | 叶绿色识别、清晰代码示例、文档导向 | 数据库、API 和开发者教育 | `采用MongoDB 风格：叶绿色识别、清晰代码示例、文档导向。` | DESIGN.md | [MongoDB DESIGN.md](https://getdesign.md/mongodb/design-md) |
| Nike 风格 | 黑白运动大字风 | 超大大写字、黑白界面、全屏摄影 | 运动、时尚和营销电商 | `采用Nike 风格：超大大写字、黑白界面、全屏摄影。` | DESIGN.md | [Nike DESIGN.md](https://getdesign.md/nike/design-md) |
| Nintendo.com 2001 风格 | Y2K 游戏机金属界面 | 斜面金属面板、网点碳纹、琥珀光、像素角色 | Y2K 游戏网站和怀旧交互体验 | `采用Nintendo.com 2001 风格：斜面金属面板、网点碳纹、琥珀光、像素角色。` | DESIGN.md | [Nintendo.com 2001 DESIGN.md](https://getdesign.md/nintendo-2001/design-md) |
| Notion 风格 | 暖色编辑型工作区 | 暖色极简、衬线标题、柔和中性色表面 | 知识工具、编辑器和效率工作区 | `采用Notion 风格：暖色极简、衬线标题、柔和中性色表面。` | DESIGN.md | [Notion DESIGN.md](https://getdesign.md/notion/design-md) |
| NVIDIA 风格 | 绿黑技术力量感 | 绿黑能量、技术图示、高性能语气 | AI 硬件、算力和技术发布 | `采用NVIDIA 风格：绿黑能量、技术图示、高性能语气。` | DESIGN.md | [NVIDIA DESIGN.md](https://getdesign.md/nvidia/design-md) |
| Ollama 风格 | 黑白本地终端 | 终端优先黑白极简和朴素留白 | 本地 AI 工具、CLI 和模型目录 | `采用Ollama 风格：终端优先黑白极简和朴素留白。` | DESIGN.md | [Ollama DESIGN.md](https://getdesign.md/ollama/design-md) |
| OpenCode 风格 | 开发者暗色编程界面 | 暗色编程表面、终端线索、紧凑技术层级 | 编程 Agent、IDE 和开发者控制台 | `采用OpenCode 风格：暗色编程表面、终端线索、紧凑技术层级。` | DESIGN.md | [OpenCode DESIGN.md](https://getdesign.md/opencode.ai/design-md) |
| Pinterest 风格 | 图片优先瀑布流发现 | 瀑布流、图片卡片、红色操作强调 | 灵感库、视觉搜索和媒体收藏 | `采用Pinterest 风格：瀑布流、图片卡片、红色操作强调。` | DESIGN.md | [Pinterest DESIGN.md](https://getdesign.md/pinterest/design-md) |
| PlayStation 风格 | 青色交互游戏零售 | 明暗层级、青色悬停信号、游戏图像 | 游戏商店、娱乐平台和发布页 | `采用PlayStation 风格：明暗层级、青色悬停信号、游戏图像。` | DESIGN.md | [PlayStation DESIGN.md](https://getdesign.md/playstation/design-md) |
| PostHog 风格 | 俏皮开发者分析 | 暗色开发者界面、吉祥物趣味、暖色强调 | 产品分析和开发者看板 | `采用PostHog 风格：暗色开发者界面、吉祥物趣味、暖色强调。` | DESIGN.md | [PostHog DESIGN.md](https://getdesign.md/posthog/design-md) |
| Raycast 风格 | 顺滑渐变暗色框架 | 暗色框架、鲜艳渐变、精致命令界面 | 启动器、命令面板和效率工具 | `采用Raycast 风格：暗色框架、鲜艳渐变、精致命令界面。` | DESIGN.md | [Raycast DESIGN.md](https://getdesign.md/raycast/design-md) |
| Renault 风格 | 极光渐变无圆角 | 鲜艳极光渐变、锐利无圆角控件、大胆字体 | 汽车和表达型产品营销 | `采用Renault 风格：鲜艳极光渐变、锐利无圆角控件、大胆字体。` | DESIGN.md | [Renault DESIGN.md](https://getdesign.md/renault/design-md) |
| Replicate 风格 | 白底代码优先机器学习 | 干净白底、直接代码示例、克制技术布局 | 模型 API、开发平台和机器学习目录 | `采用Replicate 风格：干净白底、直接代码示例、克制技术布局。` | DESIGN.md | [Replicate DESIGN.md](https://getdesign.md/replicate/design-md) |
| Resend 风格 | 极简暗色邮件开发界面 | 极简暗色、等宽强调、清晰邮件工具 | 邮件 API 和开发基础设施 | `采用Resend 风格：极简暗色、等宽强调、清晰邮件工具。` | DESIGN.md | [Resend DESIGN.md](https://getdesign.md/resend/design-md) |
| Revolut 风格 | 顺滑渐变金融科技 | 暗色精密、渐变卡片、精致金融数据 | 银行、钱包和个人金融应用 | `采用Revolut 风格：暗色精密、渐变卡片、精致金融数据。` | DESIGN.md | [Revolut DESIGN.md](https://getdesign.md/revolut/design-md) |
| Runway 风格 | 电影节编辑型创意 | 电影暗色主视觉、纸白阅读区、胶囊 CTA | 视频 AI、创意套件和媒体作品集 | `采用Runway 风格：电影暗色主视觉、纸白阅读区、胶囊 CTA。` | DESIGN.md | [Runway DESIGN.md](https://getdesign.md/runwayml/design-md) |
| Sanity 风格 | 暗色编辑珊瑚红 CMS | 大号编辑字体、等宽技术标签、稀疏珊瑚红 | 内容平台、CMS 和编辑型 SaaS | `采用Sanity 风格：大号编辑字体、等宽技术标签、稀疏珊瑚红。` | DESIGN.md | [Sanity DESIGN.md](https://getdesign.md/sanity/design-md) |
| Sentry 风格 | 粉紫密集可观测界面 | 暗色看板、密集诊断、粉紫强调 | 监控、调试和可观测控制台 | `采用Sentry 风格：暗色看板、密集诊断、粉紫强调。` | DESIGN.md | [Sentry DESIGN.md](https://getdesign.md/sentry/design-md) |
| Shopify 风格 | 电影暗色荧光绿电商 | 暗色电影图像、荧光绿信号、轻字重展示字体 | 电商平台和产品营销 | `采用Shopify 风格：暗色电影图像、荧光绿信号、轻字重展示字体。` | DESIGN.md | [Shopify DESIGN.md](https://getdesign.md/shopify/design-md) |
| SpaceX 风格 | 未来全屏黑白 | 强烈黑白、全屏航天图像、稀疏字体 | 航天、防务和宏大科技发布 | `采用SpaceX 风格：强烈黑白、全屏航天图像、稀疏字体。` | DESIGN.md | [SpaceX DESIGN.md](https://getdesign.md/spacex/design-md) |
| Spotify 风格 | 黑底绿音乐编辑风 | 黑底亮绿、粗体、专辑图主导 | 音乐、媒体和个性化内容体验 | `采用Spotify 风格：黑底亮绿、粗体、专辑图主导。` | DESIGN.md | [Spotify DESIGN.md](https://getdesign.md/spotify/design-md) |
| Starbucks 风格 | 大地绿暖色零售 | 分层大地绿、暖奶油画布、友好零售节奏 | 餐饮、生活方式和零售电商 | `采用Starbucks 风格：分层大地绿、暖奶油画布、友好零售节奏。` | DESIGN.md | [Starbucks DESIGN.md](https://getdesign.md/starbucks/design-md) |
| Stripe 风格 | 斜切流体渐变金融科技 | 紫色流体渐变、斜切区块、轻盈优雅字体 | 金融科技、SaaS 发布和技术营销 | `采用Stripe 风格：紫色流体渐变、斜切区块、轻盈优雅字体。` | DESIGN.md | [Stripe DESIGN.md](https://getdesign.md/stripe/design-md) · [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Superhuman 风格 | 高端键盘优先暗色 | 高端暗色、紫色微光、快速键盘交互 | 邮件、效率和高端桌面工具 | `采用Superhuman 风格：高端暗色、紫色微光、快速键盘交互。` | DESIGN.md | [Superhuman DESIGN.md](https://getdesign.md/superhuman/design-md) |
| Supabase 风格 | 翡翠绿代码优先暗色 | 墨绿暗色、代码面板、开发者优先层级 | 后端平台、数据库和开发者控制台 | `采用Supabase 风格：墨绿暗色、代码面板、开发者优先层级。` | DESIGN.md | [Supabase DESIGN.md](https://getdesign.md/supabase/design-md) |
| Tesla 风格 | 极度减法产品电影感 | 极少界面框架、全屏产品摄影、稀疏控件 | 汽车、硬件和高端产品发布 | `采用Tesla 风格：极少界面框架、全屏产品摄影、稀疏控件。` | DESIGN.md | [Tesla DESIGN.md](https://getdesign.md/tesla/design-md) |
| The Verge 风格 | 酸性色媒体新粗野主义 | 酸性薄荷绿和紫色、大胆编辑字体、硬边区块 | 媒体、文化、社区信息流和大胆发布 | `采用The Verge 风格：酸性薄荷绿和紫色、大胆编辑字体、硬边区块。` | DESIGN.md | [The Verge DESIGN.md](https://getdesign.md/theverge/design-md) · [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Together AI 风格 | 技术蓝图 AI | 蓝图网格、技术标签、基础设施图 | AI 基础设施和开发者平台 | `采用Together AI 风格：蓝图网格、技术标签、基础设施图。` | DESIGN.md | [Together AI DESIGN.md](https://getdesign.md/together.ai/design-md) |
| Uber 风格 | 城市黑白力量感 | 大胆黑白、紧凑字体、直接城市图像 | 出行、物流和城市服务 | `采用Uber 风格：大胆黑白、紧凑字体、直接城市图像。` | DESIGN.md | [Uber DESIGN.md](https://getdesign.md/uber/design-md) |
| Vercel 风格 | 瑞士黑白精密风 | 纯黑白、Geist 字体、锐利网格和直角 | 开发者工具、SaaS 和技术文档 | `采用Vercel 风格：纯黑白、Geist 字体、锐利网格和直角。` | DESIGN.md | [Vercel DESIGN.md](https://getdesign.md/vercel/design-md) · [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Vodafone 风格 | 纪念碑式红色通信 | 纪念碑式大写字、红色章节带、强品牌区块 | 通信、企业营销和大型服务 | `采用Vodafone 风格：纪念碑式大写字、红色章节带、强品牌区块。` | DESIGN.md | [Vodafone DESIGN.md](https://getdesign.md/vodafone/design-md) |
| VoltAgent 风格 | 虚空黑翡翠终端 | 虚空黑画布、翡翠绿信号、终端原生组件 | Agent 框架、编排和开发者平台 | `采用VoltAgent 风格：虚空黑画布、翡翠绿信号、终端原生组件。` | DESIGN.md | [VoltAgent DESIGN.md](https://getdesign.md/voltagent/design-md) |
| Warp 风格 | 块式现代终端 | 暗色 IDE 外观、命令块、现代终端交互 | CLI、终端和开发者效率工具 | `采用Warp 风格：暗色 IDE 外观、命令块、现代终端交互。` | DESIGN.md | [Warp DESIGN.md](https://getdesign.md/warp/design-md) |
| Webflow 风格 | 精致蓝色可视化构建器 | 蓝色强调的精致营销、可视化构建器构图 | 建站工具和专业创意 SaaS | `采用Webflow 风格：蓝色强调的精致营销、可视化构建器构图。` | DESIGN.md | [Webflow DESIGN.md](https://getdesign.md/webflow/design-md) |
| WIRED 风格 | 大报式科技编辑风 | 纸白高密度、衬线编辑节奏、墨蓝链接 | 科技媒体、报告和长内容出版 | `采用WIRED 风格：纸白高密度、衬线编辑节奏、墨蓝链接。` | DESIGN.md | [WIRED DESIGN.md](https://getdesign.md/wired/design-md) |
| Wise 风格 | 亮绿友好金融 | 亮绿强调、清晰语言、亲和金融结构 | 支付、转账和消费金融 | `采用Wise 风格：亮绿强调、清晰语言、亲和金融结构。` | DESIGN.md | [Wise DESIGN.md](https://getdesign.md/wise/design-md) |
| xAI 风格 | 强烈未来黑白 | 强烈黑白、未来克制、高对比技术字体 | 前沿 AI 产品和研究平台 | `采用xAI 风格：强烈黑白、未来克制、高对比技术字体。` | DESIGN.md | [xAI DESIGN.md](https://getdesign.md/x.ai/design-md) |
| Zapier 风格 | 暖橙插画自动化 | 暖橙色、友好插画、亲和工作流叙事 | 自动化、集成和无代码产品 | `采用Zapier 风格：暖橙色、友好插画、亲和工作流叙事。` | DESIGN.md | [Zapier DESIGN.md](https://getdesign.md/zapier/design-md) |

## 通用 UI 设计语言

这些是来自 [Huashu Design](https://github.com/alchaincyf/huashu-design) 的通用视觉语言，以及 [Taste Skill](https://github.com/Leonxlnx/taste-skill) 中三个明确的审美预设。与上方品牌风格不等价的项目才会独立成行。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| 包豪斯几何风格 | 三原色几何系统 | 三原色、圆三角方、模块化扁平插画 | 教育、品牌系统和视觉解释 | `采用包豪斯几何风格：三原色、圆三角方、模块化扁平插画。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 时装大字报风格 | Jacquemus 式时装编辑 | 黑白布局、满屏大标题、奢侈级留白 | 时尚、作品集、营销和发布页 | `采用时装大字报风格：黑白布局、满屏大标题、奢侈级留白。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 复古太空图录风格 | Comet / 2001 式太空图录 | 奶油黑蓝、轨道图、古典科幻字体 | AI 发布、研究工具和概念科技 | `采用复古太空图录风格：奶油黑蓝、轨道图、古典科幻字体。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 暗色开发者作品集风格 | Brittany Chiang 式作品集 | 海军蓝表面、单荧光强调、等宽标签、固定侧栏 | 开发者作品集和技术个人网站 | `采用暗色开发者作品集风格：海军蓝表面、单荧光强调、等宽标签、固定侧栏。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 商业周刊粗野主义风格 | Bloomberg Businessweek 式编辑 | 巨型 Helvetica 式字体、小正文、规则线、密集黑白网格 | 媒体、报告和观点型发布页 | `采用商业周刊粗野主义风格：巨型 Helvetica 式字体、小正文、规则线、密集黑白网格。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Duolingo 糖果风格 | 游戏化糖果界面 | 高饱和糖果色、圆角卡片、凸起可按按钮 | 教育、引导流程和趣味消费应用 | `采用Duolingo 糖果风格：高饱和糖果色、圆角卡片、凸起可按按钮。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Are.na 功能主义风格 | 高密度社区网格 | 系统字体、蓝链接、发丝分割线、信息优先列表 | 社区、目录、知识库和信息流 | `采用Are.na 功能主义风格：系统字体、蓝链接、发丝分割线、信息优先列表。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Apple Photos 暗色画廊风格 | 暗房内容优先画廊 | 近黑负空间、单视口大图、极小元数据 | 摄影、奢侈品和视觉作品集 | `采用Apple Photos 暗色画廊风格：近黑负空间、单视口大图、极小元数据。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Linear/Cursor 玻璃 Bento 风格 | Linear Look | 暗色便当格、发丝边框、柔光、磨砂表面 | AI SaaS、功能展示和 Agent 看板 | `采用Linear/Cursor 玻璃 Bento 风格：暗色便当格、发丝边框、柔光、磨砂表面。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 高端柔和风格 | 精致安静高端界面 | 柔和对比、大量留白、高端字体、克制弹簧动效 | 高端 SaaS、作品集和精致消费产品 | `采用高端柔和风格：柔和对比、大量留白、高端字体、克制弹簧动效。` | Agent Skill | [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/soft-skill) |
| 工业粗野主义风格 | 硬朗机械瑞士界面 | 锐利对比、瑞士字体、裸露结构、实验对齐 | 实验工具、技术品牌和文化网站 | `采用工业粗野主义风格：锐利对比、瑞士字体、裸露结构、实验对齐。` | Agent Skill | [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/brutalist-skill) |
| 原研哉白盒画廊风格 | Aesop 式日式留白 | 近白画布、细分割线、克制字体、内容提供色彩 | 策展电商、建筑和设计作品集 | `采用原研哉白盒画廊风格：近白画布、细分割线、克制字体、内容提供色彩。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Gucci Vault 拼贴风格 | Y2K 孟菲斯拼贴 | 复古撞色、旋转叠层、装饰字体、反网格构图 | 营销活动、概念商店和实验品牌 | `采用Gucci Vault 拼贴风格：复古撞色、旋转叠层、装饰字体、反网格构图。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Notion/Linear 极简风格 | 编辑型产品极简 | 克制配色、清晰层级、精密间距、安静产品表面 | 效率工具、编辑器和专注型 SaaS | `采用Notion/Linear 极简风格：克制配色、清晰层级、精密间距、安静产品表面。` | Agent Skill | [Taste Skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/minimalist-skill) |
| SNES 横版像素游戏风格 | 8/16-bit 滚动叙事 | 像素画、关卡换色、视差层、游戏 HUD | 交互简历、趣味发布和游戏化叙事 | `采用SNES 横版像素游戏风格：像素画、关卡换色、视差层、游戏 HUD。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| CSS 几何插画风格 | 响应式几何插画 | CSS 绘制形状、断点变形、扁平高对比配色 | 创意作品集、404 页面和技术展示 | `采用CSS 几何插画风格：CSS 绘制形状、断点变形、扁平高对比配色。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| 终端核软未来风格 | Cursor × Teenage Engineering | 等宽字主导、炭黑表面、克制光晕、等距立方体 | CLI 产品、AI 编程工具和开发基础设施 | `采用终端核软未来风格：等宽字主导、炭黑表面、克制光晕、等距立方体。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |
| Tailwind 彩色文档风格 | 彩虹分类文档 | 三栏文档、青色识别、彩虹分类、代码高亮 | 文档、API 参考和设计系统 | `采用Tailwind 彩色文档风格：三栏文档、青色识别、彩虹分类、代码高亮。` | Agent Skill | [Huashu](https://github.com/alchaincyf/huashu-design/blob/master/references/design-styles.md) |

## 游戏、IP 与场景主题

这些风格适合角色优先、游戏化、空间化或陪伴型界面。标记为 **Background Theme** 的条目只描述场景美术，不能当作完整组件系统。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| 8-bit 沙漠商队旅店风格 | 像素沙漠酒馆背景 | 暖沙色、商队道具、紧凑俯视像素房间 | Agent 房间、游戏化看板和主题工作区 | `采用8-bit 沙漠商队旅店风格：暖沙色、商队道具、紧凑俯视像素房间。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 地牢公会房间风格 | 像素 RPG 公会背景 | 石质室内、任务板氛围、俯视 RPG 房间布局 | 多 Agent 公会、任务看板和趣味运营 | `采用8-bit 地牢公会房间风格：石质室内、任务板氛围、俯视 RPG 房间布局。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 精灵森林旅店风格 | 像素森林奇幻背景 | 森林绿、木质细节、魔法旅店氛围 | 陪伴 Agent、安静看板和奇幻工作区 | `采用8-bit 精灵森林旅店风格：森林绿、木质细节、魔法旅店氛围。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 魔导工坊风格 | 像素奇幻科技工坊 | 机械道具、奥术能量、像素工坊分区 | 构建型 Agent、编程工作室和实验看板 | `采用8-bit 魔导工坊风格：机械道具、奥术能量、像素工坊分区。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 北欧奇幻酒馆风格 | 像素北欧酒馆背景 | 木结构暖意、北欧纹样、温馨奇幻酒馆光线 | 团队空间、社交 Agent 和温馨看板 | `采用8-bit 北欧奇幻酒馆风格：木结构暖意、北欧纹样、温馨奇幻酒馆光线。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 像素赛博酒馆风格 | 赛博朋克像素房间背景 | 霓虹像素标识、暗色室内、复古未来酒馆道具 | 赛博 Agent、黑客看板和趣味监控 | `采用8-bit 像素赛博酒馆风格：霓虹像素标识、暗色室内、复古未来酒馆道具。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 8-bit 雪山小屋风格 | 像素高山小屋背景 | 雪地蓝、温暖木屋灯光、紧凑高山像素室内 | 安静助手、冬季主题和氛围看板 | `采用8-bit 雪山小屋风格：雪地蓝、温暖木屋灯光、紧凑高山像素室内。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| AIRI 动漫 AI 伴侣风格 | 赛博虚拟角色界面 | 动漫角色聚焦、柔和赛博光、沉浸式陪伴控件 | AI 伴侣、虚拟主播和角色优先 Agent | `采用AIRI 动漫 AI 伴侣风格：动漫角色聚焦、柔和赛博光、沉浸式陪伴控件。` | Reference Implementation | [AIRI](https://github.com/moeru-ai/airi) |
| 动森风格 | 《集合啦！动物森友会》式界面 | 粉彩岛屿色、圆润触感控件、奶油和木质表面 | 陪伴 Agent、生活应用和趣味消费界面 | `采用动森风格：粉彩岛屿色、圆润触感控件、奶油和木质表面。` | Prompt/Component Library | [animal-island-ui](https://github.com/guokaigdg/animal-island-ui) |
| 星露谷式 8-bit 温馨农场酒馆 | 仅背景主题，非完整 UI 系统 | 温暖农场酒馆像素画、木质室内、乡村 RPG 氛围 | Agent 房间、温馨状态板和游戏化工作区 | `采用星露谷式 8-bit 温馨农场酒馆：温暖农场酒馆像素画、木质室内、乡村 RPG 氛围。` | Background Theme | [Star Office theme](https://github.com/ringhyacinth/Star-Office-UI/blob/master/backend/app.py) |
| 像素办公室风格 | 空间化多 Agent 状态板 | 俯视像素办公室、动画角色、房间化工作状态 | Agent 状态看板、多 Agent 团队和桌面宠物 | `采用像素办公室风格：俯视像素办公室、动画角色、房间化工作状态。` | Reference Implementation | [Star Office UI](https://github.com/ringhyacinth/Star-Office-UI) |

## 参考型界面

这些项目没有打包成完整风格系统，但其实际界面具有明确的视觉语言，可以供 Agent 研究和复刻。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| Understand Anything 教学型知识图谱风格 | 会教学的图谱 | 交互节点、引导关系、自然语言解释 | 代码理解、研究地图和知识 Agent | `采用Understand Anything 教学型知识图谱风格：交互节点、引导关系、自然语言解释。` | Reference Implementation | [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) |
| WeFlow 个人数据叙事风格 | 聊天记录年度报告 | 个人时间线、关系数据、年度报告叙事 | 个人分析、回顾和数据故事 | `采用WeFlow 个人数据叙事风格：个人时间线、关系数据、年度报告叙事。` | Reference Implementation | [WeFlow](https://github.com/hicccc77/WeFlow) |

## 图像素材层

图像素材层用于主视觉、插画、背景和内容图片。它们应当与基础 UI 风格组合使用，而不是代替布局和组件规则。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| 3D 渲染风格 | CG 产品图像 | 建模纵深、棚拍光线、精致材质 | 主视觉、产品和解释型画面 | `采用3D 渲染风格：建模纵深、棚拍光线、精致材质。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 动漫风格 | 日式动画视觉层 | 表现型角色、赛璐璐上色、图形化构图 | 陪伴 Agent、故事和角色产品 | `采用动漫风格：表现型角色、赛璐璐上色、图形化构图。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| Q 版风格 | 可爱紧凑角色画 | 大头、简化身体、趣味情绪线索 | 吉祥物、引导流程和友好助手 | `采用Q 版风格：大头、简化身体、趣味情绪线索。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 电影剧照风格 | 叙事电影图像 | 戏剧光线、镜头语言、场景化构图 | 主视觉、叙事和媒体产品 | `采用电影剧照风格：戏剧光线、镜头语言、场景化构图。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 漫画风格 | 连续图形叙事 | 分镜、墨线对比、对白和动作构图 | 教程、故事和趣味解释 | `采用漫画风格：分镜、墨线对比、对白和动作构图。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 赛博朋克科幻风格 | 霓虹未来视觉层 | 霓虹对比、未来界面、密集城市科技 | AI 发布、游戏和概念产品 | `采用赛博朋克科幻风格：霓虹对比、未来界面、密集城市科技。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 商业插画风格 | 通用编辑插画 | 设计化形状、受控配色、叙事场景 | 营销、解释和友好空状态 | `采用商业插画风格：设计化形状、受控配色、叙事场景。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 中国水墨风格 | 水墨视觉层 | 写意笔触、纸张质感、克制留白 | 文化、教育和诗意界面 | `采用中国水墨风格：写意笔触、纸张质感、克制留白。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 等距插画风格 | 等距系统插画 | 统一斜投影、模块场景、清晰空间系统 | 建筑、工作流和基础设施解释 | `采用等距插画风格：统一斜投影、模块场景、清晰空间系统。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 极简图像风格 | 减法视觉层 | 少量元素、受控色彩、强构图和留白 | 安静产品、编辑布局和高端品牌 | `采用极简图像风格：少量元素、受控色彩、强构图和留白。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 油画风格 | 绘画型古典视觉层 | 可见笔触、丰富色彩纵深、戏剧材质感 | 文化、叙事和表现型主视觉 | `采用油画风格：可见笔触、丰富色彩纵深、戏剧材质感。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 摄影风格 | 写实摄影视觉层 | 真实光线、相机构图、材质和人物细节 | 电商、旅行、人物和产品叙事 | `采用摄影风格：真实光线、相机构图、材质和人物细节。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 像素画风格 | 8/16-bit 视觉层 | 像素网格、有限配色、精灵图形态 | 游戏化 Agent、怀旧工具和状态板 | `采用像素画风格：像素网格、有限配色、精灵图形态。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 复古风格 | 年代感视觉层 | 老化配色、印刷质感、历史字体线索 | 营销、档案和怀旧体验 | `采用复古风格：老化配色、印刷质感、历史字体线索。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 手绘线稿风格 | 图解型手绘层 | 松弛线条、批注感、轻量视觉解释 | 教育、概念探索和解释 | `采用手绘线稿风格：松弛线条、批注感、轻量视觉解释。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |
| 水彩风格 | 柔和绘画视觉层 | 半透明色洗、柔边、有机混色 | 生活方式、健康和柔和叙事 | `采用水彩风格：半透明色洗、柔边、有机混色。` | Prompt/Component Library | [awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) |

## 动效层

动效层描述界面如何运动。应当在确定基础 UI 风格之后再选择。

| 风格名 | 英文名 / 别名 | 视觉特征 | 适合场景 | Agent 调用短语 | 可用形式 | 上游来源 |
|---|---|---|---|---|---|---|
| 苹果流体动效 | WWDC 式界面动效 | 连续几何、弹簧物理感、可打断过渡 | 高端产品界面和响应式交互 | `采用苹果流体动效：连续几何、弹簧物理感、可打断过渡。` | Agent Skill | [apple-design](https://github.com/emilkowalski/skills/tree/main/skills/apple-design) |
| Lottie 矢量动效 | 可交付矢量动画 | 路径显现、形状变形、渐变、镜头推进和时序控制 | 插画、引导、图标和品牌动效 | `采用Lottie 矢量动效：路径显现、形状变形、渐变、镜头推进和时序控制。` | Agent Skill | [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) |
| 精密产品微交互 | Linear/Vercel 经验型动效 | 目的明确的缓动、短反馈、细阴影、克制频率 | 开发者工具、SaaS 和精致产品交互 | `采用精密产品微交互：目的明确的缓动、短反馈、细阴影、克制频率。` | Agent Skill | [emilkowalski/skills](https://github.com/emilkowalski/skills) |

## 收录原则

- **以风格为单位：** 每一行代表一种视觉语言，而不只是一个仓库。
- **直观命名：** 有明确品牌或 IP 时，优先使用容易理解的名称。
- **有据可查：** 每一行都链接上游规范、Skill、Prompt 库、主题定义或实际实现。
- **合并同类：** 明显等价的风格只保留一行，同时保留多个上游来源。
- **只链接上游：** 不把个人 Fork 当作权威来源。
- **限定 UI 范围：** 不收录普通 Agent 工具、通用无样式组件库和仅用于 PPT 的风格。
- **人工维护：** 首版由个人维护，暂时不开放投稿流程。
- **暂不嵌入预览：** 后续核对来源和授权后，可以再增加截图。

## 许可与声明

本仓库原创的整理结构与说明文字采用 [知识共享署名 4.0 国际许可协议](LICENSE)。

被链接仓库、设计文档、Skill、提示词、商标、产品名称、游戏名称、截图和美术素材，仍分别遵循其权利人和原始许可证的规定。本项目是独立的参考索引，与所列品牌或权利人不存在隶属、认可或赞助关系。“某某风格”或“受某某启发”只表示参考方向，不代表获得复制受保护素材或宣称官方关联的权利。
