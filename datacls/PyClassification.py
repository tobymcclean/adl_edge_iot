from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq


class PyClassificationData:
    def __init__(self, index: int = 0, output: str = '', label: str = '', probability: float = 0.0):
        self.__index = IotValue()
        self.__output = IotValue()
        self.__label = IotValue()
        self.__class_label = IotValue()
        self.__probability = IotValue()

        self.probability = probability
        self.index = index
        self.output = output
        self.label = label

    @property
    def index(self) -> int:
        return self.__index.int32

    @index.setter
    def index(self, value: int) -> None:
        self.__index.int32 = value

    @property
    def label(self) -> str:
        return self.__label.string

    @label.setter
    def label(self, value: str) -> None:
        self.__label.string = value if value is not None else ''

    @property
    def output(self) -> str:
        return self.__output.string

    @output.setter
    def output(self, value: str) -> None:
        self.__output.string = value

    @property
    def probability(self) -> float:
        return self.__probability.float32

    @probability.setter
    def probability(self, value: float) -> None:
        self.__probability.float32 = value

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('index', self.__index))
        data.append(IotNvp('output', self.__output))
        data.append(IotNvp('label', self.__label))
        data.append(IotNvp('probability', self.__probability))
        return data


class PyClassification:

    def __init__(self, engine_id: str = '', stream_id: str = '', frame_id: int = 0):
        self.__engine_id = IotValue()
        self.__stream_id = IotValue()
        self.__frame_id = IotValue()
        self.__data = IotNvpSeq()

        self.engine_id = engine_id
        self.stream_id = stream_id
        self.frame_id = frame_id

    @property
    def engine_id(self) -> str:
        return self.__engine_id.string

    @engine_id.setter
    def engine_id(self, value: str) -> None:
        self.__engine_id.string = value

    @property
    def stream_id(self) -> str:
        return self.__stream_id.string

    @stream_id.setter
    def stream_id(self, value: str) -> None:
        self.__stream_id.string = value

    @property
    def frame_id(self) -> int:
        return self.__frame_id.uint32

    @frame_id.setter
    def frame_id(self, value: int) -> None:
        self.__frame_id.uint32 = value

    def add_data(self, value: PyClassificationData) -> None:
        seq = value.dr_data
        classification_value = IotValue()
        classification_value.nvp_seq = seq
        classification_data: IotNvp = IotNvp()
        classification_data.value = classification_value
        self.__data.push_back(classification_data)

    def add_classification(self,
                           index: int, output: str, label: str, probability: float) -> None:
        self.add_data(PyClassificationData(index, output, label, probability))

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('engine_id', self.__engine_id))
        data.append(IotNvp('stream_id', self.__stream_id))
        data.append(IotNvp('frame_id', self.__frame_id))
        dbox_value = IotValue()
        dbox_value.nvp_seq = self.__data
        data.append(IotNvp('data', dbox_value))
        return data
