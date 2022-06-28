import os

def move_file(current, destination):
    os.rename(current, destination)

class Plugin:
    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def reset_game_files(self, *args):
        map_path = "/home/deck/Documents/RLmaps/Medieval Rings/"
        rocket_league_path = "/home/deck/Games/Heroic/rocketleague/TAGame/CookedPCConsole/"
        move_file(rocket_league_path + "Labs_Underpass_P.upk", map_path + "LethMedievalRings.udk")
        move_file(map_path + "ORIGINAL_UNDERPASS.upk", rocket_league_path + "Labs_Underpass_P.upk")

    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def load_map(self, *args):
        map_path = "/home/deck/Documents/RLmaps/Medieval Rings/"
        rocket_league_path = "/home/deck/Games/Heroic/rocketleague/TAGame/CookedPCConsole/"
        move_file(rocket_league_path + "Labs_Underpass_P.upk", map_path + "ORIGINAL_UNDERPASS.upk")
        move_file(map_path + "LethMedievalRings.udk", rocket_league_path + "Labs_Underpass_P.upk")
