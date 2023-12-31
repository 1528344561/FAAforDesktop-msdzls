import json
import sys

from PyQt5.QtWidgets import QApplication

from function.script.scattered.get_battle_plan_list import get_battle_plan_list
from function.script.ui.ui_0_load_ui_file import MyMainWindow0


class MyMainWindow1(MyMainWindow0):
    """将读取配置的方法封装在此处"""

    def __init__(self):
        # 继承父类构造方法
        super().__init__()

        # opt路径
        self.opt_path = self.path_root + "\\config\\opt_main.json"

        # 从json文件中读取opt 并刷新ui
        self.opt = self.json_to_opt()
        self.opt_to_ui()

    def json_to_opt(self):
        with open(self.opt_path) as json_file:
            opt = json.load(json_file)
        return opt

    def opt_to_json(self):
        # dict → str 转换True和true
        json_str = json.dumps(self.opt, indent=4)
        # 写入
        with open(self.opt_path, 'w') as json_file:
            json_file.write(json_str)
        return None

    def opt_to_ui(self):
        # comboBox.setCurrentIndex时 如果超过了已有预设 会显示为空 不会报错
        # comboBox.clear时 会把所有选项设定为默认选项
        battle_plan_list = get_battle_plan_list(with_extension=False)

        self.GameName_Input.setText(self.opt["game_name"])
        self.Name1P_Input.setText(self.opt["name_1p"])
        self.Name2P_Input.setText(self.opt["name_2p"])
        self.ZoomRatio_Input.setCurrentIndex(self.opt["zoom_ratio"])

        self.Level1P_Input.setValue(self.opt["level_1p"])
        self.Level2P_Input.setValue(self.opt["level_2p"])
        self.AutoUseCard.setChecked(self.opt["auto_use_card"])

        self.ReloadAndDailyQuest_Active.setChecked(self.opt["reload_and_daily_quest"]["active"])
        self.FedAndWatered_Active.setChecked(self.opt["fed_and_watered"]["active"])

        self.QuestGuild_Active.setChecked(self.opt["quest_guild"]["active"])
        self.QuestGuild_Stage.setChecked(self.opt["quest_guild"]["stage"])
        self.QuestGuild_Deck.setValue(self.opt["quest_guild"]["deck"])
        self.QuestGuild_1P.addItems(battle_plan_list)
        self.QuestGuild_2P.addItems(battle_plan_list)
        self.QuestGuild_1P.setCurrentIndex(self.opt["quest_guild"]["battle_plan_1p"])
        self.QuestGuild_2P.setCurrentIndex(self.opt["quest_guild"]["battle_plan_2p"])

        self.QuestSpouse_Active.setChecked(self.opt["quest_spouse"]["active"])
        self.QuestSpouse_Deck.setValue(self.opt["quest_spouse"]["deck"])
        self.QuestSpouse_1P.addItems(battle_plan_list)
        self.QuestSpouse_2P.addItems(battle_plan_list)
        self.QuestSpouse_1P.setCurrentIndex(self.opt["quest_spouse"]["battle_plan_1p"])
        self.QuestSpouse_2P.setCurrentIndex(self.opt["quest_spouse"]["battle_plan_2p"])

        self.OfferReward_Active.setChecked(self.opt["offer_reward"]["active"])
        self.OfferReward_Deck.setValue(self.opt["offer_reward"]["deck"])
        self.OfferReward_1P.addItems(battle_plan_list)
        self.OfferReward_2P.addItems(battle_plan_list)
        self.OfferReward_1P.setCurrentIndex(self.opt["offer_reward"]["battle_plan_1p"])
        self.OfferReward_2P.setCurrentIndex(self.opt["offer_reward"]["battle_plan_2p"])

        self.MagicTowerDouble_Active.setChecked(self.opt["magic_tower_double"]["active"])
        self.MagicTowerDouble_MaxTimes.setValue(self.opt["magic_tower_double"]["max_times"])
        self.MagicTowerDouble_Stage.setValue(self.opt["magic_tower_double"]["stage"])
        self.MagicTowerDouble_Deck.setValue(self.opt["magic_tower_double"]["deck"])
        self.MagicTowerDouble_1P.addItems(battle_plan_list)
        self.MagicTowerDouble_1P.setCurrentIndex(self.opt["magic_tower_double"]["battle_plan_1p"])
        self.MagicTowerDouble_2P.addItems(battle_plan_list)
        self.MagicTowerDouble_2P.setCurrentIndex(self.opt["magic_tower_double"]["battle_plan_2p"])

        self.MagicTowerAlone1_Active.setChecked(self.opt["magic_tower_alone_1"]["active"])
        self.MagicTowerAlone1_MaxTimes.setValue(self.opt["magic_tower_alone_1"]["max_times"])
        self.MagicTowerAlone1_Stage.setValue(self.opt["magic_tower_alone_1"]["stage"])
        self.MagicTowerAlone1_Deck.setValue(self.opt["magic_tower_alone_1"]["deck"])
        self.MagicTowerAlone1_1P.addItems(battle_plan_list)
        self.MagicTowerAlone1_1P.setCurrentIndex(self.opt["magic_tower_alone_1"]["battle_plan_1p"])

        self.MagicTowerAlone2_Active.setChecked(self.opt["magic_tower_alone_2"]["active"])
        self.MagicTowerAlone2_MaxTimes.setValue(self.opt["magic_tower_alone_2"]["max_times"])
        self.MagicTowerAlone2_Stage.setValue(self.opt["magic_tower_alone_2"]["stage"])
        self.MagicTowerAlone2_Deck.setValue(self.opt["magic_tower_alone_2"]["deck"])
        self.MagicTowerAlone2_1P.addItems(battle_plan_list)
        self.MagicTowerAlone2_1P.setCurrentIndex(self.opt["magic_tower_alone_2"]["battle_plan_1p"])
        
        self.MagicTowerPrison1_Active.setChecked(self.opt["magic_tower_prison_1"]["active"])
        self.MagicTowerPrison1_Stage.setChecked(self.opt["magic_tower_prison_1"]["stage"])
        self.MagicTowerPrison1_Deck.setValue(self.opt["magic_tower_prison_1"]["deck"])
        self.MagicTowerPrison1_1P.addItems(battle_plan_list)
        self.MagicTowerPrison1_1P.setCurrentIndex(self.opt["magic_tower_prison_1"]["battle_plan_1p"])

        self.MagicTowerPrison2_Active.setChecked(self.opt["magic_tower_prison_2"]["active"])
        self.MagicTowerPrison2_Stage.setChecked(self.opt["magic_tower_prison_2"]["stage"])
        self.MagicTowerPrison2_Deck.setValue(self.opt["magic_tower_prison_2"]["deck"])
        self.MagicTowerPrison2_1P.addItems(battle_plan_list)
        self.MagicTowerPrison2_1P.setCurrentIndex(self.opt["magic_tower_prison_2"]["battle_plan_1p"])

        self.Warrior_Active.setChecked(self.opt["warrior"]["active"])
        self.Warrior_Group.setChecked(self.opt["warrior"]["is_group"])
        self.Warrior_MaxTimes.setValue(self.opt["warrior"]["max_times"])
        self.Warrior_Deck.setValue(self.opt["warrior"]["deck"])
        self.Warrior_1P.addItems(battle_plan_list)
        self.Warrior_2P.addItems(battle_plan_list)
        self.Warrior_1P.setCurrentIndex(self.opt["warrior"]["battle_plan_1p"])
        self.Warrior_2P.setCurrentIndex(self.opt["warrior"]["battle_plan_2p"])

        self.CrossServer_Active.setChecked(self.opt["cross_server"]["active"])
        self.CrossServer_Group.setChecked(self.opt["cross_server"]["is_group"])
        self.CrossServer_MaxTimes.setValue(self.opt["cross_server"]["max_times"])
        self.CrossServer_Stage.setText(self.opt["cross_server"]["stage"])
        self.CrossServer_Deck.setValue(self.opt["cross_server"]["deck"])
        self.CrossServer_1P.addItems(battle_plan_list)
        self.CrossServer_2P.addItems(battle_plan_list)
        self.CrossServer_1P.setCurrentIndex(self.opt["cross_server"]["battle_plan_1p"])
        self.CrossServer_2P.setCurrentIndex(self.opt["cross_server"]["battle_plan_2p"])

        self.Relic_Active.setChecked(self.opt["relic"]["active"])
        self.Relic_Group.setChecked(self.opt["relic"]["is_group"])
        self.Relic_MaxTimes.setValue(self.opt["relic"]["max_times"])
        self.Relic_Stage.setText(self.opt["relic"]["stage"])
        self.Relic_Deck.setValue(self.opt["relic"]["deck"])
        self.Relic_1P.addItems(battle_plan_list)
        self.Relic_2P.addItems(battle_plan_list)
        self.Relic_1P.setCurrentIndex(self.opt["relic"]["battle_plan_1p"])
        self.Relic_2P.setCurrentIndex(self.opt["relic"]["battle_plan_2p"])

        self.NormalBattle_Active.setChecked(self.opt["normal_battle"]["active"])
        self.NormalBattle_Group.setChecked(self.opt["normal_battle"]["is_group"])
        self.NormalBattle_MaxTimes.setValue(self.opt["normal_battle"]["max_times"])
        self.NormalBattle_Stage.setText(self.opt["normal_battle"]["stage"])
        self.NormalBattle_Deck.setValue(self.opt["normal_battle"]["deck"])
        self.NormalBattle_1P.addItems(battle_plan_list)
        self.NormalBattle_2P.addItems(battle_plan_list)
        self.NormalBattle_1P.setCurrentIndex(self.opt["normal_battle"]["battle_plan_1p"])
        self.NormalBattle_2P.setCurrentIndex(self.opt["normal_battle"]["battle_plan_2p"])

        self.ReceiveAwards_Active.setChecked(self.opt["receive_awards"]["active"])
        self.CrossServerReputation_Active.setChecked(self.opt["cross_server_reputation"]["active"])
        self.Customize_Active.setChecked(self.opt["customize"]["active"])

    def ui_to_opt(self):
        # battle_plan_list
        battle_plan_list = get_battle_plan_list(with_extension=False)

        def my_transformer(change_class: object, opt_1, opt_2):
            self.opt[opt_1][opt_2] = change_class.currentIndex()
            change_class.clear()
            change_class.addItems(battle_plan_list)
            change_class.setCurrentIndex(self.opt[opt_1][opt_2])

        self.opt["game_name"] = self.GameName_Input.text()
        self.opt["name_1p"] = self.Name1P_Input.text()
        self.opt["name_2p"] = self.Name2P_Input.text()
        self.opt["zoom_ratio"] = self.ZoomRatio_Input.currentIndex()  # combobox 序号

        self.opt["level_1p"] = self.Level1P_Input.value()
        self.opt["level_2p"] = self.Level2P_Input.value()
        self.opt["auto_use_card"] = self.AutoUseCard.isChecked()

        self.opt["reload_and_daily_quest"]["active"] = self.ReloadAndDailyQuest_Active.isChecked()
        self.opt["fed_and_watered"]["active"] = self.FedAndWatered_Active.isChecked()

        self.opt["quest_guild"]["active"] = self.QuestGuild_Active.isChecked()
        self.opt["quest_guild"]["stage"] = self.QuestGuild_Stage.isChecked()
        self.opt["quest_guild"]["deck"] = self.QuestGuild_Deck.value()
        my_transformer(self.QuestGuild_1P, "quest_guild", "battle_plan_1p")
        my_transformer(self.QuestGuild_2P, "quest_guild", "battle_plan_2p")

        self.opt["quest_spouse"]["active"] = self.QuestSpouse_Active.isChecked()
        self.opt["quest_spouse"]["deck"] = self.QuestSpouse_Deck.value()
        my_transformer(self.QuestSpouse_1P, "quest_spouse", "battle_plan_1p")
        my_transformer(self.QuestSpouse_2P, "quest_spouse", "battle_plan_2p")

        self.opt["offer_reward"]["active"] = self.OfferReward_Active.isChecked()
        self.opt["offer_reward"]["deck"] = self.OfferReward_Deck.value()
        my_transformer(self.OfferReward_1P, "offer_reward", "battle_plan_1p")
        my_transformer(self.OfferReward_2P, "offer_reward", "battle_plan_2p")

        self.opt["magic_tower_double"]["active"] = self.MagicTowerDouble_Active.isChecked()
        self.opt["magic_tower_double"]["max_times"] = self.MagicTowerDouble_MaxTimes.value()
        self.opt["magic_tower_double"]["stage"] = self.MagicTowerDouble_Stage.value()
        self.opt["magic_tower_double"]["deck"] = self.MagicTowerDouble_Deck.value()
        my_transformer(self.MagicTowerDouble_1P, "magic_tower_double", "battle_plan_1p")
        my_transformer(self.MagicTowerDouble_2P, "magic_tower_double", "battle_plan_2p")

        self.opt["magic_tower_alone_1"]["active"] = self.MagicTowerAlone1_Active.isChecked()
        self.opt["magic_tower_alone_1"]["max_times"] = self.MagicTowerAlone1_MaxTimes.value()
        self.opt["magic_tower_alone_1"]["stage"] = self.MagicTowerAlone1_Stage.value()
        self.opt["magic_tower_alone_1"]["deck"] = self.MagicTowerAlone1_Deck.value()
        my_transformer(self.MagicTowerAlone1_1P, "magic_tower_alone_1", "battle_plan_1p")

        self.opt["magic_tower_alone_2"]["active"] = self.MagicTowerAlone2_Active.isChecked()
        self.opt["magic_tower_alone_2"]["max_times"] = self.MagicTowerAlone2_MaxTimes.value()
        self.opt["magic_tower_alone_2"]["stage"] = self.MagicTowerAlone2_Stage.value()
        self.opt["magic_tower_alone_2"]["deck"] = self.MagicTowerAlone2_Deck.value()
        my_transformer(self.MagicTowerAlone2_1P, "magic_tower_alone_2", "battle_plan_1p")
        
        self.opt["magic_tower_prison_1"]["active"] = self.MagicTowerPrison1_Active.isChecked()
        self.opt["magic_tower_prison_1"]["stage"] = self.MagicTowerPrison1_Stage.isChecked()
        self.opt["magic_tower_prison_1"]["deck"] = self.MagicTowerPrison1_Deck.value()
        my_transformer(self.MagicTowerPrison1_1P, "magic_tower_prison_1", "battle_plan_1p")

        self.opt["magic_tower_prison_2"]["active"] = self.MagicTowerPrison2_Active.isChecked()
        self.opt["magic_tower_prison_2"]["stage"] = self.MagicTowerPrison2_Stage.isChecked()
        self.opt["magic_tower_prison_2"]["deck"] = self.MagicTowerPrison2_Deck.value()
        my_transformer(self.MagicTowerPrison2_1P, "magic_tower_prison_2", "battle_plan_1p")

        self.opt["warrior"]["active"] = self.Warrior_Active.isChecked()
        self.opt["warrior"]["is_group"] = self.Warrior_Group.isChecked()
        self.opt["warrior"]["max_times"] = self.Warrior_MaxTimes.value()
        self.opt["warrior"]["deck"] = self.Warrior_Deck.value()
        my_transformer(self.Warrior_1P, "warrior", "battle_plan_1p")
        my_transformer(self.Warrior_2P, "warrior", "battle_plan_2p")

        self.opt["cross_server"]["active"] = self.CrossServer_Active.isChecked()
        self.opt["cross_server"]["is_group"] = self.CrossServer_Group.isChecked()
        self.opt["cross_server"]["max_times"] = self.CrossServer_MaxTimes.value()
        self.opt["cross_server"]["stage"] = self.CrossServer_Stage.text()
        self.opt["cross_server"]["deck"] = self.CrossServer_Deck.value()
        my_transformer(self.CrossServer_1P, "cross_server", "battle_plan_1p")
        my_transformer(self.CrossServer_2P, "cross_server", "battle_plan_2p")

        self.opt["relic"]["active"] = self.Relic_Active.isChecked()
        self.opt["relic"]["is_group"] = self.Relic_Group.isChecked()
        self.opt["relic"]["max_times"] = self.Relic_MaxTimes.value()
        self.opt["relic"]["stage"] = self.Relic_Stage.text()
        self.opt["relic"]["deck"] = self.Relic_Deck.value()
        my_transformer(self.Relic_1P, "relic", "battle_plan_1p")
        my_transformer(self.Relic_2P, "relic", "battle_plan_2p")

        self.opt["normal_battle"]["active"] = self.NormalBattle_Active.isChecked()
        self.opt["normal_battle"]["is_group"] = self.NormalBattle_Group.isChecked()
        self.opt["normal_battle"]["max_times"] = self.NormalBattle_MaxTimes.value()
        self.opt["normal_battle"]["stage"] = self.NormalBattle_Stage.text()
        self.opt["normal_battle"]["deck"] = self.NormalBattle_Deck.value()
        my_transformer(self.NormalBattle_1P, "normal_battle", "battle_plan_1p")
        my_transformer(self.NormalBattle_2P, "normal_battle", "battle_plan_2p")

        self.opt["receive_awards"]["active"] = self.ReceiveAwards_Active.isChecked()
        self.opt["cross_server_reputation"]["active"] = self.CrossServerReputation_Active.isChecked()
        self.opt["customize"]["active"] = self.Customize_Active.isChecked()

    def click_btn_save(self):
        """点击保存配置按钮的函数"""
        self.ui_to_opt()
        self.opt_to_json()

    # def click_btn_start(self):
    #     """
    #     开始/结束按钮 需要注册的函数
    #     Args:
    #         button: 被注册的按钮对象
    #     """
    #
    #     # 先刷新数据
    #     self.refresh_process_parameter(p_id)
    #
    #     if not self.dic_p["flag_activation"][p_id]:
    #         # 创建 储存 启动进程
    #         print([p_id, self.dic_p["dic_process_opt"][p_id]])
    #         self.dic_p["process"][p_id] = multiprocessing.Process(
    #             target=self.battle_all_round,
    #             args=(p_id, self.dic_p["dic_process_opt"][p_id])
    #         )
    #         print(self.dic_p["process"][p_id])
    #         self.dic_p["process"][p_id].start()
    #         # 设置按钮文本
    #         button.sender().setText("终止\nEnd")
    #         # 设置flag
    #         self.dic_p["flag_activation"][p_id] = True
    #     else:
    #         # 中止进程
    #         # if self.dic_p["process"][p_id].is_alive():  # 判断进程是否还在运作中
    #         #     self.dic_p["process"][p_id].terminate()  # 中断进程
    #         #     self.dic_p["process"][p_id].join()  # 清理僵尸进程
    #         # 设置按钮文本
    #         button.sender().setText("开始\nLink Start")
    #         # 设置进程状态文本
    #         self.findChild(QLabel, "E_{}_7_2".format(p_id * 2 + 1)).setText("已中断进程")
    #         # 设置flag
    #         self.dic_p["flag_activation"][p_id] = False


if __name__ == "__main__":
    def main():
        # 实例化 PyQt后台管理
        app = QApplication(sys.argv)

        # 实例化 主窗口
        window = MyMainWindow1()

        # 建立槽连接 注意 多线程中 槽连接必须写在主函数
        # 注册函数：开始/结束按钮
        button = window.Button_Start
        button.clicked.connect(lambda: window.click_btn_start())
        button = window.Button_Save
        button.clicked.connect(lambda: window.click_btn_save())
        # 主窗口 实现
        window.show()

        # 运行主循环，必须调用此函数才可以开始事件处理
        sys.exit(app.exec_())


    main()
