from pathlib import Path
import pandas as pd

def main():
    # input_file = Path('labeled_data.csv')
    # input_df = pd.read_csv(input_file, header=0, names=['id', 'count','hate_speech','offensive_language','neither','majority_class','tweet'])
    input_file = Path('labeled_data.p')
    input_df = pd.read_pickle(input_file).rename(columns={"class": "majority_class"})
    output_df = parse_df(input_df)
    train_dev_test_split(output_df)

def parse_df(input_df):
    def parse_row(row):
        text = row.tweet
        # problematic = int(int(row.majority_class) != 2) # w/ offsensive
        problematic = int(int(row.majority_class) == 0) # w/o offensive
        return (text, problematic)

    return pd.DataFrame([parse_row(r) for r in input_df.itertuples()], columns=['text', 'problematic'])

def train_dev_test_split(df, train_dev_test=(0.5, 0.25, 0.25)):
    
    # output_folder = Path('../with_offensive_language')
    output_folder = Path('../without_offensive_language')
    
    train, dev, test = train_dev_test
    if ((train + test + dev) != 1) or (not all(x >= 0.0 and x <= 1.0 for x in (train_dev_test))):
        raise Exception("Error: Invalid split values")
    
    df_shuffled = df.sample(frac=1, ignore_index=True, random_state=42)
    
    train_end = int(len(df) * train)
    dev_end = int(len(df) * (train + dev))
    
    df_train = df_shuffled.iloc[:train_end].reset_index(drop=True)
    df_dev = df_shuffled.iloc[train_end:dev_end].reset_index(drop=True)
    df_test = df_shuffled.iloc[dev_end:].reset_index(drop=True)
    
    print(f"Train examples: {len(df_train)}")
    print(f"Dev examplse: {len(df_dev)}")
    print(f"Test examples: {len(df_test)}")
    
    write_output(df_train, output_folder, "train")
    write_output(df_dev, output_folder, "dev")
    write_output(df_test, output_folder, "test")

def write_output(df, output_folder, base_name):
    df.to_csv(Path(output_folder) / f"{base_name}.tsv", sep='\t', index=False)
    df.to_pickle(Path(output_folder) / f"{base_name}.pkl", compression=None, protocol=4)
    df.to_json(Path(output_folder) / f"{base_name}.json", orient="table", indent=4) # Read back with: df = pd.read_json(file_path, typ='frame', orient='table')

if __name__ == '__main__':
    main()