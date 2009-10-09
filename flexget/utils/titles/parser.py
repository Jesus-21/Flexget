class ParseWarning(Warning):
    def __init__(self, value, **kwargs):
        self.value = value
        self.kwargs = kwargs

class TitleParser(object):
    
    qualities = ['1080p', '1080', '720p', '720', 'hr', 'dvd', 'dvdrip', 'hdtv', 
                 'pdtv', 'dsr', 'dsrip', 'unknown']
    
    propers = ['proper', 'repack', 'rerip']
    
    specials = ['special']
    
    cutoffs = ['dvdrip', 'dvdscr', 'cam', 'r5', 'limited', 'xvid', 'h264', 
               'x264', 'h.264', 'x.264', 'screener', 'unrated', 
               'bluray', 'multisubs'] + propers + specials + qualities
    
    remove = ['imax']