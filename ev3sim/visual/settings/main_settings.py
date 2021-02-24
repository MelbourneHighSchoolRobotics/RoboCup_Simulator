from ev3sim.visual.settings.elements import NumberEntry, FileEntry, Checkbox

main_settings = [
    {
        "height": (lambda s: 240 if s[0] < 580 else 140),
        "objects": [
            NumberEntry(["screen", "SCREEN_WIDTH"], 720, "Screen Width", (lambda s: (0, 20))),
            NumberEntry(
                ["screen", "SCREEN_HEIGHT"], 960, "Screen Height", (lambda s: (0, 70) if s[0] < 540 else (s[0] / 2, 20))
            ),
            NumberEntry(["app", "FPS"], 30, "FPS", (lambda s: (0, 120) if s[0] < 540 else (0, 70))),
            Checkbox(["screen", "PLAY_ANIMATIONS"], True, "UI Animations", (lambda s: (0, 170) if s[0] < 540 else (s[0] / 2, 70))),
        ],
    },
    {
        "height": (lambda s: 140),
        "objects": [
            FileEntry(["app", "workspace_folder"], "", True, None, "Workspace", (lambda s: (0, 20))),
            Checkbox(["app", "console_log"], True, "Sim Console", (lambda s: (0, 70))),
        ],
    },
]
