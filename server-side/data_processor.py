class DataProcessor:
    ACTIONS = {'SET': 1, 'GET': 2, 'LLEN': 3, 'RPUSH': 4, 'LPOP': 5, 'RPOP': 6, 'LRANGE': 7, 'QUIT': 8,
               'KEYS': 14, 'DEL': 15, 'FLUSHDB': 16}
    COMMANDS_LENGTH = {'SET': 3, 'GET': 2, 'LLEN': 2, 'RPUSH': 3, 'LPOP': 2, 'RPOP': 2, 'LRANGE': 4, 'QUIT': 1,
                       'KEYS': 1, 'DEL': 2, 'FLUSHDB': 1}

    @staticmethod
    def process_input(input_string, user):
        input_array = input_string.split()
        if input_array[0] not in DataProcessor.ACTIONS:
            return "Wrong command"
        else:
            command_type = DataProcessor.ACTIONS[input_array[0]]
            if ((command_type == 4) and len(input_array) < DataProcessor.COMMANDS_LENGTH[input_array[0]]) or \
             ((command_type != 4) and len(input_array) != DataProcessor.COMMANDS_LENGTH[input_array[0]]):
                return "Wrong command"
            else:
                if command_type == 1:
                    return user.add_key_string(input_array[1], input_array[2])
                elif command_type == 2:
                    return user.get_key_string(input_array[1])
                elif command_type == 3:
                    return user.get_list_length(input_array[1])
                elif command_type == 4:
                    values = []
                    for i in range(2, len(input_array)):
                        values.append(input_array[i])
                    return user.add_list_element(input_array[1], values)
                elif command_type == 5:
                    return user.lpop(input_array[1])
                elif command_type == 6:
                    return user.rpop(input_array[1])
                elif command_type == 7:
                    return user.get_list_element(key=input_array[1], start=int(input_array[2]), end=int(input_array[3]))
                elif command_type == 8:
                    return user.save_progress()
                elif command_type == 14:
                    return user.get_all_keys()
                elif command_type == 15:
                    return user.del_key(input_array[1])
                elif command_type == 16:
                    return user.clear_all_key()

