
'''
Author:linqingbin
Description:Clean files(Factory)
'''

import os
import re
from loguru import logger
from fileclean import models


def cleanwork(fromPath, toPath, pattern, command, iscrawl=False, iter_times=0):
    '''
    File clean up

    Parameters
    ----------
    fromPath:string
        Source folder
    toPath:string
        Target folder
    pattern:string
        Regular expression partern for file match
    command:string
        delete, move or copy
    iscrawl:bool,default is False
        is crawl fodler if exists nesting folders

    Returns
    -------
    None
    '''
    task_name = "Task {0} {2} to {1} ".format(fromPath, toPath, command)
    logger.info('{task} start'.format(task=task_name))
    try:
        filelist = os.listdir(fromPath)
    except Exception:
        logger.error("Open %s error." % fromPath)
        return None
    for filename in filelist:
        filepath = fromPath + "/" + filename
        # Handling recursive problems with folders
        if os.path.isdir(filepath) and bool(int(iscrawl)) and iter_times < 10:
            iter_times += 1
            logger.info(filepath, iter_times)
            cleanwork(filepath, toPath, pattern, command, iscrawl, iter_times)
        elif re.match(pattern, filename, flags=re.IGNORECASE):
            Worker = models.selectWorker(command)
            worker = Worker(filepath, toPath, pattern)
            worker.work()
            logger.info('{task} done'.format(task=task_name))
    # logger.info('{task} end'.format(task=task_name))


def main(tasks_path):
    logger.info("Program start")
    with open(tasks_path, 'r') as f:
        tasks = f.read()
    works = [x.split(',') for x in tasks.split('\n')][1:]  # Get tasks
    logger.info("{n} tasks found".format(n=len(works)))
    for work in works:
        if len(work) == 5:
            fromPath, toPath, pattern, command, iscrawl = work
            cleanwork(fromPath, toPath, pattern, command, iscrawl)
    logger.info("Program end")
