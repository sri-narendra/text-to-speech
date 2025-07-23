import sys
import json
import base64
from gtts import gTTS
import io

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        text = input_data.get("text")
        language = input_data.get("language", "en")
        
        if not text:
            print("Error: Text parameter is required", file=sys.stderr)
            exit(1)

        # Generate speech
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save to bytes buffer
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        # Return as base64
        audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")
        
        # Output must be printed as JSON
        print(json.dumps({
            "audio": audio_base64,
            "text_length": len(text),
            "language": language
        }))

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
