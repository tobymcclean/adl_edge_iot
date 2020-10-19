from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq, IotByteSeq_from_buffer

class PyFrameData:

    def __init__(self, frame_id = 0, timestamp = 0, data = [],
                 width = 0, height = 0, channels = 0, size = 0, format = '', compression = '', framerate = 0.0):
        self.__frame_id  = IotValue()
        self.__timestamp = IotValue()
        self.__video_data = IotValue()
        self.__width  = IotValue()
        self.__height  = IotValue()
        self.__channels = IotValue()
        self.__size = IotValue()
        self.__format = IotValue()
        self.__compression = IotValue()
        self.__framerate = IotValue()

        self.frame_id = frame_id
        self.timestamp = timestamp
        self.data = data
        self.width = width
        self.height = height
        self.channels = channels
        self.size = size
        self.format = format
        self.compression = compression
        self.framerate = framerate


    @property
    def frame_id(self):
        return self.__frame_id.uint32

    @frame_id.setter
    def frame_id(self, value):
        self.__frame_id.uint32 = value

    @property
    def timestamp(self):
        return self.__timestamp.int64

    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp.int64 = value

    @property
    def video_data(self):
        return self.__video_data.byte_seq

    @video_data.setter
    def video_data(self, value):
        self.__video_data.byte_seq = IotByteSeq_from_buffer(value)

    @property
    def width(self):
        return self.__width.uint32

    @width.setter
    def width(self, value):
        self.__width.uint32 = value

    @property
    def height(self):
        return self.__height.uint32

    @height.setter
    def height(self, value):
        self.__height.uint32 = value

    @property
    def channels(self):
        return self.__channels.uint32

    @channels.setter
    def channels(self, value):
        self.__channels.uint32 = value

    @property
    def size(self):
        return self.__size.uint64

    @size.setter
    def size(self, value):
        self.__size.uint64 = value

    @property
    def format(self):
        return self.__format.string

    @format.setter
    def format(self, value):
        self.__format.string = value

    @property
    def compression(self):
        return self.__compression.string

    @compression.setter
    def compression(self, value):
        self.__compression.string = value


    @property
    def framerate(self):
        return self.__framerate.float32

    @framerate.setter
    def framerate(self, value):
        self.__framerate.float32 = value

    @property
    def dr_data(self):
        data = IotNvpSeq()
        data.append(IotNvp('frame_id', self.__frame_id))
        data.append(IotNvp('timestamp', self.__timestamp))
        data.append(IotNvp('video_data', self.__video_data))
        data.append(IotNvp('width', self.__width))
        data.append(IotNvp('height', self.__height))
        data.append(IotNvp('channels', self.__channels))
        data.append(IotNvp('size', self.__size))
        data.append(IotNvp('format', self.__format))
        data.append(IotNvp('compression', self.__compression))
        data.append(IotNvp('framerate', self.__framerate))

        return data
