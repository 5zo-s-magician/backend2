#!/usr/bin/env python
# coding: utf-8

from pydub import AudioSegment
import os
import base64
from mutagen.mp3 import MP3
from IPython.display import Audio

def audio_cut(base_mp3_file, member_part):
  mp3_file = open("soundtrack.mp3", "wb")
  decode_string = base64.b64decode(open(base_mp3_file, "rb").read())
  mp3_file.write(decode_string)
  audio = MP3("soundtrack.mp3")
  end_time =  audio.info.length
  mp3_file.close()

  # 멤버별 파트 set list를 리스트화 시키기
  timetrack = [0]
  for i in range(len(member_part)):
    timetrack.append(list(member_part)[i][0]*1000)
    timetrack.append(list(member_part)[i][1]*1000)
  timetrack.append(end_time*1000)
  print(timetrack)

  #음원 편집 용 파트!!!!
  # Opening file and extracting segment
  song = AudioSegment.from_file("soundtrack.mp3")

  for i in range(len(timetrack)-1):
    #timetrack에서 index 0부터 (0,1) (1,2) ... 식으로 잘라내고 saving 까지
    extract = song[timetrack[i]:timetrack[i+1]]
    #저장명은 곡명-extract+몇번째조각인지.mp3
    extract.export("soundtrack"+str(i)+".mp3", format="mp3")

  # print(str(i)+"번째 조각 잘라내기")
    if i == len(timetrack):
      break

  #print("음원 segment 잘라내기 완료")

  for i in range(len(timetrack)-1):
    if i % 2 == 1:
      str1 = "soundtrack"+str(i)+".mp3"
      Audio(str1)
      os.system("python -m spleeter separate -h")
      os.system("python -m spleeter separate -o output/ "+str1)
  print("끝")

  # 이렇게 하면               output/benatural/vocals.wav
  # 홀수번째 파일에 대해서만  output/benatural/accompaniment.wav 파일 두개 생김
  #위에 애들을 voice conversion에 넣어주려고 저장하는 코드..!!!!

  for g in range(len(timetrack)-1):
    if g % 2 == 1:
      file_name = "soundtrack"+str(g)
      vocals = AudioSegment.from_file("output/"+file_name+"/vocals.wav")
      vocals.export( file_name+'-vocals.wav', format="wav")

      mrs = AudioSegment.from_file("output/"+file_name+"/accompaniment.wav")
      mrs.export( file_name+'-mrs.wav', format="wav")
  return timetrack
