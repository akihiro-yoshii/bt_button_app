import argparse
import logging

import time

import bt_button.bt_button as bt_button

loglevels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
             logging.INFO, logging.DEBUG]


def parse_args():
    parser = argparse.ArgumentParser()

    args = [
        {"description": "--loglevel",
         "type": int,
         "default": 2,
         "help": "0:critical, 1:error, 2:warning, 3:info, 4:debug"},
    ]

    for c in args:
        desc = c.pop("description")
        parser.add_argument(desc, **c)

    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=loglevels[args.loglevel])

    while True:
        try:
            button = bt_button.AbShutter()
            # button.add_pushed_listener(pushed)
            button.add_released_listener(released)
            button.start()
        except bt_button.DeviceNotFoundError as e:
            logging.debug(e)

        try:
            button = bt_button.BTselfie()
            button.start()
        except bt_button.DeviceNotFoundError as e:
            logging.debug(e)

        time.sleep(1)


def pushed(event):
    print(event)


def released(event):
    print(event)
    print("Released!")


if __name__ == '__main__':
    main()
