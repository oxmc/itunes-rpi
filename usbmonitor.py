import threading
class USBDetector():
    def __init__(self):
        thread = threading.Thread(target=self._work)
        thread.daemon = True
        thread.start()
    def _work(self):
        ''' Runs the actual loop to detect the events '''
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')
        # this is module level logger, can be ignored
        LOGGER.info("Starting to monitor for usb")
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            LOGGER.info("Got USB event: %s", device.action)
            if device.action == 'add':
                # some function to run on insertion of usb
                self.on_created()
            else:
                # some function to run on removal of usb
                self.on_deleted()
