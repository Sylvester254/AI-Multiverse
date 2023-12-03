# AI Multiverse
This is a FastAPI project that integrates various AI models from Hugging Face Hub which provide different functionalities.

As of now, the generate-image and generate-speech API endpoints are ready.

### Setup
- Clone the repo: `git clone https://github.com/Sylvester254/AI-Multiverse`
- Open terminal, create and start virtual environment i.e with pip:
  - (For Linux or Mac)`python3 -m venv myenv` then `source myenv/bin/activate`
- Install the requirements in the requirements.txt
- Head over to [Hugging Face](https://huggingface.co) and create an account, if you don't already have one, then go to 
`settings/Access Tokens` and create a new Access Token with `read` permissions.
- Copy the Access Token and go back to project.
- Create a .env file in the root directory and add the API key i.e `HUGGINGFACEHUB_API_KEY='enter your key here'`
- Run `uvicorn main:app --reload` in the terminal.
- Go to  `http://127.0.0.1:8000/docs` and test the routes with Swagger UI. Alternatively you can test using `Curl` or `Postman`

#### Image generation Demo
**Testing with Swagger UI or Postman:**
```commandline
{
  "prompt": "beautiful pale cyberpunk female with heavy black eyeliner, blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city.",
  "model": "Yntec/AbsoluteReality"
}
```
**Testing with Curl:**
```commandline
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-image/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "beautiful pale cyberpunk female with heavy black eyeliner, blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city.",
  "model": "Yntec/AbsoluteReality"
}' \
--output ./generated_image.png
```

**Output:**

![beautiful_cyberpunk_female_image](/tti-images/beautiful_pale_cyberpunk_female.png)

### text to image models:
> [stabilityai/stable-diffusion-2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1)
* Developed by: Robin Rombach, Patrick Esser
* Model type: Diffusion-based text-to-image generation model
* Language(s): English
* License: CreativeML Open RAIL++-M License
* Model Description: This is a model that can be used to generate and modify images based on text prompts. It is a Latent Diffusion Model that uses a fixed, pretrained text encoder (OpenCLIP-ViT/H).
* Resources for more information: [GitHub Repository](https://github.com/Stability-AI/).

> [stablediffusionapi/newrealityxl-global-nsfw](https://huggingface.co/stablediffusionapi/newrealityxl-global-nsfw)
  

> [Lykon/dreamshaper-8](https://huggingface.co/Lykon/dreamshaper-8)
- lykon-models/dreamshaper-7 is a Stable Diffusion model that has been fine-tuned on [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5).

> [Linaqruf/animagine-xl-2.0 ](https://huggingface.co/Linaqruf/animagine-xl-2.0)
- Animagine XL 2.0 is an advanced latent text-to-image diffusion model designed to create high-resolution, detailed anime images. It's fine-tuned from Stable Diffusion XL 1.0 using a high-quality anime-style image dataset. This model, an upgrade from Animagine XL 1.0, excels in capturing the diverse and distinct styles of anime art, offering improved image quality and aesthetics.

* Developed by: Linaqruf
* Model type: Diffusion-based text-to-image generative model
* Model Description: This is a model that excels in creating detailed and high-quality anime images from text descriptions. It's fine-tuned to understand and interpret a wide range of descriptive prompts, turning them into stunning visual art.
* License: CreativeML Open RAIL++-M License
* Finetuned from model: [Stable Diffusion XL 1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)

> [Yntec/3Danimation](https://huggingface.co/Yntec/3Danimation)

> [Yntec/AbsoluteReality](https://huggingface.co/Yntec/AbsoluteReality)

> [stablediffusionapi/realistic-vision-v51](https://huggingface.co/stablediffusionapi/realistic-vision-v51)

#### Sample prompts:
`cinematic photo, caelus, honkai: star rail, boy, solo, playing guitar, living room, grey hair, short hair, yellow eyes, downturned eyes, passionate expression, casual clothes, acoustic guitar, sheet music stand, carpet, couch, window, sitting pose, strumming guitar, eyes closed., illustration, disheveled hair, detailed eyes, perfect composition, moist skin, intricate details, bokeh, professional, 4k, highly detailed`

![boy-playing-guitar](/tti-images/boy-playing-guitar.png)
_model:Lykon/dreamshaper-8_

`4d photographic image of full body image of a cute little chibi boy realistic, vivid colors octane render trending on artstation, artistic photography, photorealistic concept art, soft natural volumetric cinematic perfect light, UHD no background.`

![4d_photographic_image_of_full_body_image](/tti-images/4d_photographic_image_of_full_body_image.png)
_model:stablediffusionapi/newrealityxl-global-nsfw_

`portrait photo of muscular bearded guy in worn mech suit, light bokeh, intricate, steel metal, elegant, sharp focus, soft lighting, vibrant colors`
![portrait_photo_of_muscular_bearded_guy](/tti-images/portrait_photo_of_muscular_bearded_guy.png)
_model:stablediffusionapi/realistic-vision-v51_

### text to speech models:

> [facebook/mms-tts-eng](https://huggingface.co/facebook/mms-tts-eng)
- Massively Multilingual Speech (MMS): English Text-to-Speech
- This repository contains the English (eng) language text-to-speech (TTS) model checkpoint.
- This model is part of Facebook's Massively Multilingual Speech project, aiming to provide speech technology across a diverse range of languages. 
- You can find more details about the supported languages and their ISO 639-3 codes in the MMS Language Coverage Overview, and see all MMS-TTS checkpoints on the Hugging Face Hub: [facebook/mms-tts](https://huggingface.co/models?sort=trending&search=facebook%2Fmms-tts).

**Demo**
- Input:
```
{
  "text": "I'm doing well, thank you for asking! I hope you are doing well too.",
  "model": "facebook/mms-tts-eng"
}
```
- Output:

[Audio facebook-mms-tts-eng](/tts-audio/Im_doing_well_thank_you_facebook-mms-tts-eng.mp3)

---
> [facebook/mms-tts-swh](https://huggingface.co/facebook/mms-tts-swh)
- Massively Multilingual Speech (MMS): Swahili Text-to-Speech
- This repository contains the Swahili (swh) language text-to-speech (TTS) model checkpoint. 
- This model is part of Facebook's Massively Multilingual Speech project, aiming to provide speech technology across a diverse range of languages. 

**Demo**
- Input:
```
{
  "text": "Siku moja, walipokuwa wanapita karibu na kijiji kimoja, Sungura alipanga mtego. Aliwaambia wanakijiji kuhusu Fisi na mpango wake. Wanakijiji waliamua kumsaidia Sungura. Walipofika karibu, Fisi alishangaa kuona wanakijiji wakimkimbilia na silaha. Alikimbia kuokoa maisha yake, akiacha Sungura akiwa salama.",
  "model": "facebook/mms-tts-swh"
}
```
- Output:

 [Audio facebook-mms-tts-swh](/tts-audio/Siku_moja_walipokuwa_wanapita-facebook-mms-tts-swh.mp3)

---
> [facebook/fastspeech2-en-ljspeech](https://huggingface.co/facebook/fastspeech2-en-ljspeech):
 - English
 - Single-speaker female voice 
 - Trained on LJSpeech

**Demo**
- Input:
```
{
  "text": "I'm doing well, thank you for asking! I hope you are doing well too.",
  "model": "facebook/fastspeech2-en-ljspeech"
}
```
- Output:

[Audio facebook-fastspeech2-en-ljspeech](/tts-audio/Im_doing_well_thank_you_for_facebook-fastspeech2-en-ljspeech.mp3)

---
> [Voicemod/fastspeech2-en-male1](https://huggingface.co/Voicemod/fastspeech2-en-male1)
 - English
 - 200 male/female voices (random speaker when using the widget)
 - Trained on Common Voice v4

**Demo**
- Input:
```
{
  "text": "I'm doing well, thank you for asking! I hope you are doing well too.",
  "model": "Voicemod/fastspeech2-en-male1"
}
```
- Output:

[Audio Voicemod-fastspeech2-en-male1](/tts-audio/Im_doing_well_thank_you_for_askingVoicemod-fastspeech2-en-male1.mp3)

---
> [espnet/english_male_ryanspeech_fastspeech2](https://huggingface.co/espnet/english_male_ryanspeech_fastspeech2)
- This model was trained by Rohola Zandie using ryanspeech recipe in espnet.

**Demo**
- Input:
```
{
  "text": "I'm doing well, thank you for asking! I hope you are doing well too.",
  "model": "espnet/english_male_ryanspeech_fastspeech2"
}
```
- Output:

[Audio espnet-english_male_ryanspeech_fastspeech2](/tts-audio/Im_doing_well_thank_you_for_espnet-english_male_ryanspeech_fastspeech2.mp3)
