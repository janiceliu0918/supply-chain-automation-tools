import pandas as pd
import os

print("🔍 正在启动追踪导航雷达 (V3.0 定制版)...")

# 1. 自动扫描文件
all_files = os.listdir('/content/')
target_file = None
for file in all_files:
    if 'Daily_Tracking' in file:
        target_file = f'/content/{file}'
        break

if target_file:
    print(f"\n✅ 成功锁定文件：{target_file}")
    print("=" * 60)

    try:
        # 读取表格
        if target_file.endswith('.csv'):
            df = pd.read_csv(target_file)
        else:
            df = pd.read_excel(target_file)

        container_column = df.columns[1]
        carrier_column = df.columns[3]
        valid_count = 0

        # ==========================================
        # 🚢 你的专属船司字典 (已更新 OOCL & EVERGREEN)
        # ==========================================
        carrier_dict = {
            "ONE": "https://ecomm.one-line.com/ecom/CUP_HOM_3301.do?cntrNo=",
            "COSCO": "https://elines.coscoshipping.com/ebusiness/cargoTracking?cntrNo=",
            "MAERSK": "https://www.maersk.com/tracking/",
            "CMA CGM": "https://www.cma-cgm.com/ebusiness/tracking/search?reference=",
            "CMA": "https://www.cma-cgm.com/ebusiness/tracking/search?reference=",
            "SM LINE": "https://esvc.smlines.com/smline/CUP_HOM_3301.do?cntrNo=",
            "SML": "https://esvc.smlines.com/smline/CUP_HOM_3301.do?cntrNo=",
            "MSC": "https://www.msc.com/en/track-a-shipment?trackingNumber=",
            "ZIM": "https://www.zim.com/tools/track-a-shipment",
            "HAPAG-LLOYD": "https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container=",
            "HAPAG": "https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container=",

            # 👇 这里是你最新指定的 OOCL 和 长荣链接 (末尾加了?防止网页报错)
            "OOCL": "https://www.oocl.com/eng/ourservices/eservices/cargotracking/Pages/CargoTracking.aspx?",
            "EVERGREEN": "https://www.evergreen-logistics.com/GUEC/web-en/tracking.jsp?",
            "EMC": "https://www.evergreen-logistics.com/GUEC/web-en/tracking.jsp?"
        }

        # 👇 这里是你最新指定的兜底链接 Track-Trace
        default_url = "https://www.track-trace.com/container/trace?number="

        # 开始逐行处理
        for index, row in df.iterrows():
            container_num = str(row[container_column]).strip()
            carrier = str(row[carrier_column]).strip().upper()

            # 过滤无效柜号
            if container_num == 'nan' or len(container_num) < 10 or " " in container_num:
                continue

            valid_count += 1

            # 匹配链接
            if carrier in carrier_dict:
                tracking_url = f"{carrier_dict[carrier]}{container_num}"
                link_type = "🟢 [官网直达]"
            else:
                tracking_url = f"{default_url}{container_num}"
                link_type = "🟡 [Track-Trace]"

            print(f"{link_type} 船司: {carrier.ljust(12)} | 柜号: {container_num}")
            print(f"🔗 链接: {tracking_url}")
            print("-" * 60)

        print(f"\n🎉 运行完毕！共生成 {valid_count} 个追踪链接。")

    except Exception as e:
        print(f"❌ 读取文件时出错了：{e}")

else:
    print("\n❌ 扫描失败：请确保左侧文件夹里有包含 'Daily_Tracking' 的文件哦！")
