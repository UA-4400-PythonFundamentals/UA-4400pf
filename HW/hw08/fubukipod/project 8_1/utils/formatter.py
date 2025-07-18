__all__ = ['format_string']
COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'reset': '\033[0m',
}

def format_string(s: str, color: str = 'green') -> str:
    code = COLORS.get(color, COLORS['reset'])
    return f"{code}{s}{COLORS['reset']}"
