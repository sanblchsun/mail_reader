import logging
import os
from datetime import datetime, time
from configparser import ConfigParser
from copy import deepcopy

def _check_filters(firma_filter_def, firma_def):
    if firma_filter_def:
        firma_filter_def = firma_filter_def.split(",")
        firma_filter_def = [i.strip() for i in firma_filter_def]
        if type(firma_filter_def) is list and len(firma_filter_def) <= 100:
            for i_pattern in firma_filter_def:
                if i_pattern.lower() in firma_def.lower():
                    return True
                else:
                    return False

    logging.info("Критичная ошибка, в файле filter.ini возможно строка firma_filter = пустая")
    exit(1)


def check(firma):
    base_path = os.path.dirname(os.path.abspath(__file__))
    cfg_path = "filter.ini"
    config_path = os.path.join(base_path, cfg_path)
    # get the config
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        logging.error(f"""Конфигурационный файл не найден по ссылке:
        {cfg_path}""")
        exit(1)
    time_start = cfg.get("time", "time_start")
    time_end = cfg.get("time", "time_end")
    firma_filter = cfg.get("filter", "firma_filter")
    check_send_bot = False
    try:
        obj_time_start = time.fromisoformat(time_start)
        obj_time_end = time.fromisoformat(time_end)
        res_now = datetime.now().time()
        if obj_time_start <= obj_time_end:
            if obj_time_start <= res_now <= obj_time_end:
                check_send_bot = _check_filters(firma_filter_def=deepcopy(firma_filter),
                                                   firma_def=firma)
            else:
                if obj_time_start <= res_now or res_now <= obj_time_end:
                    check_send_bot = _check_filters(firma_filter_def=deepcopy(firma_filter),
                                                       firma_def=firma)
    except ValueError as e:
        logging.info(f"Критичная ошибка при преобразовании времени: {e}, который указан в файле filter.ini")
        exit(1)
    return check_send_bot