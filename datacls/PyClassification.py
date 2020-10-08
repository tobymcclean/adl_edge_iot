from adlinktech.datariver import IotValue, IotNvp, IotNvpSeq


class PyClassificationData:
    def __init__(self, category_id: int = -1, category_label='',
                 super_category_id: int = -1, super_category_label='',
                 metadata: str = '', probability: float = 0.0):
        self.__category_id = IotValue()
        self.__category_label = IotValue()
        self.__super_category_id = IotValue()
        self.__super_category_label = IotValue()
        self.__metadata = IotValue()
        self.__probability = IotValue()

        self.category_id = category_id
        self.category_label = category_label
        self.super_category_id = super_category_id
        self.super_category_label = super_category_label
        self.metadata = metadata
        self.probability = probability

    @property
    def category_id(self) -> int:
        return self.__category_id.int64

    @category_id.setter
    def category_id(self, value: int) -> None:
        self.__index.int64 = value

    @property
    def category_label(self) -> str:
        return self.__category_label.string

    @category_label.setter
    def category_label(self, value: str) -> None:
        self.__category_label.string = value if value is not None else ''

    @property
    def super_category_id(self) -> int:
        return self.__super_category_id.int64

    @super_category_id.setter
    def super_category_id(self, value: int) -> None:
        self.__super_category_id.int64 = value

    @property
    def super_category_label(self) -> str:
        return self.__super_category_label.string

    @super_category_label.setter
    def super_category_label(self, value: str) -> None:
        self.__super_category_label.string = value

    @property
    def metadata(self) -> str:
        return self.__metadata.string

    @metadata.setter
    def metadata(self, value: str) -> None:
        self.__metadata.string = value

    @property
    def probability(self) -> float:
        return self.__probability.float64

    @probability.setter
    def probability(self, value: float) -> None:
        self.__probability.float64 = value

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('category_id', self.__category_id))
        data.append(IotNvp('category_label', self.__category_label))
        data.append(IotNvp('super_category_id', self.__super_category_id))
        data.append(IotNvp('super_category_label', self.__super_category_label))
        data.append(IotNvp('metadata', self.__metadata))
        data.append(IotNvp('probability', self.__probability))
        return data


class PyClassification:

    def __init__(self, engine_id: str = '', model_id: str = '', frame_id: int = 0):
        self.__engine_id = IotValue()
        self.__frame_id = IotValue()
        self.__model_id = IotValue()
        self.__data = IotNvpSeq()

        self.engine_id = engine_id
        self.model_id = model_id
        self.frame_id = frame_id

    @property
    def engine_id(self) -> str:
        return self.__engine_id.string

    @engine_id.setter
    def engine_id(self, value: str) -> None:
        self.__engine_id.string = value

    @property
    def model_id(self) -> str:
        return self.__model_id.string

    @model_id.setter
    def model_id(self, value: str) -> None:
        self.__model_id.string = value

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
                           category_id: int = -1, category_label='',
                           super_category_id: int = -1, super_category_label='',
                           metadata: str = '', probability: float = 0.0) -> None:
        self.add_data(
            PyClassificationData(category_id, category_label, super_category_id, super_category_label, metadata,
                                 probability))

    @property
    def dr_data(self) -> IotNvpSeq:
        data = IotNvpSeq()
        data.append(IotNvp('engine_id', self.__engine_id))
        data.append(IotNvp('frame_id', self.__frame_id))
        data.append(IotNvp('model_id', self.__model_id))
        value = IotValue()
        value.nvp_seq = self.__data
        data.append(IotNvp('classification_data', value))
        return data
