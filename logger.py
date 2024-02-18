# -*- encoding: utf-8 -*-


import datetime
from rich.console import Console


class Logger:
  def __init__(self):
    self._status_msg = None
    self._console = Console(
      log_path=False, 
      log_time_format='  %Y-%m-%d %H:%M:%S', 
      highlighter=None,
      color_system='standard'
    )
    self._console._log_render.omit_repeated_times = True

  def set_status(self, msg):
    self._skip_status()
    self._status_msg = msg
    timestamp = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    return self._console.status(f'[cyan]{timestamp}[/cyan] [white]STATUS  [/]{self._status_msg}')
  
  def update_status(self, status, msg):
    self._status_msg = msg
    timestamp = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    status.update(f'[cyan]{timestamp}[/cyan] [white]STATUS  [/]{self._status_msg}')

  def append_status(self, status, msg):
    self._status_msg += msg
    timestamp = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
    status.update(f'[cyan]{timestamp}[/cyan] [white]STATUS  [/]{self._status_msg}')    

  def clear(self):
    self._skip_status()
    self._status_msg = None
    self._console.clear()

  def info(self, msg):
    self._skip_status()
    self._console.log(f'[green]INFO    [/]{msg}')

  def debug(self, msg):
    self._skip_status()
    self._console.log(f'[magenta]DEBUG   {msg}[/]')

  def warning(self, msg):
    self._skip_status()
    self._console.log(f'[yellow]WARNING {msg}[/]')

  def error(self, msg):
    self._skip_status()
    self._console.log(f'[red]ERROR   {msg}[/]')

  def _skip_status(self):
    if self._status_msg != None:
      self._console.log(f'[green]INFO    [/]{self._status_msg}')
      self._status_msg = None
      