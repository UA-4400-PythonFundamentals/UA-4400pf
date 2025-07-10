def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        name = f'{name} plays banjo'
    else:
        name = f'{name} does not play banjo'
    return name