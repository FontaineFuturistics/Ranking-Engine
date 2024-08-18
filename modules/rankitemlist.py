import rankitem

class RankItemList:

    # Constructor
    def __init__(self):

        # Main list
        self.item_list = []

        # Ordered list
        self.ordered_list = []
        self.list_is_valid = True

    # Add a new item to our list
    def add_item(self, new_item: rankitem.RankItem) -> None:

        # Add item to the internal list
        self.item_list.append(new_item)

        # Make list invalid
        self.list_is_valid = False

    # Attempt to order the list, return list of tuples we need to order
    def order_list(self) -> list:

        # Don't order an ordered list
        if self.list_is_valid:
            return
        
        # Try to insert each item in the list
        for item in self.item_list:

