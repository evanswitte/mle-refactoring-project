from abc import ABC

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class AbstractTransformer(ABC):
    """
    This (abstract) transformer is to be inherited by the other transformers.
    It may not be instantiated on its own. Implements 'fit' method and checks whether 'X' is a DataFrame
    """

    def fit(self, X: pd.DataFrame, y=None):
        if not isinstance(X, pd.DataFrame):
            raise TypeError("The input 'X' must be a pandas.DataFrame")
        return self


class BathBedRoomTransformer(BaseEstimator, TransformerMixin, AbstractTransformer):
    """Transformer class to create the 'bath_bed_ratio' feature and filter data.
    Creates a new feature 'bath_bed_ratio' by dividing the number of bathrooms by the number of bedrooms. It also filters out rows
    based on specific conditions of the 'bath_bed_ratio'.
    """

    def transform(self, X, y=None):
        X.copy()
        X["bath_bed_ratio"] = X["bathrooms"] / X["bedrooms"]
        for idx, ratio in enumerate(X["bath_bed_ratio"]):
            if ratio >= 2:
                X.drop(idx, inplace=True)
            elif ratio <= 0.10:
                X.drop(idx, inplace=True)
        return X


class SqftBasementTransformer(BaseEstimator, TransformerMixin, AbstractTransformer):
    """Transformer class to process the 'sqft_basement' feature. Performs transformations on the 'sqft_basement'
    feature. It replaces missing values indicated by '?' with NaN, calculates the square footage
    of the basement by subtracting 'sqft_above' from 'sqft_living', and converts the datatype
    of 'sqft_basement' to float.
    """

    def transform(self, X, y=None):
        X.copy()
        X["sqft_basement"] = X["sqft_basement"].replace("?", np.nan)
        X["sqft_basement"] = X["sqft_living"] - X["sqft_above"]
        X["sqft_basement"] = X["sqft_basement"].astype(float)
        return X


class ViewWaterfrontTransformer(BaseEstimator, TransformerMixin, AbstractTransformer):
    """Transformer class to process the 'view' and 'waterfront' features. Performs transformations on the 'view' and 'waterfront'
    features. It fills missing values in 'view' and 'waterfront' columns with 0.
    """

    def transform(self, X, y=None):
        X.copy()
        X["view"] = X["view"].fillna(0)
        X["waterfront"] = X["waterfront"].fillna(0)
        return X


class LastKnownChangeTransformer(BaseEstimator, TransformerMixin, AbstractTransformer):
    """Transformer class to process the 'yr_renovated' and 'yr_built' features. Performs transformations on the 'yr_renovated' and 'yr_built'
    features. It creates a new feature 'last_known_change' that represents the last known change in the property,
    either through renovation or construction. If 'yr_renovated' is missing or equal to 0, it takes the 'yr_built'
    value as the last known change. Otherwise, it takes the 'yr_renovated' value. It also drops the 'yr_renovated'
    and 'yr_built' columns from the DataFrame.
    """

    def transform(self, X, y=None):
        X.copy()
        last_known_change = []
        for idx, yr_re in X.yr_renovated.items():
            if str(yr_re) == "nan" or yr_re == 0.0:
                last_known_change.append(X.yr_built[idx])
            else:
                last_known_change.append(int(yr_re))
        X["last_known_change"] = last_known_change
        X.drop("yr_renovated", axis=1, inplace=True)
        X.drop("yr_built", axis=1, inplace=True)
        return X
