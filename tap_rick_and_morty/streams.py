"""Stream type classes for tap-rick-and-morty."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_rick_and_morty.client import RickAndMortyStream


class CharactersStream(RickAndMortyStream):
    """Define custom stream."""
    name = "characters"
    path = "/character"
    primary_keys = ["id"]
    replication_key = "created"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The id of the character."
        ),
        th.Property(
            "name",
            th.StringType,
            description="The name of the character."
        ),
        th.Property(
            "status",
            th.StringType,
            description="The status of the character ('Alive', 'Dead' or 'unknown')."
        ),
        th.Property(
            "species",
            th.StringType,
            description="The species of the character."
        ),
        th.Property(
            "type",
            th.StringType,
            description="The type or subspecies of the character."
        ),
        th.Property(
            "gender",
            th.StringType,
            description="The gender of the character ('Female', 'Male', 'Genderless' or 'unknown')."
        ),
        th.Property(
            "origin",
            th.ObjectType(
                th.Property(
                    "name",
                    th.StringType,
                    description="The name of the origin."
                ),
                th.Property(
                    "url",
                    th.StringType,
                    description="The url of the origin."
                )
            ),
            description="Name and link to the character's origin location."
        ),
        th.Property(
            "location",
            th.ObjectType(
                th.Property(
                    "name",
                    th.StringType,
                    description="The name of the location."
                ),
                th.Property(
                    "url",
                    th.StringType,
                    description="The url of the location."
                )
            ),
            description="Name and link to the character's last known location endpoint."
        ),
        th.Property(
            "image",
            th.StringType,
            description="Link to the character's image. All images are 300x300px and most are medium shots or portraits since they are intended to be used as avatars."
        ),
        th.Property(
            "episode",
            th.ArrayType(th.StringType),
            description="List of episodes in which this character appeared."
        ),
        th.Property(
            "url",
            th.StringType,
            description="Link to the character's own URL endpoint."
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="Time at which the location was created in the database."
        ),
    ).to_dict()


class LocationsStream(RickAndMortyStream):
    """Define custom stream."""
    name = "locations"
    path = "/location"
    primary_keys = ["id"]
    replication_key = "created"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The id of the location."
        ),
        th.Property(
            "name",
            th.StringType,
            description="The name of the location."
        ),
        th.Property(
            "type",
            th.StringType,
            description="The type of the location."
        ),
        th.Property(
            "dimension",
            th.StringType,
            description="The dimension in which the location is located."
        ),
        th.Property(
            "residents",
            th.ArrayType(th.StringType),
            description="List of character who have been last seen in the location."
        ),
        th.Property(
            "url",
            th.StringType,
            description="Link to the location's own endpoint."
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="Time at which the location was created in the database."
        ),
    ).to_dict()


class EpisodesStream(RickAndMortyStream):
    """Define custom stream."""
    name = "episodes"
    path = "/episode"
    primary_keys = ["id"]
    replication_key = "created"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The id of the episode."
        ),
        th.Property(
            "name",
            th.StringType,
            description="The name of the episode."
        ),
        th.Property(
            "air_date",
            th.StringType,
            description="The air date of the episode."
        ),
        th.Property(
            "episode",
            th.StringType,
            description="The code of the episode."
        ),
        th.Property(
            "characters",
            th.ArrayType(th.StringType),
            description="List of characters who have been seen in the episode."
        ),
        th.Property(
            "url",
            th.StringType,
            description="Link to the episode's own endpoint."
        ),
        th.Property(
            "created",
            th.DateTimeType,
            description="Time at which the location was created in the database."
        ),
    ).to_dict()
