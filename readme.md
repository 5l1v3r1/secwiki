# secwiki
一个使用selenium+phantomjs写的小项目。插件化、本地化。
# 目的
由于自己的rss炸了，所以写了爬虫来抓取文章并且保存为pdf文档。
也起到文章分类知识聚合存档的一个效果。
# 依赖
- python3
- bs4
- requests
- selenium
- phantomjs
# 插件
```python
def run():
    posts = []
    post = {
        'date': date,
        'title': title,
        'url': url,
        'cate': cate
    }
    posts.append(post)
    return posts
```
插件目录在`plugin`目录，格式如上，需要定义`run`方法并且返回`posts`数组
# BUG
```
Message: {"errorMessage":"Refused to evaluate a string as JavaScript because 'unsafe-eval' is not an allowed source of script in the following Content Security Policy directive: \"script-src github.githubassets.com\".\n","request":{"objectName":"","statusCode":200,"headers":{"Cache":"no-cache","Content-Type":"application/json;charset=UTF-8"}}} Screenshot: available via screen
```
由于`phantomjs`暂停项目开发遗留的这个问题，未找到解决方案。

如果目标网站直接是静态pdf(比如`http://1.com/1.pdf`)，那么会出现输出的pdf为空白，未找到解决方案。
# END
个人项目，欢迎star、fork、pr，欢迎贡献爬虫插件。