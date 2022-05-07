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


def main():

    export_quality: str

    while True:
        export_quality = input('Quality: ')
        if export_quality in ['high', 'low']:
            break
        
        print('Invalid Quality, Choose "high" or "low"')

    if export_quality == 'high':
        video_exporter = WMVVideoExporter()
        audio_exporter = WAVAudioExporter()

    elif export_quality == 'low':
        video_exporter = AVIVideoExporter()
        audio_exporter = MP3AudioExporter()

    video_exporter.prepare_export('video_data')
    audio_exporter.prepare_export('audio_data')

    video_exporter.do_export('usr/tmp/video')
    audio_exporter.do_export('usr/tmp/audio')


if __name__ == '__main__':
    main()


    

