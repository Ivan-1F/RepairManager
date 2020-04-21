import json
import time
import stext as st

help_msg = '''------MCDR RepairManager插件------
§a命令帮助如下:§r
§6!!repair help§r 显示帮助信息
§6!!repair add <name> <comment> here§r 在当前位置添加一个名为name的报修
§6!!repair add <name> <comment> [<position>]§r
§7position为坐标，格式为<x> <y> <z> <dim>§r
§7在(x,y,z)添加一个报修§r
§7dim为纬度，0为§2主世界§7，-1为§4地狱§7，1为§5末地§r
§6!!repair detail <name>§r 显示name的详细信息
§6!!repair fix <name>§r 标记name为已修复
§6!!repair unfix <name>§r 标记name为未修复
§6!!repair rename <name>§r 标记name为未修复
§6!!repair modify <name> <comment>§r 修改name的注释为comment
--------------------------------'''
format_error = "§c格式错误，请输入§6!!repair help§c查看帮助信息§r"
cant_find_error = "§c无法找到输入的名称！§r"

Prefix = '!!repair'
PluginName = "RepairManager"
DataPath = "plugins/" + PluginName + "/data.json"
data = []
global global_server
global global_info

def load_data():
    global data
    try:
        with open(DataPath) as file:
            data = json.load(file, encoding='utf8')
            data = data["repair_data"]
    except:
        return

def save_data():
    global data
    try:
        with open(DataPath, "w") as file:
            json.dump(data, file)
    except:
        return

def add_data(name, comment, pos_x, pos_y, pos_z, dim, fixed):
    global data


def show_detail(name):
    global global_server
    global global_info
    global data
    server = global_server
    info = global_info

    load_data()

    arr_pos = -1

    for i in range(0, len(data)):
        if data[i]["name"] == name:
            arr_pos = i
            break
    if arr_pos == -1:
        server.reply(info, cant_find_error) # can not find data
        return

    comment = data[arr_pos]["comment"]
    fixed = data[arr_pos]["fixed"]
    pos_x = data[arr_pos]["x"]
    pos_y = data[arr_pos]["y"]
    pos_z = data[arr_pos]["z"]
    dim = data[arr_pos]["dim"]
    # server.say(data)

    server.reply(info, "名称 : " + name)
    server.reply(info, "注释 : " + comment)
    if dim == 0:
        server.reply(info, "坐标 : §2主世界§r[x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))
    elif dim == -1:
        server.reply(info, "坐标 : §4地狱§r[x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))
    elif dim == 1:
        server.reply(info, "坐标 : §5末地§r[x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))

    if fixed:
        server.reply(info, "是否修复 : §2True§r")
    else:
        server.reply(info, "是否修复 : §4False§r")


def show_list(server, player):
    global data

    load_data()
    for i in range(0, len(data)):
        output = st.SText(" - " + data[i]["name"] + "   §7" + data[i]["comment"])
        # output = st.SText(" - " + data[i]["name"], color=st.SColor.red)
        output.hover_text = st.SText("点击查看任务详细")
        output.set_click_command("!!repair detail " + data[i]["name"])
        st.show_to_player(server, player, output)
        # server.tell(info.player, " - " + data[i]["name"] + "   §7" + data[i]["comment"])

def on_load(server,module):
    server.add_help_message("一个用于报修机器故障的插件")
    
def on_info(server, info):
    global global_server
    global global_info
    global_server = server
    global_info = info

    content = info.content
    splited_content = content.split()
    player = info.player
    if splited_content[0] != Prefix:
        return

    if len(splited_content) == 1:
        show_list(server, player)
        return
    
    if splited_content[1] == "help":
        server.reply(info, help_msg)
        return

    if splited_content[1] == "detail":
        if len(splited_content) != 3:
            server.reply(info, format_error)
            return
        show_detail(splited_content[2])
        return

    if splited_content[1] == "add":
        if len(splited_content) == 8:
            if splited_content[4].isdigit() and splited_content[5].isdigit() and \
                    splited_content[6].isdigit() and splited_content[7].isdigit():
                # Format Correct
                server.reply(info, "正在添加……")
                name = splited_content[2]
                comment = splited_content[3]
                pos_x = splited_content[4]
                pos_y = splited_content[5]
                pos_z = splited_content[6]
                dim = splited_content[7]
                fixed = False
            else:
                server.reply(info, format_error)
                return
        elif len(splited_content) == 5:
            if splited_content[4] != "here":
                server.reply(info, format_error)
            else:
                # Format Correct


        return
