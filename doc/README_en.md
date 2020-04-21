# RepairManager

A [MCDReforged](https://github.com/Fallen-Breath/MCDReforged/) plugin to manage machine repairments，require [PlayerInfoAPI](https://github.com/TISUnion/PlayerInfoAPI).

# Install

1. Drag `RepairManager.py` and `PlayerInfoAPI.py` to the `/plugins` folder.
2. Use `!!MCDR reload all` to reload MCDR

# Usage

`!!repair` show repairment list（unfixed）
`!!repair fixed` show repairment list（fixed）
`!!repair help` show help message
`!!repair add <name> <comment> here` create a repairment at your location
`!!repair add <name> <comment> [<position>]` create a repairment at (x,y,z)
(the format of <position> is `<x> <y> <z> <dim>` ; dim means dimension，0 is overworld，-1 is nether，1 is the end)

`!!repair detail <name>` show the detail information of <name>
`!!repair fix <name>` 标记name为已修复
`!!repair unfix <name>` 标记name为未修复
`!!repair rename <name> <new_name>` 重命名
`!!repair modify <name> <comment>` 修改name的注释为comment

