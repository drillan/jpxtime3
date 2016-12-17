# jpxtime
manage JPX(Nikkei 225 derivatives) trading hours and days

## Installation

```bash
pip install jpxtime3
```

## Examples
```python
from datetime import datetime
import jpxtime3 as jpxtime

# 取引時間中の場合は1が返る
jpxtime.is_open(datetime(2016, 1, 5, 10, 0))
```
```
1
```
```python
# 取引時間外の場合は0が返る
jpxtime.is_open(datetime(2016, 1, 5, 8, 0))
```
```
0
```
```python
# 引数を指定しない場合はデフォルトで現在時刻が入る
jpxtime.is_open()
```
```
1
```
```python
# クロージングオークションの場合は2が返る
jpxtime.is_open(datetime(2016, 1, 5, 15, 10))
```
```
2
```
```python
# 年月をタプルで指定してSQ日を取得
jpxtime.get_sq((2016, 1))
```
```
datetime.date(2016, 1, 8)
```
```python
# 年月をintで指定してSQ日を取得
jpxtime.get_sq((201601))
```
```
datetime.date(2016, 1, 8)
```
```python
# 年月をstrで指定してSQ日を取得
jpxtime.get_sq('201601')
```
```
datetime.date(2016, 1, 8)
```
```python
# 2015/12/30 9:00から2016年1月限のSQ日までの期間を取得(年換算(365日))
jpxtime.get_t(datetime(2015, 12, 30, 9), jpxtime.get_sq((2016, 1)))
```
```
0.024657534246575342
```
```python
# 2015/12/30 9:00から2016年1月限のSQ日までの期間を営業日で取得(年換算(245日))
jpxtime.get_t(datetime(2015, 12, 30, 9), jpxtime.get_sq((2016, 1)), 245)
```
```
0.02040816326530612
```

## Command
現在時刻のjpxtime3.is_openの戻り値が返る
```bash
python -m jpxtime3
echo $?
```