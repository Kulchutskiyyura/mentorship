class Separator:
    def __init__(self, data):
        self._data = data

    def run(self, separators: set, include_separators=False):
        separated_list = []
        last_index = 0

        for position, sign in enumerate(self._data):
            if sign in separators:
                if not position == last_index:
                    if not include_separators and position:
                        separated_list.append(self._data[last_index: position])
                    else:
                        separated_list.append(self._data[last_index: position + 1])
                last_index = position + 1

        if last_index != len(self._data):
            separated_list.append(self._data[last_index:])

        return separated_list