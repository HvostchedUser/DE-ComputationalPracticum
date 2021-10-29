class ColorManipulations:

    @staticmethod
    def rgb_to_hex_color(rgb):
        rgb_int = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        return ("#%02x%02x%02x" % rgb_int)

    @staticmethod
    def shade(rgb):
        return int(rgb[0] / 1.1), int(rgb[1] / 1.1), int(rgb[2] / 1.1)

    @staticmethod
    def light(rgb):
        r = rgb[0] + (255 - rgb[0]) / 2
        g = rgb[1] + (255 - rgb[1]) / 2
        b = rgb[2] + (255 - rgb[2]) / 2
        return (int(r), int(g), int(b))

    @staticmethod
    def color_shift(rgb1, rgb2,k=0.5):
        return (rgb1[0]-(rgb1[0]-rgb2[0])*k,rgb1[1]-(rgb1[1]-rgb2[1])*k,rgb1[2]-(rgb1[2]-rgb2[2])*k)
