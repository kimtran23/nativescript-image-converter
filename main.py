import os
import shutil

conversion = raw_input('Which folder would you like to create? [1 for Android, 2 for iOS]: ')

if conversion != '1' and conversion != '2':
    print('Invalid input')
else:
    path = raw_input('Enter path to image folder (ex: ~/Desktop/Image): ')
    src = os.path.expanduser(path)
    counter = 0

    if conversion == '1':
        dest = src + '/android'

        # Delete main android folder if it already exists
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        
        # Create main android folder
        os.mkdir(dest)

        # Create subfolders
        low = dest + '/drawable-ldpi'           # 0.75x
        medium = dest + '/drawable-mdpi'        # 1x
        high = dest + '/drawable-hdpi'          # 1.5x
        xhigh = dest + '/drawable-xhdpi'        # 2x
        xxhigh = dest + '/drawable-xxhdpi'      # 3x
        xxxhigh = dest + '/drawable-xxxhdpi'    # 4x

        os.mkdir(low)
        os.mkdir(medium)
        os.mkdir(high)
        os.mkdir(xhigh)
        os.mkdir(xxhigh)
        os.mkdir(xxxhigh)
        
        # Iterate through each file and copy it to its corresponding Android folder
        for f in os.listdir(src):
            if f.endswith('.png') and '@' in f:
                fname = f.split('@')[0]
                size = f.split('@')[1].rsplit('.', 1)[0]

                if size == '0.75x':
                    shutil.copy(src + '/' + f, low + '/' + fname + '.png')
                    counter += 1
                elif size == '1x':
                    shutil.copy(src + '/' + f, medium + '/' + fname + '.png')
                    counter += 1
                elif size == '1.5x':
                    shutil.copy(src + '/' + f, high + '/' + fname + '.png')
                    counter += 1
                elif size == '2x':
                    shutil.copy(src + '/' + f, xhigh + '/' + fname + '.png')
                    counter += 1
                elif size == '3x':
                    shutil.copy(src + '/' + f, xxhigh + '/' + fname + '.png')
                    counter += 1
                elif size == '4x':
                    shutil.copy(src + '/' + f, xxxhigh + '/' + fname + '.png')
                    counter += 1
                else:
                    print(f + ' does not have a recognizable size and was therefore not copied')
            else:
                print(f + ' does not have a supported naming convention and was therefore not copied')

        print(str(counter) + ' images successfully copied to ' + dest)

    elif conversion == '2':
        dest = src + '/iOS'

        if os.path.isdir(dest):
            shutil.rmtree(dest)

        # Create main iOS folder
        os.mkdir(dest)

        # Iterate through each Android subfolder to retrieve the files
        for root, dirs, files in os.walk(src):
            folder = root.rsplit('/', 1)[1]

            if folder.startswith('drawable-'):
                if folder == 'drawable-ldpi':
                    size = '@0.75x'
                elif folder == 'drawable-mdpi':
                    size = '@1x'
                elif folder == 'drawable-hdpi':
                    size = '@1.5x'
                elif folder == 'drawable-xhdpi':
                    size = '@2x'
                elif folder == 'drawable-xxhdpi':
                    size = '@3x'
                elif folder == 'drawable-xxxhdpi':
                    size = '@4x'
                
                for f in files:
                    fname = f.rsplit('.', 1)[0]
                    shutil.copy(os.path.join(root, f), dest + '/' + fname + size + '.png')
                    counter += 1

        print(str(counter) + ' images successfully copied to ' + dest)
