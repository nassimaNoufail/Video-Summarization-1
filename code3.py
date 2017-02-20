ffmpeg -i m1.mp4 m1.wav
sox m1.wav m2.wav trim 0 10
sox m2.wav leftchannel.wav remix 1
sox leftchannel.wav -r 16000 m3.wav
pocketsphinx_continuous -infile m3.wav
