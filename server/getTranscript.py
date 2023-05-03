from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def get_time(time):
   time = (int)(time)
   return (str)(time // 60) + ":" + (str)(time % 60) 

def format_transcript(transcript):
    # format the transcript
    formatted_transcript = TextFormatter().format_transcript(transcript)
    return formatted_transcript


def get_transcript(video_id):
    """
    This function takes a YouTube video ID and returns the transcript.

    Args:
        video_id: The YouTube video ID.

    Returns:
        The transcript.
    """
    # words that are not part of the transcript
    NON_TRANSCRIPT_WORDS = ["[Music]", "[Applause]", "[Laughter]",
                            "[Music Playing]", "[Music playing]", "[music]", 
                            "[applause]", "[laughter]", "[music playing]", "[Music playing in background]", 
                            "[music playing in background]", "[Music Playing In Background]", "[Music Playing in Background]",
                            "[Music playing in background]", "[Music Playing in background]", "[Music playing in the background]",
                            "[Music Playing in the background]", "[Music playing in the background]", "[Music Playing In The Background]",
                            "[Music playing in the background]", "[Music Playing in the background]", "[Music playing in the background]", 
                            "[Music Playing In The Background]", "[Music playing in the background]", "[Music Playing in the background]", 
                            "[Music playing in the background]", "[Music Playing In The Background]", "[Music playing in the background]", 
                            "[Music Playing in the background]", "[Music playing in the background]", "[Music Playing In The Background]"]

    # Get the transcript.
    transcript__list = YouTubeTranscriptApi.list_transcripts(video_id)
    
    num_transcript = len(list(transcript__list))
    if num_transcript >= 1:
        defualt_transcript = transcript__list.find_transcript(['en']) # find the English transcript
        transcript = defualt_transcript.fetch() # list of dictionaries
    else:
        transcript = None
        return transcript

    # Remove non-transcript text.
    cleaned_transcript = []
    for line in transcript:
        text = line["text"]
        if not any(w in text.lower() for w in NON_TRANSCRIPT_WORDS):
            cleaned_transcript.append(line)

    return format_transcript(cleaned_transcript)



def translate_transcript(transcript , language):
    # translate the transcript
    translated_transcript = transcript.translate(language)
    return translated_transcript




print(get_transcript('irGpkX9xHVg'))


