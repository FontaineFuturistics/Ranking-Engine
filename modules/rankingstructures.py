# The structure containing and ranking all items
class RankList:

    # Constructor
    def __init__(self):

        # List containing all items in no order
        self.source_list = []

        # Ranked list
        self.ranked_list = []

        # List of tuples of items to compare
        self.compare_list = []

    def add_item(self, name: str, desc: str) -> None:

        # Add a new item to our source list
        self.source_list.append(RankItem(name, desc))

    def compare_next(self) -> None:

        # Get the next two items to compare
        c_tuple = self.compare_list.pop()

        # TODO actually compare the items

# A Single item being ranked, internal to the RankList class
class RankItem:

    # Constructor
    def __init__(self, name: str, desc: str):

        # Basic attributes
        self.name = name
        self.desc = desc

        # All items compared to be higher than us
        self.higher_items = []

        # All items compared to be lower than us
        self.lower_items = []

    # Add higher item
    def add_higher(self, other: RankItem) -> None:
        