import pandas as pd
def scoring_single(chain, email_text):
    return chain.invoke(email_text)

def bulk_scoring(chain, file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    else:
        raise ValueError(f"Either CSV or XLSX File must be provided")
    results = df.copy()
    results[['classification', 'reason', 'score']] = results['email'].apply(
        lambda x: pd.Series(chain.invoke(x))
    )

    return results

def run_scoring(chain, email_text=None, file_path=None):
    if email_text:
        return scoring_single(chain, email_text)
    elif file_path:
        return bulk_scoring(chain, file_path)
    else:
        raise ValueError("Either email_text or file_path must be provided.")