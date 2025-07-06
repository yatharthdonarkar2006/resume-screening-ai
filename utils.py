import pandas as pd

def export_results(df, filename, filetype='csv'):
    if filetype == 'csv':
        df.to_csv(filename, index=False)
    elif filetype == 'excel':
        df.to_excel(filename, index=False)
    else:
        raise ValueError('Unsupported file type') 