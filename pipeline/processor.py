import os
import sys

import pandas as pd
from preprocessing_king_county import PreprocessingKingCountyData

PREPROCESSOR = PreprocessingKingCountyData()


def load_file_to_dataframe(file_path: str) -> pd.DataFrame:
    """Load a file into a Pandas DataFrame.

    This function reads the file located at the given file path and returns a Pandas DataFrame.
    The file format is determined based on the file extension.

    Parameters:
    ----------
    file_path : str
        Path to the file to be loaded.

    Returns:
    ----------
    df : DataFrame
        Loaded DataFrame.

    Raises:
    ----------
    ValueError:
        If the file extension is not supported.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == ".csv":
        df = pd.read_csv(file_path)
    elif file_extension.lower() == ".xlsx":
        df = pd.read_excel(file_path)
    elif file_extension.lower() == ".json":
        df = pd.read_json(file_path)
    elif file_extension.lower() == ".pkl":
        df = pd.read_pickle(file_path)
    else:
        print("Invalid file extension. Supported formats: CSV, XLSX, JSON, PKL.")
        sys.exit(1)

    return df


def main() -> None:
    """Main function to run the data preprocessing script.

    This function is the entry point of the script. It expects the file path to be specified as a command-line argument.
    The file is loaded into a Pandas DataFrame, preprocessed using the predefined PREPROCESSOR, and the transformed DataFrame
    is saved as a CSV file.

    Raises:
    ----------
    ValueError:
        If the file path is not provided as an argument.
    """
    if len(sys.argv) < 2:
        print("Please specify the file path as an argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    df = load_file_to_dataframe(file_path)

    transformed_df = PREPROCESSOR.preprocess_fit_transform(df)
    transformed_df.to_csv("transformed_data.csv", index=False)


if __name__ == "__main__":
    main()
