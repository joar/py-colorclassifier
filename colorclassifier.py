'''
py-color-classifier
Copyright (C) 2011  Joar Wandborg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import colorsys
import logging

from collections import OrderedDict

logger = logging.getLogger()
logging.basicConfig()
# logger.setLevel(logging.INFO)


class Classifier():
    '''
    Color range definitions, currently all added by me (Joar).

    Colors ranges might overlap, colors preceding other have the advantage.

    Wiki* colors taken from http://goo.gl/X8Pp3 [books.google.com], via
    http://en.wikipedia.org/wiki/Color and does not cover the full colorspace
    '''
    color_map = OrderedDict({
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
            's': [1, 100],
            'v': [1, 100]},
        'Orange': {
            'h': [10, 43],
            's': [0, 100],
            'v': [0, 100]},
        'Yellow': {
            'h': [44, 70],
            's': [0, 100],
            'v': [0, 100]},
        'Green': {
            'h': [71, 165],
            's': [0, 100],
            'v': [0, 100]},
        'Turquoise': {
            'h': [166, 185],
            's': [0, 100],
            'v': [0, 100]},
        'Blue2': {
                'h': [186, 265],
                's': [0, 100],
                'v': [0, 100]},
        'WikiRed': {
            'h': [0, 7],
            's': [0, 100],
            'v': [61, 100]},
        'WikiOrange': {
            'h': [8, 60],
            's': [0, 100],
            'v': [90, 100]},
        'WikiYellow': {
            'h': [61, 120],
            's': [0, 100],
            'v': [90, 100]},
        'WikiGreen': {
            'h': [121, 188],
            's': [0, 100],
            'v': [64, 100]},
        'WikiBlue': {
            'h': [189, 252],
            's': [0, 100],
            'v': [64, 100]},
        'WikiViolet': {
            'h': [253, 264],
            's': [0, 100],
            'v': [64, 100]},
        })

    matrix = {
        'h': dict()}

    def __init__(self, **kwargs):
        for i in range(0, 361):
            self.matrix['h'].update({i: OrderedDict()})

        self.populate_colorspace()

        if kwargs.get('rgb'):
            self.set_rgb(
                kwargs.get('rgb'))

    def set_rgb(self, rgb):
        for i in range(len(rgb)):
            rgb[i] /= 255

        self.hsv = colorsys.rgb_to_hsv(*rgb)
        logger.info('Setting self.hsv to {hsv} based on rgb: {rgb}'.format(
                hsv=self.hsv,
                rgb=rgb))

    def populate_colorspace(self):
        for name, data in self.color_map.items():
            logger.debug(data['h'])
            if 'h' in data:
                for i in range(data['h'][0], data['h'][1] + 1):
                    self.matrix['h'][i].update({
                            name: data})
                    logger.debug('Appending {name} to h:{i}'.format(
                            name=name,
                            i=i))

    def find_color(self):
        (h, s, v) = self.hsv

        hue = round(h * 360, 0)
        sat = round(s * 100, 0)
        val = round(v * 100, 0)

        logger.debug(self.matrix['h'][hue])
        for name, data in self.matrix['h'][hue].items():
            if 's' in data and 'v' in data:
                if sat in range(data['s'][0], data['s'][1] + 1) \
                        and val in range(data['v'][0], data['v'][1] + 1):
                    logger.debug('sat and val found in range of {name}'.format(
                            name=name))
                    return dict(
                        name=name,
                        data=self.matrix['h'][hue][name])
            else:
                logger.debug('No s and v in data')
        logger.info('Returning False, this is the data at hue: {hue}\n'
                     '{data}'.format(
                hue=hue,
                data=self.matrix['h'][hue]))
        return False

    def get_name(self):
        data = self.find_color()
        if data and 'name' in data.keys():
            return data['name']

        return False


if __name__ == '__main__':
    cc = Classifier(rgb=[198, 224, 255])
    print(cc.get_name())
    cc.set_rgb([255, 0, 0])
    print(cc.get_name())
    cc.set_rgb([255, 170, 0])
    print(cc.get_name())
    cc.set_rgb([0, 0, 0])
    print(cc.get_name())
