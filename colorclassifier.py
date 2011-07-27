import colorsys
import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.DEBUG)

class ColorClassification():
    color_map = {
        'LightBlue': {
            'h': [212, 258],
            's': [13, 51], 
            'v': [91, 100]},
        'Blue': {
            'h': [212, 258],
            's': [0, 100],
            'v': [0, 100]},
        'Red': {
            'h': [0, 9],
            's': [0, 100],
            'v': [0, 100]}}

    matrix = {
        'h': dict()}

    def __init__(self, **kwargs):
        for i in range(0, 361):
            self.matrix['h'].update({i: dict()})

        self.populate_colorspace()

        if kwargs.get('rgb'):
            self.set_rgb(
                kwargs.get('rgb'))

    def set_rgb(self, rgb):
        for i in range(len(rgb)):
            rgb[i] /= 255

        logger.info('Setting self.hsv to {hsv} based on rgb: {rgb}'.format(
                hsv = self.hsv,
                rgb = rgb))

        self.hsv = colorsys.rgb_to_hsv(*rgb)

    def populate_colorspace(self):
        for name, data in self.color_map.items():
            logger.debug(data['h'])
            if 'h' in data:
                for i in range(data['h'][0], data['h'][1] + 1):
                    self.matrix['h'][i].update({
                            name: data})
                    logger.debug('Appending {name} to h:{i}'.format(
                            name = name,
                            i = i))

    def find_color(self):
        pass
    
    def get_name(self):
        (h, s, v) = self.hsv

        hue = round(h * 360, 0)
        sat = round(s * 100, 0)
        val = round(v * 100, 0)

        logger.debug(self.matrix['h'][hue])
        for name, data in self.matrix['h'][hue].items():
            if 's' in data and 'v' in data:
                logger.debug('s and v in data')
                logger.debug('------\ns: {s}\nv: {v}\nsat: {sat}\nval: {val}\n'.format(
                        s = data['s'],
                        sat = sat,
                        v = data['v'],
                        val = val))
                if sat in range(data['s'][0], data['s'][1] + 1) \
                        and val in range(data['v'][0], data['v'][1] + 1):
                    logger.debug('sat and val found in range of {name}'.format(
                            name = name))
                    return [dict(
                        name = name,
                        data = self.matrix['h'][hue][name])]
            else:
                logger.debug('No s and v in data')
        logger.debug('Returning False, this is the data at hue: {hue}\n{data}'.format(
                hue = hue,
                data = self.matrix['h'][hue]))
        return False
    

if __name__ == '__main__':
    cc = ColorClassification(rgb=[198, 224, 255])
    print(cc.get_name())
    cc.set_rgb([255, 0, 0])
    print(cc.get_name())
    cc.set_rgb([255, 255, 0])
    print(cc.get_name())
