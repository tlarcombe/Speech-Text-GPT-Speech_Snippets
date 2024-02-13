def text_to_speech(text: str, gender: str = Gender.FEMALE.value) -> None:
    engine = pyttsx3.init()

    engine.setProperty("rate", WORDS_PER_MINUTE_RATE)
    voices = engine.getProperty("voices")
    voice_id = voices[0].id if gender == "male" else voices[1].id
    engine.setProperty("voice", voice_id)

    engine.say(text)
    engine.runAndWait()
