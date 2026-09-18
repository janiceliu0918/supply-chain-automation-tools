import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Normalize a supplied invoice workbook to CSV.")
parser.add_argument("input", type=Path, help="Path to an XLSX workbook; use synthetic data for public examples")
parser.add_argument("--output", type=Path, default=Path("ready_for_candata.csv"))
args = parser.parse_args()

# ==========================================
# 🔧 核心预处理区
# ==========================================
# 1. 读取原始文件（如果是 Excel，请保持 read_excel。如果是你刚上传的 csv，请换成 read_csv）
df = pd.read_excel(args.input, header=None, dtype=str)

# 2. 动态定位表头（终极防弹逻辑：无视空格、大小写和标点）
is_header = df.apply(lambda row: row.astype(str).str.upper().str.replace(' ', '', regex=False).str.replace('.', '', regex=False).str.contains('HSCODE', regex=False).any(), axis=1)

if not is_header.any():
    raise ValueError("No HS Code header found in input workbook")
else:
    header_idx = df[is_header].index[0]
    df.columns = df.iloc[header_idx]
    df = df.iloc[header_idx + 1:].reset_index(drop=True)

    # 清理表头换行符
    df.columns = df.columns.astype(str).str.strip().str.replace('\n', '', regex=False)

    # 3. 解决重名列问题（比如有两个 DESCRIPTION，自动变成 DESCRIPTION 和 DESCRIPTION_1）
    def deduplicate_columns(columns):
        counts = {}
        new_columns = []
        for col in columns:
            if col not in counts:
                counts[col] = 0
                new_columns.append(col)
            else:
                counts[col] += 1
                new_columns.append(f"{col}_{counts[col]}")
        return new_columns
    df.columns = deduplicate_columns(df.columns)

# ==========================================
# 🧠 智能抓取区（无视客户怎么改表头）
# ==========================================
try:
    # 智能找 HS Code
    hs_col = [col for col in df.columns if 'HS' in str(col).upper() and 'CODE' in str(col).upper()][0]

    # 智能找 Total (金额)
    total_col = [col for col in df.columns if 'TOTAL' in str(col).upper()][0]

    # 智能找 Qty (不管它叫 QTY 还是 Qty(pcs) 还是 Quantity)
    qty_col = [col for col in df.columns if 'QTY' in str(col).upper() or 'PCS' in str(col).upper() or 'QUANTITY' in str(col).upper()][0]

    # 智能找英文品名 (找带有 DESC, COMMODITY, ITEM 的列。如果有多个，通常靠右的是英文)
    desc_cols = [col for col in df.columns if 'DESC' in str(col).upper() or 'COMMODITY' in str(col).upper() or 'ITEM' in str(col).upper()]
    eng_desc_col = desc_cols[-1] if desc_cols else "English Commodity" # 取最后一个匹配的

    print(f"🔍 成功识别列：HS->[{hs_col}], 品名->[{eng_desc_col}], 数量->[{qty_col}], 总价->[{total_col}]")

    # 提取我们需要的四列，并统一命名成内部标准格式
    clean_df = df[[hs_col, eng_desc_col, qty_col, total_col]].copy()
    clean_df.columns = ["HsCode", "English Commodity", "Qty(pcs)", total_col]

except IndexError as e:
    print(f"🚨 找不到关键列！请检查原表。现在的表头是: {df.columns.tolist()}")
    raise e

# ==========================================
# 🧹 数据清洗 & 终极排版区
# ==========================================
# 清除垃圾行（Subtotal / Total / 空白行等）
clean_df = clean_df.dropna(subset=["HsCode"])
clean_df = clean_df[~clean_df["HsCode"].astype(str).str.contains("Subtotal|Total|Shipping|Insurance|Cushions/Mats", case=False, na=False)]

# 👇 就是替换下面这一行！用这行全新的代码覆盖掉原来的 👇
# 清洗海关编码（去回车、去空格、去所有的小数点）
clean_df["HsCode"] = clean_df["HsCode"].astype(str).str.replace("\n", "", regex=False).str.replace(" ", "", regex=False).str.replace(".", "", regex=False)

# 暴力排版：直接在第 2 列的位置插入克隆的 HsCode，并且强制改名
clean_df.insert(1, "HsCode_Copy", clean_df["HsCode"])
clean_df.columns = ["HsCode", "HsCode", "English Commodity", "Qty(pcs)", total_col]

# 导出下载
output_filename = args.output
clean_df.to_csv(output_filename, index=False)
print(f"Wrote {output_filename}")

print("CSV written with duplicate HS columns; validate against destination requirements before operational use.")
