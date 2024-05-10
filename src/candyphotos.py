class CandyPhotos:
    green = "images/7.png"
    red = "images/8.png"
    orange = "images/9.png"
    yellow = "images/10.png"
    purple = "images/11.png"
    blue = "images/12.png"

    @classmethod
    def load_photos(cls):
        return [cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.blue]
