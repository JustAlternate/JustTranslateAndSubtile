import deepl


def translate(text, lang):
    auth_key = "0cac304a-e207-914b-1d55-555c005f7bb6:fx"
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=lang)
    return result.text


def translate_srt_file(input_file, output_file, target_lang):
    # Read the original SRT file and extract the text content
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()

    # Translate the whole text
    translated_text = translate(original_text, target_lang)
    print(translated_text)

    # Save the translated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)


if __name__ == "__main__":
    input_file_path = "output.srt"
    output_file_path = "translated_srt_file.srt"
    target_language = "EN-US"  # Change this to the target language code
    translate_srt_file(input_file_path, output_file_path, target_language)
