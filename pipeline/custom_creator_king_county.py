import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class SqftPriceCreator(BaseEstimator, TransformerMixin):
    """Transformer class to create the 'sqft_price' feature in a DataFrame.
    by dividing the 'price' column by the sum of 'sqft_living' and 'sqft_lot' columns.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.copy()
        X["sqft_price"] = (X["price"] / (X["sqft_living"] + X["sqft_lot"])).round(2)
        return X


class CenterDistanceCreator(BaseEstimator, TransformerMixin):
    """Transformer class to create distance-related features based on center coordinates.
    Creates three new features: 'delta_lat','delta_long', and 'center_distance' based on the latitude and longitude of each
    property in relation to a center location."""

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.copy()
        # Absolute difference of latitude between centre and property
        X["delta_lat"] = np.absolute(47.62774 - X["lat"])
        # Absolute difference of longitude between centre and property
        X["delta_long"] = np.absolute(-122.24194 - X["long"])
        # Distance between centre and property
        X["center_distance"] = (
            ((X["delta_long"] * np.cos(np.radians(47.6219))) ** 2 + X["delta_lat"] ** 2)
            ** (1 / 2)
            * 2
            * np.pi
            * 6378
            / 360
        )
        return X


# This function helps us to calculate the distance between the house overlooking the seafront and the other houses.
def dist(long, lat, ref_long, ref_lat):
    """dist computes the distance in km to a reference location. Input: long and lat of
    the location of interest and ref_long and ref_lat as the long and lat of the reference location
    """
    delta_long = long - ref_long
    delta_lat = lat - ref_lat
    delta_long_corr = delta_long * np.cos(np.radians(ref_lat))
    return (
        ((delta_long_corr) ** 2 + (delta_lat) ** 2) ** (1 / 2) * 2 * np.pi * 6378 / 360
    )


class WaterDistanceCreator(BaseEstimator, TransformerMixin):
    """Transformer class to create the 'water_distance' feature based on waterfront proximity.
    Calculates the distance between each property and the waterfront. It creates a new feature called 'water_distance' that represents the
    minimum distance to the waterfront for each property.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.copy()
        water_list = X.query("waterfront == 1")

        water_distance = []
        # For each row in our data frame we now calculate the distance to the seafront
        for idx, lat in X.lat.items():
            ref_list = []
            for i, j in zip(list(water_list.long), list(water_list.lat)):
                ref_list.append(dist(X.long[idx], X.lat[idx], i, j).min())
            water_distance.append(min(ref_list))
        X["water_distance"] = water_distance
        return X


class DropNoPredictionValues(BaseEstimator, TransformerMixin):
    """Transformer class to drop irrelevant columns from a DataFrame. Drops specified columns from the DataFrame.
    It is used to remove columns that are not relevant for prediction purposes.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.copy()
        drop_lst = ["sqft_price", "date", "delta_lat", "delta_long", "bath_bed_ratio"]
        features_label = [x for x in X.columns if x not in drop_lst]

        return X[features_label]
