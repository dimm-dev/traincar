import os
import sys

def script_run():
    os.chdir("/usr/lib/python3/dist-packages/traincar")
    sys.path.insert(0, '/usr/lib/python3/dist-packages/traincar')
    from game.game import app_run
    app_run()

if __name__ == '__main__':
    from game.game import app_run
    app_run()
