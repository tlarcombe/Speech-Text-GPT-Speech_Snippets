#!/bin/python

async def get_transcript(audio_file_path: str, 
                         text_to_draw_while_waiting: str) -> Optional[str]:
    openai.api_key = os.environ.get("OPENAI_API_KEY") ## Define your OpenAI API key as a system variable
    audio_file = open(audio_file_path, "rb")
    transcript = None

    async def transcribe_audio() -> None:
        nonlocal transcript
        try:
            response = openai.Audio.transcribe(
                model="whisper-1", file=audio_file, language="en")
            transcript = response.get("text")
        except Exception as e:
            print(e)

    draw_thread = Thread(target=print_text_while_waiting_for_transcription(
        text_to_draw_while_waiting))
    draw_thread.start()

    transcription_task = asyncio.create_task(transcribe_audio())
    await transcription_task

    if transcript is None:
        print("Timeout :-(.")

    return transcript
