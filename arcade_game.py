"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active:bool, touching_ghost:bool):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """

    if power_pellet_active == False and touching_ghost == True:
        return False
    elif power_pellet_active == True and touching_ghost == False:
        return False
    elif power_pellet_active == False and touching_ghost == False:
        return False
    elif power_pellet_active == True and touching_ghost == True:
        return True
    



def score(touching_power_pellet:bool, touching_dot:bool):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """

    if touching_power_pellet == True:
        return True
    elif touching_dot == False:
        return False

    if touching_dot == True:
        return True
    elif touching_dot == False:
        return False



def lose(power_pellet_active:bool, touching_ghost:bool):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """

    if power_pellet_active == True and touching_ghost == True:
        return False
    elif power_pellet_active == True and touching_ghost == False:
        return False
    elif power_pellet_active == False and touching_ghost == False:
        return False
    elif power_pellet_active == False and touching_ghost == True:
        return True


def win(has_eaten_all_dots:bool, power_pellet_active:bool, touching_ghost:bool):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    if has_eaten_all_dots == True and power_pellet_active == True and touching_ghost == True:
        return True
    elif has_eaten_all_dots == True and power_pellet_active == False and touching_ghost == True:
        return False
    elif has_eaten_all_dots == True and power_pellet_active == False and touching_ghost == False:
        return True
    elif has_eaten_all_dots == False and power_pellet_active == True and touching_ghost == True:
        return False
    elif has_eaten_all_dots == False and power_pellet_active == False and touching_ghost == True:
        return False
    elif has_eaten_all_dots == False and power_pellet_active == True and touching_ghost == False:
        return False
