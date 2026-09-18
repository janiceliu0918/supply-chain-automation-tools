import unittest,subprocess,sys,tempfile
from pathlib import Path
import pandas as pd
SCRIPT=Path(__file__).resolve().parents[1]/'candata_import/import_tool.py'
class InvoiceTests(unittest.TestCase):
    def run_case(self,rows):
        with tempfile.TemporaryDirectory() as d:
            inp=Path(d)/'synthetic.xlsx';out=Path(d)/'out.csv'
            pd.DataFrame(rows).to_excel(inp,index=False,header=False)
            result=subprocess.run([sys.executable,str(SCRIPT),str(inp),'--output',str(out)],capture_output=True)
            return result.returncode,out.read_text() if out.exists() else ''
    def test_valid_synthetic_invoice(self):
        status,out=self.run_case([['HS Code','Description','Qty','Total'],['0000.01','DEMO','2','20']])
        self.assertEqual(status,0);self.assertIn('000001,000001,DEMO,2,20',out)
    def test_missing_header_fails(self):
        status,out=self.run_case([['Unknown','Description','Qty','Total'],['x','DEMO','2','20']]);self.assertNotEqual(status,0);self.assertEqual(out,'')
    def test_missing_required_column_fails(self):
        status,out=self.run_case([['HS Code','Description','Qty'],['0000','DEMO','2']]);self.assertNotEqual(status,0);self.assertEqual(out,'')
if __name__=='__main__':unittest.main()
