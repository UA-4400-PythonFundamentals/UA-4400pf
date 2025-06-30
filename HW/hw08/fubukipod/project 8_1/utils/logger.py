__all__ = ['log_in_file']
import datetime

def log_in_file(message: str, filename: str = 'app.log'):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{timestamp}] {message}'
    print(line)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(line + '\n')
