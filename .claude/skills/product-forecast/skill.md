---
name: product-forecast
description: 세일즈 예측 vs 실적 자동 비교 (Product Forecast). 사용자가 직접 정리한 A&F 완성 파일 1개를 입력받아 ±20% 기준으로 자동 적용/검토 분류. Summary 시트에 월별 판정 컬럼을 추가한 결과 파일 + 4월·5월 통합 단일 리포트 자동 생성. "product forecast", "PF 실행", "비교 파일 만들어줘", "판매 비교", "A&F 만들어줘", "실적 비교", "af compare" 등을 언급하면 자동 실행.
allowed-tools:
  - Bash
  - Read
---

# Product Forecast 스킬

사용자가 직접 정리한 **A&F 파일 1개**로 예측 vs 실적 비교 + 통합 리포트 자동 생성.

## 워크플로우

```
A&F 완성 파일 (Excel)
       ↓
  af_compare.py       ← Summary 시트 읽기 → 월별 판정 분류
       ↓
  _result.xlsx        ← 원본 A&F 복사본 + Summary에 판정 컬럼 추가 (색상 포함)
  _report.html/.pdf   ← 4월·5월 통합 단일 리포트
```

## A&F 파일 구조 (필수)

| 시트 | 내용 | 주요 컬럼 |
|------|------|----------|
| `Summary` | 월별 확정 실적 + FC | PLU, 제품군, 제품명, `N월`, `N월 (FC)` … |
| `YY.MM` 또는 `YY.MM.DD` | 월별 실적 (예: `26.04`, `25.05.17`) | 행 레이블(PLU), 섹션명 |

> **Summary 시트** = 실적/FC의 출처 (사용자가 직접 확정한 값)
> **월별 시트** = 섹션명 매핑에만 사용
> 월 데이터는 Summary에서 자동 감지 (`N월` / `N월 (FC)` 컬럼 쌍)

## 실행 방법

```bash
# 기본 실행 (±20%)
python3 20-operations/product-forecast/af_compare.py '<A&F 파일.xlsx>'

# 임계값 변경
python3 20-operations/product-forecast/af_compare.py '<A&F 파일.xlsx>' --threshold 0.25
```

## 처리 내용

1. Summary 시트에서 월 데이터 자동 감지 (`N월` / `N월 (FC)` 컬럼 쌍)
2. 월별 실적 시트에서 PLU → 섹션명 매핑 추출
3. K-PLU 자동 제외
4. 오차 계산 → **±20% 기준** 분류 (자동 적용 / 검토 필요)
5. 원본 파일 복사 → Summary 시트에 `N월 판정` 컬럼 추가 + 색상
6. 4월·5월 통합 단일 HTML/PDF 리포트 생성

## 출력 파일

| 파일 | 내용 |
|------|------|
| `*_result.xlsx` | A&F 원본 복사본 + Summary에 월별 판정 컬럼 (초록=자동/노랑=검토) |
| `*_{N}월_report.html` | 월별 개별 리포트 (4월, 5월 각각 별도 파일) |
| `*_{N}월_report.pdf` | PDF (weasyprint 또는 wkhtmltopdf 필요, 없으면 Cmd+P) |

> 리포트는 반드시 월별 개별 파일로 분리 출력. 통합 단일 파일 금지.

## 판정 기준

| 판정 | 기준 |
|------|------|
| **자동 적용** | 오차 ±20% 이내 |
| **검토 필요** | 오차 ±20% 초과 |

## K-PLU 제외

K로 시작하는 PLU (국내 제조 품목)는 자동 제외.

## Step 5: 주문 파일 분기 합계 자동 조정

### 실행
```bash
python3 20-operations/product-forecast/step5_order_update.py '<Order 파일.xlsx>'
```

### 대상 파일 구조
| 컬럼 | 내용 |
|------|------|
| BX | 4월 실제판매량 |
| BZ | 5월 실제판매량 |
| CA | 검토 여부 |
| CB | **최종 검토** ("자동 적용" / 비워둠) |
| CC-CE | 4월·5월·6월 예측 (`=CH*$CC$8` 수식) |
| CH | 분기 합계 (`=BS{행}*계수` 수식) |
| Row 8 | CC·CD·CE 월별 가중치 |

### 처리 내용
1. CB = "자동 적용" 행 대상
2. 새 CH 계수 = BZ ÷ CD가중치(row8) ÷ BS값
3. CH 수식 `=BS{행}*{계수}` 의 계수만 교체 → CC/CD/CE 전부 비례 재계산
4. **결과**: CD = BZ (5월 예측 = 5월 실제판매량)

### 출력
- `{원본파일명}_step5.xlsx` — CH 수식 계수가 업데이트된 주문 파일

---

## 스크립트 위치

```
20-operations/product-forecast/
├── af_compare.py            ← A&F → result.xlsx + 월별 리포트
├── step5_order_update.py    ← 주문 파일 분기합계(CH) 자동 조정
├── step4_report.py          ← (레거시) 단일월 리포트 생성기
├── step1_raw_clean.py       ← (초기 데이터 정제용) Raw 판매량 집계
├── step2_bulk_deduct.py     ← (초기 데이터 정제용) 단체주문 차감
└── step3_fc_compare.py      ← (레거시) 구버전 비교 스크립트
```
