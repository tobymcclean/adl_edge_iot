from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq, IotByteSeq_from_buffer


class PyDetectionPointData:
    def __init__(self, obj_id=0, obj_label='', class_id=0, class_label='', x=0.0, y=0.0, radius=0.0, probability=0.0,
                 meta=''):
        self._obj_id = IotValue()
        self._obj_label = IotValue()
        self._class_id = IotValue()
        self._class_label = IotValue()
        self._x = IotValue()
        self._y = IotValue()
        self._radius = IotValue()
        self._probability = IotValue()
        self._meta = IotValue()
        self.obj_id = obj_id
        self.obj_label = obj_label
        self.class_id = class_id
        self.class_label = class_label
        self.x = x
        self.y = y
        self.radius = radius
        self.probability = probability
        self.meta = meta

    @property
    def obj_id(self):
        return self._obj_id.int32

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id.int32 = value

    @property
    def obj_label(self):
        return self._obj_label.string

    @obj_label.setter
    def obj_label(self, value):
        self._obj_label.string = value

    @property
    def class_id(self):
        return self._class_id.int32

    @class_id.setter
    def class_id(self, value):
        self._class_id.int32 = value

    @property
    def class_label(self):
        return self._class_label.string

    @class_label.setter
    def class_label(self, value):
        self._class_label.string = value

    @property
    def x(self):
        return self._x.float32

    @x.setter
    def x(self, value):
        self._x.float32 = value

    @property
    def y(self):
        return self._y.float32

    @y.setter
    def y(self, value):
        self._y.float32 = value

    @property
    def radius(self):
        return self._radius.float32

    @radius.setter
    def radius(self, value):
        self._radius.float32 = value

    @property
    def probability(self):
        return self._probability.float32

    @probability.setter
    def probability(self, value):
        self._probability.float32 = value

    @property
    def meta(self):
        return self._meta.string

    @meta.setter
    def meta(self, value):
        self._meta.string = value

    @property
    def dr_data(self):
        data = IotNvpSeq()
        data.append(IotNvp('obj_id', self._obj_id))
        data.append(IotNvp('obj_label', self._obj_label))
        data.append(IotNvp('class_id', self._class_id))
        data.append(IotNvp('class_label', self._class_label))
        data.append(IotNvp('x', self._x))
        data.append(IotNvp('y', self._y))
        data.append(IotNvp('radius', self._radius))
        data.append(IotNvp('probability', self._probability))
        data.append(IotNvp('meta', self._meta))
        return data


class PyDetectionPoint:
    def __init__(self, engine_id='', stream_id='', frame_id=0):
        self._engine_id = IotValue()
        self._stream_id = IotValue()
        self._frame_id = IotValue()
        self._data = []
        self.engine_id = engine_id
        self.stream_id = stream_id
        self.frame_id = frame_id

    @property
    def engine_id(self):
        return self._engine_id.string

    @engine_id.setter
    def engine_id(self, value):
        self._engine_id.string = value

    @property
    def stream_id(self):
        return self._stream_id.string

    @stream_id.setter
    def stream_id(self, value):
        self._stream_id.string = value

    @property
    def frame_id(self):
        return self._frame_id.uint32

    @frame_id.setter
    def frame_id(self, value):
        self._frame_id.uint32 = value

    def add_data(self, value):
        if value is not None:
            self._data.append(value)

    @property
    def dr_data(self):
        data = IotNvpSeq()
        data.append(IotNvp('engine_id', self._engine_id))
        data.append(IotNvp('stream_id', self._stream_id))
        data.append(IotNvp('frame_id', self._frame_id))
        nvp_seq = IotNvpSeq()
        for value in self._data:
            iot_value = IotValue()
            iot_value.nvp_seq = value.dr_data
            it = IotNvp()
            it.value = iot_value
            nvp_seq.push_back(it)
        seq_value = IotValue()
        seq_value.nvp_seq = nvp_seq
        data.append(IotNvp('data', seq_value))
        return data
