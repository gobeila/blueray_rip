class Stream:

    def __init__(self, type = "", format = "", audio_short_code = "", audio_long_code = ""):
        self.type = type
        self.format = format
        self.audio_short_code = audio_short_code
        self.audio_long_code = audio_long_code

    def __repr__(self) -> str:
        return f"Stream('{self.type}', '{self.format}', '{self.audio_short_code}', '{self.audio_long_code}')"
    
    def __str__(self) -> str:
        return f"{self.type} - {self.audio_long_code} - {self.format}\n"
