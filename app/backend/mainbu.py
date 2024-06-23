from .model import DummyModel, GermanMinstrel as GermanModel, LocalGermanMinstrel

# to test in local, replace GermanModel() with DummyModel()
# germanModel = DummyModel() # local test
germanModel = GermanModel() # production
localModel = LocalGermanMinstrel()