/*import re
print(re.search("sunck", "sunck is a good man"))
#匹配[0-9]\d
#\D 匹配非数字[^0-9]
#\w匹配数字字母和下划线效果同[0-9a-zA-Z]
#\W匹配非数字字母和下划线效果同[^0-9a-zA-Z]
#[A-K][a-z]
print(re.search("[0-9]", "sunck is a go9od man"))*/
#[^sunck]匹配sunck这几个字符以外的字符^为脱字符，表示不匹配集合的字符
#\s匹配任意的空白字符串(空格，换行，回车，换页，制表)效果同[ \f\n\r\t] /S相反
#\b 匹配单词和空格的边界
#\B匹配非单词边界
import urllib.request
response = urllib.request.request.urlopen("http://www.baidu.com")
data = response.read().decode("utf-8")
print(data)
