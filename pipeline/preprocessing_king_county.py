import numpy as np
from custom_creator_king_county import (
    CenterDistanceCreator,
    DropNoPredictionValues,
    SqftPriceCreator,
    WaterDistanceCreator,
)
from custom_transformer_king_county import (
    BathBedRoomTransformer,
    LastKnownChangeTransformer,
    SqftBasementTransformer,
    ViewWaterfrontTransformer,
)
from sklearn.pipeline import Pipeline


class PreprocessingKingCountyData:
    def __init__(self):
        self.data_cleaning_pipeline = Pipeline(
            [
                ("bathroom_bedroom_ratio", BathBedRoomTransformer()),
                ("sqft_basement", SqftBasementTransformer()),
                ("view_and_waterfront", ViewWaterfrontTransformer()),
                ("last_known_change", LastKnownChangeTransformer()),
            ]
        )

        self.feature_engineering_pipeline = Pipeline(
            [
                ("sqft_price", SqftPriceCreator()),
                ("center_distance", CenterDistanceCreator()),
                ("water_distance", WaterDistanceCreator()),
                ("no_pred_values", DropNoPredictionValues()),
            ]
        )

        self.preprocessor_pipe = Pipeline(
            [
                ("data_cleaning", self.data_cleaning_pipeline),
                ("feature_engineering", self.feature_engineering_pipeline),
            ]
        )

    def preprocess_fit_transform(self, df):
        return self.preprocessor_pipe.fit_transform(df)

    def preprocess_transform(self, df):
        return self.preprocessor_pipe.transform(df)
