import pandas as pd
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
INPUT_FOLDER = os.path.join(current_dir, 'archive')

import pathlib
OUTPUT_FOLDER = os.path.join(current_dir, 'output')
pathlib.Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

def load_yelp_orig_data():
    PATH_TO_YELP_REVIEWS = os.path.join(INPUT_FOLDER, 'yelp_academic_dataset_review.json')

    # read the entire file into a python array
    with open(PATH_TO_YELP_REVIEWS, 'r',encoding='utf-8') as f:
        data = f.readlines()

    # remove the trailing "\n" from each line
    data = map(lambda x: x.rstrip(), data)

    data_json_str = "[" + ','.join((data)) + "]"

    # now, load it into pandas
    data_df = pd.read_json(PATH_TO_YELP_REVIEWS, lines=True)

    data_df.head(100000).to_csv(os.path.join(OUTPUT_FOLDER,'output_reviews_top.csv'))

if __name__ == '__main__':
  load_yelp_orig_data()