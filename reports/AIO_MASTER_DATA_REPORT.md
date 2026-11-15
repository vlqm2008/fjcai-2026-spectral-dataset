# AIO (ALL-IN-ONE): TỔNG HỢP TOÀN DIỆN DỮ LIỆU BÀI BÁO KHOA HỌC FJCAI 2026 & CITA 2027

> **Bài báo gốc:** *"Spectral Consistency Regularization for Long-Horizon Probabilistic Forecasting with Temporal Fusion Transformers"*  
> **Tác giả:** Dinh-Phu Vo, Duc-Hien Nguyen, Phuoc-Tung Nguyen (FJCAI 2026)  
> **Phiên bản tài liệu:** All-In-One Data Master Guide (AIO v1.0)  
> **Tệp dữ liệu gốc tại Desktop:** [DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv](file:///C:/Users/Admin/Desktop/DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv)

---

## MỤC LỤC AIO
1. [Vị trí toàn bộ file dữ liệu trên máy tính](#1-vị-trí-toàn-bộ-file-dữ-liệu-trên-máy-tính)
2. [Từ điển dữ liệu chuẩn mực (Data Dictionary - 18 Cột)](#2-từ-điển-dữ-liệu-chuẩn-mực-data-dictionary---18-cột)
3. [Thống kê mô tả 6 tài sản tài chính (Descriptive Statistics)](#3-thống-kê-mô-tả-6-tài-sản-tài-chính-descriptive-statistics)
4. [Cơ chế chuẩn hóa phi rò rỉ & Phân chia tập dữ liệu (Leak-Free Protocol)](#4-cơ-chế-chuẩn-hóa-phi-rò-rỉ--phân-chia-tập-dữ-liệu-leak-free-protocol)
5. [Bản đồ ánh xạ: Từng cột Data đi vào khối nào của Model TFT](#5-bản-đồ-ánh-xạ-từng-cột-data-đi-vào-khối-nào-của-model-tft)
6. [Bảng kết quả thực nghiệm của Model trên Data (Table I, II, III)](#6-bảng-kết-quả-thực-nghiệm-của-model-trên-data-table-i-ii-iii)
7. [Cách nạp dữ liệu nhanh trong Python & Excel](#7-cách-nạp-dữ-liệu-nhanh-trong-python--excel)

---

## 1. VỊ TRÍ TOÀN BỘ FILE DỮ LIỆU TRÊN MÁY TÍNH

| Tên dữ liệu | Đường dẫn tệp trên máy tính | Quy mô | Mô tả |
|---|---|:---:|---|
| **Data gốc tiện dùng (Desktop)** | [DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv](file:///C:/Users/Admin/Desktop/DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv) | 19,033 dòng | Bản sao trực tiếp ngoài màn hình Desktop (mở được ngay bằng Excel) |
| **Data gốc Master (Ổ D)** | [fjcai_spectral_6assets_master.csv](file:///D:/01_AI_Research_Projects/cita2027-data-engine/data/fjcai_spectral_benchmark/fjcai_spectral_6assets_master.csv) | 19,033 dòng | Tệp gốc bảng dọc (Long-format) 18 cột theo đúng thiết kế bài báo |
| **Thư mục 6 tệp từng mã (Ổ D)** | [fjcai_spectral_benchmark/](file:///D:/01_AI_Research_Projects/cita2027-data-engine/data/fjcai_spectral_benchmark) | 6 tệp CSV | Tách riêng: `AAPL`, `MSFT`, `GOOG`, `AMZN`, `META`, `SP500` |
| **Data S&P 500 (SPY)** | [artifacts/processed/SPY_...csv](file:///C:/Users/Admin/Desktop/Cita2027Goc/cita2027-phase2/artifacts/processed/SPY_20261104T095117433396Z_b41a8489.csv) | 5,492 ngày | Chuỗi thời gian chứng khoán Mỹ giai đoạn dài 2005 - 2026 |
| **Data Bitcoin (BTCUSDT)** | [btcusdt_data/snapshots/...csv](file:///C:/Users/Admin/Desktop/Cita2027Goc/cita2027-phase2/artifacts/btcusdt_data/snapshots/05088f11c7929995ef6dd28e5135669ebaf37465928c62c826a15f245520299a.csv) | 2,694 ngày | Chuỗi nến 1 ngày tiền số Binance Spot liên tục 24/7 (2017 - 2024) |
| **Bảng số liệu kết quả Model** | [fjcai_all_6assets_comprehensive_metrics.csv](file:///C:/Users/Admin/Desktop/FJCAI_2026_RESULTS/fjcai_all_6assets_comprehensive_metrics.csv) | 54 dòng | Kết quả đối chuẩn chi tiết qua 6 mã, 3 mốc cắt, 3 horizon |

---

## 2. TỪ ĐIỂN DỮ LIỆU CHUẨN MỰC (DATA DICTIONARY - 18 CỘT)

Toàn bộ 19,033 dòng dữ liệu trong tệp gốc không chứa bất kỳ ô trống nào (`Null = 0`). Ý nghĩa từng cột:

| STT | Tên cột (Column Name) | Kiểu dữ liệu | Miền giá trị (Min → Max) | Công thức / Định nghĩa toán học |
|:---:|---|:---:|:---:|---|
| 1 | **`date`** | String | 2010-01-04 → 2022-12-30 | Ngày giao dịch thị trường (`YYYY-MM-DD`). |
| 2 | **`ticker`** | String | `AAPL` → `^GSPC` | Ký hiệu mã chứng khoán (`AAPL`, `MSFT`, `GOOG`, `AMZN`, `META`, `^GSPC`). |
| 3 | **`asset`** | String | `AAPL` → `SP500` | Tên gọi chuẩn hóa của tài sản. |
| 4 | **`adj_close`** | Float64 | 5.43 → 4,796.56 | Giá đóng cửa đã điều chỉnh sau cổ tức và chia tách cổ phiếu (USD). |
| 5 | **`volume`** | Float64 | 1.58e5 → 1.06e10 | Khối lượng cổ phiếu khớp lệnh trong phiên giao dịch. |
| 6 | **`log_return`** | Float64 | -0.3064 → +0.2594 | Lợi suất log hàng ngày: $r_t = \ln(P_t / P_{t-1})$. Biến mục tiêu gốc. |
| 7 | **`sin_dow`** | Float64 | -0.9511 → +0.9511 | Mã hóa lượng giác thứ trong tuần: $\sin(2\pi \cdot \text{day} / 5)$. |
| 8 | **`cos_dow`** | Float64 | -0.8090 → +1.0000 | Mã hóa lượng giác thứ trong tuần: $\cos(2\pi \cdot \text{day} / 5)$. |
| 9 | **`sin_month`** | Float64 | -1.0000 → +1.0000 | Mã hóa lượng giác tháng trong năm: $\sin(2\pi \cdot \text{month} / 12)$. |
| 10 | **`cos_month`** | Float64 | -1.0000 → +1.0000 | Mã hóa lượng giác tháng trong năm: $\cos(2\pi \cdot \text{month} / 12)$. |
| 11 | **`rolling_mean_20d`** | Float64 | -0.0699 → +0.0231 | Trung bình trượt lợi suất cửa sổ 20 ngày giao dịch (1 tháng). |
| 12 | **`rolling_vol_20d`** | Float64 | 0.0000 → 0.0823 | Độ biến động trượt (Độ lệch chuẩn) cửa sổ 20 ngày. |
| 13 | **`rolling_mean_60d`** | Float64 | -0.0699 → +0.0123 | Trung bình trượt lợi suất cửa sổ 60 ngày giao dịch (1 quý). |
| 14 | **`rolling_vol_60d`** | Float64 | 0.0000 → 0.0823 | Độ biến động trượt (Độ lệch chuẩn) cửa sổ 60 ngày. |
| 15 | **`momentum_20d`** | Float64 | -0.3716 → +0.5860 | Tỷ lệ biến động giá 20 ngày: $(P_t - P_{t-20}) / P_{t-20}$. |
| 16 | **`momentum_60d`** | Float64 | -0.5015 → +1.0897 | Tỷ lệ biến động giá 60 ngày: $(P_t - P_{t-60}) / P_{t-60}$. |
| 17 | **`split_2021`** | String | `train_val`, `test_ood` | Nhãn phân chia mốc 2021-06-30 ($\le$: huấn luyện, $>$: kiểm định OOD). |
| 18 | **`z_return_2021`** | Float64 | -13.258 → +11.147 | Lợi suất đã chuẩn hóa $z$-score chỉ dùng tham số in-sample: $z = (r - \mu)/\sigma$. |

---

## 3. THỐNG KÊ MÔ TẢ 6 TÀI SẢN TÀI CHÍNH (DESCRIPTIVE STATISTICS)

| Ký hiệu | Tên tài sản | Số mẫu | Ngày bắt đầu | Ngày kết thúc | Train ($t \le 2021-06-30$) | Test ($t > 2021-06-30$) | Kỳ vọng $\mu$ | Độ lệch chuẩn $\sigma$ |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`AAPL`** | Apple Inc. | 3,272 | 2010-01-04 | 2022-12-30 | 2,893 | 379 | +0.001050 | 0.017825 |
| **`MSFT`** | Microsoft Corp. | 3,272 | 2010-01-04 | 2022-12-30 | 2,893 | 379 | +0.000838 | 0.015914 |
| **`GOOG`** | Alphabet Inc. | 3,272 | 2010-01-04 | 2022-12-30 | 2,893 | 379 | +0.000720 | 0.016332 |
| **`AMZN`** | Amazon.com Inc. | 3,272 | 2010-01-04 | 2022-12-30 | 2,893 | 379 | +0.001122 | 0.019731 |
| **`META`** | Meta Platforms | 2,673 | 2012-05-18 | 2022-12-30 | 2,294 | 379 | +0.000962 | 0.023182 |
| **`^GSPC`** | S&P 500 Index | 3,272 | 2010-01-04 | 2022-12-30 | 2,893 | 379 | +0.000461 | 0.010965 |
| **TỔNG** | **6 Tài sản gộp** | **19,033** | — | — | **16,759** | **2,274** | — | — |

---

## 4. CƠ CHẾ CHUẨN HÓA PHI RÒ RỈ & PHÂN CHIA TẬP DỮ LIỆU (LEAK-FREE PROTOCOL)

1. **Chuẩn hóa không rò rỉ tương lai (No-Lookahead Leakage):**  
   Với mỗi mốc cắt thời gian $t_{cut}$, tham số trung bình $\mu_i$ và độ lệch chuẩn $\sigma_i$ của tài sản $i$ **chỉ được tính trên tập dữ liệu lịch sử trước mốc cắt** ($\tau \le t_{cut}$):
   $$z_\tau^{(i)} = \frac{r_\tau^{(i)} - \mu_i}{\sigma_i}$$
   Mọi chỉ số đánh giá (MAE, RMSE, sMAPE) và hàm mất mát trong quá trình tối ưu hóa đều được tính trên thang đo chuẩn hóa $z$.
2. **3 Mốc cắt huấn luyện (Training Cutoffs):**
   - `2017-12-31`: Thị trường tăng trưởng ổn định, biến động thấp.
   - `2019-12-31`: Giai đoạn tiền khủng hoảng COVID-19.
   - `2021-06-30`: **Mốc cắt trọng tâm của bài báo**, là chế độ biến động khắc nghiệt nhất với các cú sốc và đảo chiều xu hướng vĩ mô.
3. **3 Chân trời dự báo đa bước (Forecasting Horizons):**
   - $H = 60$ ngày (~3 tháng giao dịch - Ngắn/Trung hạn).
   - $H = 120$ ngày (~6 tháng giao dịch - Trung hạn, trọng tâm kiểm thử).
   - $H = 250$ ngày (~1 năm giao dịch tài chính - Dài hạn).

---

## 5. BẢN ĐỒ ÁNH XẠ: TỪNG CỘT DATA ĐI VÀO KHỐI NÀO CỦA MODEL TFT

```
[DỮ LIỆU ĐẦU VÀO TRONG CSV] ───────────────> [KHỐI KIẾN TRÚC MÔ HÌNH TFT] ───────────────> [ĐIỀU CHUẨN SPECTRAL]
1. ticker                              ──> Entity Embeddings (Định danh từng mã cổ phiếu)
2. sin/cos dow, month (Biến lịch)      ──> Temporal Decoder (Mã hóa tính chu kỳ tuần/tháng)
3. volume, rolling_vol, momentum       ──> Variable Selection Networks (Tự động lọc biến quan trọng)
4. log_return / z_return               ──> Quantile Heads (Dự báo 3 đường phân vị: q10, q50, q90)
                                                    │
                                                    ▼
                                           [Đường phân vị trung vị q50]
                                                    │
                                                    ▼
                                           cumsum(q50) ──> rFFT ──> Khớp dải tần số thấp K (L_spec)
```

- **Khối Variable Selection Networks (VSN):** Nhận các cột `volume`, `rolling_vol_20d/60d`, `momentum_20d/60d`. Khi thị trường biến động (như đợt sập COVID 2020), VSN tự động gán trọng số cao cho cột `rolling_vol` và giảm trọng số các cột nhiễu.
- **Khối Temporal Self-Attention:** Học mối quan hệ phụ thuộc xa giữa các bước thời gian trong quá khứ và tương lai trên chân trời $H=60, 120, 250$.
- **Hàm mất mát phổ Spectral Loss ($\mathcal{L}_{spec}$):** Lấy đường đi tích lũy của phân vị trung vị $\hat{s}_t = \text{cumsum}(\hat{z}_t(0.5))$ biến đổi qua Fourier rFFT để khớp năng lượng tần số thấp ($K = \lfloor 0.25 N_f \rfloor$) với dữ liệu thực tế. Nhờ đó, model bị "khóa" không thể bay bổng lệch khỏi xu hướng dài hạn của Data.

---

## 6. BẢNG KẾT QUẢ THỰC NGHIỆM CỦA MODEL TRÊN DATA (TABLE I, II, III)

### Bảng I: Hiệu năng toàn cầu tại mốc 2021-06-30 và $H = 120$ ngày

| Mô hình (Model) | MAE | RMSE | sMAPE | Coverage (10-90%) | Winkler Score | Spectral Loss ($\mathcal{L}_{spec}$) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **TFT Baseline (Mô hình gốc)** | 1.007 | 1.320 | 1.294 | 0.556 (55.6%) | 5.496 | 41.1865 |
| **SpectralTFT (Đề xuất của bài báo)**| **0.663** | **0.896** | **1.062** | **0.870 (87.0%)** | **3.230** | **1.6691** |
| **Mức độ cải thiện** | **-34.1%** | **-32.1%** | **-17.9%** | **+31.4% (về sát chuẩn 80%)** | **-41.2%** | **-95.9%** |

### Bảng II: Mức giảm sai số MAE của SpectralTFT qua 3 mốc cắt ($H = 120$)

| Mốc huấn luyện (Training Cutoff) | Tính chất giai đoạn thị trường | TFT Baseline MAE | SpectralTFT MAE | Mức giảm lỗi MAE (%) |
|---|---|:---:|:---:|:---:|
| **2017-12-31** | Thị trường tăng trưởng ổn định (Low Volatility) | 0.943 | **0.598** | **-36.6%** |
| **2019-12-31** | Giai đoạn tiền khủng hoảng COVID | 0.998 | **0.641** | **-35.8%** |
| **2021-06-30** | Hậu đại dịch, biến động cực đoan & đảo chiều xu hướng | 1.007 | **0.663** | **-34.1%** |

---

## 7. CÁCH NẠP DỮ LIỆU NHANH TRONG PYTHON & EXCEL

### Trong Python:
```python
import pandas as pd

# Nạp trực tiếp tệp master ngoài Desktop
df = pd.read_csv(r"C:\Users\Admin\Desktop\DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv")

print(f"Tổng số dòng: {len(df)}")  # 19,033 dòng
print(f"Các mã cổ phiếu: {df['ticker'].unique()}")  # ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', '^GSPC']
```

### Trong Excel:
Chỉ cần ra màn hình máy tính của bạn và **nhấp đúp chuột vào tệp `DATA_GOC_BAI_BAO_FJCAI_6ASSETS.csv`** là Excel sẽ tự động mở bảng dữ liệu lên với đầy đủ 18 cột để bạn tra cứu.
