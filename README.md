# Supply-chain workflow examples

Small Python and AutoHotkey examples for invoice preparation, carrier-link navigation,
Outlook drafting and simulated logistics analysis. These are scripts, not a deployed platform.
No measured efficiency, accuracy or production-usage claim is made.

## Workflow and evidence

| Module | Input → output | Limits |
|---|---|---|
| `candata_import/import_tool.py` | XLSX → detected header / normalized HS columns → CSV | Requires identifiable HS Code, description, quantity and total columns. Duplicate HS output columns preserve the existing format. Validate with the destination system before use. |
| `workflow-automation/tracking_tool.py` | Colab `/content/` tracking sheet → carrier URLs | Assumes specific input column positions; carrier links may change. |
| `workflow-automation/outlook_email_automation.ahk` | Windows hotkeys → Outlook drafting/navigation | Requires Windows/Outlook and a compatible AutoHotkey version; not verified on every environment. |
| `logistics-compliance-analytics/data_generator.py` | Seeded simulated records → CSV | Simulation, not observed shipment performance or predictive validation. |

Python/Pandas handle spreadsheet operations; NumPy generates synthetic data. The Power BI
screenshot is an illustration: no editable PBIX/DAX model is included.

## Reproduce the invoice example

```bash
python -m pip install -r requirements.txt
python examples/create_synthetic_invoice.py
python candata_import/import_tool.py examples/synthetic_invoice.xlsx --output examples/synthetic_output.csv
python -m unittest discover -s tests -v
```

The fixture uses fictional labels and dummy codes, not customs advice or real transactions.
Missing input/required fields fail instead of producing a successful-looking result;
missing HS headers raise an explicit error. Review outputs before operational import.

## Publication scope

An operational-looking hard-coded input identifier was replaced with a supplied path.
Its status was uncertain; no original identifier or source invoice is needed in this example.
The old identifier remains in earlier Git commits pending a separate publication review.
Do not commit private input workbooks or generated operational reports. No history rewrite
or repository visibility change has been performed.
