import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. 设定基础参数
num_records = 5000
np.random.seed(42)  # 保证每次生成的数据一样

# 2. 定义数据字典 (结合你的真实业务知识)
origins = ['Shanghai, CN', 'Shenzhen, CN', 'Yokohama, JP', 'Busan, KR']
destinations = ['Vancouver, BC']
carriers = ['COSCO', 'Maersk', 'Evergreen', 'ONE', 'Hapag-Lloyd']
shipping_modes = ['Ocean - FCL', 'Ocean - LCL']
hs_codes = ['6109.10', '8517.12', '9403.50', '3926.90'] # 真实的HS Code (衣服, 手机, 家具, 塑料)
customs_statuses = ['Released', 'Pending IID', 'CBSA Hold', 'CFIA Hold']
customs_status_probs = [0.85, 0.08, 0.05, 0.02] # 设定合理的概率分布

# 3. 生成基础订单数据
data = {
    'Container_ID': [f"CONT{str(i).zfill(6)}" for i in range(1, num_records + 1)],
    'Origin': np.random.choice(origins, num_records),
    'Destination': np.random.choice(destinations, num_records),
    'Carrier': np.random.choice(carriers, num_records),
    'Shipping_Mode': np.random.choice(shipping_modes, num_records, p=[0.7, 0.3]),
    'HS_Code': np.random.choice(hs_codes, num_records),
    'Customs_Status': np.random.choice(customs_statuses, num_records, p=customs_status_probs)
}

df = pd.DataFrame(data)

# 4. 生成时间逻辑 (这是展现你业务理解的核心)
# 设定计划出港时间
df['Scheduled_Departure'] = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_records)]

# 模拟实际出港时间 (加入轻微延误)
delay_days = np.random.exponential(scale=1.5, size=num_records).astype(int) # 多数情况不延误，少数延误几天
df['Actual_Departure'] = df['Scheduled_Departure'] + pd.to_timedelta(delay_days, unit='d')

# 模拟海上航行时间 (不同港口时间不同，这里简单用均值处理)
ocean_transit_days = np.random.normal(loc=20, scale=3, size=num_records).astype(int)
df['Actual_Arrival_Port'] = df['Actual_Departure'] + pd.to_timedelta(ocean_transit_days, unit='d')

# 模拟清关时间 (核心痛点！)
# 正常 Released 可能只要 1 天，但 CBSA Hold 可能要 7-14 天
def calculate_customs_delay(status):
    if status == 'Released':
        return np.random.randint(1, 3)
    elif status == 'Pending IID':
        return np.random.randint(3, 7)
    elif status in ['CBSA Hold', 'CFIA Hold']:
        return np.random.randint(7, 21)
    return 1

df['Customs_Clearance_Days'] = df['Customs_Status'].apply(calculate_customs_delay)
df['Customs_Release_Date'] = df['Actual_Arrival_Port'] + pd.to_timedelta(df['Customs_Clearance_Days'], unit='d')

# 5. 计算 KPI (延误率等)
# 假设标准交货期是 25 天
df['Scheduled_Arrival_Warehouse'] = df['Scheduled_Departure'] + pd.to_timedelta(25, unit='d')
# 假设从港口提货到仓库需要 2 天
df['Actual_Arrival_Warehouse'] = df['Customs_Release_Date'] + pd.to_timedelta(2, unit='d')

df['Total_Transit_Days'] = (df['Actual_Arrival_Warehouse'] - df['Scheduled_Departure']).dt.days
df['Is_Late'] = df['Actual_Arrival_Warehouse'] > df['Scheduled_Arrival_Warehouse']

# 6. 保存数据
df.to_csv("Simulated_Vancouver_Logistics_Data.csv", index=False)
print("数据生成完毕！")
