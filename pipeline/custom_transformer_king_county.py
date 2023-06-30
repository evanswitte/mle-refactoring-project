import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class BathBedRoomTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    

    def transform(self, X, y=None):
        X.copy()
        X["bath_bed_ratio"] = X["bathrooms"] / X["bedrooms"]
        for idx, ratio in enumerate(X["bath_bed_ratio"]):
            if ratio >= 2:
                X.drop(idx, inplace=True)
            elif ratio <= 0.10:
                X.drop(idx, inplace=True)
        return X
    
    
class SqftBasementTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    

    def transform(self, X, y=None):
        X.copy()
        X["sqft_basement"] = X["sqft_basement"].replace("?", np.nan)
        X["sqft_basement"] = X["sqft_living"] - X["sqft_above"]
        X["sqft_basement"] = X["sqft_basement"].astype(float)
        return X
    

class ViewWaterfrontTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self,X, y=None):
        X.copy()
        X["view"] = X["view"].fillna(0)
        X["waterfront"] = X["waterfront"].fillna(0)
        return X
    

class LastKnownChangeTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self,X, y=None):
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