import ad2usb
import time
import traceback

class NoDeviceError(Exception):
    pass

class CommError(Exception):
    pass

class TimeoutError(Exception):
    pass

class Firmware(object):
    STAGE_START = 0
    STAGE_WAITING = 1
    STAGE_BOOT = 2
    STAGE_LOAD = 3
    STAGE_UPLOADING = 4
    STAGE_DONE = 5

    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def upload(dev, filename, progress_callback=None):
        def do_upload():
            with open(filename) as f:
                for line in f:
                    line = line.rstrip()

                    if line[0] == ':':
                        dev.write(line + "\r")
                        res = dev.read_line()

                        if progress_callback is not None:
                            progress_callback(Firmware.STAGE_UPLOADING)

                        time.sleep(0.05)

        def read_until(pattern, timeout=0.0):
            start_time = time.time()
            buf = ''
            position = 0

            while True:
                try:
                    char = dev.read()

                    if char is not None and char != '':
                        if char == pattern[position]:
                            position = position + 1
                            if position == len(pattern):
                                break
                        else:
                            position = 0

                except Exception, err:
                    traceback.print_exc(err)

                if timeout > 0 and time.time() - start_time > timeout:
                    raise TimeoutError('Timed out waiting for pattern: {0}'.format(pattern))

        if dev is None:
            raise NoDeviceError('No device specified for firmware upload.')

        if progress_callback is not None:
            progress_callback(Firmware.STAGE_START)

        dev.close_reader()
        while dev._read_thread.is_alive():
            if progress_callback is not None:
                progress_callback(Firmware.STAGE_WAITING)

            time.sleep(1)

        try:
            if progress_callback is not None:
                progress_callback(Firmware.STAGE_BOOT)

            dev.write("=")
            read_until('!boot', timeout=10.0)

            if progress_callback is not None:
                progress_callback(Firmware.STAGE_LOAD)

            dev.write("=")
            read_until('!load', timeout=10.0)

            do_upload()
            if progress_callback is not None:
                progress_callback(Firmware.STAGE_DONE)

        except TimeoutError, err:
            print traceback.print_exc(err)
            pass