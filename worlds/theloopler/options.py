from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class SpecificSanity(Toggle):
    """
    With Specific Sanity, every single combination of track, car,
    and loop difficulty that's enabled will be a check.
    You wouldn't want this for a normal sync.
    Completing all checks of this type is the equivalent
    of the achievement 'The Loopler', only if all regions below
    are enabled.
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
    All Tracks, Loops, Combinations: Complete every
    instance of the listed item.
    Max Level: Reach Level 42
    Everything: All of the above.
    """

    display_name = "Goal"

    option_infinity = 0
    option_all_tracks = 1
    option_all_loops = 2
    option_all_combinations = 3
    option_max_level = 4
    option_everything = 5

    default = option_max_level

class StartingItemsRandomized(Toggle):
    """
    If this option is enabled, the car, track, and 
    difficulty you start with will be randomized.
    This means that you may not start with Infinity, 
    Bronze, and Dura unlocked.
    Only enable this if you are confident in your abilities.
    """

    display_name = "Starting Items Randomized"
    
class SpecificSanityBronze(Toggle):
    """
    If this option is enabled, all combinations with a
    Bronze track will be checks.
    Of course, this only matters if you have Specific Sanity enabled.
    """

    display_name = "Bronze Combinations Enabled"
    default = True

class SpecificSanitySilver(Toggle):
    """
    If this option is enabled, all combinations with a 
    Silver track will be checks.
    Of course, this only matters if you have Specific Sanity enabled.
    """

    display_name = "Silver Combinations Enabled"
    default = True
    
class SpecificSanityGold(Toggle):
    """
    If this option is enabled, all combinations with a 
    Gold track will be checks.
    Of course, this only matters if you have Specific Sanity enabled.
    """

    display_name = "Gold Combinations Enabled"
    default = True
    
class SpecificSanityEmerald(Toggle):
    """
    If this option is enabled, all combinations with an 
    Emerald track will be checks.
    Of course, this only matters if you have Specific Sanity enabled.
    """

    display_name = "Emerald Combinations Enabled"
    default = True
    
class SpecificSanityDiamond(Toggle):
    """
    If this option is enabled, all combinations with a 
    Diamond track will be checks.
    Of course, this only matters if you have Specific Sanity enabled.
    """

    display_name = "Diamond Combinations Enabled"
    default = True

@dataclass
class TheLooplerOptions(PerGameCommonOptions):
    specific_sanity: SpecificSanity
    trap_chance: TrapChance
    goal: Goal
    starting_items_rando: StartingItemsRandomized
    specific_sanity_bronze: SpecificSanityBronze
    specific_sanity_silver: SpecificSanitySilver
    specific_sanity_gold: SpecificSanityGold
    specific_sanity_emerald: SpecificSanityEmerald
    specific_sanity_diamond: SpecificSanityDiamond

option_groups = [
    OptionGroup(
        "Specific Sanity Options",
        [SpecificSanity, SpecificSanityBronze, SpecificSanitySilver, SpecificSanityGold, SpecificSanityEmerald, SpecificSanityDiamond]
    )
]

option_presets = {
    "Normal": {
        "specific_sanity": False,
        "trap_chance": 10,
        "goal": 4,
        "starting_items_rando": False,
        "specific_sanity_bronze": False,
        "specific_sanity_silver": False,
        "specific_sanity_gold": False,
        "specific_sanity_emerald": False,
        "specific_sanity_diamond": False
    },
    "Rain": {
        "specific_sanity": True,
        "trap_chance": 100,
        "goal": 5,
        "starting_items_rando": True,
        "specific_sanity_bronze": True,
        "specific_sanity_silver": True,
        "specific_sanity_gold": True,
        "specific_sanity_emerald": True,
        "specific_sanity_diamond": True
    },
}