# my_manjaro_config

我的manjaro配置文件,本配置文件项目由`chezmoi`提交；

## 另附上manjaro安装配置过程：

### 更换国内源

```shell
sudo pacman-mirrors -i -c China -m rank
```

### 更新系统

```shell
sudo pacman -Syu
```

### 同步时间 

```shell
timedatectl set-ntp true
```

### 安装AUR助手

```shell
sudo pacman -S yay
```

### 中文输入法

```shell
sudo pacman -S fcitx fcitx-im fcitx-configtool
```

> 若使用Google输入法执行：
>
> ```shell
> sudo pacman -S fcitx-googlepinyin
> ```
>
> 若使用搜狗输入法则执行以下操作
>
> ```shell
> yay -S fcitx-qt4 qtwebkit-bin fcitx-sogoupinyin
> ```



### 安装所需应用

| 当前安装 |           **应用名**            |     **功能**      |                           **说明**                           | 重要程度（于我而言） |
| :------: | :-----------------------------: | :---------------: | :----------------------------------------------------------: | :------------------: |
|    √     |            chromium             |      浏览器       |                  我一直在用的唯一一款浏览器                  |        ❤❤❤❤❤❤        |
|    √     | intellij-idea-community-edition |        ide        |                         社区版就是好                         |        ❤❤❤❤❤❤        |
|    √     |           jdk-openjdk           |        jdk        |                             饭碗                             |        ❤❤❤❤❤❤        |
|    √     |               git               |        git        |                             筷子                             |        ❤❤❤❤❤❤        |
|    √     |           vim/neovim            |    文本编辑器     |         据说vim号称编辑器之神；装上spacevim更优秀；          |        ❤❤❤❤❤         |
|    √     |            alacritty            |    终端模拟器     |         GPU加速，我倒是没多少感觉，可能我的GPU太烂了         |        ❤❤❤❤❤         |
|    √     |              fish               |       shell       | 配置`fish_config`，设置为默认shell`sudo chsh -s (which fish)`; |        ❤❤❤❤❤         |
|    √     |           oh-my-fish            |    fish拓展包     |        安装：`curl -L https://get.oh-my.fish \| fish`        |        ❤❤❤❤❤         |
|    √     |              redis              | 键值对存储数据库  |                            常用到                            |        ❤❤❤❤❤         |
|    √     |             docker              |   就是docker咯    |                     装得下，世界就是你的                     |        ❤❤❤❤❤         |
|    √     |             chezmoi             |   点文件git管理   |               妈妈再也不用担心我的配置文件丢了               |         ❤❤❤❤         |
|    √     |             Typora              | markdown编写工具  |                       方便，好用，美观                       |         ❤❤❤❤         |
|    √     |              mycli              | MySQL命令行客户端 |                          就比较装哔                          |         ❤❤❤❤         |
|    √     |             mariadb             |      数据库       |                          就一数据库                          |         ❤❤❤❤         |
|    √     |     visual-studio-code-bin      |      vscode       |                         现在也不常用                         |         ❤❤❤❤         |
|    √     |             remmina             |  远程桌面客户端   |                用你还不是因为我懒得记ip，密码                |         ❤❤❤❤         |
|    √     |           virtualbox            |      虚拟机       |                 虚拟机的话用来用去还是这个好                 |         ❤❤❤          |
|    ×     |       netease-cloud-music       |    网易云音乐     |            linux下最好的中文音乐播放软件（据说）             |         ❤❤❤          |
|    √     |            Timeshift            |   系统备份工具    |                      偶尔备份是个好习惯                      |         ❤❤❤          |
|    √     |             JMeter              |   java压测工具    |                            还可以                            |         ❤❤❤          |
|    √     |      redis-desktop-manager      |  Redis可视化工具  |                            还不错                            |          ❤❤          |
|    √     |            Flameshot            |    截图并编辑     |             设置快捷键Ctrl+Alt+A，符合长期QQ习惯             |          ❤❤          |
|    √     |              ngrok              |     内网穿透      |                                                              |          ❤❤          |
|    ×     |           latte-dock            |  桌面美化--托盘   |              挺好看的，反正我喜欢，在kde中使用               |          ❤❤          |
|    ×     |               mpv               |      播放器       |                     简单，好用（不常用）                     |          ❤           |
|    ×     |              uget               |     下载工具      |           说真的，我还是觉得迅雷好用，是我的错觉吗           |          ❤           |
|    ×     |             dbeaver             | 数据库可视化界面  |                 偶尔卡死，原因未知，有点吃藕                 |          ❤           |

> 注：以上选装

> ps：为什么有六星选项？	因为我玩`克鲁赛德战记`啊，请叫我`肝多夫`

| 是否推荐安装 | 应用名（i3wm中使用）  |          功能           |                             说明                             |
| :----------: | :-------------------: | :---------------------: | :----------------------------------------------------------: |
|      √       |    xorg-xbacklight    |      调节屏幕亮度       |                              --                              |
|      √       |  mate-power-manager   |        电池管理         |                     用于挂起，熄屏什么的                     |
|      √       |       py3status       |      i3status拓展       |                     就是美化i3wm状态栏的                     |
|      √       |        pydbus         |     Python的dbus库      |                       py3status中使用                        |
|      √       |      alsa-utils       | Linux声音支持的替代实现 |                              --                              |
|      √       | deepin-system-monitor |       任务管理器        |                    深度的东西还是挺漂亮的                    |
|      √       | networkmanager_dmenu  |        wifi管理         |                          能记住密码                          |
|      √       |         rofi          |       应用运行器        |                             很棒                             |
|      √       |       alacritty       |          终端           |                    我在配置文件里写的这个                    |
|      √       |  nerd-fonts-complete  | 字体（含多种字符图标）  | 本人使用`https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/Hack` |

> 注：以上个人推荐，与本配置相关

### 获取配置文件

1. 创建chezmoi目录并clone配置文件项目

   ```shell
   chezmoi init https://github.com/lolilijve/my_manjaro_config.git
   ```

2. 与当前使用的配置文件比较

   ```shell
   chezmoi diff
   ```

3. 若想保留当前文件可使用

   ```shell
   chezmoi add 文件路径
   ```

4. 若确认无误可使用项目中的配置文件覆盖当前配置

   ```shell
   chezmoi apply
   ```

   > 注意：
   >
   > 1. 需要安装`chezmoi`
   > 2. 部分配置当即生效，部分需重启，视软件而定
   > 3. 千万不要轻易使用`chezmoi update`，此操作相当于拉取线上配置并直接覆盖当前使用的配置