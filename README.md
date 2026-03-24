# Athanasy 简体中文汉化补丁

为 Steam 游戏 **[Athanasy](https://store.steampowered.com/app/1769320/Athanasy/)** 制作的简体中文本地化补丁。当前版本：**V1.0**

## 补丁内容

- 全部剧情对话翻译（约 7000 条）
- UI 界面文本翻译（菜单、设置、帮助等）
- 角色名称中文化
- 成就标题与描述翻译
- 中文菜单按钮图片
- 中文字体支持（Noto Sans SC）

## 安装方法

1. **下载** 前往 [Releases](../../releases) 页面，下载最新版本的 `Athanasy_Chinese.zip`
2. **找到** 游戏安装目录（Steam 库 → 右键 Athanasy → 管理 → 浏览本地文件）
   - 通常路径为：`...\Steam\steamapps\common\Athanasy\`
3. **解压** 将 zip 内容直接解压到游戏根目录（即 `Athanasy\` 文件夹），选择覆盖已有文件
4. **启动游戏** → 进入 **Settings（设置）** → 点击右下角的语言切换按钮，切换至中文

## 卸载方法

在 Steam 中右键 Athanasy → 属性 → 已安装文件 → **验证游戏文件完整性**，即可还原所有被修改的文件。

## 注意事项

- 首次启动可能稍慢（游戏需要编译翻译文件），之后启动速度恢复正常
- 本补丁不修改任何游戏性内容，不影响存档和成就
- 支持随时在俄语 / 英语 / 中文之间切换

## 项目结构

```
game/
├── code/sys/sys_language.rpy        # 语言配置（添加中文支持）
├── fonts/NotoSansSC-Regular.ttf     # 中文字体
└── tl/chinese/                      # 中文翻译文件
    ├── font_config.rpy              # 字体覆盖配置
    ├── screens.rpy                  # UI 文本翻译
    ├── script.rpy                   # 角色名翻译
    ├── code/sys/                    # 成就翻译
    ├── code/text/                   # 剧情对话翻译（20个文件）
    └── images/                      # 中文菜单按钮图片
```

## 许可

本汉化补丁仅供学习交流使用。游戏版权归原开发者所有。
字体 Noto Sans SC 基于 [SIL Open Font License](https://scripts.sil.org/OFL) 授权。
