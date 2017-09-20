1、在处理csv文件时，发现有部分的数据会自动换行，文件放到linux下，就会被认为是多行；  
解决方法：使用pandas模块进行处理  
import pandas as pd  
fp = pd.read_csv('test.csv')  

pandas会识别这样的换行，不会认为是新的一行  
