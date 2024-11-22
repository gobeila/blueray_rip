from collections import defaultdict

from model.stream import Stream


class Title:

    def __init__(self, disc_title = "", chapters_count = "", length_of_chapter = "", file_size_human = "", file_size_bytes = "", file_name = "", audio_short_code = "", audio_long_code = "", streams = defaultdict(Stream)):
        self.disc_title = disc_title
        self.chapters_count = chapters_count
        self.length_of_chapter = length_of_chapter
        self.file_size_human = file_size_human
        self.file_size_bytes = file_size_bytes
        self.file_name = file_name
        self.audio_short_code = audio_short_code
        self.audio_long_code = audio_long_code
        self.streams = streams

    def __repr__(self) -> str:
        return f"Title('{self.disc_title}', '{self.chapters_count}', '{self.length_of_chapter}', '{self.file_size_human}', '{self.file_size_bytes}', '{self.file_name}', '{self.audio_long_code}', '{self.audio_short_code}', {self.streams})"
    
    def __str__(self) -> str:
        result = f"{self.disc_title} {self.file_name} {self.file_size_human}\n"
        for key in self.streams.keys():
            result += f"\tStream {key}: "
            result += str(self.streams[key])
        return result