1、在处理csv文件时，发现有部分的数据会自动换行，文件放到linux下，就会被认为是多行；  
解决方法：使用pandas模块进行处理  
import pandas as pd  
fp = pd.read_csv('test.csv')  

pandas会识别这样的换行，不会认为是新的一行  


2、import matplotlib.pyplot as plt 报错如下：  
no display name and no $DISPLAY environment variable
解决方法：    
linux系统下执行：export DISPLAY=:0.0  
import matplotlib  
matplotlib.use('Agg')  

参考：https://stackoverflow.com/questions/37604289/tkinter-tclerror-no-display-name-and-no-display-environment-variable?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa  





