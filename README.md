# bilibili直播弹幕互动游戏
基于bilibili直播的游戏，观众可以通过弹幕和游戏互动
如 https://space.bilibili.com/10915722?spm_id_from=333.337.0.0

## 原理介绍
- 游戏画面和交互逻辑基于pygame编写
- 观众弹幕通过爬虫获取，https://github.com/xfgryujk/blivedm
- 两者通过多进程协调

## 运行游戏
1.  申请开启bilibili直播间，获取直播间地址
2.  修改blivedm/client.py中的地址
3.  python3 main.py
4.  在直播间共享游戏屏幕，等待玩家加入

## 直播效果
### 第一版游戏
- 弹幕输入“加入游戏”即可加入游戏
- 弹幕输入“wsad”可移动位置
<div align=center><img src="https://github.com/wangwenxi-handsome/bilibili-bullet-chat-game/blob/main/show.jpg"/></div>

### 第二版游戏
- 弹幕输入“加入游戏”即可加入游戏
- 弹幕输入“rgb”可更改颜色

### 设计难点
- 直播画面和游戏是不同步的，往往有近5秒甚至更长的延迟，导致这个弹幕游戏必然是低交互式的
- 自从2022.3月以来，b站上的弹幕游戏类型卷了起来，但有一定吸引力的只有 修勾老板 和 弹幕狼人杀
