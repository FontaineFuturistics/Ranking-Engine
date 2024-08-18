# A single item to be ranked
class RankItem:

    # Constructor
    def __init__(self, item_name: str, item_desc: str) -> None:
        
        # Item properties
        self.name = item_name
        self.desc = item_desc

        # Item ranking
        self.lesser_items = []
        self.greater_items = []

    # Return the index of the highest-index item in source_list we are greater than. Return -1 if no such item exists
    def find_greatest_lesser_item(self, source_list: list) -> int:

        # Return -1 if list is emptry
        if len(source_list) == 0:
            return -1

        # Iterate backwards through the list until we find an item in lesser_items
        for index in range(len(source_list), 0):
            
            # Get the item
            item = source_list[index]

            # If its lesser than us, return the index
            if item in self.lesser_items:
                return index
            
        # If we find nothing, return -1
        return -1
    
    # Return the index of the lowest-index item in source_list we are less than. Return -1 if no such item exists
    def find_greatest_lesser_item(self, source_list: list) -> int:

        # Return -1 if the list is empty
        if len(source_list) == 0:
            return -1
        
        # Iterate through the list until we find an item in greater_items
        for index in range(len(source_list)):
            
            # Get the item
            item = source_list[index]

            # If its greater than us, return the index
            if item in self.greater_items:
                return index
        
        # If we find nothing, return -1
        return -1