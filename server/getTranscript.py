from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import time


def get_time(time):
   time = (int)(time)
   return (str)(time // 60) + ":" + (str)(time % 60) 

def format_transcript(transcript):
    # format the transcript
    formatted_transcript = TextFormatter().format_transcript(transcript)
    return formatted_transcript.replace("\n", " ")

def get_transcript(video_id):
    
    start_time = time.time()
    # Get the transcript.
    transcript__list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = None
    
    num_transcript = len(list(transcript__list))
    if num_transcript >= 1:
        defualt_transcript = transcript__list.find_transcript(['en']) # find the English transcript
        transcript = defualt_transcript.fetch() # list of dictionaries
    else:
        return transcript

    end_time = time.time()
    print("time to get transcript: " + str(end_time - start_time))
    return format_transcript(transcript)


def translate_transcript(transcript , language):
    # translate the transcript
    translated_transcript = transcript.translate(language)
    return translated_transcript


