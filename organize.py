import os
import time
import sys


#Defined File Types
filetypes = {
    "images": [
        "jpeg","png","gif","bmp","tiff","svg","webp","ico","psd"
    ],
    "documents": [
        "pdf","txt","doc","docx","xls","xlsx","ppt","pptx","odt","ods","odp","csv","rtf","html","htm","xml","swf","eot","ttf","woff","woff2","json","yml","yaml","log","md","sql","py"
    ],
    "audio": [
        "mp3","wav","aac","ogg","wma","m4a","flac","aiff","alac"
    ],
    "video": [
        "mp4","avi","mov","wmv","mpg","ogv","3gp","3g2","mkv","flv","m4v"
    ],
    "archives": [
        "zip","rar","7z","tar","gz","bz2","tgz"
    ]
}

#Geting path
currentpath = os.getcwd()


#Defined Variables
errorfiles = []
successcount =0
filecount =1



#Showing The ProgressBar
def progressbar(total,current):
    percent = (current/total)*100
    sys.stdout.write("\r[{0:50s}] {1:.1f}%".format('#'*int(percent/2),percent))
    sys.stdout.flush()



value = sys.argv
if(len(value)>=2):

    if(value[1] == "--current"):
        currentpath = currentpath
    elif(value[1]=="--help"):
        print("""
Usage: organize.py [options]

Options:
    --current : Use the current directory
    --help    : Show this help message and exit
    """)
        sys.exit()
else:
    currentpath =input("Enter the path: ")



if(currentpath[0] == "/"):
    
    
        path = currentpath
        all = os.listdir(path)
        for x in all:
            progressbar(len(all),filecount)
            filecount=filecount+1
            if os.path.isdir(path + "/" + x):
                successcount=successcount
            else:

                try:
                    if(x.split('.')[-1] in filetypes['images']):
                        try:
                            os.mkdir(path + "/" + "IMAGES")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "IMAGES" + "/" + x)

                    elif(x.split('.')[-1] in filetypes['documents']):
                        try:
                            os.mkdir(path + "/" + "DOCUMENTS")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "DOCUMENTS" + "/" + x)

                    elif(x.split('.')[-1] in filetypes['audio']):
                        try:
                            os.mkdir(path + "/" + "AUDIO")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "AUDIO" + "/" + x)
                    
                    elif(x.split('.')[-1] in filetypes['video']):
                        try:
                            os.mkdir(path + "/" + "VIDEO")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "VIDEO" + "/" + x)
                    
                    elif(x.split('.')[-1] in filetypes['archives']):
                        try:
                            os.mkdir(path + "/" + "ARCHIVES")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "ARCHIVES" + "/" + x)
                    else:
                        try:
                            os.mkdir(path + "/" + "OTHERS")
                        except:
                            seccesscount = successcount+1
                        os.rename(path + "/" + x, path + "/" + "OTHERS" + "/" + x)
                except Exception as e:
                    errorfiles.append(x)
else:
    #Format Path For Working On Windows
    path = currentpath.replace("\\", "\\\\")

    all = os.listdir(path)


    for x in all:
        progressbar(len(all),filecount)
        filecount=filecount+1
        if os.path.isdir(path + "\\" + x):
            successcount=successcount
        else:

            try:
                if(x.split('.')[-1] in filetypes['images']):
                    try:
                        os.mkdir(path + "\\" + "IMAGES")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "IMAGES" + "\\" + x)

                elif(x.split('.')[-1] in filetypes['documents']):
                    try:
                        os.mkdir(path + "\\" + "DOCUMENTS")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "DOCUMENTS" + "\\" + x)

                elif(x.split('.')[-1] in filetypes['audio']):
                    try:
                        os.mkdir(path + "\\" + "AUDIO")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "AUDIO" + "\\" + x)
                
                elif(x.split('.')[-1] in filetypes['video']):
                    try:
                        os.mkdir(path + "\\" + "VIDEO")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "VIDEO" + "\\" + x)
                
                elif(x.split('.')[-1] in filetypes['archives']):
                    try:
                        os.mkdir(path + "\\" + "ARCHIVES")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "ARCHIVES" + "\\" + x)
                else:
                    try:
                        os.mkdir(path + "\\" + "OTHERS")
                    except:
                        seccesscount = successcount+1
                    os.rename(path + "\\" + x, path + "\\" + "OTHERS" + "\\" + x)
            except Exception as e:
                errorfiles.append(x)

print("  TASK COMPLETED\n")


if(len(errorfiles)>0):
    print("Error while geting these files\n\n")
    for x in errorfiles:
        print(x)

