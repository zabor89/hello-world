from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

#def show_files_by_date(dir):
#    entrys = sorted(entrys, key=lambda e: e.stat().st_mtime)
#for entry in entrys:
#    print(entry.name)


#os.listdir("D:\FILIP's stuff\hello-world")
#print(os.listdir("D:\FILIP's stuff\hello-world"))
#print(os.getcwd())
#filename = input ("Enter filename: ")
#print ("The file name is: %s" % (filename) )
#listdir("D:\FILIP's stuff\hello-world")

#l = sorted(list(os.listdir()))

#print(l)
