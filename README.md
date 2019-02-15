# jpxtime3

JPX指数先物オプションの取引日や取引時間, 満期日などを管理

## Installation

```bash
pip install jpxtime3
```

## Examples

```python
from datetime import datetime
import jpxtime3

# 取引時間中の場合は1が返る
jpxtime3.is_open(datetime(2016, 1, 5, 10, 0))
```

```python
1
```

```python
# 取引時間外の場合は0が返る
jpxtime3.is_open(datetime(2016, 1, 5, 8, 0))
```

```python
0
```

```python
# 引数を指定しない場合はデフォルトで現在時刻が入る
jpxtime3.is_open()
```

```python
1
```

```python
# クロージングオークションの場合は2が返る
jpxtime3.is_open(datetime(2016, 1, 5, 15, 10))
```

```python
2
```

```python
# 年月をタプルで指定してSQ日を取得
jpxtime3.get_sq((2016, 1))
```

```python
datetime.date(2016, 1, 8)
```

```python
# 年月をintで指定してSQ日を取得
jpxtime3.get_sq((201601))
```

```python
datetime.date(2016, 1, 8)
```

```python
# 年月をstrで指定してSQ日を取得
jpxtime3.get_sq('201601')
```

```python
datetime.date(2016, 1, 8)
```

```python
# 2015/12/30 9:00から2016年1月限のSQ日までの期間を取得(年換算(365日))
jpxtime3.get_t(datetime(2015, 12, 30, 9), jpxtime3.get_sq((2016, 1)))
```

```python
0.024657534246575342
```

```python
# 2015/12/30 9:00から2016年1月限のSQ日までの期間を営業日で取得(年換算(245日))
jpxtime3.get_t(datetime(2015, 12, 30, 9), jpxtime3.get_sq((2016, 1)), 245)
```

```python
0.02040816326530612
```

```python
# 取引日を取得(ナイトセッションの場合は翌営業日)
jpxtime3.get_nominal_trading_day(datetime.datetime(2019, 1, 4, 17, 0))
```

```python
datetime.date(2019, 1, 7)
```

```python
# 翌取引日の寄付の日時を取得
jpxtime3.get_next_opening(datetime.datetime(2019, 1, 4, 9))
```

```python
datetime.datetime(2019, 1, 4, 16, 30)
```

```python
# 翌取引日の大引けの日時を取得
jpxtime3.get_next_closing(datetime.datetime(2019, 1, 7, 23))
```

```python
datetime.datetime(2019, 1, 9, 15, 15)
```

```python
# 前取引日の寄付の日時を取得
jpxtime3.get_prev_opening(datetime.datetime(2019, 1, 7, 10))
```

```python
datetime.datetime(2018, 12, 28, 16, 30)
```

```python
# 前取引日の大引けの日時を取得
jpxtime3.get_prev_closing(datetime.datetime(2019, 1, 4, 10))
```

```python
datetime.datetime(2018, 12, 28, 15, 15)
```

## Command

現在時刻のjpxtime3.is_openの戻り値が返る

```bash
python -m jpxtime3
echo $?
```