#!/usr/bin/env python3
# This file is automatically generated!
# Timestamp:          02/08/2019 @ 17:14:09.101604 (UTC)

from enum import IntEnum
from spheroboros.common import commands
from spheroboros.common.helpers import text_to_pascal_case


class DevicesEnum(IntEnum):
    api_and_shell = 0x10
    system_info = 0x11
    system_mode = 0x12
    power = 0x13
    drive = 0x16
    sensor = 0x18
    connection = 0x19
    io = 0x1A
    firmware = 0x1D
    factory_test = 0x1F


def get_device_path_by_did(did):
    device_name = DevicesEnum(did).name
    return text_to_pascal_case(device_name)


def get_command_path_by_cid(did, cid):
    device_name = DevicesEnum(did).name

    command_name = eval(
        'commands.{}.CommandsEnum({}).name'.format(
            device_name,
            cid
        )
    )

    return text_to_pascal_case(command_name)
