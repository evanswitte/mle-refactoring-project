"""This script contains all the functions used in the transformer classes for data cleaning and in the creator classes for feature engineering."""
import numpy as np
import pandas as pd


def bath_bed_ratio_outlier(df):
    df.copy()
    df["bath_bed_ratio"] = df["bathrooms"] / df["bedrooms"]
    for idx, ratio in enumerate(df["bath_bed_ratio"]):
        if ratio >= 2:
            df.drop(idx, inplace=True)
        elif ratio <= 0.10:
            df.drop(idx, inplace=True)
    return df


def sqft_basement(df):
    df.copy()
    df["sqft_basement"] = df["sqft_basement"].replace("?", np.nan)
    df["sqft_basement"] = df["sqft_basement"].astype(float)
    df["sqft_basement"] = df["sqft_living"] - df["sqft_above"]
    return df


def fill_missings_view_wf(df):
    df.copy()
    df["view"] = df["view"].fillna(0)
    df["waterfront"] = df["waterfront"].fillna(0)
    return df


def calculate_last_change(df):
    df.copy()
    last_known_change = []
    for idx, yr_re in df.yr_renovated.items():
        if str(yr_re) == "nan" or yr_re == 0.0:
            last_known_change.append(df.yr_built[idx])
        else:
            last_known_change.append(int(yr_re))
    df["last_known_change"] = last_known_change
    df.drop("yr_renovated", axis=1, inplace=True)
    df.drop("yr_built", axis=1, inplace=True)
    return df


def calculate_sqft_price(df):
    df.copy()
    df["sqft_price"] = (df["price"] / (X["sqft_living"] + df["sqft_lot"])).round(2)
    return df


def calculate_center_distance(df):
    df.copy()
    # Absolute difference of latitude between centre and property
    df["delta_lat"] = np.absolute(47.62774 - df["lat"])
    # Absolute difference of longitude between centre and property
    df["delta_long"] = np.absolute(-122.24194 - df["long"])
    # Distance between centre and property
    df["center_distance"] = (
        ((df["delta_long"] * np.cos(np.radians(47.6219))) ** 2 + df["delta_lat"] ** 2)
        ** (1 / 2)
        * 2
        * np.pi
        * 6378
        / 360
    )
    return df


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


def calculate_water_distance(df):
    df.copy()
    water_list = df.query("waterfront == 1")

    water_distance = []
    # For each row in our data frame we now calculate the distance to the seafront
    for idx, lat in df.lat.items():
        ref_list = []
        for i, j in zip(list(water_list.long), list(water_list.lat)):
            ref_list.append(dist(df.long[idx], df.lat[idx], i, j).min())
        water_distance.append(min(ref_list))
    df["water_distance"] = water_distance
    return df
