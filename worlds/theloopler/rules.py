from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, Rule

from .options import Goal

if TYPE_CHECKING:
    from .world import TheLooplerWorld

# The three parts of a combination. Every combination has the following preset;
# Combination: {Track Name} {Car Name} Car {Difficulty}

TRACKS = ["Infinity", "Hotdog", "Crown", "Whistle", "Whirl", "Donut", "Triangle", "Burger", "Mheep"]
CARS = ["Dura", "Gold", "Slot", "Ghost", "Drift", "Rocket", "Luck", "Tank", "Freeze"]
LOOPS = ["Bronze", "Silver", "Gold", "Emerald", "Diamond"]

def track_item(track: str) -> str:
    return f"Track: {track} Track"

def car_item(car: str) -> str:
    return f"Car: {car} Car"

def loop_item(loop: str) -> str:
    return f"Loop: {loop} Loop"

def track_rule(world, track: str) -> Rule | None:
    name = track_item(track)
    return None if name in world.starting_item_names else Has(name)

def car_rule(world, car: str) -> Rule | None:
    name = car_item(car)
    return None if name in world.starting_item_names else Has(name)

def loop_rule(world, loop: str) -> Rule | None:
    name = loop_item(loop)
    return None if name in world.starting_item_names else Has(name)

def all_of(*rules: Rule | None) -> Rule | None:
    result: Rule | None = None
    for rule in rules:
        if rule is None:
            continue
        result = rule if result is None else result & rule
    return result

def goal_rule(world: TheLooplerWorld) -> Rule | None:
    start = world.starting_item_names
    tracks = [track_item(t) for t in TRACKS if track_item(t) not in start]
    cars = [car_item(c) for c in CARS if car_item(c) not in start]
    loops = [loop_item(l) for l in LOOPS if loop_item(l) not in start]

    goal = world.options.goal
    if goal == Goal.option_infinity:
        return None
    if goal == Goal.option_all_tracks:
        return HasAll(*tracks)
    if goal == Goal.option_all_loops:
        return HasAll(*loops)
    if goal == Goal.option_all_combinations:
        return HasAll(*cars, *tracks, *loops)
    if goal == Goal.option_max_level:
        return None
    if goal == Goal.option_everything:
        return HasAll(*tracks, *cars, *loops)
    raise ValueError(f"Unhandled goal: {goal}")

def set_all_entrance_rules(world: TheLooplerWorld) -> None:
    for track in TRACKS:
        rule = track_rule(world, track)
        if rule is not None:
            world.set_rule(world.get_entrance(f"{track} Track Available"), rule)

    for car in CARS:
        rule = car_rule(world, car)
        if rule is not None:
            world.set_rule(world.get_entrance(f"{car} Car Available"), rule)

    for loop in LOOPS:
        rule = loop_rule(world, loop)
        if rule is not None:
            world.set_rule(world.get_entrance(f"{loop} Difficulty Available"), rule)

    goal = goal_rule(world)
    if goal is not None:
        world.set_rule(world.get_entrance("Goal Available"), goal)

def set_all_location_rules(world: TheLooplerWorld) -> None:
    if not world.options.specific_sanity:
        return

    for track in TRACKS:
        for car in CARS:
            rule = all_of(track_rule(world, track), car_rule(world, car))
            if rule is None:
                continue
            for loop in LOOPS:
                location = world.get_location(f"Combination: {track} {car} Car {loop}")
                world.set_rule(location, rule)

def set_completion_condition(world: TheLooplerWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)

def set_all_rules(world: TheLooplerWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)
    set_completion_condition(world)