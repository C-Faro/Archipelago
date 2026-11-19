from _collections_abc import Mapping
from typing  import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as theloopler_options

from .rules import CARS, TRACKS, LOOPS

class TheLooplerWorld(World):
    game = "The Loopler"

    web = web_world.TheLooplerWebWorld()

    options_dataclass = theloopler_options.TheLooplerOptions
    options: theloopler_options.TheLooplerOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    item_name_groups = {
        "Cars": items.CAR_TABLE,
        "Tracks": items.TRACK_TABLE,
        "Loops": items.LOOP_TABLE,
        "Traps": items.TRAP_TABLE,
        "Cards": {n for n in items.ITEM_NAME_TO_ID if n.startswith("Card: ")},
        "Charms": {n for n in items.ITEM_NAME_TO_ID if n.startswith("Charm: ")},
        "Gates": {n for n in items.ITEM_NAME_TO_ID if n.startswith("Gate: ")},
    }
    location_name_groups = {
        "Level Ups": {n for n in locations.LOCATION_NAME_TO_ID if n.startswith("Level Up: ")},
        "Combinations": {n for n in locations.LOCATION_NAME_TO_ID if n.startswith("Combination: ")},
        **{
            f"{loop} Combinations": {
                n for n in locations.LOCATION_NAME_TO_ID
                if n.startswith("Combination: ") and n.endswith(f" {loop}")
            }
            for loop in LOOPS
        },
        **{
            f"{track} Combinations": {
                n for n in locations.LOCATION_NAME_TO_ID
                if n.startswith(f"Combination: {track} ")
            }
            for track in TRACKS
        },
        **{
            f"{car} Car Combinations": {
                n for n in locations.LOCATION_NAME_TO_ID
                if n.startswith("Combination: ") and f" {car} Car " in n
            }
            for car in CARS
        },
    }

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TheLooplerItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "specific_sanity", "trap_chance", "goal", "starting_items_rando",
            "specific_sanity_bronze", "specific_sanity_silver", "specific_sanity_gold",
            "specific_sanity_emerald", "specific_sanity_diamond", "progressive_difficulties",
            "progressive_cars", "progressive_tracks", "macguffins_required",
            "macguffins_extra"
        )