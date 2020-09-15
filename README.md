# **局域网关机工具**

------

## **前因**
家里有个小可爱睡觉前电脑总是开着热点，但是一到睡觉时间要关电脑，但与床距离至少三米远。这距离对于她来说太远啦，所以就给她做了这个工具，不用下床就可以用手机关开电脑啦。

## **功能**
- [x] 局域网控制关机
- [x] 主题颜色设置
- [ ] 无线开关
- [ ] 文件管理
- [ ] 局域网网址生成二维码

## 预览
- 主页：
- ![主页预览](./static/image/home_page_preview_yellow.png)

- 小可爱要求的粉红主题(被吐槽是橘红)：
- ![粉色主题](./static/image/home-page-preview_pink.png)

## **实现**
- **python3**
- **aiohttp**
- **jqueey-mobile**

> 讲道理这个简单的功能是不需要用 **python** 协程实现的，但是刚好学习了一段时间，就用 **aiohttp** 实现了；前端用的是 **jqueey-mobile** ，原因跟前面 **aiohttp** 一样。

## **使用**
### **源码**
- 需要python3环境
- pip 工具
```
git clone https://github.com/shenchucheng/EasyShutdown.git
cd EasyShutdown
pip install aiohttp
./app.py 
```
- 手机打开电脑局域网ip:8080访问，例如 192.168.1.100:8080