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

    regions = [menu, dura_car, gold_car, slot_car, ghost_car, drift_car, rocket_car, luck_car, tank_car, freeze_car]

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

    menu.connect(dura_car, "Dura Car Available")
    menu.connect(gold_car, "Gold Car Available")
    menu.connect(slot_car, "Slot Car Available")
    menu.connect(ghost_car, "Ghost Car Available")
    menu.connect(drift_car, "Drift Car Available")
    menu.connect(rocket_car, "Rocket Car Available")
    menu.connect(luck_car, "Luck Car Available")
    menu.connect(tank_car, "Tank Car Available")
    menu.connect(freeze_car, "Freeze Car Available")

    