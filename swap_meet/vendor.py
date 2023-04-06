
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        first_item_self = self.inventory[0]
        first_item_other = other_vendor.inventory[0]

        self.swap_items(other_vendor, first_item_self, first_item_other)

        return True
    
    def get_by_category(self, string_category):
        category_list = []

        for item in self.inventory:
            if item.get_category() == string_category:
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, string_category):
        list_of_same_categories = self.get_by_category(string_category)
        #cant be after highest_condition becuase list_of_same_categories could be empty:
        if not list_of_same_categories or len(list_of_same_categories) == 0:
            return None

        highest_condition = list_of_same_categories[0]

        for category in list_of_same_categories:
            if category.condition > highest_condition.condition:
                highest_condition = category
        return highest_condition
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return False

        item_self_want = self.get_best_by_category(their_priority)
        item_they_want = other_vendor.get_best_by_category(my_priority)

        if not item_self_want or not item_they_want:
            return False
        
        self.swap_items(other_vendor, item_self_want, item_they_want)
        return True
    