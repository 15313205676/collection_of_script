#此脚本用于批量改对接文件夹中的文件路径
# -*- coding: UTF-8 -*-

import os,sys,re
#获取当前文件路径
path=os.getcwd()
#获取当前目录下的文件夹
dir_list=os.listdir()
#遍历当前目录
for i in dir_list:
    target_path=path+'/'+i
    if os.path.isdir(target_path):
    #改变当前目录
        os.chdir(target_path)
        lst_file=target_path+'/'+'bestranking.lst'
        f=open(lst_file,'r')
        text=f.read()
        #修改文本内容
        change_text=re.sub(r'./second_',target_path+'/second_',text)
        #输出文本内容
        f_new=open('change_'+i+'.lst','w+')
        f_new.write(change_text)
        f.close()
        f_new.close()
        print(i+' finished')
print('Work is done')
