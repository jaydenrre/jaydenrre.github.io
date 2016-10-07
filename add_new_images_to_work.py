import glob, os
import unicodedata

def addImgs(fileName, imgFolderDir): # name of file to get new images, folder of new images
    imgsInFolder = [] #list the images in the folder
    for pathAndFilename in glob.iglob(os.path.join(imgFolderDir, '*.JPG')): #cycle through filenames in folder
        name, ext = os.path.splitext(os.path.basename(pathAndFilename))
        imgsInFolder.append(name+ext) #add the names to the list
    
    imgsInFile = [] #list of images in existing file
    reading = open(fileName, 'r') #file being read
    newFileName = 'moded_'+fileName.split('\\')[-1]

    writing = open(newFileName, 'w') #file being created
    
    lines = reading.readlines() #list of all the lines in the file
    bookmarkAt = 0
    for i in range(len(lines)): 
        if '<!--bookmark-->' in lines[i]: #check for tracer
            print('bookmark at index '+str(i))
            bookmarkAt = i
            break # a break is needed else the loop will continue after the bool change and write the bookmark in to the new file
        writing.write(lines[i]) #write lines, not tracer then write
        if '<img' in lines[i].split(): # if it is an image line add it to the list
            imgsInFile.append(lines[i].split()[1].split('/')[-1].replace('"',''))
            #Keep only whats after the slash and replace the " with blank
            #bookmark is not added so that after new data is written it can be written on to the new file
    ## up to now the moded_ file is rewriten up to the bookmark
    ## now we need to add HTML text containg all the pics that are not in the file
    imgsToAdd = list(set(imgsInFolder)-set(imgsInFile)) # imgs in folder will allways be biger than images in HTML file since we are adding pics
    for imgName in imgsToAdd:
        writing.write('''
                <div class="slide">
					<div class="inSlide">
						<img src="''' 'images\\'+ imgName +'''" />
						<div>'''+ imgName.split('.')[0].replace('_',' ').title() + '''</div> 
						<div> | </div>
						<div>combustion ???????? on cotton paper</div>
					</div>
				</div>
        ''') # swap _ with spaces and make all first chars caps
    # writing.write('<!--bookmark-->') # at the end of the images add the new tracer
    
    # new html text added to moded_ file
    for line in lines[bookmarkAt:]: 
        writing.write(line)
    writing.close()



    
def rename(imgFolderDir):  # renameing function to special chars,accents and spaces
    newNames = [] #make a list to see results
    for pathAndFilename in glob.iglob(os.path.join(imgFolderDir, '*.jpg')): #cycle through files in the folder
        name, ext = os.path.splitext(os.path.basename(pathAndFilename)) #create name and extension vars
        nfkd_form = unicodedata.normalize('NFKD', name) #work on the strings...idk
        newName = "".join([c for c in nfkd_form if not unicodedata.combining(c)]).replace(' ', '_') #from the worked string remove accents, and replace spaces for _
        newNames.append(name+ext) #add the new name to the list of names
        #os.rename(pathAndFilename, newName+ext) #change the file names
    print(newNames)
    
        
    
    #make a list of paths of pics in pics polder
    #read html doc till tracer
    #list all pic paths
    #remove tracer
    #for pics in folders and not in html pics:
        #insert text at tracer with pic path and title
    #add tracer
    #save and close



def main():
    fileName = os.path.join(os.path.dirname(__file__),'work.html')
    imgFolderDir = os.path.dirname(os.path.realpath(__file__))+'\images'
    # print('working in: '+ imgFolderDir)
    addImgs(fileName,imgFolderDir)
    #rename(imgFolderDir)
    #input("testing")

main()


# def rename(dir, pattern, titlePattern):
#     for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
#         title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#         os.rename(pathAndFilename, 
#                   os.path.join(dir, titlePattern % title + ext))
