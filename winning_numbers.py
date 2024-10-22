def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    correct_guesses = 0
    prize = 0
    # if user_list[0] == winning_list[0]:
    #     correct_guesses += 1
    # elif user_list[0] == winning_list[1]:
    #     correct_guesses += 1
    # elif user_list[0] == winning_list[2]:
    #     correct_guesses += 1

    # if user_list[1] == winning_list[0]:
    #     correct_guesses += 1
    # elif user_list[1] == winning_list[1]:
    #     correct_guesses += 1
    # elif user_list[1] == winning_list[2]:
    #     correct_guesses += 1

    # if user_list[2] == winning_list[0]:
    #     correct_guesses += 1
    # elif user_list[2] == winning_list[1]:
    #     correct_guesses += 1
    # elif user_list[2] == winning_list[2]:
    #     correct_guesses += 1

    if len(user_list) == 3:
        if user_list[0] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[0])
        elif user_list[0] == winning_list[1]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[1])
        elif user_list[0] == winning_list[2]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[2])
        elif user_list[1] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[1])
            winning_list.remove(winning_list[0])
        elif user_list[1] == winning_list[1]:
            correct_guesses += 1
            user_list.remove(user_list[1])
            winning_list.remove(winning_list[1])
        elif user_list[1] == winning_list[2]:
            correct_guesses += 1
            user_list.remove(user_list[1])
            winning_list.remove(winning_list[2])
        elif user_list[2] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[2])
            winning_list.remove(winning_list[0])
        elif user_list[2] == winning_list[1]:
            correct_guesses += 1
            user_list.remove(user_list[2])
            winning_list.remove(winning_list[1])
        elif user_list[2] == winning_list[2]:
            correct_guesses += 1
            user_list.remove(user_list[2])
            winning_list.remove(winning_list[2])
    if len(user_list) == 2:
        if user_list[0] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[0])
        elif user_list[0] == winning_list[1]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[1])
        elif user_list[1] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[1])
            winning_list.remove(winning_list[0])
        elif user_list[1] == winning_list[1]:
            correct_guesses += 1
            user_list.remove(user_list[1])
            winning_list.remove(winning_list[1])
    if len(user_list) == 1:
        if user_list[0] == winning_list[0]:
            correct_guesses += 1
            user_list.remove(user_list[0])
            winning_list.remove(winning_list[0])

    if correct_guesses == 3:
        prize = "First"
    elif correct_guesses == 2:
        prize = "Second"
    elif correct_guesses == 1:
        prize = "Third"
    elif correct_guesses == 0:
        prize = "No"
    
    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize

winning_numbers([5,14,17], [5,14,6])
winning_numbers([17,17,17], [4,5,17])
winning_numbers([-5,14,17], [-5,14,6])
winning_numbers([-5,14.8,17], [-5,17,14.8])
winning_numbers([5j,14.8,17], [5j,17,14.8])
winning_numbers([5j,True,True], [5j,False,True])