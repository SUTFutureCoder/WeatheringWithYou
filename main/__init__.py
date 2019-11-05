from spider import cyber_japan_data

class Main:

  def __init__(self):
    return

  def Run(self):
    # 爬取数据并转换
    obj_cyber = cyber_japan_data.CyberJapanData()
    # parsed_cyber_data = obj_cyber.get_data_by_tile(29086, 12887)
    parsed_cyber_data = obj_cyber.get_data_by_tile(29104, 12914)
    print(parsed_cyber_data)

    return
