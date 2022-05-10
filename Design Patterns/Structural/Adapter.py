from abc import ABC, abstractmethod


class PngInterface(ABC):

    @abstractmethod
    def draw(self):
        '''Draw PNG file'''


class PngImage(PngInterface):

    def __init__(self, png):
        self.png = png
        self.format = 'raster'

    def draw(self):
        print('drawing ' + self.get_image())

    def get_image(self):
        return 'png'


# Implemented before, perhaps not by us.
# Incompatible with PngInterface
class SvgImage:

    def __init__(self, svg):
        self.svg = svg
        self.format = 'vector'

    def get_image(self):
        return 'svg'

# SvgImage -> SvgAdapter(PngInterface) -> PngInterface compatible svg
class SvgAdapter(PngInterface):

    def __init__(self, svg: SvgImage):
        self.svg = svg

    def rasterize(self):
        return 'rasterized ' + self.svg.get_image()

    def draw(self):
        img = self.rasterize()
        print('drawing ' + img)


regular_png = PngImage("some data")
regular_png.draw()

example_svg = SvgImage("some data")
example_adapter = SvgAdapter(example_svg)
example_adapter.draw()



    
    

    
    
