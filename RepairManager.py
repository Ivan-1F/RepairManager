import json
import time

help_msg = '''------MCDR RepairManager插件------
§a命令帮助如下:§r
§6!!repair help§r 显示帮助信息
§6!!repair reload§r 重新加载数据
§6!!repair add <name> [<comment>]§r 在当前位置添加一个名为name的报修
§6!!repair add <name> [<comment>] [<x> <y> <z>]§r 在(x,y,z)添加一个名为name的报修
§6!!repair detail <name>§r 显示name的详细信息
§6!!repair fix <name>§r 标记name为已修复
§6!!repair unfix <name>§r 标记name为未修复
§6!!repair rename <name>§r 标记name为未修复
§6!!repair modify <name> <comment>§r 修改name的注释为comment
--------------------------------'''
Prefix = '!!repair'
PluginName = "RepairManager"
data_path = "plugins/" + PluginName + "/"

def load_data():
    file = open(data_path + 'data.json',encoding='utf-8')
    data = json.load(file)
    data = data["repair_data"]
    return data

def on_load(server,module):
    server.add_help_message("一个用于报修机器故障的插件")
def on_info(server, info):
    content = info.content
    splited_content = content.split()
    if splited_content[0] != Prefix:
        return

    if len(splited_content) == 1:
        data = load_data()
        for i in range(0,len(data)):
            server.tell(info.player, " - " + data[i]["name"] + "   §7" + data[i]["comment"])
            #server.tell(info.player, {"text":"test","clickEvent":{"action":"run_command","value":"!!qb make"}})
        return


    
    if splited_content[1] == "help":
        server.tell(info.player, help_msg)
        return
        
    if splited_content[1] == "reload":
        data=load_data()
        server.say("§a数据重载成功")
        return
