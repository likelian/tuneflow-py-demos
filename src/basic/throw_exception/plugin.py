from tuneflow_py import TuneflowPlugin, Song, ParamDescriptor
from typing import Any, Dict


class ThrowExceptionExample(TuneflowPlugin):
    @staticmethod
    def provider_id():
        return "andantei"

    @staticmethod
    def plugin_id():
        return "throw-exception-example"

    @staticmethod
    def params(song: Song) -> Dict[str, ParamDescriptor]:
        return {}

    @staticmethod
    def run(song: Song, params: Dict[str, Any]):
        """
        Throw an exception during execution. You should be able to see that
        the plugin in TuneFlow Desktop turns red after execution.
        """
        a = 1/0
