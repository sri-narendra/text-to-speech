import sys
import json
from gtts import gTTS
import io
import base64

def main():
    try:
        # Read and parse input
        input_data = json.load(sys.stdin)
        text = input_data.get("text")
        lang = input_data.get("language", "en")
        
        if not text:
            raise ValueError("Text parameter is required")

        # Generate speech
        tts = gTTS(text=text, lang=lang)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        # Prepare response
        response = {
            "audio": base64.b64encode(audio_buffer.read()).decode("utf-8"),
            "language": lang,
            "text_length": len(text)
        }
        
        print(json.dumps(response))

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
