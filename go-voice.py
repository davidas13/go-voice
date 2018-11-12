# Created By: DavidWong

from gtts import gTTS
import os
import re
import sys


lang = 'id'

def main():
    if len(sys.argv) == 3:
        fileVoice = sys.argv[1]
        dirOutput = sys.argv[2]

        if os.path.basename(fileVoice).split('.')[1] == 'txt':
            try:
                with open(fileVoice) as file:  
                    data = file.readlines()  
                    patt = re.compile(r'([\w\s\-\_][^\n]+)')
                    output = patt.search(data[0])

                    if output:
                        dirSave = os.path.join(dirOutput, output.group())
                        # os.mkdir(dirSave)
                        try:
                            dirAm = [dr for dr in os.listdir(dirOutput) if output.group() in dr ]
                            print(dirSave)
                            if not os.path.isdir(dirSave):
                                os.mkdir(dirSave)
                            else:
                                dirSave = str(dirSave) + ' ({})'.format(len(dirAm)+1)
                                os.mkdir(dirSave)
                                
                            for line in range(len(data)):
                                print(data[line])
                                tts = gTTS(data[line], lang=lang)
                                tts.save('{}/{}_{}.mp3'.format(dirSave, output.group(),line))
                        except WindowsError:
                            print('> Tidak bisa menemukan path yang dituju!')
            except IOError:
                print('> Tidak Menemukan File: "{}"'.format(fileVoice))
if __name__ == '__main__':
    main()