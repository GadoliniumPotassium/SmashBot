class EventHandler:
    def __init__(self, client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        # add a command to the commands array
        self.commands.append(command)

    def command_handler(self, message):

        # loop through command array
        for command in self.commands:

            # if the message starts with a command trigger
            if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        # returns the results of the function
                        return self.client.send_message(message.channel,
                                                        str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            # return the results of the function
                            return self.client.send_message(message.channel,
                                                            str(command['function'](message, self.client, args)))
                            break
                        else:
                            # return argument error
                            return self.client.send_message(message.channel,
                                                            'command "{}" requires {} argument(s) "{}"'.format(
                                                                command['trigger'], command['args_num'],
                                                                ', '.join(command['args_name'])))
                            break
                else:
                    break
