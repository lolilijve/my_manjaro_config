#刷国内源
pacman-mirrors -c China -m rank
#更新系统
pacman -Syyu

# 安装 yay -- 软件库拓展
pacman -S yay
# 安装 fish -- 超好用的shell（使用fish_config进行配置）
pacman -S fish
# 安装 git
pacman -S git
# 安装 idea -- 钟爱的开发工具
pacman -S intellij-idea-community-edition
# 安装 pycharm -- python ide
pacman -S pycharm-community-edition
# 安装 chromium -- 浏览器
# （网站收藏，笔记，VPN，接口测试等）
pacman -S chromium
# 安装 jdk(idea自带，先不装)
# pacman -S jdk-openjdk
# 安装 neovim -- 文本编辑器
pacman -S neovim
# 安装 docker -- 容器
pacman -S docker
# 安装 alacritty -- 终端
pacman -S alacritty
# 安装 py3status -- i3status拓展
pacman -S py3status
# 安装 rofi
pacman -S rofi
# 安装 pcmanfm -- 文件管理器
pacman -S pcmanfm
# 安装 ranger -- 命令行文件管理器
pacman -S ranger
# 安装 htop 系统监视器
pacman -S htop
# 安装 feh -- 用于设置壁纸
pacman -S feh
# 安装 xcompmgr -- 用于设置透明度
pacman -S xcompmgr
# 安装 chezmoi -- 配置文件管理工具
pacman -S chezmoi
# 安装 dbeaver -- 数据库可视化客户端
pacman -S dbeaver
# 安装 uget -- 下载工具
pacman -S uget
# 安装 ibus -- 中文输入法
pacman -S ibus-rime
# 安装 wqy-microhei -- 中文字体
pacman -S wqy-microhei
# 安装 pavucontrol -- 音频控制器
pacman -S pavucontrol
# 安装 v2ray -- 梯子
pacman -S v2ray
# 安装 proxychains -- 转发
pacman -S proxychains-ng
# 安装 visualvm -- java分析工具
pacman -S visualvm
# 安装 npm
pacman -S npm
# 安装 utools
# （打开应用，搜索文件，音乐播放，内网穿透，文档查看等）
sudo yay -S utools
echo "执行qtconfig-qt4，在 Interface -> Default Input Method，把默认的输入法引擎由 xim 更改为 ibus"

#清理垃圾
pacman -Rns $(pacman -Qdtq)
pacman -Scc

# 另：数据库，redis等请安装 在docker中

# JMeter 压测工具
# Typora markdown编辑器
# mycli MySQL命令行客户端
# visual-studio-code-bin 编辑器
# remmina 远程桌面客户端
# Timeshift 备份工具
# redis-desktop-manager Redis可视化工具
# deepin-wine-wechat 微信
