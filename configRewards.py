

class ConfigRewards:
    cell_clean = -1
    cell_dirty = 10
    cell_inaccessible = -100
    cell_finish = 100

    @staticmethod
    def display():
        print("Rewards")
        print("-------")
        print(f"cell clean = {ConfigRewards.cell_clean}")
        print(f"cell dirty = {ConfigRewards.cell_dirty}")
        print(f"cell clean = {ConfigRewards.cell_inaccessible}")