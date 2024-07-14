## CodeMerger

merge: 将多个字符串文档拼接成一个文档
split: 将用merge拼接的文档拆分，同时还原其相对目录结构

**拼接**
```
python ./codemerger.py merge sampleuse/inputfiles sampleuse/outfile.txt
```
- inputfiles 中配置需要拼接的文档
- outfile.txt 为拼接后的输出



**拆分**
```
python ./codemerger.py split sampleuse/outfile.txt sampleuse/outputdir
```
- outputdir：指定拆分文档的root目录

