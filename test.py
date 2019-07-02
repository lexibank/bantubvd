# Each language in our database has around 430 words associated with it.


def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_languages(cldf_dataset):
    # This database contains 4,254 lexical items from 10 Bantu languages
    assert len(list(cldf_dataset["LanguageTable"])) == 10


def test_forms(cldf_dataset):
    # This database contains 4,254 lexical items from 10 Bantu languages
    # we get some more as we split some entries:
    #   - id 00594 = lòòrà, ròòrà
    #   - id 00751 = -jà, -jààxà
    #   - id 01398 = ɓéè/méè
    assert len(list(cldf_dataset["FormTable"])) == 4254 + 3


def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 430


def test_sources(cldf_dataset):
    # 1 source per language, except for language 5 which has two sources, and language 6 with none
    assert len(cldf_dataset.sources) == 10
