# 济南大学假冒伪劣本科毕业论文 LaTeX 模板

**假冒伪劣的** UJN 本科毕业论文 Latex 模板，从未得到学校的授权，山寨货，作者写的初衷也是为了方便自己和朋友们写论文，在可维护性和代码风格上也没有进行专门设计，仅注重易用性，所以随便用用就好啦 ( ‘-ωก̀ )

效果请看示例：[这里是示例 PDF](build/main.pdf)

## 使用方法

开始整活前，请先确保已经安装如下环境并能在命令行中运行（就是配个 PATH），否则我们将会浪费不必要的生命在毫无意义的环境配置问题上：

1. 一个包含常用宏包的 LaTeX 发行版，额外注意要有 `xelatex` 引擎和 `ctex` 宏集，推荐 TeX Live 新版本

2. 一个你觉得功能足够强大以至于能坚持用它写完毕业论文的文本编辑器

3. Python3

### 编译方式

保证环境配置正确后：

- Windows 推荐用安装了 LaTeX Workshop 插件的 VSCode 直接打开项目，之后打开 `main.tex`，按按钮就能编译，新手友好。

    - 或者用命令行，执行 `python run.py` 即可，出错了就先 `python run.py clean` 再 `python run.py`。

- Linux 和 macOS（理论上）推荐用命令行，拿到手直接 `make`，出错了就先 `make clean` 再 `make`，当然 VSCode 也支持。详情请看 Makefile。

不出意外编译完后可以看到 `build` 目录下生成了 `main.pdf` 和其他一大堆文件，我们只需要关心 `main.pdf`，它就是我们的论文。

接下来参照如下的项目结构和模板中的注释，开始整活吧！

> LaTex 语法和背景知识请自行用正确的搜索引擎查找学习

## 项目组织

``` text
.vscode/                - VSCode 配置
build/                  - 编译产物，一般只需关心生成的 PDF
chapter/                - 章节文件，主要修改这个
    ch2-basic/
        abstract-cn.tex     - 中文摘要
        abstract-en.tex     - 英文摘要
        ...
        thanks.tex          - 致谢
    ch8-text-cn.tex         - 外文翻译的译文
docs/                   - 要插入的文档，看下面说明
figures/                - 图片目录
main.tex                - 主文件
translation.tex         - 翻译文件
others.tex              - 其他文件
ref.bib                 - 参考文献库
Makefile                - Makefile
run.py                  - Python 编译脚本
```

记得把 `docs` 路径下出现的主要是填一些个人信息的样例文档换成你的，记得不能再整活。

这些文档，有的还要留空给老师填写评语，所以在 Word 中填好生成 PDF 再替换是更高效的做法。

## 其他

有可能还会再做的 TODO：

- 支持热更新
- 支持按章节、按页等单独编译

大概不再会完成的 TODO：

- 支持 what you see is what you mean 的 Lyx
- 将 meta info 封装到人类更容易阅读和修改的 YAML 中
- TeXStudio 这种更专用的 LaTex 编辑器，甚至是神 の Vim 的配置
- 减少宏包依赖，防止出现诡异甚至智障的问题
- 消灭所有为凑间距而产生的 warning
- 更高层次的自动化脚本
- 完成 macOS 的测试
- Markdown 支持
- ......
