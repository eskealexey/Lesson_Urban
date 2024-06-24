class Grape:
    def __init__(self, color, tip):
        self.color = color
        self.tip = tip

    def view_color(self):
        return self.color

def introspection_info(obj):
    dict_ = {}
    dict_['type'] = type(obj)
    dict_['attributes'] = obj.__dir__()
    dict_['module'] = obj.__module__
    dict_['state'] = obj.__getstate__()

    return dict_

grape = Grape('black', 'technik')
grape_info = introspection_info(grape)

for k, v in grape_info.items():
    print(f'{k}: {v}')

