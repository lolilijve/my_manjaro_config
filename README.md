# my_manjaro_config

我的manjaro配置文件,本配置文件项目由`chezmoi`提交；

## 另附上manjaro安装配置过程：

### manjaro-i3系统镜像
>  https://manjaro.org/download/community/i3/

### 更换国内源

```shell
sudo pacman-mirrors -c China -m rank
```

### 更新系统

```shell
sudo pacman -Syu
```

### 同步时间 

```shell
timedatectl set-ntp true
```

### 安装AUR助手(i3镜像中貌似已包含)

```shell
sudo pacman -S yay
```

### 中文输入法

```shell
sudo pacman -S ibus-rime
yay -S ibus-qt
```

> 执行`qtconfig-qt4`，在 **Interface** -> **Default Input Method**，把默认的输入法引擎由 **xim** 更改为 **ibus**

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

   ```shellz
   chezmoi apply
   ```

   > 注意：
   >
   > 1. 需要安装`chezmoi`
   > 2. 部分配置当即生效，部分需重启，视软件而定
   > 3. 千万不要轻易使用`chezmoi update`，此操作相当于拉取线上配置并直接覆盖当前使用的配置

### 安装所需应用

> 参照~/.my-manjaro中文件
