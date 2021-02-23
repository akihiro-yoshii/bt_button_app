import argparse
import logging

import time

import bt_button

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

    ab_shutter = bt_button.AbShutter(MAC_AB)
    # button.add_pushed_listener(pushed)
    ab_shutter.add_released_listener(released)

    bt_selfie = bt_button.BTselfie(MAC_BS)

    while True:
        if not ab_shutter.is_connected():
            try:
                ab_shutter.connect()
            except bt_button.DeviceNotFoundError as e:
                logging.debug(e)

        if not bt_selfie.is_connected():
            try:
                bt_selfie.connect()
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
