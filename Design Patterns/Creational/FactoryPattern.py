from abc import ABC, abstractmethod
import pathlib


class VideoExporter(ABC):
    '''Basic representation of video exporting codec'''

    @abstractmethod
    def prepare_export(self, video_data):
        '''Prepares video to be exported'''

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        '''Export the Video to the folder'''


class WMVVideoExporter(VideoExporter):
    '''Lossless video exporter for high quality'''

    def prepare_export(self, video_data):
        print('Getting video data ready for WAV exportation')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video to {folder}')


class AVIVideoExporter(VideoExporter):
    '''High speed and low quality video codec'''

    def prepare_export(self, video_data):
        print('Preparing data for the AVI exportation.')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data to {folder}')


class BestVideoExporter(VideoExporter):
    '''Master Quality Video Exporter'''

    def prepare_export(self, video_data):
        print('Preparing video data to export as Best')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video to {folder}')


class AudioExporter(ABC):
    '''Basic representation for Audio exporting codec'''

    @abstractmethod
    def prepare_export(self, audio_data):
        '''Prepares audio data to export'''

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        '''Exports Audio file into specified path'''


class WAVAudioExporter(AudioExporter):
    '''Lossless codec for high quality'''

    def prepare_export(self, audio_data):
        print('Preparing audio data to be exported as WAV')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio data to {folder}')


class MP3AudioExporter(AudioExporter):
    '''Low quality audio exporter'''

    def prepare_export(self, audio_data):
        print('Preparing audio data to be exported as MP3')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio file to {folder}')


class BestAudioExporter(AudioExporter):
    '''Master Quality Audio Exporter'''

    def prepare_export(self, audio_data):
        print('Preparing audio data to be exported as Best')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio file to {folder}')


class ExporterFactory(ABC):
    '''Basic representation of exporter factories'''

    @abstractmethod
    def get_video_exporter(self):
        '''Returns an instance of video exporter'''

    @abstractmethod
    def get_audio_exporter(self):
        '''Returns an instance of audio exporter'''


class FastExporter(ExporterFactory):
    '''Fast and low quality exporters'''

    def get_video_exporter(self) -> VideoExporter:
        return AVIVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MP3AudioExporter()


class HighQualityExporter(ExporterFactory):
    '''High Quality exporters'''

    def get_video_exporter(self) -> VideoExporter:
        return WMVVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()

class MasterQualityExporter(ExporterFactory):
    '''Lossless Quality exporters'''

    def get_video_exporter(self) -> VideoExporter:
        return BestVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return BestAudioExporter()


def getExporters() -> ExporterFactory:

    factories = {
        'low': FastExporter(),
        'high': HighQualityExporter(),
        'master': MasterQualityExporter(),
    }

    while True:
        export_quality = input('Quality: ')
        if export_quality in factories.keys():
            return factories[export_quality]
        
        print('Invalid Quality, Choose "master", "high" or "low"')


def main(fac):

    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()
    
    video_exporter.prepare_export('video_data')
    audio_exporter.prepare_export('audio_data')

    video_exporter.do_export('usr/tmp/video')
    audio_exporter.do_export('usr/tmp/audio')


if __name__ == '__main__':
    fac = getExporters()
    main(fac)


    

