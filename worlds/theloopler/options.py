from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class SpecificSanity(Toggle):
    """
    With Specific Sanity, every single combination of track, car, and loop difficulty will be a check.
    You wouldn't want this for a normal sync.
    It adds 400+ checks.
    """
    display_name = "Specific Sanity"

class TrapChance(Range):
    """
    Percentage chance any filler will be a trap.
    """
    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 25

class Goal(Choice):
    """
    The final achievement you are working towards.
    Infinity: Reach Infinity
    All Tracks, Loops, Combinations: Complete every instance of the listed item.
    Max Level: Reach Level 42
    Everything: All of the above.
    """

    display_name = "Goal"

    option_infinity = 0
    option_all_tracks = 1
    option_all_loops = 2
    option_all_cars_tracks_combinations = 3
    option_max_level = 4
    option_everything = 5

    default = option_max_level

class StartingItemsRandomized(Toggle):
    """
    If this option is enabled, the car, track, and difficulty you start with will be randomized.
    This means that you may not start with Infinity, Bronze, and Dura unlocked.
    Only enable this if you are confident in your abilities.
    """

    display_name = "Starting Items Randomized"


@dataclass
class TheLooplerOptions(PerGameCommonOptions):
    specific_sanity: SpecificSanity
    trap_chance: TrapChance
    goal: Goal
    starting_items_rando: StartingItemsRandomized

option_groups = [
    OptionGroup(
        "The Basics",
        [SpecificSanity, TrapChance, Goal],
    )
]

option_presets = {
    "Normal": {
        "specific_sanity": False,
        "trap_chance": 10,
        "goal": 4,
        "starting_items_rando": False,
    },
    "Rain": {
        "specific_sanity": True,
        "trap_chance": 100,
        "goal": 5,
        "starting_items_rando": True,
    },
}