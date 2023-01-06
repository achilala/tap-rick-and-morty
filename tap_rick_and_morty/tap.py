"""RickAndMorty tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_rick_and_morty.streams import (
    RickAndMortyStream,
    CharactersStream,
    LocationsStream,
    EpisodesStream,
)

STREAM_TYPES = [
    CharactersStream,
    LocationsStream,
    EpisodesStream,
]


class TapRickAndMorty(Tap):
    """RickAndMorty tap class."""
    name = "tap-rick-and-morty"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapRickAndMorty.cli()
