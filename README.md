# JustTranslateAndSubtile

This Repository can be used to transcribe a mp4 video.
It uses forks of whisper AI from openai, including faster-whisper and whisper-ctranslate2

# Installation

- Clone this repo :
```
git clone https://github.com/JustAlternate/JustTranslateAndSubtile
```

- Install and create a python3.10 virtualenv :

```
pip install virtualenv
virtualenv -p python3.10 myenv
source myenv/bin/activate
```
- Install all required python3.10 packages :

```pip install -r requirements.txt```

- Make sure you have ffmpeg installed in your system :

Arch Linux : `pacman -S ffmpeg`

Macos : `brew install ffmpeg`

Ubuntu : `apt-get install ffmpeg`

Windows : `consider switching to linux bro.`

# Usage

You will have to first choose a model for whisper to use.

## Official whisper models

This is a list of models you can use :

- small
- medium    <--- I recommend
- large-v1
- large-v2  <--- Slower but more consistent

Lets try and transcribe the example.mp4 file I gave you.

## We split the audio from the video using ffmpeg : 

```
ffmpeg -i example.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav
```

## We transcribe the output.wav audio file into a srt file which will contain the subtitles. /!\ this can take a very long time.

```
whisper-ctranslate2 --device cpu --compute_type int8 --threads 6 --language fr --task transcribe --output_format srt --model large-v2 output.wav --word_timestamps True --max_line_width 50 --max_line_count 1
```

You can use `whisper-ctranslate2 --help` if you want to change this command as your need.

## Then we can translate the srt file : (OPTIONAL)

/!\ You need a deepl API key for this.

```
python translate.py output.srt translated_srt_file.srt EN-US
```
You can find a list of all available languages on the deepl API documentation.

## Take a look at your subtitles

You can either directly look at the `translated_srt_file.srt` created to see your translated subtitles.

Or you can use vlc to watch your video with the desired subtitles :

```
vlc --sub-file translated_srt_file.srt example.mp4
```

# Using a unofficial model from huggingface.co

If you want to use a model from huggingface you will first have to convert it to be used by whisper-ctranslate2 :
```
ct2-transformers-converter --model <author/model> --output_dir <model> --copy_files tokenizer.json --quantization int8 --force
```

Replace <author/model> by for example : `pierreguillou/whisper-medium-french` and make sure to copy the right tokenizer file.
For the quantization consider replacing int8 with float16 if you want to use your GPU to transcribe rather than your CPU

