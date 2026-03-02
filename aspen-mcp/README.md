# Aspen Plus MCP Server

透過 MCP 協議操控 Aspen Plus 的模擬伺服器。

---

## 0. 總則 — 從零開始建模流程

1. 開啟 Aspen Plus 並載入 `.bkp` 檔案
2. 添加 Component（例如 WATER、ETHANOL、METHANOL）
3. 設定物性方法（例如 NRTL、PENG-ROB、UNIQUAC、IDEAL）
4. 放置 Block 與 Stream
5. 連接 Stream 到 Block 的 Port
6. 設定 Block 與 Stream 參數
7. 執行模擬
8. 讀取結果

> **提示：** 當找不到正確的參數名稱、port 名稱或 block 類型時，請使用 `search_properties` 工具以關鍵字搜尋。它會搜尋所有 YAML 定義檔中的 properties、ports 等資訊，回傳匹配的結果與說明。
>
> 範例：`search_properties("radfrac distillate")` → 會列出 RadFrac 相關的 distillate port 和 property。

---

## 1. Block 的使用方式

### RadFrac（蒸餾塔）

Ports：

| Port | 說明 |
|------|------|
| F(IN) | 進料口 |
| LD(OUT) | 液相蒸餾物出口（塔頂） |
| VD(OUT) | 氣相蒸餾物出口（塔頂） |
| B(OUT) | 塔底出口 |

參數：

| 參數名稱 | 型別 | 說明 |
|----------|------|------|
| number_of_stages | integer | 理論板數 |
| condenser_type | string | 冷凝器類型（TOTAL、PARTIAL-V、PARTIAL-V-L、NONE） |
| reboiler_type | string | 再沸器類型（KETTLE、THERMOSIPHON、NONE） |
| reflux_ratio | float | 回流比 |
| distillate_rate | float | 蒸餾物與進料比（D:F） |
| feed_stage | integer | 進料板位置（需指定 stream_name） |
| condenser_pressure | float | 冷凝器壓力（第 1 板壓力） |

### Heater（加熱器 / 冷卻器）

| 參數名稱 | 型別 | 說明 |
|----------|------|------|
| temperature | float | 出口溫度 |
| pressure | float | 出口壓力 |
| duty | float | 熱負荷 |
| vapor_fraction | float | 出口氣相分率 |

### Pump（泵）

| 參數名稱 | 型別 | 說明 |
|----------|------|------|
| discharge_pressure | float | 出口壓力 |
| pressure_increase | float | 增壓量 |
| efficiency | float | 泵效率 |

---

## 2. Stream 的使用方式

### MATERIAL（物質流）

輸入參數：

| 參數名稱 | 型別 | 說明 |
|----------|------|------|
| temperature | float | 溫度 |
| pressure | float | 壓力 |
| total_flow | float | 總流量 |
| vapor_fraction | float | 氣相分率 |
| component_flow | float | 各組分流量（需指定 component） |

輸出參數（模擬後讀取）：

| 參數名稱 | 型別 | 說明 |
|----------|------|------|
| output_temperature | float | 輸出溫度 |
| output_component_flow | float | 輸出各組分莫耳流量（需指定 component） |
| output_total_flow | float | 輸出總流量 |
