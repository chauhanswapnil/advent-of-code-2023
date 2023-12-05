counts = [-1, 0, 1, 10, 2, 7, 2, 3, 2, 5, 2, 1, 2, 3, 2, 1, 0, 10, 4, 10, 10, 6, 10, 10, 3, 9, 9, 5, 4, 0, 6, 6, 5, 1, 3, 2, 1, 0, 0, 0, 2, 4, 4, 10, 3, 10, 6, 7, 5, 0, 7, 0, 2, 0, 0, 0, 1, 0, 9, 10, 4, 10, 0, 8, 10, 2, 10, 10, 7, 10, 10, 0, 2, 0, 1, 1, 2, 3, 2, 1, 0, 0, 0, 10, 9, 8, 0, 9, 8, 4, 1, 1, 5, 1, 0, 2, 1, 0, 5, 10, 1, 10, 10, 9, 7, 10, 10, 8, 4, 2, 7, 1, 2, 5, 3, 4, 2, 0, 1, 0, 4, 5, 3, 7, 10, 10, 5, 6, 3, 5, 5, 1, 6, 2, 2, 1, 0, 2, 0, 0, 10, 0, 10, 1, 10, 3, 5, 0, 0, 0, 5, 1, 5, 2, 3, 1, 2, 0, 0, 10, 6, 10, 10, 3, 10, 10, 7, 8, 2, 8, 10, 10, 9, 5, 2, 2, 1, 3, 3, 4, 0, 0, 1, 0, 10, 0, 10, 10, 2, 10, 8, 10, 10, 1, 6, 2, 9, 1, 4, 0, 0, 3, 0, 4, 2, 1, 1, 1, 0]
# counts = [-1, 4, 2, 2, 1, 0, 0]

output = {str(i): 1 for i in range(1, len(counts))}


def recursive_func(card_id: int):
    if counts[card_id] > 0:
        # print(f"Running loop for {card_id}: {card_id+1} to {card_id + counts[card_id] + 1}")
        for i in range(card_id + 1, card_id + counts[card_id] + 1):
            # print(f"I is {i}")
            id_to_add = str(recursive_func(card_id=i))
            # print(f"ID To add {id_to_add}")
            # if id_to_add not in output.keys():
            #     output[id_to_add] = 1
            output[id_to_add] = output[id_to_add] + 1
        return card_id
    else:
        # print(f"Returning Card: {card_id}")
        # if card_id not in output.keys():
        #     output[str(card_id)] = 1
        return card_id


if __name__ == "__main__":
    for i in range(1, len(counts)):
        recursive_func(card_id=i)
    print(sum(output.values()))
