import os,struct

HEAD_STRUCT='=lq'
TRACK_NUM = 9999
FILE_NUM = 33

now_path = os.getcwd()
path = raw_input('Please set your file path:')
fw = open("DataCollect.txt",'w')
os.chdir(path)
for n in range(0,FILE_NUM):
    fileName = str("%02d" % n )+'.dat'
    if os.path.exists(fileName):
        print fileName +'is exist\n'
        fr = open(fileName,'rb')
        os.chdir(now_path)
        fw.write(fileName+':\n')
        fw.write('------------------------\n')
        os.chdir(path)
        for m in range(0,TRACK_NUM):
            (count,time)=struct.unpack(HEAD_STRUCT,fr.read(4+8))
            if(count):
                print "track:%d\t,count:%d,\ttime:%d"%(m,count,time)
                fw.write("track:%d\t,count:%d,\ttime:%d\n"%(m,count,time))  
        fr.close()
        fw.write('\n')
    else:
        print fileName +'is not exist\n'
    print'\n'
fw.close() 
os.system("pause")
