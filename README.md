# 济南大学假冒伪劣本科毕业论文 LaTeX 模板

**假冒伪劣的** UJN 本科毕业论文 Latex 模板，从未得到学校的授权，山寨货。作者写的初衷也是为了方便自己和朋友们在 Linux 下做毕设时写论文，在可维护性和代码风格上也没有进行专门设计，仅注重易用性，所以随便用用就好啦 ( ‘-ωก̀ )

效果请看示例：[这是论文正文部分的示例 PDF](build/main/main.pdf)，[这是外文翻译部分的示例 PDF](build/trans/trans.pdf)

## 使用方法

若不想折腾本地环境，可以先试试看在线的 Overleaf，编译前记得选择 xelatex 引擎就好，[这是 Overleaf 模板链接](https://www.overleaf.com/latex/templates/ujnthesis/kywhqyrtqxgg)

**以下是本地环境的配置要求。**

开始整活前，请先确保已经安装如下环境并能在命令行中运行（就是配个 PATH），否则我们将会浪费不必要的生命在毫无意义的环境配置问题上：

1. 一个包含常用宏包的 LaTeX 发行版，额外注意要有 `xelatex` 引擎和 `ctex` 宏集，推荐 TeX Live 新版本

2. 一个你觉得功能足够强大以至于能坚持用它写完毕业论文的文本编辑器

3. Python3

### 编译方式

保证环境配置正确后：

- Windows 推荐用安装了 LaTeX Workshop 插件的 VS Code 直接打开项目，之后打开 `main.tex` 或者 `trans.tex`，按按钮就能编译，新手友好。

    - 或者用命令行，执行 `python run.py` 参照打印出的帮助信息再执行就好。

- Linux 和 macOS（理论上，未测试）推荐用命令行，拿到手直接 `make`（或指定`make trans`），出错了就先 `make clean` 再 `make`，当然也支持 VS Code。详情请看 Makefile。

编译完后可以看到 `build` 目录下生成了`main`和`trans`两个目录，目录内的 PDF 就是我们的论文。若不做进一步的开发则其余文件不必关心。

接下来参照下文中项目结构和模板中的注释，相应编译论文正文或外文翻译，根据自身需要注释或解注对应的文档部分，就可以开始整活啦～

### 字体说明

我已经把论文写作中的常用字体（宋体、黑体和 Times New Roman）做了内嵌，所以字体天然以 Windows 为标准，**各平台无需额外配置，即可保证统一的渲染效果**。

如果你需要使用楷体等更多字体，请自行下载对应的 ttf 字体文件于`fonts`目录内，并参照`ujnthesis`宏包中极其龌龊的实现方式进行命令封装，或者直接重构它（

> LaTex 语法和背景知识请自行用正确的搜索引擎查找学习

## 项目组织

``` text
.vscode/                - VSCode 配置
build/                  - 编译产物，一般只需关心生成的 PDF
chapter/                - 论文正文章节文件，主要修改这个
    abstract-cn.tex     - 中文摘要
    abstract-en.tex     - 英文摘要
    ...
    thanks.tex          - 致谢
docs/                   - 要插入的文档，看下面说明
figures/                - 图片目录
fonts/                  - 内嵌字体目录
main.tex                - 论文正文主文件
trans.tex               - 外文翻译文件
ref.bib                 - 参考文献库
Makefile                - Makefile
run.py                  - Python 编译脚本
```

把 `docs` 路径下出现的主要是填一些个人信息的样例文档换成你的，记得不能再整活。

这些文档，有的还要留空给老师填写评语，所以在 Word 中填好生成 PDF 再替换是更高效的做法。

## 其他

有可能还会再做的 TODO：

- 支持热更新
- 支持按章节、按页等单独编译
- 其他影响毕业论文格式审查以至影响毕业的 bug

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
