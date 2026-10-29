from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class TheLooplerWebWorld(WebWorld):
    game = "The Loopler"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up The Loopler for a Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["CoFar"]
    )

    tutorials = [setup_en]

    option_groups = option_groups
    option_presets = option_presets