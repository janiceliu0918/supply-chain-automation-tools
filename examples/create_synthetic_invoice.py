"""Create fictional data only; run from the repository root."""
from pathlib import Path
import pandas as pd
out=Path('examples/synthetic_invoice.xlsx')
pd.DataFrame([['Synthetic invoice - not company data','','',''],['HS Code','Description','Qty','Total'],['0000.00','DEMO ITEM A','2','20.00'],['0000.01','DEMO ITEM B','3','45.00']]).to_excel(out,index=False,header=False)
print(out)
