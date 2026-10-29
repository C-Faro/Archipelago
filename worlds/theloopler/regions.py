from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from worlds import TheLooplerWorld

def create_and_connect_regions(world: TheLooplerWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: TheLooplerWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    dura_car = Region("Dura Car", world.player, world.multiworld)
    gold_car = Region("Gold Car", world.player, world.multiworld)
    slot_car = Region("Slot Car", world.player, world.multiworld)
    ghost_car = Region("Ghost Car", world.player, world.multiworld)
    drift_car = Region("Drift Car", world.player, world.multiworld)
    rocket_car = Region("Rocket Car", world.player, world.multiworld)
    luck_car = Region("Luck Car", world.player, world.multiworld)
    tank_car = Region("Tank Car", world.player, world.multiworld)
    freeze_car = Region("Freeze Car", world.player, world.multiworld)
    infinity_track = Region("Infinity Track", world.player, world.multiworld)
    hotdog_track = Region("Hotdog Track", world.player, world.multiworld)
    crown_track = Region("Crown Track", world.player, world.multiworld)
    whistle_track = Region("Whistle Track", world.player, world.multiworld)
    whirl_track = Region("Whirl Track", world.player, world.multiworld)
    donut_track = Region("Donut Track", world.player, world.multiworld)
    triangle_track = Region("Triangle Track", world.player, world.multiworld)
    burger_track = Region("Burger Track", world.player, world.multiworld)
    mheep_track = Region("Mheep Track", world.player, world.multiworld)
    bronze_diffi = Region("Bronze Difficulty", world.player, world.multiworld)
    silver_diffi = Region("Silver Difficulty", world.player, world.multiworld)
    gold_diffi = Region("Gold Difficulty", world.player, world.multiworld)
    emerald_diffi = Region("Emerald Difficulty", world.player, world.multiworld)
    diamond_diffi = Region("Diamond Difficulty", world.player, world.multiworld)
    goal = Region("Goal", world.player, world.multiworld)

    regions = [menu, dura_car, gold_car, slot_car, ghost_car, drift_car, rocket_car, luck_car, tank_car, freeze_car,
               infinity_track, hotdog_track, crown_track, whistle_track, whirl_track, donut_track, triangle_track, burger_track, mheep_track,
               bronze_diffi, silver_diffi, gold_diffi, emerald_diffi, diamond_diffi, goal]

    world.multiworld.regions += regions

def connect_regions(world: TheLooplerWorld) -> None:
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
    goal = world.get_region("Goal")

    menu.connect(dura_car, "Dura Car Available")
    menu.connect(gold_car, "Gold Car Available")
    menu.connect(slot_car, "Slot Car Available")
    menu.connect(ghost_car, "Ghost Car Available")
    menu.connect(drift_car, "Drift Car Available")
    menu.connect(rocket_car, "Rocket Car Available")
    menu.connect(luck_car, "Luck Car Available")
    menu.connect(tank_car, "Tank Car Available")
    menu.connect(freeze_car, "Freeze Car Available")
    menu.connect(infinity_track, "Infinity Track Available")
    menu.connect(hotdog_track, "Hotdog Track Available")
    menu.connect(crown_track, "Crown Track Available")
    menu.connect(whistle_track, "Whistle Track Available")
    menu.connect(whirl_track, "Whirl Track Available")
    menu.connect(donut_track, "Donut Track Available")
    menu.connect(triangle_track, "Triangle Track Available")
    menu.connect(burger_track, "Burger Track Available")
    menu.connect(mheep_track, "Mheep Track Available")
    menu.connect(bronze_diffi, "Bronze Difficulty Available")
    menu.connect(silver_diffi, "Silver Difficulty Available")
    menu.connect(gold_diffi, "Gold Difficulty Available")
    menu.connect(emerald_diffi, "Emerald Difficulty Available")
    menu.connect(diamond_diffi, "Diamond Difficulty Available")
    menu.connect(goal, "Goal Available")

    