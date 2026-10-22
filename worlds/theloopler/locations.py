from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from worlds import TheLooplerWorld

LOCATION_NAME_TO_ID = {
    "Track: Infinity Completed": 1,
    "Track: Hotdog Completed": 2,
    "Track: Crown Completed": 3,
    "Track: Whistle Completed": 4,
    "Track: Whirl Completed": 5,
    "Track: Donut Completed": 6,
    "Track: Triangle Completed": 7,
    "Track: Burger Completed": 8,
    "Track: Mheep Completed": 9,
    "Car: Dura Completed": 11,
    "Car: Gold Completed": 12,
    "Car: Slot Completed": 13,
    "Car: Ghost Completed": 14,
    "Car: Drift Completed": 15,
    "Car: Rocket Completed": 16,
    "Car: Luck Completed": 17,
    "Car: Tank Completed": 18,
    "Car: Freeze Completed": 19,
    "Loop: Bronze Completed": 21,
    "Loop: Silver Completed": 22,
    "Loop: Gold Completed": 23,
    "Loop: Emerald Completed": 24,
    "Loop: Diamond Completed": 25,
    "Level Up: Level 2 Item 1": 101,
    "Level Up: Level 2 Item 2": 102,
    "Level Up: Level 2 Item 3": 103,
    "Level Up: Level 3 Item 1": 104,
    "Level Up: Level 3 Item 2": 105,
    "Level Up: Level 3 Item 3": 106,
    "Level Up: Level 4 Item 1": 107,
    "Level Up: Level 4 Item 2": 108,
    "Level Up: Level 4 Item 3": 109,
    "Level Up: Level 4 Item 4": 110,
    "Level Up: Level 5 Item 1": 111,
    "Level Up: Level 5 Item 2": 112,
    "Level Up: Level 5 Item 3": 113,
    "Level Up: Level 5 Item 4": 114,
    "Level Up: Level 6 Item 1": 115,
    "Level Up: Level 6 Item 2": 116,
    "Level Up: Level 6 Item 3": 117,
    "Level Up: Level 7 Item 1": 118,
    "Level Up: Level 7 Item 2": 119,
    "Level Up: Level 7 Item 3": 120,
    "Level Up: Level 8 Item 1": 121,
    "Level Up: Level 8 Item 2": 122,
    "Level Up: Level 8 Item 3": 123,
    "Level Up: Level 9 Item 1": 124,
    "Level Up: Level 9 Item 2": 125,
    "Level Up: Level 9 Item 3": 126,
    "Level Up: Level 9 Item 4": 127,
    "Level Up: Level 10 Item 1": 128,
    "Level Up: Level 10 Item 2": 129,
    "Level Up: Level 10 Item 3": 130,
    "Level Up: Level 10 Item 4": 131,
    "Level Up: Level 11 Item 1": 132,
    "Level Up: Level 11 Item 2": 133,
    "Level Up: Level 11 Item 3": 134,
    "Level Up: Level 12 Item 1": 135,
    "Level Up: Level 12 Item 2": 136,
    "Level Up: Level 12 Item 3": 137,
    "Level Up: Level 13 Item 1": 138,
    "Level Up: Level 13 Item 2": 139,
    "Level Up: Level 13 Item 3": 140,
    "Level Up: Level 14 Item 1": 141,
    "Level Up: Level 14 Item 2": 142,
    "Level Up: Level 14 Item 3": 143,
    "Level Up: Level 15 Item 1": 144,
    "Level Up: Level 15 Item 2": 145,
    "Level Up: Level 15 Item 3": 146,
    "Level Up: Level 15 Item 4": 147,
    "Level Up: Level 16 Item 1": 148,
    "Level Up: Level 16 Item 2": 149,
    "Level Up: Level 16 Item 3": 150,
    "Level Up: Level 17 Item 1": 151,
    "Level Up: Level 17 Item 2": 152,
    "Level Up: Level 17 Item 3": 153,
    "Level Up: Level 18 Item 1": 154,
    "Level Up: Level 18 Item 2": 155,
    "Level Up: Level 18 Item 3": 156,
    "Level Up: Level 19 Item 1": 157,
    "Level Up: Level 19 Item 2": 158,
    "Level Up: Level 19 Item 3": 159,
    "Level Up: Level 20 Item 1": 160,
    "Level Up: Level 20 Item 2": 161,
    "Level Up: Level 20 Item 3": 162,
    "Level Up: Level 20 Item 4": 163,
    "Level Up: Level 21 Item 1": 164,
    "Level Up: Level 21 Item 2": 165,
    "Level Up: Level 21 Item 3": 166,
    "Level Up: Level 22 Item 1": 167,
    "Level Up: Level 22 Item 2": 168,
    "Level Up: Level 22 Item 3": 169,
    "Level Up: Level 23 Item 1": 170,
    "Level Up: Level 23 Item 2": 171,
    "Level Up: Level 23 Item 3": 172,
    "Level Up: Level 24 Item 1": 173,
    "Level Up: Level 24 Item 2": 174,
    "Level Up: Level 24 Item 3": 175,
    "Level Up: Level 25 Item 1": 176,
    "Level Up: Level 25 Item 2": 177,
    "Level Up: Level 25 Item 3": 178,
    "Level Up: Level 25 Item 4": 179,
    "Level Up: Level 26 Item 1": 180,
    "Level Up: Level 26 Item 2": 181,
    "Level Up: Level 26 Item 3": 182,
    "Level Up: Level 27 Item 1": 183,
    "Level Up: Level 27 Item 2": 184,
    "Level Up: Level 27 Item 3": 185,
    "Level Up: Level 28 Item 1": 186,
    "Level Up: Level 28 Item 2": 187,
    "Level Up: Level 28 Item 3": 188,
    "Level Up: Level 29 Item 1": 189,
    "Level Up: Level 29 Item 2": 190,
    "Level Up: Level 29 Item 3": 191,
    "Level Up: Level 30 Item 1": 192,
    "Level Up: Level 30 Item 2": 193,
    "Level Up: Level 30 Item 3": 194,
    "Level Up: Level 31 Item 1": 195,
    "Level Up: Level 31 Item 2": 196,
    "Level Up: Level 31 Item 3": 197,
    "Level Up: Level 32 Item 1": 198,
    "Level Up: Level 32 Item 2": 199,
    "Level Up: Level 32 Item 3": 200,
    "Level Up: Level 33 Item 1": 201,
    "Level Up: Level 33 Item 2": 202,
    "Level Up: Level 33 Item 3": 203,
    "Level Up: Level 34 Item 1": 204,
    "Level Up: Level 34 Item 2": 205,
    "Level Up: Level 34 Item 3": 206,
    "Level Up: Level 35 Item 1": 207,
    "Level Up: Level 35 Item 2": 208,
    "Level Up: Level 35 Item 3": 209,
    "Level Up: Level 36 Item 1": 210,
    "Level Up: Level 36 Item 2": 211,
    "Level Up: Level 36 Item 3": 212,
    "Level Up: Level 37 Item 1": 213,
    "Level Up: Level 37 Item 2": 214,
    "Level Up: Level 37 Item 3": 215,
    "Level Up: Level 38 Item 1": 216,
    "Level Up: Level 38 Item 2": 217,
    "Level Up: Level 38 Item 3": 218,
    "Level Up: Level 39 Item 1": 219,
    "Level Up: Level 39 Item 2": 220,
    "Level Up: Level 39 Item 3": 221,
    "Level Up: Level 40 Item 1": 222,
    "Level Up: Level 40 Item 2": 223,
    "Level Up: Level 40 Item 3": 224,
    "Level Up: Level 41 Item 1": 225,
    "Level Up: Level 41 Item 2": 226,
    "Level Up: Level 41 Item 3": 227,
    "Level Up: Level 42 Item 1": 228,
    "Level Up: Level 42 Item 2": 229,
    "Level Up: Level 42 Item 3": 230,
    "Combination: Infinity Dura Car Bronze": 300,
    "Combination: Infinity Dura Car Silver": 301,
    "Combination: Infinity Dura Car Gold": 302,
    "Combination: Infinity Dura Car Emerald": 303,
    "Combination: Infinity Dura Car Diamond": 304,
    "Combination: Infinity Gold Car Bronze": 305,
    "Combination: Infinity Gold Car Silver": 306,
    "Combination: Infinity Gold Car Gold": 307,
    "Combination: Infinity Gold Car Emerald": 308,
    "Combination: Infinity Gold Car Diamond": 309,
    "Combination: Infinity Slot Car Bronze": 310,
    "Combination: Infinity Slot Car Silver": 311,
    "Combination: Infinity Slot Car Gold": 312,
    "Combination: Infinity Slot Car Emerald": 313,
    "Combination: Infinity Slot Car Diamond": 314,
    "Combination: Infinity Ghost Car Bronze": 315,
    "Combination: Infinity Ghost Car Silver": 316,
    "Combination: Infinity Ghost Car Gold": 317,
    "Combination: Infinity Ghost Car Emerald": 318,
    "Combination: Infinity Ghost Car Diamond": 319,
    "Combination: Infinity Drift Car Bronze": 320,
    "Combination: Infinity Drift Car Silver": 321,
    "Combination: Infinity Drift Car Gold": 322,
    "Combination: Infinity Drift Car Emerald": 323,
    "Combination: Infinity Drift Car Diamond": 324,
    "Combination: Infinity Rocket Car Bronze": 325,
    "Combination: Infinity Rocket Car Silver": 326,
    "Combination: Infinity Rocket Car Gold": 327,
    "Combination: Infinity Rocket Car Emerald": 328,
    "Combination: Infinity Rocket Car Diamond": 329,
    "Combination: Infinity Luck Car Bronze": 330,
    "Combination: Infinity Luck Car Silver": 331,
    "Combination: Infinity Luck Car Gold": 332,
    "Combination: Infinity Luck Car Emerald": 333,
    "Combination: Infinity Luck Car Diamond": 334,
    "Combination: Infinity Tank Car Bronze": 335,
    "Combination: Infinity Tank Car Silver": 336,
    "Combination: Infinity Tank Car Gold": 337,
    "Combination: Infinity Tank Car Emerald": 338,
    "Combination: Infinity Tank Car Diamond": 339,
    "Combination: Infinity Freeze Car Bronze": 340,
    "Combination: Infinity Freeze Car Silver": 341,
    "Combination: Infinity Freeze Car Gold": 342,
    "Combination: Infinity Freeze Car Emerald": 343,
    "Combination: Infinity Freeze Car Diamond": 344,
    "Combination: Hotdog Dura Car Bronze": 345,
    "Combination: Hotdog Dura Car Silver": 346,
    "Combination: Hotdog Dura Car Gold": 347,
    "Combination: Hotdog Dura Car Emerald": 348,
    "Combination: Hotdog Dura Car Diamond": 349,
    "Combination: Hotdog Gold Car Bronze": 350,
    "Combination: Hotdog Gold Car Silver": 351,
    "Combination: Hotdog Gold Car Gold": 352,
    "Combination: Hotdog Gold Car Emerald": 353,
    "Combination: Hotdog Gold Car Diamond": 354,
    "Combination: Hotdog Slot Car Bronze": 355,
    "Combination: Hotdog Slot Car Silver": 356,
    "Combination: Hotdog Slot Car Gold": 357,
    "Combination: Hotdog Slot Car Emerald": 358,
    "Combination: Hotdog Slot Car Diamond": 359,
}

