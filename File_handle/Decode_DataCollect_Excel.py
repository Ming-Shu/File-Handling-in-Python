import os,struct,xlwt

HEAD_STRUCT='=lq'
TRACK_NUM = 9999+1
FILE_NUM = 32+1

now_path = os.getcwd()
path = raw_input('Please set your folder path:')
fw = open("DataCollect.txt",'w')
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Statistics",cell_overwrite_ok=True)

os.chdir(path)
for n in range(0,FILE_NUM):
    fileName = str("%02d" % n )+'.dat'
    if os.path.exists(fileName):
        print fileName +' is exist\n'
        fr = open(fileName,'rb')
        os.chdir(now_path)
        fw.write(fileName+':\n')
        fw.write('------------------------\n')
        os.chdir(path)
        a=0
        for m in range(0,TRACK_NUM):
            (count,time)=struct.unpack(HEAD_STRUCT,fr.read(4+8))
            sheet1.write(0, 0+n*4, fileName)
            sheet1.write(2, 0+n*4, "Track NO")
            sheet1.write(2, 1+n*4, "Count")
            sheet1.write(2, 2+n*4, "Time(s)")
            sheet1.write(2, 3+n*4, " ")
            if(count and m>0):
                print "track:%d ,count:%d, time:%d"%(m,count,time)
                fw.write("track:%d ,count:%d, time:%d\n"%(m,count,time))
                sheet1.write(a+3,0+n*4,m)
                sheet1.write(a+3,1+n*4,count)
                sheet1.write(a+3,2+n*4,time)
                sheet1.write(a+3,3+n*4, " ")
                a=a+1
            elif(m==0):
                print "Total language count:%d"%(count)
                print'------------------------\n'
                fw.write("Total language count:%d\n" % count)
                fw.write('------------------------\n')
                sheet1.write(1, 0+n*4, "Total:")
                sheet1.write(1,1+n*4,count)
        fr.close()
        fw.write('\n')
    else:
        print fileName +' is not exist\n'
    print'\n'
fw.close()
os.chdir(now_path)
book.save("DataCollect.xls")
os.system("pause")
