from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, Rule

from .options import Goal

if TYPE_CHECKING:
    from .world import TheLooplerWorld

# Combination: {Track Name} {Car Name} Car {Difficulty}

TRACKS = ["Infinity", "Hotdog", "Crown", "Whistle", "Whirl", "Donut", "Triangle", "Burger", "Mheep"]
CARS = ["Dura", "Gold", "Slot", "Ghost", "Drift", "Rocket", "Luck", "Tank", "Freeze"]
LOOPS = ["Bronze", "Silver", "Gold", "Emerald", "Diamond"]

FULL_TRACKS = []
FULL_CARS = []
FULL_LOOPS = []

def fill_tables():
    for i in TRACKS:
        FULL_TRACKS.append(f"Track: {i} Track")
    for i in CARS:
        FULL_CARS.append(f"Car: {i} Car")
    for i in LOOPS:
        FULL_LOOPS.append(f"Loop: {i} Loop")

def track_item(track: str) -> str:
    return f"Track: {track} Track"

def car_item(car: str) -> str:
    return f"Car: {car} Car"

def loop_item(loop: str) -> str:
    return f"Loop: {loop} Loop"

def track_rule(world: TheLooplerWorld, track: str) -> Rule | None:
    rule: Rule
    name = track_item(track)
    if name in world.starting_item_names:
        return None
    elif world.options.progressive_tracks:
        rule = Has("Track: Progressive Track", FULL_TRACKS.index(name))
        print(rule)
    else:
        rule = Has(name)

    return rule

def car_rule(world: TheLooplerWorld, car: str) -> Rule | None:
    rule: Rule
    name = car_item(car)
    if name in world.starting_item_names:
        return None
    elif world.options.progressive_cars:
        rule = Has("Car: Progressive Car", FULL_CARS.index(name))
        print(rule)
    else:
        rule = Has(name)

    return rule

def loop_rule(world: TheLooplerWorld, loop: str) -> Rule | None:
    rule: Rule
    name = loop_item(loop)
    if name in world.starting_item_names:
        return None
    elif world.options.progressive_difficulties:
        rule = Has("Loop: Progressive Loop", FULL_LOOPS.index(name))
        print(rule)
    else:
        rule = Has(name)

    return rule

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

def specific_sanity_loops(world: TheLooplerWorld) -> list[str]:
    if not world.options.specific_sanity:
        return []
    enabled = {
        "Bronze": world.options.specific_sanity_bronze,
        "Silver": world.options.specific_sanity_silver,
        "Gold": world.options.specific_sanity_gold,
        "Emerald": world.options.specific_sanity_emerald,
        "Diamond": world.options.specific_sanity_diamond,
    }
    return [loop for loop in LOOPS if enabled[loop]]

def set_all_location_rules(world: TheLooplerWorld) -> None:
    loops = specific_sanity_loops(world)
    if not loops:
        return
    for track in TRACKS:
        for car in CARS:
            rule = all_of(track_rule(world, track), car_rule(world, car))
            if rule is None:
                continue
            for loop in loops:
                location = world.get_location(f"Combination: {track} {car} Car {loop}")
                world.set_rule(location, rule)

def set_completion_condition(world: TheLooplerWorld) -> None:
    if world.options.macguffins_required == 0:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
    else:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player) & state.has("Grand Prix Trophy", world.player, world.options.macguffins_required)

def set_all_rules(world: TheLooplerWorld) -> None:
    fill_tables()
    set_all_location_rules(world)
    set_all_entrance_rules(world)
    set_completion_condition(world)