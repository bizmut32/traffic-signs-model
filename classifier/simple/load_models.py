from pathlib import Path

import classifier
from classifier.simple.model import get_model


def load_model():
    cnns = []
    for i in range(0, 4):
        model = get_model()
        model.load_weights('{path}/models/model_committee{i}.h5'.format(path=Path(classifier.__file__).parent, i=i))
        cnns.append(model)
    return cnns
