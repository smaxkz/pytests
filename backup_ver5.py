import os
import time
import zipfile

source = '/home/user/Code'
target_dir = '/home/user/Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M')

comment = input('Введите комментарий --> ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

archDirName = ''
zip_command = zipfile.ZipFile(target, 'w')
for dir, subdirs, files in os.walk(source):
    archDirName = '/'.join([archDirName, os.path.basename(dir)]).strip('/')
    zip_command.write(dir, archDirName)
    for file in files:
        archFileName = archDirName + '/' + file
        zip_command.write(os.path.join(dir, file), archFileName)
zip_command.close()
print('Резервная копия успешно создана в', target)
