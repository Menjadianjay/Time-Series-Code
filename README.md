Python coursework for a time-series course exponential moving average (EMA) analysis of a bank customer-balance dataset and of BBCA.JK (Bank Central Asia) stock prices from Yahoo Finance. Code comments and notebook text are in Indonesian.

## What's in the repo

All code lives under `Src_Tugas_1/`, including the Tugas 2 and 3 work.

| Assignment | Path | What it does | Data source |
|---|---|---|---|
| Tugas 1 | `Src_Tugas_1/srcs/Tugas1/` | Only a copy of the dataset (`bank-full-copy.csv`); no script on `main` | local CSV |
| Tugas 2 | `Src_Tugas_1/srcs/Tugas2/tugas2_225314118.py` | Rebuilds a date column for the bank dataset and plots `balance` with EMA 9, 21 and 55 | local CSV |
| Tugas 2 (example) | `Src_Tugas_1/srcs/Tugas2/contohploy.py` | Downloads the last 360 days of BBCA.JK, plots EMA 21 / 55 and marks buy/sell points where they cross | Yahoo Finance via `yfinance` |
| Tugas 3 | `Src_Tugas_1/srcs/Tugas3_Preprocessing/Preprocessing_225314118.ipynb` | Downloads 5 years of BBCA.JK, checks for nulls and duplicates, plots Close/High/Low against EMA 9/12/30, and fits linear trendlines over three date ranges | Yahoo Finance via `yfinance` |

## Requirements

- Python 3. The notebook's saved kernel metadata reports Python 3.13.2; no minimum version is declared anywhere in the repo.
- Packages: `pandas`, `numpy`, `matplotlib`, `yfinance`, plus Jupyter to open the notebook.
- Internet access for `contohploy.py` and the notebook (they query Yahoo Finance). Tugas 2 works offline.

The repo has no `requirements.txt` or lockfile, so versions are not pinned. The Tugas 2 script was run for this README with Python 3.13, pandas 3.0.5, numpy 2.5.3 and matplotlib 3.11.2.

## Installation

```bash
git clone https://github.com/Menjadianjay/Time-Series-Code.git
cd Time-Series-Code
pip install pandas numpy matplotlib yfinance notebook
```

## Usage

### Tugas 2: EMA on the bank dataset

The script reads `srcs\tugas2\bank-full.csv`, a Windows-style path relative to the current directory, so it expects to be run from `Src_Tugas_1/`.

On Windows (not tested here):

```bat
cd Src_Tugas_1
python srcs\Tugas2\tugas2_225314118.py
```

On Linux or macOS the hardcoded path fails with `FileNotFoundError`. Change line 9 of the script to `data_path = r"srcs/Tugas2/bank-full.csv"`, then run from `Src_Tugas_1/`:

```bash
cd Src_Tugas_1
python srcs/Tugas2/tugas2_225314118.py
```

A Matplotlib window opens showing the raw balance (gray) and the three EMAs. With the path fixed, the script produced 45,211 rows with dates running from 2008-05-05 to 2010-11-17 (checked headlessly; the plot window itself was not viewed).

How the dates are made: the CSV has only `day` and `month`. The script starts at year 2008 and increments the year each time the month goes from `dec` to `jan` between consecutive rows, so it assumes the rows are in chronological order. The plot's title says "Rerata Tabungan Nasabah" (average savings), but it plots each row's own `balance`, not an average.

### Tugas 2 example: BBCA.JK crossover signals

```bash
python Src_Tugas_1/srcs/Tugas2/contohploy.py
```

Not executed for this README (no access to Yahoo Finance from the environment where it was written). The plot title says "CIMSA" and the y-axis says "Price in TL", which look like leftovers from a template and do not match BBCA.JK.

### Tugas 3: stock preprocessing notebook

```bash
jupyter notebook Src_Tugas_1/srcs/Tugas3_Preprocessing/Preprocessing_225314118.ipynb
```

Run the cells top to bottom. Not executed for this README. Things to know:

- It calls `history(period='5y')`, so the data window moves with the day you run it. Plots and the row count mentioned in the notebook text (1,208) will differ from the saved outputs.
- Plot legends read "EMA 90 / 180 / 360" while the code uses spans 9, 12 and 30. The per-period loop uses spans 9, 15 and 30 on the `Low` price.

## Data

`bank-full.csv` is semicolon-separated with 17 columns (`age`, `job`, `marital`, `education`, `default`, `balance`, `housing`, `loan`, `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`, `y`) and 45,211 rows. These columns match the public Bank Marketing dataset from the UCI repository, but the repo itself does not state where the file came from or under what terms it is shared.

The file is committed three times, byte-identical (4.6 MB each):

- `Src_Tugas_1/data/bank-full.csv`
- `Src_Tugas_1/srcs/Tugas1/bank-full-copy.csv`
- `Src_Tugas_1/srcs/Tugas2/bank-full.csv` (the copy the Tugas 2 script reads)

## Testing

There are no tests and no CI configuration.

## Project structure

```
Src_Tugas_1/
├── data/bank-full.csv
└── srcs/
    ├── Tugas1/bank-full-copy.csv
    ├── Tugas2/
    │   ├── bank-full.csv
    │   ├── contohploy.py
    │   └── tugas2_225314118.py
    └── Tugas3_Preprocessing/Preprocessing_225314118.ipynb
.vscode/settings.json   # editor settings only
```

## Contributing

There is no contribution guide. Issues and pull requests can be opened on the GitHub repository; no review process or support policy is published.

## License

No license file is present, so no license is granted by default. The repository owner needs to choose and add one.
