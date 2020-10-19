from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq, IotByteSeq_from_buffer


class PyDetectionBoxData:
    def __init__(self, tracker_obj_id: int = 0, category_id: int = 0, category_label: str = '',
                 x1: float = 0.0, y1: float = 0.0, x2: float = 0.0, y2: float = 0.0, probability: float = 0.0,
                 color: str = '', metadata: str = ''):
        self.__tracker_obj_id = IotValue()
        self.__category_id = IotValue()
        self.__category_label = IotValue()
        self.__x1 = IotValue()
        self.__y1 = IotValue()
        self.__x2 = IotValue()
        self.__y2 = IotValue()
        self.__probability = IotValue()
        self.__color = IotValue()
        self.__metadata = IotValue()

        self.tracker_obj_id = tracker_obj_id
        self.cateogry_id = category_id
        self.category_label = category_label
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.probability = probability
        self.color = color
        self.metadata = metadata

    @property
    def tracker_obj_id(self) -> int:
        return self.__tracker_obj_id.int64

    @tracker_obj_id.setter
    def tracker_obj_id(self, value: int) -> None:
        self.__tracker_obj_id.int64 = value

    @property
    def category_id(self) -> int:
        return self.__category_id.int64

    @category_id.setter
    def category_id(self, value: int) -> None:
        try:
            self.__class_id.int64 = int(value)
        except TypeError:
            print(f'Classid type error {value}')
            self.__class_id.int64 = -1

    @property
    def category_label(self) -> str:
        return self.__category_label.string

    @category_label.setter
    def category_label(self, value: str) -> None:
        self.__category_label.string = value if value is not None else ''

    @property
    def x1(self) -> float:
        return self.__x1.float64

    @x1.setter
    def x1(self, value: float) -> None:
        self.__x1.float64 = float(value)

    @property
    def y1(self) -> float:
        return self.__y1.float64

    @y1.setter
    def y1(self, value: float) -> None:
        self.__y1.float64 = float(value)

    @property
    def x2(self) -> float:
        return self.__x2.float64

    @x2.setter
    def x2(self, value: float) -> None:
        self.__x2.float64 = float(value)

    @property
    def y2(self) -> float:
        return self.__y2.float64

    @y2.setter
    def y2(self, value: float) -> None:
        self.__y2.float64 = float(value)

    @property
    def probability(self) -> float:
        return self.__probability.float64

    @probability.setter
    def probability(self, value: float) -> None:
        self.__probability.float64 = float(value)

    @property
    def color(self) -> str:
        return self.__color.string

    @color.setter
    def color(self, value: str) -> None:
        self.__color.string = value if value is not None else ''

    @property
    def metadata(self) -> str:
        return self.__metadata.string

    @metadata.setter
    def metadata(self, value: str) -> None:
        self.__metadata.string = value if value is not None else ''

    @property
    def dr_data(self):
        data = IotNvpSeq()
        data.append(IotNvp('tracker_obj_id', self.__tracker_obj_id))
        data.append(IotNvp('category_id', self.__category_id))
        data.append(IotNvp('category_label', self.__category_label))
        data.append(IotNvp('x1', self.__x1))
        data.append(IotNvp('y1', self.__y1))
        data.append(IotNvp('x2', self.__x2))
        data.append(IotNvp('y2', self.__y2))
        data.append(IotNvp('probability', self.__probability))
        data.append(IotNvp('color', self.__color))
        data.append(IotNvp('metadata', self.__metadata))
        return data


class PyDepthDetectionBoxData(PyDetectionBoxData):
    def __init__(self, obj_id=0, obj_label='', class_id=0, class_label='', x1=0.0, y1=0.0, x2=0.0, y2=0.0,
                 probability=0.0, meta='', dist_x=0.0, dist_y=0.0, dist_z=0.0):
        super().__init__(obj_id, obj_label, class_id, class_label, x1, y1, x2, y2, probability, meta)
        self.__dist_x = IotValue()
        self.__dist_y = IotValue()
        self.__dist_z = IotValue()

        self.dist_x = dist_x
        self.dist_y = dist_y
        self.dist_z = dist_z

    @property
    def dist_x(self) -> float:
        return self.__dist_x.float64

    @dist_x.setter
    def dist_x(self, value: float) -> None:
        self.__dist_x.float64 = value

    @property
    def dist_y(self) -> float:
        return self.__dist_y.float64

    @dist_y.setter
    def dist_y(self, value: float) -> None:
        self.__dist_y.float64 = value

    @property
    def dist_z(self) -> float:
        return self.__dist_z.float64

    @dist_z.setter
    def dist_z(self, value: float) -> None:
        self.__dist_z.float64 = value

    @property
    def dr_data(self):
        data = super().dr_data
        data.append(IotNvp('dist_x', self.__dist_x))
        data.append(IotNvp('dist_y', self.__dist_y))
        data.append(IotNvp('dist_z', self.__dist_z))
        return data


class PyDetectionBox:

    def __init__(self, engine_id='', frame_id=0):
        self.__engine_id = IotValue()
        self.__frame_id = IotValue()
        self.__data = IotNvpSeq()

        self.engine_id = engine_id
        self.frame_id = frame_id

    @property
    def engine_id(self):
        return self.__engine_id.string

    @engine_id.setter
    def engine_id(self, value):
        self.__engine_id.string = value

    @property
    def frame_id(self):
        return self.__frame_id.uint32

    @frame_id.setter
    def frame_id(self, value):
        self.__frame_id.uint32 = value

    def add_data(self, value: PyDetectionBoxData):
        seq = value.dr_data
        value = IotValue()
        value.nvp_seq = seq
        it = IotNvp()
        it.value = value
        self.__data.push_back(it)

    def add_box(self, tracker_obj_id: int = 0, category_id: int = 0, category_label: str = '',
                x1: float = 0.0, y1: float = 0.0, x2: float = 0.0, y2: float = 0.0, probability: float = 0.0,
                color: str = '', metadata: str = ''):
        self.add_data(
            PyDetectionBoxData(tracker_obj_id, category_id, category_label, x1, y1, x2, y2, probability, color,
                               metadata))

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('engine_id', self.__engine_id))
        data.append(IotNvp('frame_id', self.__frame_id))
        dbox_value = IotValue()
        dbox_value.nvp_seq = self.__data
        data.append(IotNvp('detection_box_data', dbox_value))
        return data


class PyDepthDetectionBox(PyDetectionBox):

    def add_box(self,
                obj_id, obj_label, class_id, class_label, x1, y1, x2, y2, probability, meta,
                dist_x, dist_y, dist_z):
        self.add_data(PyDepthDetectionBoxData(obj_id, obj_label, class_id, class_label, x1, y1, x2, y2,
                                              probability, meta, dist_x, dist_y, dist_z))
