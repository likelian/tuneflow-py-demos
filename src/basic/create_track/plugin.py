from tuneflow_py import TuneflowPlugin, Song, ParamDescriptor, TrackType
from typing import Any, Dict


class CreateTrackExample(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "create-track-example"

    @staticmethod
    def params(song: Song) -> Dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: Dict[str, Any]):
        print("=============================")
        print("In this example you will see a new, empty midi track being added to the song.")
        song.create_track(TrackType.MIDI_TRACK, index=0)
