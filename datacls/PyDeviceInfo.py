import logging as log

from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq


class PyDeviceInfo:

    def __init__(self, stream_id='', mac_address='', ip_address='', port=0, uri='', manufacturer='ADLINK',
                 serial='v0.1', model='video-analytics-pipeline', fw_version='', dev_id='', status='DEVICE_STATUS_ONLINE', kind='DEVICE_KIND_UNKNOWN', protocol='INTERFACE_DDS'):
        self.__stream_id = IotValue()
        self.__mac_address = IotValue()
        self.__ip_address = IotValue()
        self.__port = IotValue()
        self.__uri = IotValue()
        self.__manufacturer = IotValue()
        self.__model = IotValue()
        self.__serial = IotValue()
        self.__fw_version = IotValue()
        self.__dev_id = IotValue()
        self.__status = IotValue()
        self.__kind = IotValue()
        self.__protocol = IotValue()

        self.stream_id = stream_id
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.port = port
        self.uri = uri
        self.manufacturer = manufacturer
        self.model = model
        self.serial = serial
        self.fw_version = fw_version
        self.dev_id = dev_id
        self.status = status
        self.kind = kind
        self.protocol = protocol

    @property
    def stream_id(self):
        return self.__stream_id.string

    @stream_id.setter
    def stream_id(self, value):
        self.__stream_id.string = str(value)

    @property
    def mac_address(self):
        return self.__mac_address.string

    @mac_address.setter
    def mac_address(self, value):
        self.__mac_address.string = str(value)

    @property
    def ip_address(self):
        return self.__ip_address.string

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address.string = str(value)

    @property
    def port(self):
        return self.__port.int32

    @port.setter
    def port(self, value):
        self.__port.int32 = int(value)

    @property
    def uri(self):
        return self.__uri.string

    @uri.setter
    def uri(self, value):
        self.__uri.string = str(value)

    @property
    def manufacturer(self):
        return self.__manufacturer.string

    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer.string = str(value)

    @property
    def model(self):
        return self.__model.string

    @model.setter
    def model(self, value):
        self.__model.string = str(value)

    @property
    def serial(self):
        return self.__serial.string

    @serial.setter
    def serial(self, value):
        self.__serial.string = str(value)

    @property
    def fw_version(self):
        return self.__fw_version.string

    @fw_version.setter
    def fw_version(self, value):
        self.__fw_version.string = str(value)

    @property
    def status(self):
        return self.__status.string

    @status.setter
    def status(self, value):
        self.__status.string = str(value)

    @property
    def kind(self):
        return self.__kind.string

    @kind.setter
    def kind(self, value):
        self.__kind.string = str(value)

    @property
    def protocol(self):
        return self.__protocol.string

    @protocol.setter
    def protocol(self, value):
        self.__protocol.string = str(value)

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('stream_id', self.__stream_id))
        data.append(IotNvp('mac_address', self.__mac_address))
        data.append(IotNvp('ip_address', self.__ip_address))
        data.append(IotNvp('port', self.__port))
        data.append(IotNvp('uri', self.__uri))
        data.append(IotNvp('manufacturer', self.__manufacturer))
        data.append(IotNvp('model', self.__model))
        data.append(IotNvp('serial', self.__serial))
        data.append(IotNvp('fw_version', self.__fw_version))
        data.append(IotNvp('dev_id', self.__dev_id))
        data.append(IotNvp('status', self.__status))
        data.append(IotNvp('kind', self.__kind))
        data.append(IotNvp('protocol', self.__protocol))

        return data
