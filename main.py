import argparse
import logging

import time

import bt_button
import bluepy

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
    ab_shutter.attach_pushed_listener(pushed)
    ab_shutter.attach_released_listener(released)

    bt_selfie = bt_button.BTselfie(MAC_BS)
    bt_selfie.attach_clicked_listener(released)

    smart_palette = bt_button.SmartPalette(MAC_PA)
    smart_palette.attach_pushed_listener(bt_button.SmartPaletteButton.RED, pushed)

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

        if not smart_palette.is_connected():
            try:
                smart_palette.connect()
            except bt_button.DeviceNotFoundError as e:
                logging.debug(e)
            # except bluepy.btle.BTLEDisconnectError as e:
            #     logging.debug(e)

        time.sleep(1)


def pushed(event = None):
    print(event)
    print("Pushed!")


def released(event):
    print(event)
    print("Released!")


if __name__ == '__main__':
    main()
