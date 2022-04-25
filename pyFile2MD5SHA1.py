#coding=UTF-8
# XingHe Studio File to MD5 and SHA1
# 星河创作室(XingHeStudio.com)
# Create by Stream.Wang 2012-04-10
# Modify by Stream.Wang 2012-08-19

def fil_changefileext(filename,extname=''):
    # FIL ChangeFileExt 改变文件扩展名
    # filename    输入的文件路径名
    # extname=''  要更改分扩展名，如 .txt
    import os
    try:
        if extname[0]<>'.':
            extname='.'+extname
    except:
        extname=''
    if os.path.splitext(filename)[1]=='':
        uouttxt=filename+'.'+extname
    elif os.path.splitext(filename)[1]=='.':
        uouttxt=filename+extname    
    else:
        uouttxt=filename[:0-len(os.path.splitext(filename)[1])]+extname
    return uouttxt

def fil_str2file(fstr,filename):
    # FIL STR2File 把字符串保存到文件 
    try:
        outfile=open(filename,'w')
        outfile.writelines(fstr)
        outfile.close()
        return True    
    except:
        return False

#系统主程序开始
#-------------------------------------------------------
if __name__ == '__main__':    
    import os,sys,math
    #if len(sys.argv)==1 : sys.argv.append(r'd:\Root.Disk\Disk.Download\Temp\FreeNAS-8.0.4-RELEASE-x64.iso')
    #if len(sys.argv)==2 : sys.argv.append('t:')
    print r'Help:'
    print r'    pyFile2MD5SHA1.EXE [inFile] [output Path]'
    print r'    Example: pyFile2MD5SHA1.EXE "c:\test.iso" "d:\" '
    print r'          or pyFile2MD5SHA1.EXE "c:\test.iso" '
    print r''
    try:
        if len(sys.argv)>1:
            filepathname=sys.argv[1]
            if os.path.isfile(filepathname) :
                fmaxs = os.path.getsize(filepathname) + 0.00 #文件大小
                fpos = 0.00 #文件读取指针
                fbfs= 1024*512 #文件读取缓冲大小
                ppos=0 #文件读取百分比
                pmax=80.00 - len('[] Done! ') #最大进度条字符长度
                poutstr='*'* 1 #进度条部长
                pjy=0 #输出计数          
                ffm=os.path.basename(filepathname) #输入文件名
                ffp=str(os.path.dirname(filepathname)) #输入文件路径
                if ffp[-1]<> '\\' :ffp=ffp+'\\'
                print 'Program Runing "'+ffm+'" ...'
                #处理输出路径
                try:
                    ofp=sys.argv[2]
                except:
                    ofp=None  
                if ofp <> None :
                    if os.path.isdir(ofp)<>True:
                        ofp=ffp
                        print 'Output path Error ! Correct the default Setup .'
                else:
                    ofp=ffp
                if ofp[-1]<> '\\' :ofp=ofp+'\\'                    
                print 'MD5 and SHA1 output Path is "'+ofp+'"'            
                #生成输出文件名
                fmd5=fil_changefileext(ffm,'.md5') #md5输出路径名
                fsha1=fil_changefileext(ffm,'.sha') #sha1输出路径名
                #开始处理
                import hashlib
                try:
                    umd5str = hashlib.md5()
                    usha1str = hashlib.sha1()
                    xfilepathname=unicode(filepathname,'utf8')
                    #需要使用二进制格式读取文件内容
                    ufile = file(xfilepathname,'rb')
                    sys.stdout.write("[")
                    sys.stdout.flush()
                    while True:
                        datas = ufile.read(fbfs)
                        if not datas: break
                        umd5str.update( datas )
                        usha1str.update( datas )
                        fpos=fpos+fbfs
                        if fpos>=fmaxs : fpos=fmaxs
                        ppos=int(math.floor(fpos / fmaxs * pmax ))
                        if pjy<>ppos:
                            sys.stdout.write("*"* (ppos-pjy))
                            sys.stdout.flush()
                        pjy=ppos 
                    uoutstrmd5=str(umd5str.hexdigest())
                    uoutstrsha1=str(usha1str.hexdigest())
                    ufile.close()
                    print '] Done! '
                    fil_str2file(uoutstrmd5+'    *'+ffm,ofp+fmd5)
                    fil_str2file(uoutstrsha1+'    *'+ffm,ofp+fsha1)
                    print 'Task is completed !' + r' [ XingHe Studio File to MD5 and SHA1 ]'                
                except:        
                    print 'Error !' + r' [ XingHe Studio File to MD5 and SHA1 ]'
            else:
                print 'File "'+filepathname+'" not exist!'+ r' [ XingHe Studio File to MD5 and SHA1 ]'
        else:
            print  r' [ XingHe Studio File to MD5 and SHA1 ]'
    except: r' [ XingHe Studio File to MD5 and SHA1 ]'