class TheLooplerLocation(Location):
    game = "The Loopler"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TheLooplerWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: TheLooplerWorld) -> None:
    menu = world.get_region("Menu")
    dura_car = world.get_region("Dura Car")
    gold_car = world.get_region("Gold Car")
    slot_car = world.get_region("Slot Car")
    ghost_car = world.get_region("Ghost Car")
    drift_car = world.get_region("Drift Car")
    rocket_car = world.get_region("Rocket Car")
    luck_car = world.get_region("Luck Car")
    tank_car = world.get_region("Tank Car")
    freeze_car = world.get_region("Freeze Car")
    infinity_track = world.get_region("Infinity Track")
    hotdog_track = world.get_region("Hotdog Track")
    crown_track = world.get_region("Crown Track")
    whistle_track = world.get_region("Whistle Track")
    whirl_track = world.get_region("Whirl Track")
    donut_track = world.get_region("Donut Track")
    triangle_track = world.get_region("Triangle Track")
    burger_track = world.get_region("Burger Track")
    mheep_track = world.get_region("Mheep Track")
    bronze_diffi = world.get_region("Bronze Difficulty")
    silver_diffi = world.get_region("Silver Difficulty")
    gold_diffi = world.get_region("Gold Difficulty")
    emerald_diffi = world.get_region("Emerald Difficulty")
    diamond_diffi = world.get_region("Diamond Difficulty")

    menu_locations = get_location_names_with_ids(
        ["Level Up: Level 1 Item 1", "Level Up: Level 1 Item 2", "Level Up: Level 1 Item 3",
         "Level Up: Level 2 Item 1", "Level Up: Level 2 Item 2", "Level Up: Level 2 Item 3",
         "Level Up: Level 3 Item 1", "Level Up: Level 3 Item 2", "Level Up: Level 3 Item 3",
         "Level Up: Level 4 Item 1", "Level Up: Level 4 Item 2", "Level Up: Level 4 Item 3", "Level Up: Level 4 Item 4",
         "Level Up: Level 5 Item 1", "Level Up: Level 5 Item 2", "Level Up: Level 5 Item 3", "Level Up: Level 5 Item 4",
         "Level Up: Level 6 Item 1", "Level Up: Level 6 Item 2", "Level Up: Level 6 Item 3",
         "Level Up: Level 7 Item 1", "Level Up: Level 7 Item 2", "Level Up: Level 7 Item 3",
         "Level Up: Level 8 Item 1", "Level Up: Level 8 Item 2", "Level Up: Level 8 Item 3",
         "Level Up: Level 9 Item 1", "Level Up: Level 9 Item 2", "Level Up: Level 9 Item 3", "Level Up: Level 9 Item 4",
         "Level Up: Level 10 Item 1", "Level Up: Level 10 Item 2", "Level Up: Level 10 Item 3", "Level Up: Level 10 Item 4",
         "Level Up: Level 11 Item 1", "Level Up: Level 11 Item 2", "Level Up: Level 11 Item 3",
         "Level Up: Level 12 Item 1", "Level Up: Level 12 Item 2", "Level Up: Level 12 Item 3",
         "Level Up: Level 13 Item 1", "Level Up: Level 13 Item 2", "Level Up: Level 13 Item 3",
         "Level Up: Level 14 Item 1", "Level Up: Level 14 Item 2", "Level Up: Level 14 Item 3",
         "Level Up: Level 15 Item 1", "Level Up: Level 15 Item 2", "Level Up: Level 15 Item 3", "Level Up: Level 15 Item 4",
         "Level Up: Level 16 Item 1", "Level Up: Level 16 Item 2", "Level Up: Level 16 Item 3",
         "Level Up: Level 17 Item 1", "Level Up: Level 17 Item 2", "Level Up: Level 17 Item 3",
         "Level Up: Level 18 Item 1", "Level Up: Level 18 Item 2", "Level Up: Level 18 Item 3",
         "Level Up: Level 19 Item 1", "Level Up: Level 19 Item 2", "Level Up: Level 19 Item 3",
         "Level Up: Level 20 Item 1", "Level Up: Level 20 Item 2", "Level Up: Level 20 Item 3", "Level Up: Level 20 Item 4",
         "Level Up: Level 21 Item 1", "Level Up: Level 21 Item 2", "Level Up: Level 21 Item 3",
         "Level Up: Level 22 Item 1", "Level Up: Level 22 Item 2", "Level Up: Level 22 Item 3",
         "Level Up: Level 23 Item 1", "Level Up: Level 23 Item 2", "Level Up: Level 23 Item 3",
         "Level Up: Level 24 Item 1", "Level Up: Level 24 Item 2", "Level Up: Level 24 Item 3",
         "Level Up: Level 25 Item 1", "Level Up: Level 25 Item 2", "Level Up: Level 25 Item 3", "Level Up: Level 25 Item 4",
         "Level Up: Level 26 Item 1", "Level Up: Level 26 Item 2", "Level Up: Level 26 Item 3",
         "Level Up: Level 27 Item 1", "Level Up: Level 27 Item 2", "Level Up: Level 27 Item 3",
         "Level Up: Level 28 Item 1", "Level Up: Level 28 Item 2", "Level Up: Level 28 Item 3",
         "Level Up: Level 29 Item 1", "Level Up: Level 29 Item 2", "Level Up: Level 29 Item 3",
         "Level Up: Level 30 Item 1", "Level Up: Level 30 Item 2", "Level Up: Level 30 Item 3",
         "Level Up: Level 31 Item 1", "Level Up: Level 31 Item 2", "Level Up: Level 31 Item 3",
         "Level Up: Level 32 Item 1", "Level Up: Level 32 Item 2", "Level Up: Level 32 Item 3",
         "Level Up: Level 33 Item 1", "Level Up: Level 33 Item 2", "Level Up: Level 33 Item 3",
         "Level Up: Level 34 Item 1", "Level Up: Level 34 Item 2", "Level Up: Level 34 Item 3",
         "Level Up: Level 35 Item 1", "Level Up: Level 35 Item 2", "Level Up: Level 35 Item 3",
         "Level Up: Level 36 Item 1", "Level Up: Level 36 Item 2", "Level Up: Level 36 Item 3",
         "Level Up: Level 37 Item 1", "Level Up: Level 37 Item 2", "Level Up: Level 37 Item 3",
         "Level Up: Level 38 Item 1", "Level Up: Level 38 Item 2", "Level Up: Level 38 Item 3",
         "Level Up: Level 39 Item 1", "Level Up: Level 39 Item 2", "Level Up: Level 39 Item 3",
         "Level Up: Level 40 Item 1", "Level Up: Level 40 Item 2", "Level Up: Level 40 Item 3",
         "Level Up: Level 41 Item 1", "Level Up: Level 41 Item 2", "Level Up: Level 41 Item 3",
         "Level Up: Level 42 Item 1", "Level Up: Level 42 Item 2", "Level Up: Level 42 Item 3",
         ]
    )

    menu.add_locations(menu_locations, TheLooplerLocation)

    dura_car_locations = get_location_names_with_ids(["Car: Dura Completed"])
    gold_car_locations = get_location_names_with_ids(["Car: Gold Completed"])
    slot_car_locations = get_location_names_with_ids(["Car: Slot Completed"])
    ghost_car_locations = get_location_names_with_ids(["Car: Ghost Completed"])
    drift_car_locations = get_location_names_with_ids(["Car: Drift Completed"])
    rocket_car_locations = get_location_names_with_ids(["Car: Rocket Completed"])
    luck_car_locations = get_location_names_with_ids(["Car: Luck Completed"])
    tank_car_locations = get_location_names_with_ids(["Car: Tank Completed"])
    freeze_car_locations = get_location_names_with_ids(["Car: Freeze Completed"])

    dura_car.add_locations(dura_car_locations, TheLooplerLocation)
    gold_car.add_locations(gold_car_locations, TheLooplerLocation)
    slot_car.add_locations(slot_car_locations, TheLooplerLocation)
    ghost_car.add_locations(ghost_car_locations, TheLooplerLocation)
    drift_car.add_locations(drift_car_locations, TheLooplerLocation)
    rocket_car.add_locations(rocket_car_locations, TheLooplerLocation)
    luck_car.add_locations(luck_car_locations, TheLooplerLocation)
    tank_car.add_locations(tank_car_locations, TheLooplerLocation)
    freeze_car.add_locations(freeze_car_locations, TheLooplerLocation)

    infinity_track_locations = get_location_names_with_ids(["Track: Infinity Completed"])
    hotdog_track_locations = get_location_names_with_ids(["Track: Hotdog Completed"])
    crown_track_locations = get_location_names_with_ids(["Track: Crown Completed"])
    whistle_track_locations = get_location_names_with_ids(["Track: Whistle Completed"])
    whirl_track_locations = get_location_names_with_ids(["Track: Whirl Completed"])
    donut_track_locations = get_location_names_with_ids(["Track: Donut Completed"])
    triangle_track_locations = get_location_names_with_ids(["Track: Triangle Completed"])
    burger_track_locations = get_location_names_with_ids(["Track: Burger Completed"])
    mheep_track_locations = get_location_names_with_ids(["Track: Mheep Completed"])

    infinity_track.add_locations(infinity_track_locations, TheLooplerLocation)
    hotdog_track.add_locations(hotdog_track_locations, TheLooplerLocation)
    crown_track.add_locations(crown_track_locations, TheLooplerLocation)
    whistle_track.add_locations(whistle_track_locations, TheLooplerLocation)
    whirl_track.add_locations(whirl_track_locations, TheLooplerLocation)
    donut_track.add_locations(donut_track_locations, TheLooplerLocation)
    triangle_track.add_locations(triangle_track_locations, TheLooplerLocation)
    burger_track.add_locations(burger_track_locations, TheLooplerLocation)
    mheep_track.add_locations(mheep_track_locations, TheLooplerLocation)

    bronze_diffi_locations = get_location_names_with_ids([
        "Loop: Bronze Completed",
        "Combination: Infinity Dura Car Bronze", "Combination: Infinity Gold Car Bronze",
        "Combination: Infinity Slot Car Bronze", "Combination: Infinity Ghost Car Bronze",
        "Combination: Infinity Drift Car Bronze", "Combination: Infinity Rocket Car Bronze",
        "Combination: Infinity Luck Car Bronze", "Combination: Infinity Tank Car Bronze",
        "Combination: Infinity Freeze Car Bronze"
    ])