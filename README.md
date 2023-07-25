# JustTranslateAndSubtile

This Repository can be used to transcribe a mp4 video.
It uses forks of whisper AI from openai, including faster-whisper and whisper-ctranslate2

# Installation

- Clone this repo :
```git clone https://github.com/JustAlternate/JustTranslateAndSubtile```

- Install and create a python3.10 virtualenv :

```pip install virtualenv```  
```virtualenv -p python3.10 myenv```  
```source myenv/bin/activate```  

- Install all required python3.10 packages :

```pip install -r requirements.txt```

- Make sure you have ffmpeg installed in your system :

Arch Linux : `pacman -S ffmpeg`

Macos : `brew install ffmpeg`

Ubuntu : `apt-get install ffmpeg`

Windows : `consider switching to linux bro.`

# Usage

Now everything should be good to go.

You will have to first choose a model for whisper to use.

This is a list of models you can use :

Official whisper models :
- small
- medium  <--- I recommend
- large-v1
- large-v2 <--- Slower but more consistent

Lets try and transcribe the example.mp4 file I gave you.

1) We split the audio from the video using ffmpeg : 

```ffmpeg -i example.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav```

2) We transcribe the output.wav audio file into a srt file which will contain the subtitles. /!\ this can take a very long time.

```
whisper-ctranslate2 --device cpu --compute_type int8 --threads 6 --language fr --task transcribe --output_format srt --model medium output.wav --word_timestamps True --max_line_width 40 --max-line-count 1
```

You can use `whisper-ctranslate2 --help` if you want to change this command as your need.

# Using a unnofficial model from huggingface.co

If you want to use a model from huggingface you will first have to convert it to be used by whisper-ctranslate2 :
```ct2-transformers-converter --model <author/model> --output_dir <model> --copy_files tokenizer.json --quantization int8 --force```

Replace <author/model> by for example : pierreguillou/whisper-medium-french and make sure to copy the right tokenizer file.
For the quantization consider replacing int8 with float16 if you want to use your GPU to transcribe rather than your CPU

