import pandas as pd
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
    """Preprocessing pipeline for King County real estate data. This class encapsulates the preprocessing steps for King County real estate data.
       It consists of two main pipelines: data cleaning pipeline and feature engineering pipeline.


    Methods:
    ----------
    preprocess_fit_transform(df):
        Fit and transform the input DataFrame using the preprocessing pipeline.
    preprocess_transform(df):
        Transform the input DataFrame using the preprocessing pipeline.

    """

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

    def preprocess_fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit and transform the input DataFrame using the preprocessing pipeline.

        This method fits the preprocessing pipeline to the input DataFrame and applies the transformations.

        Parameters:
        ----------
        df : DataFrame
            Input DataFrame.

        Returns:
        ----------
        preprocessed_df : DataFrame
            Preprocessed DataFrame after fitting and transforming the data.
        """
        return self.preprocessor_pipe.fit_transform(df)

    def preprocess_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform the input DataFrame using the preprocessing pipeline.

        This method applies the transformations from the preprocessing pipeline to the input DataFrame.

        Parameters:
        ----------
        df : DataFrame
            Input DataFrame.

        Returns:
        ----------
        preprocessed_df : DataFrame
            Preprocessed DataFrame after transforming the data.
        """
        return self.preprocessor_pipe.transform(df)
