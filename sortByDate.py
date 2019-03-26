import sys, glob, os, time

files=glob.glob("*")
if sys.argv[0] == "sortByDate.py":
    files.sort(key=os.path.getmtime, reverse=False)

elif sys.argv[1] == "asc":
    files.sort(key=os.path.getmtime, reverse=False)

elif sys.argv[1] == "desc":
    files.sort(key=os.path.getmtime, reverse=True)

for file in files:
    dateString = dateString=time.strftime('%H: %M: %S: %m/ %d/ %Y',
    time.gmtime(os.path.getmtime(file)))
    print (file,dateString)
