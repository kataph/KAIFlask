import model
if model.GERMAN_MINSTREL_ADDRESS != "local":
    from .model import DummyModel, GermanMinstrel as GermanModel
else:
    from .model import LocalGermanMinstrel as GermanModel

dummyModel = DummyModel()
germanModel = GermanModel()