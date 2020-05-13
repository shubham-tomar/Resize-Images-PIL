from PIL import Image
from glob import glob
import pandas as pd

class resize_img():

    def __init__(self):

        folderpath = "C:\\Users\\shubham\\Pictures"
        allfiles = glob(folderpath + "/*")
        # print(allfiles)
        imgdataset = []
        for f in allfiles:
            picFolderPath = []
            picFolderPath.extend(glob(f+'\\images/*'))
            # print(picFolderPath)
            # print(f)
            imgdataset.extend(self.resizeImages(picFolderPath,f))

        # print(imgdataset)
        IMGData = pd.DataFrame(data = imgdataset, columns=['Name','Size']) # Dataset to get the idea about avg. size of pictures
        # print(IMGData)
        #IMGData.to_csv('ImageDetails.csv')

    # Main Function******************************************************************
    
    def resizeImages(self,imagesPath,folderPath):

        imgNameList = []
        for img in imagesPath:
            tempList = []
            image = Image.open(img)
            imgname = img.split('\\')[-1]
            try:
                imgtype = img.split('_')[1]
            except:
                imgtype = 'logo.png'
            tempList.append(imgname)
            tempList.append(image.size)
            imgNameList.append(tempList)

            print(image.mode,image.format,imgname,imgtype,image.size)
            try:
                if imgtype == 'brand':
                    
                    ### Main work Starts Here
                    
                    w = 900  # Desired width 
                    wpercent = (w / float(image.size[0]))  
                    #New Height for desired width to maintain aspect ratio
                    hsize = int((float(image.size[1]) * float(wpercent))) 
                    nimg = image.resize((w,hsize))
                    print(nimg.size)
                    nimg.save(folderPath+'\\images\\resize_'+imgname)
                elif imgtype == 'logo.png':
                    w = 100
                    wpercent = (w / float(image.size[0]))
                    hsize = int((float(image.size[1]) * float(wpercent)))
                    nimg = image.resize((w,hsize))
                    print(nimg.size)
                    nimg.save(folderPath+'\\images\\resize_'+imgname)
                else:
                    w = 400
                    wpercent = (w / float(image.size[0]))
                    hsize = int((float(image.size[1]) * float(wpercent)))
                    nimg = image.resize((w,hsize))
                    print(nimg.size)
                    nimg.save(folderPath+'\\images\\resize_'+imgname)
            except Exception as e:
                print('Exception Error :',e)
                continue
        return imgNameList


resizeObj = resize_img()
