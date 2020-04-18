# Youdao-mindmap-to-Xmind
将有道云笔记的.mindmap脑图文件转换为Xmind文件/ Transfer Youdao Cloud Mind Map file to Xmind file
---
#### Xmind使用环境：测试使用的是Xmind 2020（Xmind Zen 10.1.2)，没有在其他环境内测试过

#### Python脚本版本为Python 3

---
## 想法
之前用有道云笔记做了一些脑图，后面发现导出图片和居然要会员，就感觉很不爽。但是这些脑图有点多，感觉很不甘心，于是就花了一点时间写了这个脚本~~（想整活是主要的，不想充会员是次要的（滑稽））

## 原理简述
#### 有道云笔记
有道云的功能相对Xmind来说比较单一。有道云的.mindmap 文件实际上是一个json格式的文件，里面的nodes列表就是节点列表，里面主要存储的内容有：

- 节点ID(实际上是一个Hash)
- 节点内容
- 节点样式（字体等）
- 父节点ID(parentid)

#### Xmind
.xmind文件实际上是一个压缩文件，解压后的content.json就是主要记录节点内容的文件，里面有一个固定的框架结构，节点的内容以递归的形式存储在rootTopic下
#### 转换方法
有道云笔记的节点存储形式实际上是一个单向联通图，通过遍历所有节点的方式将其转换为强联通图，最后从根节点开始递归遍历并记录节点，最后写入Xmind文件

## 使用方法
将有道云中的脑图文件右键另存为*input.mindmap*到mind.py的同级目录下，运行Python脚本，转换的XMind文件在Output文件夹内(Out.xmind)
