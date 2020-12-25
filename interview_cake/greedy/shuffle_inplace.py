import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # If it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_from in range(0, len(the_list) - 1):
        # Choose a random not-yet-placed item to place there
        # (Could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all ready been placed
        random_choice_index = get_random(index_from, last_index_in_the_list)

        # Place our random choice in the spot by swapping
        if random_choice_index != index_from:
            the_list[index_from], the_list[random_choice_index] = the_list[random_choice_index], the_list[index_from]