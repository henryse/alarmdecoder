#!/usr/bin/env python

import sys, time
import pyad2usb.ad2usb

def handle_firmware(stage):
    if stage == pyad2usb.ad2usb.util.Firmware.STAGE_START:
        handle_firmware.wait_tick = 0
        handle_firmware.upload_tick = 0
    elif stage == pyad2usb.ad2usb.util.Firmware.STAGE_WAITING:
        if handle_firmware.wait_tick == 0:
            sys.stdout.write('Waiting for device.')
        handle_firmware.wait_tick += 1

        sys.stdout.write('.')
        sys.stdout.flush()
    elif stage == pyad2usb.ad2usb.util.Firmware.STAGE_BOOT:
        if handle_firmware.wait_tick > 0: print ""
        print "Rebooting device.."
    elif stage == pyad2usb.ad2usb.util.Firmware.STAGE_LOAD:
        print 'Waiting for boot loader..'
    elif stage == pyad2usb.ad2usb.util.Firmware.STAGE_UPLOADING:
        if handle_firmware.upload_tick == 0:
            sys.stdout.write('Uploading firmware.')

        handle_firmware.upload_tick += 1

        if handle_firmware.upload_tick % 30 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
    elif stage == pyad2usb.ad2usb.util.Firmware.STAGE_DONE:
        print "\r\nDone!"

def main():
    device = '/dev/ttyUSB0'
    firmware = None

    if len(sys.argv) < 2:
        print "Syntax: {0} <firmware> [interface]".format(sys.argv[0])
        sys.exit(1)

    firmware = sys.argv[1]
    if len(sys.argv) > 2:
        device = sys.argv[2]

    print "Flashing device: {0}\r\nFirmware: {1}".format(device, firmware)

    dev = pyad2usb.ad2usb.devices.SerialDevice(interface=device)
    dev.open(baudrate=19200)

    time.sleep(3)
    pyad2usb.ad2usb.util.Firmware.upload(dev, firmware, handle_firmware)

    dev.close()

if __name__ == "__main__":
    main()
