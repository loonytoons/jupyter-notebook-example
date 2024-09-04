from data_morph.data.loader import DataLoader
from data_morph.shapes.factory import ShapeFactory
from data_morph.morpher import DataMorpher


def generate_datamorph_example(dataset: str = "panda", output_shape: str = "star", output_dir: str = 'data_morph/output'):
    assert dataset in DataLoader.AVAILABLE_DATASETS, f"Unexpected dataset value requested - recieved: {dataset}; supported: {DataLoader.AVAILABLE_DATASETS}"
    assert output_shape in ShapeFactory.AVAILABLE_SHAPES, f"Unexpected output shape requested - recieved: {output_shape}; supported: {ShapeFactory.AVAILABLE_SHAPES}"
   
    dataset = DataLoader.load_dataset(dataset)
    shape_factory = ShapeFactory(dataset)
    target_shape = shape_factory.generate_shape(output_shape)

    morpher = DataMorpher(
        decimals=2,
        in_notebook=True,  # whether you are running in a Jupyter Notebook
        output_dir='data_morph/output',
        #keep_frames=True,
        forward_only_animation=True
    )

    result = morpher.morph(start_shape=dataset, target_shape=target_shape)