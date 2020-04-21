import json
import time
import stext as st

help_msg = '''------MCDR RepairManager插件------
§a命令帮助如下:§r
§6!!repair§r 显示报修列表（未修复）
§6!!repair fixed§r 显示报修列表（已修复）
§6!!repair help§r 显示帮助信息
§6!!repair add <name> <comment> here§r 在当前位置添加一个名为name的报修
§6!!repair add <name> <comment> [<position>]§r
§7position为坐标，格式为<x> <y> <z> <dim>§r
§7在(x,y,z)添加一个报修§r
§7dim为纬度，0为§2主世界§7，-1为§4地狱§7，1为§5末地§r
§6!!repair detail <name>§r 显示name的详细信息
§6!!repair fix <name>§r 标记name为已修复
§6!!repair unfix <name>§r 标记name为未修复
§6!!repair rename <name> <new_name>§r 重命名
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
    load_data()
    new = {"name" : name, "comment" : comment,
           "pos_x" : pos_x, "pos_y" : pos_y,
           "pos_z" : pos_z, "dim" : dim, "fixed" : fixed}
    data.append(new)
    save_data()

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
    pos_x = data[arr_pos]["pos_x"]
    pos_y = data[arr_pos]["pos_y"]
    pos_z = data[arr_pos]["pos_z"]
    dim = data[arr_pos]["dim"]
    # server.say(data)

    server.reply(info, "名称 : " + name)
    server.reply(info, "注释 : " + comment)
    if dim == 0:
        server.reply(info, "坐标 : §2主世界§r [x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))
    elif dim == -1:
        server.reply(info, "坐标 : §4地狱§r [x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))
    elif dim == 1:
        server.reply(info, "坐标 : §5末地§r [x:{} ,y:{} ,z:{}]".format(pos_x, pos_y, pos_z))

    if fixed:
        server.reply(info, "是否修复 : §2True§r")
    else:
        server.reply(info, "是否修复 : §4False§r")

def show_fixed_list():
    global global_server
    global global_info
    global data
    server = global_server
    info = global_info
    player = info.player

    load_data()

    for i in range(0, len(data)):
        if(data[i]["fixed"] == False):
            continue    # 未被修复
        output = st.SText(" - " + data[i]["name"] + "   §7" + data[i]["comment"])
        output.hover_text = st.SText("点击查看任务详细")
        output.set_click_command("!!repair detail " + data[i]["name"])
        st.show_to_player(server, player, output)

def show_list():
    global data
    load_data()

    global global_server
    global global_info
    server = global_server
    info = global_info

    player = info.player

    for i in range(0, len(data)):
        if(data[i]["fixed"] == True):
            continue    # 已被修复
        output = st.SText(" - " + data[i]["name"] + "   §7" + data[i]["comment"])
        output.hover_text = st.SText("点击查看任务详细")
        output.set_click_command("!!repair detail " + data[i]["name"])
        st.show_to_player(server, player, output)

    show_fixed_list = st.SText("显示已修复的报修", color=st.SColor.gray)
    show_fixed_list.set_click_command("!!repair fixed")
    st.show_to_player(server, player, show_fixed_list)

def add_successful_info(dim, pos_x, pos_y, pos_z):
    global global_server
    global global_info

    server = global_server
    info = global_info
    if dim == 0:
        server.reply(info, "已在 §2主世界§r [x:{} ,y:{} ,z:{}] 创建了报修".format(pos_x, pos_y, pos_z))
    elif dim == -1:
        server.reply(info, "已在 §4地狱§r [x:{} ,y:{} ,z:{}] 创建了报修".format(pos_x, pos_y, pos_z))
    elif dim == 1:
        server.reply(info, "已在 §5末地§r [x:{} ,y:{} ,z:{}] 创建了报修".format(pos_x, pos_y, pos_z))

def fix(name):
    global global_server
    global global_info
    global data
    load_data()
    server = global_server
    info = global_info
    for i in range(0, len(data)):
        if(data[i]["name"] == name):
            if(data[i]["fixed"] == False):
                data[i]["fixed"] = True
                save_data()
                server.reply(info, "§a已将这项报修标记为已修复！§r")
            else:
                server.reply(info, "§c这项报修已经被修复！§r")

def unfix(name):
    global global_server
    global global_info
    global data
    load_data()
    server = global_server
    info = global_info
    for i in range(0, len(data)):
        if(data[i]["name"] == name):
            if(data[i]["fixed"] == True):
                data[i]["fixed"] = False
                save_data()
                server.reply(info, "§a已将这项报修标记为未修复！§r")
            else:
                server.reply(info, "§c这项报修还未被修复！§r")

def rename(name, newname):
    global global_server
    global global_info
    global data
    load_data()
    server = global_server
    info = global_info
    if(name == newname):
        server.reply(info, "§c新名称与旧名称相同！§r")
        return
    for i in range(0, len(data)):
        if (data[i]["name"] == name):
            data[i]["name"] = newname
            server.reply(info, "§a成功将§6" + name + "§a重命名为§6" + newname + "§r")
            save_data()
            return
    server.reply(info, "§c未找到§6" + name)

def modify(name, comment):
    global global_server
    global global_info
    global data
    load_data()
    server = global_server
    info = global_info
    for i in range(0, len(data)):
        if (data[i]["name"] == name):
            data[i]["comment"] = comment
            server.reply(info, "§a成功将§6" + name + "§a的注释改为§6" + comment + "§r")
            save_data()
            return
    server.reply(info, "§c未找到§6" + name)


def on_load(server,module):
    server.add_help_message(Prefix, "一个用于报修机器故障的插件")
    
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
        show_list()
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
            if splited_content[4].strip('-').isdigit() and splited_content[5].strip('-').isdigit() and \
                    splited_content[6].strip('-').isdigit() and splited_content[7].strip('-').isdigit():
                # Format Correct
                name = splited_content[2]
                comment = splited_content[3]
                pos_x = int(splited_content[4])
                pos_y = int(splited_content[5])
                pos_z = int(splited_content[6])
                dim = int(splited_content[7])
                fixed = False
                add_data(name, comment, pos_x, pos_y, pos_z, dim, fixed)
                add_successful_info(dim, pos_x, pos_y, pos_z)

            else:
                server.reply(info, format_error)
                print("坐标错误")
                return
        elif len(splited_content) == 5:
            if splited_content[4] != "here":
                server.reply(info, format_error)
            else:
                # Format Correct
                # here
                PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
                result = PlayerInfoAPI.getPlayerInfo(server, info.player)
                name = splited_content[2]
                comment = splited_content[3]
                dim = result["Dimension"]
                pos_x = int(result["Pos"][0])
                pos_y = int(result["Pos"][1])
                pos_z = int(result["Pos"][2])
                fixed = False
                add_data(name, comment, pos_x, pos_y, pos_z, dim, fixed)
                global_info = info
                add_successful_info(dim, pos_x, pos_y, pos_z)
        else:
            server.reply(info, format_error)
        return

    if splited_content[1] == "fixed":
        if len(splited_content) != 2:
            server.reply(info, format_error)
            return
        show_fixed_list()

    if splited_content[1] == "fix":
        if len(splited_content) != 3:
            server.reply(info, format_error)
            return
        fix(splited_content[2])
        return

    if splited_content[1] == "unfix":
        if len(splited_content) != 3:
            server.reply(info, format_error)
            return
        unfix(splited_content[2])
        return

    if splited_content[1] == "rename":
        if len(splited_content) != 4:
            server.reply(info, format_error)
            return
        rename(splited_content[2], splited_content[3])
        return

    if splited_content[1] == "modify":
        if len(splited_content) != 4:
            server.reply(info, format_error)
            return
        modify(splited_content[2], splited_content[3])
        return
