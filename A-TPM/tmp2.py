class YourApp:
    def __init__(self):
        # 初始化配置加载器
        # 假设 JsonFunction 已经定义
        self.Swan01Config = JsonFunction(file_path=".Swan01Config/Swan01Config.json")
        self.CraneConfig = JsonFunction(file_path=".Crane01Config/Crane01Config.json")

        # 【核心改动】: 初始化配置缓存字典
        # 用于存储不同 gui_type 的实时修改后的配置
        self.config_cache = {
            "Swan01": self.Swan01Config.items,  # 初始加载 Swan01 的配置
            "Crane01": self.CraneConfig.items  # 初始加载 Crane01 的配置
        }

        # 当前活跃的配置
        self.current_gui_type = None
        self.swan01_config = {}

        # 首次调用 setup_gui 进行初始化
        self.setup_gui("Swan01")

    def setup_gui(self, gui_type="Swan01", color="yellow"):
        # 假设这两个对象在 __init__ 中加载了数据
        # self.Swan01Config.items 是一个字典（可变对象）

        if gui_type == "Swan01":
            # 此时 self.swan01_config 指向 self.Swan01Config.items 的那个字典对象
            self.swan01_config = self.Swan01Config.items
        else:
            # 此时 self.swan01_config 指向 self.CraneConfig.items 的那个字典对象
            self.swan01_config = self.CraneConfig.items
        self.swan01_config["color"] = color



# 假设的 JsonFunction 类
class JsonFunction:
    def __init__(self, file_path):
        # 模拟从文件加载配置
        self.items = {"setting_A": f"initial_{file_path}", "color": "blue"}


if __name__ == '__main__':
    app = YourApp()
    app.setup_gui()
    app.setup_gui(gui_type="Swan01", color="red")
    app.setup_gui(gui_type="Crane01", color="green")
    print(app.Swan01Config.items)
    print(app.CraneConfig.items)