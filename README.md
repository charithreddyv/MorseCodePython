# MorseCodePython
A Simple Application to convert Text to MorseCode(with Audio)

![alt text](https://github.com/charithreddyv/MorseCodePython/blob/master/Morse_Code/International_Morse_Code.svg)

The application converts given input string of English characters , numerics and some special characters into MorseCode in characters and also plays  the audio for each character

if the input character is not found then it is denoted with a `/`

In this application a ```"dit" is denoted by "." ``` and a ```"dah" is denoted by "-"```

#setup

* Create a virtualenv  and activate it 

  ``` virtualenv <env_name>/bin/activate ```

* Installing the dependencies

  ``` pip install -r requirements.txt ```

* For some os's we need ffmpeg for decoding the audio files (for ubunut or most of the linux bases ) :

  ```sudo apt install ffmpeg``` [other os's](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
  
  Source for all the MorseCode audio and images [wikipedia](https://en.wikipedia.org/wiki/Morse_code)

