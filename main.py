from UtilityMapLibrary import UtilityMap


map_matrix = [
            [".",   ".",    ".",    ".",    "+1"],
            [".",   ".",    ".",    ".",    "-1"],
            [".",   "|",    ".",    ".",    "."],
            [".",   ".",    ".",    ".",    "."]
        ]
        
map = UtilityMap(map_matrix)
map.getUtilityCalculatedMap()
map.printArrowMap()
map.printUtilityMap()
print("###########################")
