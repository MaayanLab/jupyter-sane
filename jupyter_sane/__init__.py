#!/usr/bin/env python3

import os
import sh
import sys
import click
import signal
import tempfile

python = sh.Command(sys.executable)
ipykernel = python.bake(m='ipykernel')
jupyter = python.bake(m='jupyter')

def handle_interrupt(cmd, *kargs, **kwargs):
  proc = cmd(
    *kargs,
    **kwargs,
    _in=sys.stdin,
    _out=sys.stdout,
    _err=sys.stderr,
    _bg=True,
  )
  while True:
    try:
      return proc.wait()
    except KeyboardInterrupt:
      proc.signal(signal.SIGINT)

class JupyterHelpPassthrough(click.Command):
  def format_help(self, ctx, formatter):
    handle_interrupt(jupyter, '--help')
    click.echo('')
    return super().format_help(ctx, formatter)

@click.command('jupyter',
  help='Run a ipython jupyter kernel using this active environment.',
  cls=JupyterHelpPassthrough,
  context_settings=dict(
    ignore_unknown_options=True,
    allow_interspersed_args=False,
  ),
)
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
def jupyter_cli(args=[]):
  command, *args = args
  if command in {'console', 'qtconsole'}:
    if not any(arg.startswith('--kernel=') for arg in args):
      args.insert(0, '--kernel=python-sane')
  with tempfile.TemporaryDirectory() as tmpdir:
    handle_interrupt(
      ipykernel.install,
      '--user',
      '--name', 'python-sane',
      '--display-name', 'Python (sane)',
      '--env', 'PYTHONPATH', ':'.join(sys.path),
      _env=dict(os.environ, HOME=tmpdir),
    )
    handle_interrupt(
      jupyter,
      command,
      *args,
      _env=dict(os.environ, HOME=tmpdir),
    )

if __name__ == '__main__':
  jupyter_cli()
