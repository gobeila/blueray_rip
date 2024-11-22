from model.disc import Disc

INFO_TYPE = 0
CINFO_VALUE_TYPE = 0
CINFO_VALUE = 2
TINFO_INDEX = 0
TINFO_VALUE_TYPE = 1
TINFO_VALUE = 3
SINFO_INDEX = 1
SINFO_VALUE_TYPE = 2
SINFO_VALUE = 4

def get_disk_info():
    return "This is the info"

def read_file_output(filename) -> Disc:
    disc = Disc()

    with open(filename, 'r') as file:
        for line in file:
            parse_line(line, disc)

    return disc
                
def parse_line(line, disc):
    values = line.split(":")
    info_values = values[1].split(",")

    match values[INFO_TYPE]:
        case "CINFO":
            value = clean(info_values[CINFO_VALUE])
            match int(info_values[CINFO_VALUE_TYPE]): 
                case 1:
                    disc.type = value
        case "TINFO":
            title = disc.titles[int(info_values[TINFO_INDEX])]
            value = clean(info_values[TINFO_VALUE])
            match int(info_values[TINFO_VALUE_TYPE]):
                case 2:
                    title.disc_title = value
                case 8:
                    title.chapters_count = value
                case 9:
                    title.length_of_chapter = value
                case 10:
                    title.file_size_human = value
                case 11:
                    title.file_size_bytes = value
                case 27:
                    title.file_name = value
                case 28:
                    title.audio_short_code = value
                case 29:
                    title.audio_long_code = value
        case "SINFO":
            stream = disc.titles[int(info_values[TINFO_INDEX])].streams[int(info_values[SINFO_INDEX])]
            value = clean(info_values[SINFO_VALUE])
            match int(info_values[SINFO_VALUE_TYPE]):
                case 1:
                    stream.type = value
                case 3:
                    stream.audio_short_code = value
                case 4:
                    stream.audio_long_code = value
                case 7:
                    stream.format = value

            
def clean(str) -> str:
    return str.translate(dict.fromkeys(map(ord, '\n"'), None))