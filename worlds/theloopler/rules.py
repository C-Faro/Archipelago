from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import TheLooplerWorld

def set_all_rules(world: TheLooplerWorld) -> None:




def set_all_entrance_rules(world: TheLooplerWorld) -> None:
    infinity_available = world.get_entrance("Infinity Track Available")
    hotdog_available = world.get_entrance("Hotdog Track Available")
    crown_available = world.get_entrance("Crown Track Available")
    whistle_available = world.get_entrance("Whistle Track Available")
    whirl_available = world.get_entrance("Whirl Track Available")
    donut_available = world.get_entrance("Donut Track Available")
    triangle_available = world.get_entrance("Triangle Track Available")
    burger_available = world.get_entrance("Burger Track Available")
    mheep_available = world.get_entrance("Mheep Track Available")