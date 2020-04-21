# RepairManager

[中文](https://github.com/wyf0762/RepairManager/blob/master/README.md)

A [MCDReforged](https://github.com/Fallen-Breath/MCDReforged/) plugin to manage machine repairments，require [PlayerInfoAPI](https://github.com/TISUnion/PlayerInfoAPI).

# Install

1. Drag `RepairManager.py` and `PlayerInfoAPI.py` to the `/plugins` folder.
2. Use `!!MCDR reload all` to reload MCDR

# Usage

 - `!!repair` show repairment list（unfixed）
 - `!!repair fixed` show repairment list（fixed）
 - `!!repair help` show help message
 - `!!repair add <name> <comment> here` create a repairment at your location
 - `!!repair add <name> <comment> [<position>]` create a repairment at (x,y,z)
    - (the format of `<position>` is `<x> <y> <z> <dim>` ; dim means dimension，0 is overworld，-1 is nether，1 is the end)
 - `!!repair detail <name>` show the detail information of `<name>`
 - `!!repair fix <name>` mark `<name>` fixed
 - `!!repair unfix <name>` mark `<name>` unfixed
 - `!!repair rename <name> <new_name>` rename `<name>` to `<new_name>`
 - `!!repair modify <name> <comment>` edit the comment of `<name>` to `<comment>`
 [English](https://github.com/wyf0762/RepairManager/blob/master/doc/README_en.md)

